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

```json
{
  "name": "generated-jwk",
  "description": "Auto-generated RSA JWK",
  "type": "RSA"
}
```

### Request Body Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | JWK name (unique identifier) |
| description | string | No | JWK description |
| type | string | Yes | JWK type: `RSA`, `EC`, `OCT`, `OKP` |

### Notes

- `name` must be unique within the project
- `type` determines the cryptographic algorithm:
  - `RSA`: RSA key pair
  - `EC`: Elliptic Curve key pair
  - `OCT`: Octet sequence (symmetric key)
  - `OKP`: Octet Key Pair (Edwards Curve or Montgomery Curve)
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

## cURL Example

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "generated-jwk",
    "description": "Auto-generated RSA JWK",
    "type": "RSA"
  }'
```

## Notes and Warnings

- **JWK Name**: 
  - Must be unique within the project
- **JWK Types**: 
  - `RSA`: Recommended for most use cases, supports signing and encryption
  - `EC`: Smaller key sizes, good for constrained environments
  - `OCT`: Symmetric keys for encryption
  - `OKP`: Modern curve-based keys (Ed25519, X25519)
- **Automatic Deployment**: 
  - JWK is automatically deployed after generation
  - Deployment results are returned in the response
- **Security**: 
  - Generated keys are cryptographically secure
  - Private keys are encrypted at rest
- **Permissions**: 
  - Requires `ROLE_API_SECURITY` permission
  - Requires `ROLE_DEPLOY_UNDEPLOY_PROXIES` permission for deployment

## Related Documentation

- [List JWKs](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-jwks/) - List all JWKs
- [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) - Create JWK from other sources
- [Get JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/get-jwk/) - Get a specific JWK

