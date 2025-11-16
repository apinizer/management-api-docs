---
layout: default
permalink: /02-api-reference/04-api-proxies/endpoints/get-endpoint/
---

# Get Endpoint

## Overview

Retrieves detailed information about a specific endpoint (API method). Policy details are not included by default.

## Endpoint

```
GET /apiops/projects/{projectName}/apiProxies/{apiProxyName}/endpoints/{endpointId}/
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
| apiProxyName | string | Yes | API Proxy name |
| endpointId | string | Yes | Endpoint ID |

### Query Parameters

None

## Response

### Success Response (200 OK)

```json
{
  "id": "endpoint-id",
  "endpoint": "/api/users",
  "description": "Get all users",
  "active": true,
  "httpMethod": "GET",
  "backendResourceUrl": "/users",
  "backendHttpMethod": "GET"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| id | string | Endpoint unique identifier |
| endpoint | string | Endpoint path/name |
| description | string | Endpoint description |
| active | boolean | Whether endpoint is active/enabled |
| httpMethod | string | HTTP method for the endpoint |
| backendResourceUrl | string | Backend resource URL |
| backendHttpMethod | string | HTTP method for backend call |

### EnumHttpRequestMethod

- `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `TRACE`, `ALL`

**Note:** Policy lists are not included. Use [List Endpoint Policies](/02-api-reference/04-api-proxies/endpoints/list-endpoint-policies) to retrieve policy details.

### Error Response (400 Bad Request)

```json
{
  "error": "bad_request",
  "error_description": "Endpoint with ID (endpoint-id) was not found!"
}
```

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
  "error_description": "ApiProxy (name: MyAPI) was not found!"
}
```

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Full JSON Body Example

This endpoint does not require a request body.

## Notes and Warnings

- **Endpoint ID**: Use [List Endpoints](/02-api-reference/04-api-proxies/endpoints/list-endpoints) to get endpoint IDs
- **Policy Details**: Policy lists are not included. Use [List Endpoint Policies](/02-api-reference/04-api-proxies/endpoints/list-endpoint-policies) to retrieve policies
- **Permissions**: Requires `ROLE_MANAGE_PROXIES` permission

## Related Documentation

- [List Endpoints](/02-api-reference/04-api-proxies/endpoints/list-endpoints) - List all endpoints
- [List Endpoint Policies](/02-api-reference/04-api-proxies/endpoints/list-endpoint-policies) - List endpoint policies
- [Update Endpoint](/02-api-reference/04-api-proxies/endpoints/update-endpoint) - Update an endpoint
- [Delete Endpoint](/02-api-reference/04-api-proxies/endpoints/delete-endpoint) - Delete an endpoint
