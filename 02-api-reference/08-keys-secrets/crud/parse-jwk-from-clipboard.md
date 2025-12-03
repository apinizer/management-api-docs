---
layout: default
permalink: /02-api-reference/08-keys-secrets/crud/parse-jwk-from-clipboard/
---

# Parse JWK from Clipboard

## Overview

Parses a JWK (JSON Web Key) from a JSON string (clipboard) and creates it. This is a convenience endpoint for creating JWKs from copied JSON strings.

## Endpoint

```
POST /apiops/projects/{projectName}/jwks/parse-from-clipboard
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
  "description": "JWK from JSON string",
  "jwkStr": "{\"kty\":\"RSA\",\"n\":\"...\",\"e\":\"AQAB\"}",
  "kid": "key-id-1"
}
```

**Note:** If `jwkStr` contains a JWK Set (array of keys), use `kid` to specify which key to use from the array.

### Request Body Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | JWK name (unique identifier) |
| description | string | No | JWK description |
| jwkStr | string | Yes | JWK JSON string |
| kid | string | Conditional | Key ID (kid) - Required when `jwkStr` contains a JWK Set (array of keys) to specify which key to use |

## Response

Same as [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) response format.

## cURL Example

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/parse-from-clipboard" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-jwk",
    "description": "JWK from clipboard",
    "jwkStr": "{\"kty\":\"RSA\",\"n\":\"...\",\"e\":\"AQAB\"}"
  }'
```

## Related Documentation

- [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) - Create JWK with source type COPY_PASTE
- [List JWKs](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-jwks/) - List all JWKs

