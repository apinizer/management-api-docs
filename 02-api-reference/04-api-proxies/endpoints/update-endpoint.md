# Update Endpoint

## Overview

Updates an existing endpoint (API method) in an API proxy. Only provided fields are updated; omitted fields remain unchanged.

## Endpoint

```
PATCH /apiops/projects/{projectName}/apiProxies/{apiProxyName}/endpoints/{endpointId}/
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
  "name": "/api/users/updated",
  "description": "Updated endpoint description",
  "httpMethod": "GET",
  "backendResourceUrl": "/users/v2",
  "backendHttpMethod": "GET"
}
```

#### Request Body Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| name | string | No | - | Endpoint path/name (if provided, must be unique with httpMethod) |
| description | string | No | - | Endpoint description |
| httpMethod | string | No | - | HTTP method for the endpoint |
| backendResourceUrl | string | No | - | Backend resource URL |
| backendHttpMethod | string | No | - | HTTP method for backend call |

**Note:** All fields are optional. Only provided fields are updated.

**Enum: httpMethod / backendHttpMethod (EnumHttpRequestMethod)**
- `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `TRACE`, `ALL`

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
- Invalid field values

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

### Example 1: Update Endpoint Description Only

```bash
curl -X PATCH \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Updated endpoint description"
  }'
```

### Example 2: Update Backend URL

```bash
curl -X PATCH \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "backendResourceUrl": "/users/v2",
    "backendHttpMethod": "GET"
  }'
```

### Example 3: Update Multiple Fields

```bash
curl -X PATCH \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "/api/users/updated",
    "description": "Updated endpoint",
    "backendResourceUrl": "/users/v2"
  }'
```

## Usage Scenarios

### Scenario 1: Update Description Only

Update only the endpoint description without changing other fields.

**Request Body:**
```json
{
  "description": "New description"
}
```

### Scenario 2: Change Backend URL

Update the backend URL that the endpoint routes to.

**Request Body:**
```json
{
  "backendResourceUrl": "https://new-backend.example.com/api/users"
}
```

### Scenario 3: Change HTTP Method

Change the HTTP method for the endpoint.

**Request Body:**
```json
{
  "httpMethod": "POST"
}
```

**Note:** Ensure the new `name` and `httpMethod` combination doesn't conflict with existing endpoints.

## Notes and Warnings

- **Partial Updates**: Only provided fields are updated. Omitted fields remain unchanged
- **Unique Combination**: If updating `name` or `httpMethod`, ensure the new combination doesn't conflict with existing endpoints
- **Endpoint ID**: Use [List Endpoints](./list-endpoints.md) to get endpoint IDs
- **Permissions**: Requires `ROLE_MANAGE_PROXIES` permission

## Related Documentation

- [List Endpoints](./list-endpoints.md) - List all endpoints
- [Get Endpoint](./get-endpoint.md) - Get endpoint details
- [Create Endpoint](./create-endpoint.md) - Create a new endpoint
- [Delete Endpoint](./delete-endpoint.md) - Delete an endpoint
- [Update Endpoint Status](./update-endpoint-status.md) - Enable/disable endpoint

