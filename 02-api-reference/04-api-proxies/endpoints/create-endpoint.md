# Create Endpoint

## Overview

Creates a new REST endpoint (API method) in an API proxy. This operation is only available for REST API proxies.

## Endpoint

```
POST /apiops/projects/{projectName}/apiProxies/{apiProxyName}/endpoints/
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
| apiProxyName | string | Yes | API Proxy name (must be REST type) |

### Request Body

#### Full JSON Body Example

```json
{
  "name": "/api/users",
  "description": "Get all users",
  "httpMethod": "GET",
  "backendResourceUrl": "/users",
  "backendHttpMethod": "GET"
}
```

#### Request Body Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| name | string | Yes | - | Endpoint path/name (must be unique with httpMethod) |
| description | string | No | - | Endpoint description |
| httpMethod | string | Yes | - | HTTP method for the endpoint |
| backendResourceUrl | string | Yes | - | Backend resource URL |
| backendHttpMethod | string | Yes | - | HTTP method for backend call |

**Enum: httpMethod / backendHttpMethod (EnumHttpRequestMethod)**
- `GET` - GET method
- `POST` - POST method
- `PUT` - PUT method
- `DELETE` - DELETE method
- `PATCH` - PATCH method
- `OPTIONS` - OPTIONS method
- `HEAD` - HEAD method
- `TRACE` - TRACE method
- `ALL` - All methods

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
  "error_description": "Endpoint can only be added to REST API Proxies!"
}
```

**Common Causes:**
- API Proxy is not REST type (SOAP proxies don't support manual endpoint creation)
- Endpoint name and HTTP method combination already exists
- Missing required fields (name, httpMethod, backendResourceUrl, backendHttpMethod)
- Invalid HTTP method values

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

### Example 1: Create GET Endpoint

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "/api/users",
    "description": "Get all users",
    "httpMethod": "GET",
    "backendResourceUrl": "/users",
    "backendHttpMethod": "GET"
  }'
```

### Example 2: Create POST Endpoint

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "/api/users",
    "description": "Create a new user",
    "httpMethod": "POST",
    "backendResourceUrl": "/users",
    "backendHttpMethod": "POST"
  }'
```

### Example 3: Create Endpoint with Different Backend Method

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "/api/users/search",
    "description": "Search users",
    "httpMethod": "POST",
    "backendResourceUrl": "/users/search",
    "backendHttpMethod": "GET"
  }'
```

## Usage Scenarios

### Scenario 1: Add Custom Endpoint

Add a custom endpoint that wasn't in the original OpenAPI specification.

**Request Body:**
```json
{
  "name": "/api/custom-endpoint",
  "description": "Custom endpoint",
  "httpMethod": "GET",
  "backendResourceUrl": "/custom",
  "backendHttpMethod": "GET"
}
```

### Scenario 2: Add Endpoint with Different Backend URL

Create an endpoint that routes to a different backend URL.

**Request Body:**
```json
{
  "name": "/api/external-data",
  "description": "Fetch external data",
  "httpMethod": "GET",
  "backendResourceUrl": "https://external-api.com/data",
  "backendHttpMethod": "GET"
}
```

## Notes and Warnings

- **REST Only**: Endpoints can only be added to REST API proxies. SOAP endpoints are defined in the WSDL
- **Unique Combination**: The combination of `name` and `httpMethod` must be unique within the API proxy
- **Default Active**: New endpoints are created with `active: true` by default
- **Backend URL**: The `backendResourceUrl` can be a relative path or absolute URL
- **Permissions**: Requires `ROLE_MANAGE_PROXIES` permission

## Related Documentation

- [List Endpoints](./list-endpoints.md) - List all endpoints
- [Get Endpoint](./get-endpoint.md) - Get endpoint details
- [Update Endpoint](./update-endpoint.md) - Update an endpoint
- [Delete Endpoint](./delete-endpoint.md) - Delete an endpoint

