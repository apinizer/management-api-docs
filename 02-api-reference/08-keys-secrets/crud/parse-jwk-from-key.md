---
layout: default
permalink: /02-api-reference/08-keys-secrets/crud/parse-jwk-from-key/
---

# Parse JWK from Key

## Overview

Parses a JWK (JSON Web Key) from an existing key (public or private) and creates it. This is a convenience endpoint for extracting JWKs from keys.

## Endpoint

```
POST /apiops/projects/{projectName}/jwks/parse-from-key
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
  "name": "my-jwk",
  "description": "JWK from key",
  "keyName": "my-key",
  "environmentId": "env-id-123",
  "useType": "SIGN",
  "keystoreAlgorithm": "RSA"
}
```

### Request Body Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | JWK name (unique identifier) |
| description | string | No | JWK description |
| keyName | string | Yes | Key name |
| environmentId | string | Yes | Environment ID |
| useType | string | Yes | Use type: `SIGN`, `ENCRYPT` |
| keystoreAlgorithm | string | Yes | Keystore algorithm (e.g., `RSA`) |

## Response

Same as [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) response format.

## cURL Example

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/parse-from-key" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-jwk",
    "description": "JWK from key",
    "keyName": "my-key",
    "environmentId": "env-id-123",
    "useType": "SIGN",
    "keystoreAlgorithm": "RSA"
  }'
```

## Related Documentation

- [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) - Create JWK with source type PUBLIC_KEY or PRIVATE_KEY
- [List JWKs](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-jwks/) - List all JWKs

