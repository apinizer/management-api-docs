---
layout: default
permalink: /02-api-reference/09-api-proxy-groups/crud/list-api-proxy-groups/
---

# List API Proxy Groups

## Overview

Retrieves all API Proxy Groups for a specified project. API Proxy Groups allow you to group multiple API Proxies together and manage them as a single unit.

## Endpoint

```
GET /apiops/projects/{projectName}/apiProxyGroups/
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

### Query Parameters

None.

## Response

### Success Response (200 OK)

```json
{
  "success": true,
  "resultList": [
    {
      "id": "group-id-1",
      "name": "PaymentAPIGroup",
      "description": "Payment API Group"
    },
    {
      "id": "group-id-2",
      "name": "UserAPIGroup",
      "description": "User Management API Group"
    }
  ],
  "resultCount": 2
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Indicates if the request was successful |
| resultList | array[object] | List of API Proxy Groups |
| resultCount | integer | Total number of API Proxy Groups |

### API Proxy Group Object

| Field | Type | Description |
|-------|------|-------------|
| id | string | API Proxy Group ID |
| name | string | API Proxy Group name |
| description | string | API Proxy Group description |

### Notes

- Returns only basic information (id, name, description)
- Empty list (`[]`) is returned if no groups exist
- `resultCount` is 0 if no groups exist

### Error Response (401 Unauthorized)

```json
{
  "error": "unauthorized_client",
  "error_description": "Invalid token"
}
```

### Error Response (404 Not Found)

```json
{
  "error": "not_found",
  "error_description": "Project(MyProject) was not found or user does not have privilege to access it!"
}
```

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxyGroups/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Notes and Warnings

- **Basic Information**: 
  - Returns only basic group information
  - Does not include API Proxy members or detailed settings
- **Permissions**: 
  - Requires `ROLE_MANAGE_PROXY_GROUPS` permission
  - User must have access to the project

## Related Documentation

- [Create API Proxy Group](/02-api-reference/09-api-proxy-groups/crud/02-api-reference/09-api-proxy-groups/crud/create-api-proxy-group/) - Create a new API Proxy Group
- [Get Environments](/02-api-reference/09-api-proxy-groups/crud/02-api-reference/09-api-proxy-groups/deployment/list-environments/) - Get environments for a group
