---
layout: default
permalink: /02-api-reference/08-keys-secrets/crud/delete-keystore/
---

# Delete Keystore

## Overview

Deletes an existing keystore and undeploys it from all environments.

## Endpoint

```
DELETE /apiops/projects/{projectName}/keystores/{keystoreName}/
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
| keystoreName | string | Yes | Name of the keystore to delete |

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
  "https://demo.apinizer.com/apiops/projects/MyProject/keystores/my-keystore/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Related Documentation

- [List Keystores](/management-api-docs/02-api-reference/08-keys-secrets/crud/list-keystores/) - List all keystores
- [Create Keystore](/management-api-docs/02-api-reference/08-keys-secrets/crud/create-keystore/) - Create a new keystore

