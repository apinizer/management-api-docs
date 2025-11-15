# Update Endpoint Status

## Overview

Enables or disables an endpoint (API method) in an API proxy. When disabled, the endpoint is not accessible.

## Endpoint

```
PATCH /apiops/projects/{projectName}/apiProxies/{apiProxyName}/endpoints/{endpointId}/status/
```

## Authentication

Requires a Personal API Access Token.

**Header:**
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
| apiProxyName | string | Yes | API Proxy name |
| endpointId | string | Yes | Endpoint ID |

### Request Body

#### Full JSON Body Example

```json
{
  "active": false
}
```

#### Request Body Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| active | boolean | Yes | - | Whether endpoint is active/enabled (`true` = enabled, `false` = disabled) |

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
  "error_description": "Endpoint with ID (endpoint-id) was not found!"
}
```

**Common Causes:**
- Endpoint ID does not exist
- Missing `active` field

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

### Example 1: Disable Endpoint

```bash
curl -X PATCH \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/status/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "active": false
  }'
```

### Example 2: Enable Endpoint

```bash
curl -X PATCH \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/status/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "active": true
  }'
```

## Notes and Warnings

- **Endpoint ID**: Use [List Endpoints](./list-endpoints.md) to get endpoint IDs
- **Disabled Endpoints**: Disabled endpoints return 404 Not Found when accessed
- **Policies**: Policies remain associated with the endpoint even when disabled
- **Permissions**: Requires `ROLE_MANAGE_PROXIES` permission

## Related Documentation

- [List Endpoints](./list-endpoints.md) - List all endpoints
- [Get Endpoint](./get-endpoint.md) - Get endpoint details
- [Update Endpoint](./update-endpoint.md) - Update endpoint configuration
- [Delete Endpoint](./delete-endpoint.md) - Delete an endpoint
