---
layout: default
permalink: /02-api-reference/08-keys-secrets/crud/get-keystore/
---

# Get Keystore

## Overview

Retrieves detailed information about a specific keystore including its complete configuration and keystore file content.

## Endpoint

```
GET /apiops/projects/{projectName}/keystores/{keystoreName}/
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
| keystoreName | string | Yes | Name of the keystore |

## Response

Same as [List Keystores](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-keystores/) response format, but returns a single keystore.

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/projects/MyProject/keystores/my-keystore/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Related Documentation

- [List Keystores](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-keystores/) - List all keystores
- [Create Keystore](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-keystore/) - Create a new keystore

