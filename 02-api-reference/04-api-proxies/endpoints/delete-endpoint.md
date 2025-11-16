---
layout: default
permalink: /02-api-reference/04-api-proxies/endpoints/delete-endpoint/
---

# Delete Endpoint

## Overview

Deletes an endpoint (API method) from an API proxy. This operation is only available for REST API proxies. The endpoint is permanently removed.

## Endpoint

```
DELETE /apiops/projects/{projectName}/apiProxies/{apiProxyName}/endpoints/{endpointId}/
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
| apiProxyName | string | Yes | API Proxy name (must be REST type) |
| endpointId | string | Yes | Endpoint ID |

### Query Parameters

None

### Request Body

This endpoint does not require a request body.

## Response

### Success Response (200 OK)

```json
{
  "success": true
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Indicates if the request was successful |

### Error Response (400 Bad Request)

```json
{
  "error": "bad_request",
  "error_description": "Endpoint can only be deleted from REST API Proxies!"
}
```

### Common Causes

- API Proxy is not REST type (SOAP endpoints cannot be deleted manually)
- Endpoint ID does not exist

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
curl -X DELETE \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Full JSON Body Example

This endpoint does not require a request body.

## Notes and Warnings

- **REST Only**: Endpoints can only be deleted from REST API proxies. SOAP endpoints are managed through WSDL reparsing
- **Permanent Deletion**: Endpoint deletion is permanent and cannot be undone
- **Policies**: All policies associated with the endpoint are also deleted
- **Endpoint ID**: Use [List Endpoints](../../../../02-api-reference/04-api-proxies/endpoints/list-endpoints/) to get endpoint IDs
- **Permissions**: Requires `ROLE_MANAGE_PROXIES` permission

## Related Documentation

- [List Endpoints](../../../../02-api-reference/04-api-proxies/endpoints/list-endpoints/) - List all endpoints
- [Get Endpoint](../../../../02-api-reference/04-api-proxies/endpoints/get-endpoint/) - Get endpoint details
- [Create Endpoint](../../../../02-api-reference/04-api-proxies/endpoints/create-endpoint/) - Create a new endpoint
- [Update Endpoint](../../../../02-api-reference/04-api-proxies/endpoints/update-endpoint/) - Update an endpoint
