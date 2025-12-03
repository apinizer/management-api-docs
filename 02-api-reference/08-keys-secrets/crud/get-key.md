---
layout: default
permalink: /02-api-reference/08-keys-secrets/crud/get-key/
---

# Get Key

## Overview

Retrieves detailed information about a specific cryptographic key including its complete configuration and key material.

## Endpoint

```
GET /apiops/projects/{projectName}/keys/{keyName}/
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

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| keyName | string | Yes | Name of the key |

## Response

Same as [List Keys](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-keys/) response format, but returns a single key.

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/projects/MyProject/keys/my-key/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Related Documentation

- [List Keys](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-keys/) - List all keys
- [Create Key](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-key/) - Create a new key

