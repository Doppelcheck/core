import logging
from typing import Dict, List, Optional
from .trust_chain import TrustChain
from .models import ModelOrchestrator
from .evidence import EvidenceStore
from .protocols import VerificationProtocol

logger = logging.getLogger(__name__)


class Verifier:
    """
    Main verification orchestrator that coordinates the verification process
    using various components of the Doppelcheck infrastructure.
    """

    def __init__(
            self,
            model: str = "local:mistral",
            evidence_store_url: Optional[str] = None,
            trust_threshold: float = 0.8
    ):
        self.model_orchestrator = ModelOrchestrator(model_id=model)
        self.evidence_store = EvidenceStore(url=evidence_store_url)
        self.trust_chain = TrustChain()
        self.protocol = VerificationProtocol()
        self.trust_threshold = trust_threshold

    async def verify(
            self,
            claim: str,
            sources: List[Dict],
            context: Optional[Dict] = None
    ) -> Dict:
        """
        Verify a claim against provided sources using the configured model
        and verification infrastructure.

        Args:
            claim: The claim to verify
            sources: List of source documents/references
            context: Optional additional context

        Returns:
            Dict containing verification results and trust metrics
        """
        logger.info(f"Starting verification for claim: {claim[:100]}...")

        # Extract key claims and evidence
        extracted_claims = await self.protocol.extract_claims(claim)

        # Validate sources
        validated_sources = await self.protocol.validate_sources(sources)

        # Build trust chain
        trust_chain = await self.trust_chain.build(
            claims=extracted_claims,
            sources=validated_sources
        )

        # Get model verification
        verification = await self.model_orchestrator.verify(
            claim=claim,
            sources=validated_sources,
            trust_chain=trust_chain,
            context=context
        )

        # Store evidence
        evidence_id = await self.evidence_store.store(
            claim=claim,
            sources=validated_sources,
            verification=verification,
            trust_chain=trust_chain
        )

        # Compile final result
        result = {
            "claim": claim,
            "verification": verification,
            "trust_score": trust_chain.trust_score,
            "evidence_id": evidence_id,
            "sources": validated_sources,
            "timestamp": self.protocol.get_timestamp()
        }

        return result
