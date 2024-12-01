# Doppelcheck: Core

Open-source infrastructure for building trustworthy information verification systems.

## Overview

Doppelcheck: Core provides fundamental building blocks for creating decentralized verification systems. Instead of being yet another centralized fact-checking service, it establishes protocols and APIs that enable organizations to build and operate independent verification systems while maintaining interoperability.

## Key Features

- Standardized verification protocols and trust metrics
- Flexible model orchestration for local and cloud LLMs 
- Distributed evidence store with integrity verification
- Plugin system for custom verification strategies
- Comprehensive API for integration

## Architecture

The infrastructure consists of four main components:

### 1. Verification Protocol Layer
- Trust chain establishment and validation
- Claim extraction interfaces
- Source validation protocols
- Standardized trust metrics

### 2. Model Orchestration Layer
- Support for local and cloud LLM providers
- Access controls and audit capabilities
- Consistent verification standards
- Model output validation

### 3. Distributed Evidence Store
- PostgreSQL-based artifact storage
- Peer-to-peer verification networks
- Data sovereignty guarantees
- Cross-platform verification formats

### 4. API Layer
- OAuth 2.0 authentication
- Plugin distribution system
- Third-party integration capabilities
- Comprehensive input validation

## Getting Started

*Documentation in progress*

### Prerequisites
- Python 3.8+
- PostgreSQL
- OpenSSL

### Installation
TODO

### Basic Usage
```python
from doppelcheck import Verifier, SourceManager

# Initialize verifier with local model
verifier = Verifier(model="local:mistral")

# Create source manager
sources = SourceManager()

# Verify a claim
result = verifier.verify(
    claim="This is a claim to verify",
    sources=sources.search()
)
```

## Development Status

This project development did not start yet. For now, this repository contains only experiments and proofs of concept.

The roadmap includes:

1. Core verification protocols and trust metrics
2. Model orchestration layer
3. Distributed evidence store
4. API gateway and plugin system
5. Reference implementations
6. Developer documentation

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
TODO
