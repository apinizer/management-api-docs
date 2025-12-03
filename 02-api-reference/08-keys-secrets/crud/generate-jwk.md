---
layout: default
permalink: /02-api-reference/08-keys-secrets/crud/generate-jwk/
---

# Generate JWK

## Overview

Generates a new JWK (JSON Web Key) programmatically and deploys it to environments. This endpoint creates a cryptographically secure JWK based on the specified type and parameters.

## Endpoint

```
POST /apiops/projects/{projectName}/jwks/generate
```

## Authentication

Requires a Personal API Access Token.

### Header

```
Authorization: Bearer YOUR_TOKEN
```

## Request

### Headers

| Header | Value | Required |
|--------|-------|----------|
| Authorization | Bearer {token} | Yes |
| Content-Type | application/json | Yes |

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |

### Request Body

The request body structure varies based on the JWK `type`. All types require `name` and `type` fields.

#### Type: RSA

```json
{
  "name": "generated-rsa-jwk",
  "description": "Auto-generated RSA JWK",
  "type": "RSA",
  "rsa": {
    "keySize": 2048
  }
}
```

**RSA Parameters:**
- `keySize` (integer): Key size in bits. Common values: `2048`, `3072`, `4096`
  - `2048`: Standard size, good balance of security and performance
  - `3072`: Higher security, recommended for long-term use
  - `4096`: Maximum security, slower operations

#### Type: EC (Elliptic Curve)

```json
{
  "name": "generated-ec-jwk",
  "description": "Auto-generated EC JWK",
  "type": "EC",
  "ec": {
    "crv": "P-256"
  }
}
```

**EC Parameters:**
- `crv` (string): Curve name. Valid values:
  - `P-256`: 256-bit curve (NIST P-256, secp256r1)
  - `P-384`: 384-bit curve (NIST P-384, secp384r1)
  - `P-521`: 521-bit curve (NIST P-521, secp521r1)

#### Type: OCT (Octet Sequence - Symmetric Key)

```json
{
  "name": "generated-oct-jwk",
  "description": "Auto-generated symmetric key",
  "type": "OCT",
  "oct": {
    "keySize": 256
  }
}
```

**OCT Parameters:**
- `keySize` (integer): Key size in bits. Common values: `128`, `192`, `256`
  - `128`: 128-bit key (16 bytes)
  - `192`: 192-bit key (24 bytes)
  - `256`: 256-bit key (32 bytes) - Recommended

#### Type: OKP (Octet Key Pair)

```json
{
  "name": "generated-okp-jwk",
  "description": "Auto-generated OKP JWK",
  "type": "OKP",
  "okp": {
    "crv": "Ed25519"
  }
}
```

**OKP Parameters:**
- `crv` (string): Curve name. Valid values:
  - `Ed25519`: Edwards Curve for signing (Ed25519)
  - `Ed448`: Edwards Curve for signing (Ed448)
  - `X25519`: Montgomery Curve for key exchange (X25519)
  - `X448`: Montgomery Curve for key exchange (X448)

### Request Body Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | JWK name (unique identifier) |
| description | string | No | JWK description |
| type | string | Yes | JWK type: `RSA`, `EC`, `OCT`, `OKP` |
| rsa | object | Conditional | RSA-specific parameters (required if type is RSA) |
| ec | object | Conditional | EC-specific parameters (required if type is EC) |
| oct | object | Conditional | OCT-specific parameters (required if type is OCT) |
| okp | object | Conditional | OKP-specific parameters (required if type is OKP) |

### RSA Object Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| keySize | integer | Yes | Key size in bits. Valid values: `2048`, `3072`, `4096` |

### EC Object Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| crv | string | Yes | Curve name. Valid values: `P-256`, `P-384`, `P-521` |

### OCT Object Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| keySize | integer | Yes | Key size in bits. Valid values: `128`, `192`, `256` |

### OKP Object Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| crv | string | Yes | Curve name. Valid values: `Ed25519`, `Ed448`, `X25519`, `X448` |

### Notes

- `name` must be unique within the project
- `type` determines the cryptographic algorithm and which type-specific object (`rsa`, `ec`, `oct`, or `okp`) must be provided
- Type-specific parameters are required based on the selected `type`
- JWK is automatically deployed to all environments after generation

## Response

### Success Response (200 OK)

```json
{
  "success": true,
  "deploymentResult": {
    "success": true,
    "message": "Deployment completed successfully",
    "environmentResults": [
      {
        "environmentName": "production",
        "success": true,
        "message": "Deployed successfully"
      }
    ]
  }
}
```

### Error Response (400 Bad Request)

```json
{
  "error": "bad_request",
  "error_description": "JWK name can not be empty!"
}
```

or

```json
{
  "error": "bad_request",
  "error_description": "JWK type can not be empty!"
}
```

or

```json
{
  "error": "bad_request",
  "error_description": "JWK (name: generated-jwk) is already exist! Try update operation if want to change its value."
}
```

## cURL Examples

### Example 1: Generate RSA JWK (2048-bit)

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "generated-rsa-jwk",
    "description": "Auto-generated RSA 2048-bit JWK",
    "type": "RSA",
    "rsa": {
      "keySize": 2048
    }
  }'
```

### Example 2: Generate RSA JWK (4096-bit)

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "generated-rsa-4096-jwk",
    "description": "Auto-generated RSA 4096-bit JWK",
    "type": "RSA",
    "rsa": {
      "keySize": 4096
    }
  }'
```

### Example 3: Generate EC JWK (P-256)

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "generated-ec-jwk",
    "description": "Auto-generated EC P-256 JWK",
    "type": "EC",
    "ec": {
      "crv": "P-256"
    }
  }'
```

### Example 4: Generate EC JWK (P-384)

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "generated-ec-p384-jwk",
    "description": "Auto-generated EC P-384 JWK",
    "type": "EC",
    "ec": {
      "crv": "P-384"
    }
  }'
```

### Example 5: Generate OCT JWK (256-bit symmetric key)

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "generated-oct-jwk",
    "description": "Auto-generated 256-bit symmetric key",
    "type": "OCT",
    "oct": {
      "keySize": 256
    }
  }'
```

### Example 6: Generate OKP JWK (Ed25519)

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "generated-okp-jwk",
    "description": "Auto-generated Ed25519 JWK",
    "type": "OKP",
    "okp": {
      "crv": "Ed25519"
    }
  }'
```

### Example 7: Generate OKP JWK (X25519 for key exchange)

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "generated-x25519-jwk",
    "description": "Auto-generated X25519 JWK for key exchange",
    "type": "OKP",
    "okp": {
      "crv": "X25519"
    }
  }'
```

## Notes and Warnings

- **JWK Name**: 
  - Must be unique within the project
- **JWK Types and Use Cases**: 
  - **RSA**: 
    - Recommended for most use cases, supports signing and encryption
    - Key sizes: 2048 (standard), 3072 (high security), 4096 (maximum security)
    - Larger keys provide better security but slower operations
    - Use for JWT signing (RS256, RS384, RS512) and encryption (RSA-OAEP)
  - **EC (Elliptic Curve)**: 
    - Smaller key sizes, good for constrained environments
    - Curves: P-256 (256-bit), P-384 (384-bit), P-521 (521-bit)
    - Use for JWT signing (ES256, ES384, ES512)
    - More efficient than RSA for same security level
  - **OCT (Symmetric Key)**: 
    - Symmetric keys for encryption and signing
    - Key sizes: 128, 192, 256 bits
    - Use for JWT signing (HS256, HS384, HS512) and encryption (AES)
    - Requires secure key distribution
  - **OKP (Octet Key Pair)**: 
    - Modern curve-based keys
    - Ed25519/Ed448: For signing (EdDSA algorithm)
    - X25519/X448: For key exchange (ECDH)
    - Very efficient and secure
    - Use for modern applications requiring high performance
- **Type-Specific Parameters**: 
  - Each JWK type requires its corresponding parameter object (`rsa`, `ec`, `oct`, or `okp`)
  - Parameters must match the selected `type`
  - Invalid parameter combinations will result in validation errors
- **Automatic Deployment**: 
  - JWK is automatically deployed after generation
  - Deployment results are returned in the response
- **Security**: 
  - Generated keys are cryptographically secure
  - Private keys are encrypted at rest
  - Key generation uses secure random number generators
- **Performance Considerations**: 
  - RSA: Larger key sizes (4096) are slower but more secure
  - EC: Faster than RSA for equivalent security
  - OKP: Fastest option, ideal for high-performance scenarios
  - OCT: Fastest for symmetric operations
- **Permissions**: 
  - Requires `ROLE_API_SECURITY` permission
  - Requires `ROLE_DEPLOY_UNDEPLOY_PROXIES` permission for deployment

## Related Documentation

- [List JWKs](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-jwks/) - List all JWKs
- [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) - Create JWK from other sources
- [Get JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/get-jwk/) - Get a specific JWK

