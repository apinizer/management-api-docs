---
layout: default
permalink: /02-api-reference/08-keys-secrets/crud/delete-key/
---

# Delete Key

## Overview

Deletes an existing cryptographic key and undeploys it from all environments.

## Endpoint

```
DELETE /apiops/projects/{projectName}/keys/{keyName}/
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
| keyName | string | Yes | Name of the key to delete |

## Response

### Success Response (200 OK)

```json
{
  "success": true,
  "deploymentResult": {
    "success": true,
    "message": "Undeployment completed successfully",
    "environmentResults": [
      {
        "environmentName": "production",
        "success": true,
        "message": "Undeployed successfully"
      }
    ]
  }
}
```

## cURL Example

```bash
curl -X DELETE \
  "https://demo.apinizer.com/apiops/projects/MyProject/keys/my-key/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Related Documentation

- [List Keys](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-keys/) - List all keys
- [Create Key](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-key/) - Create a new key

