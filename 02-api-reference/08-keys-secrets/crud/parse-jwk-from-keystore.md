---
layout: default
permalink: /02-api-reference/08-keys-secrets/crud/parse-jwk-from-keystore/
---

# Parse JWK from Keystore

## Overview

Parses a JWK (JSON Web Key) from a keystore alias and creates it. This is a convenience endpoint for extracting JWKs from keystores.

## Endpoint

```
POST /apiops/projects/{projectName}/jwks/parse-from-keystore
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
  "description": "JWK from keystore",
  "keyStoreName": "my-keystore",
  "environmentName": "production",
  "aliasName": "my-alias",
  "useType": "SIGN",
  "keystoreAlgorithm": "RSA"
}
```

### Request Body Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | JWK name (unique identifier) |
| description | string | No | JWK description |
| keyStoreName | string | Yes | Keystore name |
| environmentName | string | Yes | Environment name |
| aliasName | string | Yes | Alias name in keystore |
| useType | string | Yes | Use type: `SIGN`, `ENCRYPT` |
| keystoreAlgorithm | string | Yes | Keystore algorithm (e.g., `RSA`) |

## Response

Same as [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) response format.

## cURL Example

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/parse-from-keystore" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-jwk",
    "description": "JWK from keystore",
    "keyStoreName": "my-keystore",
    "environmentName": "production",
    "aliasName": "my-alias",
    "useType": "SIGN",
    "keystoreAlgorithm": "RSA"
  }'
```

## Related Documentation

- [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) - Create JWK with source type KEYSTORE
- [List JWKs](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-jwks/) - List all JWKs

