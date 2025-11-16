---
layout: default
permalink: /02-api-reference/04-api-proxies/endpoints/list-endpoint-policies/
---

# List Endpoint Policies

## Overview

Retrieves all policies (request, response, and error) for a specific endpoint (API method). This endpoint returns the same information as [Get Endpoint](/management-api-docs/02-api-reference/04-api-proxies/endpoints/get-endpoint/) but includes policy details.

## Endpoint

```
GET /apiops/projects/{projectName}/apiProxies/{apiProxyName}/endpoints/{endpointId}/policies/
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
  "backendHttpMethod": "GET",
  "requestPolicyList": [
    {
      "type": "policy-api-based-throttling",
      "name": "throttling-policy",
      "description": "Throttling policy",
      "active": true
    }
  ],
  "responsePolicyList": [
    {
      "type": "policy-script",
      "name": "response-logging",
      "description": "Response logging",
      "active": true
    }
  ],
  "errorPolicyList": []
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
| requestPolicyList | array | List of request pipeline policies |
| responsePolicyList | array | List of response pipeline policies |
| errorPolicyList | array | List of error pipeline policies |

#### Policy Object Fields (in policy lists)

| Field | Type | Description |
|-------|------|-------------|
| type | string | Policy type |
| name | string | Policy name |
| description | string | Policy description |
| active | boolean | Whether policy is active |

**Note:** Policy objects contain only basic information. For full policy details, use the [Policies API](/management-api-docs/05-policies/).

### EnumHttpRequestMethod

- `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `TRACE`, `ALL`

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
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/policies/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Full JSON Body Example

This endpoint does not require a request body.

## Notes and Warnings

- **Endpoint ID**: Use [List Endpoints](/management-api-docs/02-api-reference/04-api-proxies/endpoints/list-endpoints/) to get endpoint IDs
- **Policy Details**: Policy objects contain basic information only. For full policy configuration, use the [Policies API](/management-api-docs/05-policies/)
- **Empty Lists**: If no policies exist in a pipeline, an empty array is returned
- **Permissions**: Requires `ROLE_MANAGE_PROXIES` permission

## Related Documentation

- [List Endpoints](/management-api-docs/02-api-reference/04-api-proxies/endpoints/list-endpoints/) - List all endpoints
- [Get Endpoint](/management-api-docs/02-api-reference/04-api-proxies/endpoints/get-endpoint/) - Get endpoint details (without policies)
- [Policies API](/management-api-docs/05-policies/) - Policy management API
