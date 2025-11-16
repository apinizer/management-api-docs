---
layout: default
permalink: /02-api-reference/09-api-proxy-groups/deployment/deploy-api-proxy-group/
---

# Deploy API Proxy Group

## Overview

Deploys an API Proxy Group to a specific environment. All API Proxies in the group are deployed together.

## Endpoint

```
POST /apiops/projects/{projectName}/apiProxyGroups/{apiProxyGroupName}/environments/{environmentName}/
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
| apiProxyGroupName | string | Yes | API Proxy Group name |
| environmentName | string | Yes | Environment name to deploy to |

### Request Body

None.

## Response

#### Success Response (200 OK)

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

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Indicates if the request was successful |
| deploymentResult | object | Deployment result. See [Deployment Result Object](#deployment-result-object) |

### Deployment Result Object

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Overall deployment success status |
| message | string | Deployment message |
| environmentResults | array[object] | Results per environment |

### Environment Result Object

| Field | Type | Description |
|-------|------|-------------|
| environmentName | string | Environment name |
| success | boolean | Deployment success status for this environment |
| message | string | Deployment message for this environment |

### Error Response (400 Bad Request)

```json
{
  "error": "bad_request",
  "error_description": "API Proxy Group (PaymentAPIGroup) is not found or user does not have privilege to access it!"
}
```

or

```json
{
  "error": "bad_request",
  "error_description": "Environment (production) is not found or user does not have privilege to access it!"
}
```

## cURL Example

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxyGroups/PaymentAPIGroup/environments/production/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Notes and Warnings

- **Group Deployment**: 
  - All API Proxies in the group are deployed together
  - Group-level settings (CORS, cache, etc.) are also deployed
- **Environment Must Exist**: 
  - Environment must exist and be accessible
- **Permissions**: 
  - Requires `ROLE_MANAGE_PROXY_GROUPS` permission
  - Requires `ROLE_DEPLOY_UNDEPLOY_PROXIES` permission
  - User must have access to the project and environment

## Related Documentation

- [Undeploy API Proxy Group](/02-api-reference/09-api-proxy-groups/deployment/undeploy-api-proxy-group) - Undeploy group from environment
- [List Environments](/02-api-reference/09-api-proxy-groups/deployment/list-environments) - List environments for group
