---
layout: default
permalink: /02-api-reference/08-keys-secrets/crud/parse-jwk-from-url/
---

# Parse JWK from URL

## Overview

Parses a JWK (JSON Web Key) from a URL and creates it. This is a convenience endpoint that combines parsing and creation in a single operation.

## Endpoint

```
POST /apiops/projects/{projectName}/jwks/parse-from-url
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
  "description": "JWK from URL",
  "url": "https://example.com/.well-known/jwks.json",
  "urlOptionConnectTimeout": 5000,
  "urlOptionReadTimeout": 10000,
  "urlOptionSizeLimit": 1048576,
  "kid": "key-id-1"
}
```

**Note:** If the URL returns a JWK Set (array of keys), use `kid` to specify which key to use from the array.

### Request Body Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | JWK name (unique identifier) |
| description | string | No | JWK description |
| url | string | Yes | URL to fetch JWK from |
| urlOptionConnectTimeout | integer | No | Connection timeout in milliseconds (default: 5000) |
| urlOptionReadTimeout | integer | No | Read timeout in milliseconds (default: 10000) |
| urlOptionSizeLimit | integer | No | Maximum response size in bytes (default: 1048576) |
| kid | string | Conditional | Key ID (kid) - Required when the URL returns a JWK Set (array of keys) to specify which key to use |

## Response

Same as [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) response format.

## cURL Example

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/jwks/parse-from-url" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-jwk",
    "description": "JWK from URL",
    "url": "https://example.com/.well-known/jwks.json"
  }'
```

## Related Documentation

- [Create JWK](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-jwk/) - Create JWK with source type URL
- [List JWKs](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-jwks/) - List all JWKs

