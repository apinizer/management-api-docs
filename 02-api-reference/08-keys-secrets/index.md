---
layout: default
permalink: /02-api-reference/08-keys-secrets/
---

# Keys & Secrets API

## Overview

The Keys & Secrets API provides endpoints for managing cryptographic keys, keystores, JWKs (JSON Web Keys), and certificates in Apinizer. These resources are essential for secure communication, encryption, authentication, and digital signatures in API Proxies.

## API Sections

### JWKs (JSON Web Keys)
- [List JWKs](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-jwks/) - Get all JWKs for a project
- [Get JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/get-jwk/) - Get a specific JWK
- [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) - Create a new JWK
- [Update JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/update-jwk/) - Update an existing JWK
- [Delete JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/delete-jwk/) - Delete a JWK
- [Generate JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/generate-jwk/) - Generate a new JWK
- [Parse JWK from URL](/management-api-docs/02-api-reference/08-keys-secrets/crud/parse-jwk-from-url/) - Parse and create JWK from URL
- [Parse JWK from Clipboard](/management-api-docs/02-api-reference/08-keys-secrets/crud/parse-jwk-from-clipboard/) - Parse and create JWK from JSON string
- [Parse JWK from Certificate](/management-api-docs/02-api-reference/08-keys-secrets/crud/parse-jwk-from-certificate/) - Parse and create JWK from certificate
- [Parse JWK from Key](/management-api-docs/02-api-reference/08-keys-secrets/crud/parse-jwk-from-key/) - Parse and create JWK from key
- [Parse JWK from Keystore](/management-api-docs/02-api-reference/08-keys-secrets/crud/parse-jwk-from-keystore/) - Parse and create JWK from keystore

### Keystores
- [List Keystores](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-keystores/) - Get all keystores for a project
- [Get Keystore](/management-api-docs/02-api-reference/08-keys-secrets/crud/get-keystore/) - Get a specific keystore
- [Create Keystore](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-keystore/) - Create a new keystore
- [Update Keystore](/management-api-docs/02-api-reference/08-keys-secrets/crud/update-keystore/) - Update an existing keystore
- [Delete Keystore](/management-api-docs/02-api-reference/08-keys-secrets/crud/delete-keystore/) - Delete a keystore

### Keys (Crypto Keys)
- [List Keys](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-keys/) - Get all keys for a project
- [Get Key](/management-api-docs/02-api-reference/08-keys-secrets/crud/get-key/) - Get a specific key
- [Create Key](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-key/) - Create a new key
- [Update Key](/management-api-docs/02-api-reference/08-keys-secrets/crud/update-key/) - Update an existing key
- [Delete Key](/management-api-docs/02-api-reference/08-keys-secrets/crud/delete-key/) - Delete a key

### Certificates
- [List Certificates](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-certificates/) - Get all certificates for a project
- [Get Certificate](/management-api-docs/02-api-reference/08-keys-secrets/crud/get-certificate/) - Get a specific certificate
- [Create Certificate](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-certificate/) - Create a new certificate
- [Update Certificate](/management-api-docs/02-api-reference/08-keys-secrets/crud/update-certificate/) - Update an existing certificate
- [Delete Certificate](/management-api-docs/02-api-reference/08-keys-secrets/crud/delete-certificate/) - Delete a certificate
- [Export Certificate](/management-api-docs/02-api-reference/08-keys-secrets/crud/export-certificate/) - Export certificate as ZIP file
- [Get Truststore Certificates](/management-api-docs/02-api-reference/08-keys-secrets/crud/get-truststore-certificates/) - Get certificates from environment truststore

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_API_SECURITY` - Required for all keys and secrets operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](/management-api-docs/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/management-api-docs/01-getting-started/error-handling/) - Error response formats
