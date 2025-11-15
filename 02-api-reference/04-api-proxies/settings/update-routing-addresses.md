# Update Routing Addresses

## Overview

Updates routing addresses (backend endpoints) for an API proxy. Routing addresses define where API requests are forwarded.

## Endpoint

```
PATCH /apiops/projects/{projectName}/apiProxies/{apiProxyName}/settings/addresses/
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

### Request Body

#### Full JSON Body Example

```json
[
  {
    "address": "https://backend1.example.com",
    "weight": 100,
    "soapType": "SOAP11"
  },
  {
    "address": "https://backend2.example.com",
    "weight": 50,
    "soapType": "SOAP11"
  }
]
```

#### Request Body Fields

The request body is an array of routing address objects.

**Routing Address Object:**

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| address | string | Yes | - | Backend address URL |
| weight | integer | No | 1 | Load balancing weight (required if loadBalanceAlgorithm=WEIGHTED) |
| soapType | string | No* | SOAP11 | SOAP version (required if API type is SOAP) |

**Enum: soapType (EnumSoapApiPortType)**
- `SOAP11` - SOAP 1.1
- `SOAP12` - SOAP 1.2

**Note:** 
- For REST APIs, `soapType` is not required
- For SOAP APIs, `soapType` defaults to `SOAP11` if not provided
- Weight is used when load balancing algorithm is `WEIGHTED`

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
  "error_description": "Address is required"
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

### Example 1: Update REST API Backend Addresses

```bash
curl -X PATCH \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/settings/addresses/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "address": "https://backend1.example.com",
      "weight": 100
    },
    {
      "address": "https://backend2.example.com",
      "weight": 50
    }
  ]'
```

### Example 2: Update SOAP API Backend Addresses

```bash
curl -X PATCH \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/settings/addresses/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "address": "https://soap-backend.example.com/Service",
      "weight": 100,
      "soapType": "SOAP11"
    },
    {
      "address": "https://soap-backend2.example.com/Service",
      "weight": 50,
      "soapType": "SOAP12"
    }
  ]'
```

## Usage Scenarios

### Scenario 1: Single Backend Address

Configure a single backend address.

**Request Body:**
```json
[
  {
    "address": "https://api.example.com"
  }
]
```

### Scenario 2: Load Balanced Backends

Configure multiple backend addresses with weights for load balancing.

**Request Body:**
```json
[
  {
    "address": "https://backend1.example.com",
    "weight": 100
  },
  {
    "address": "https://backend2.example.com",
    "weight": 50
  },
  {
    "address": "https://backend3.example.com",
    "weight": 25
  }
]
```

**Note:** Ensure load balancing algorithm is set to `WEIGHTED` (via routing settings).

## Notes and Warnings

- **Address Format**: Must be a valid URL (http:// or https://)
- **Weight**: Used for weighted load balancing (higher weight = more traffic)
- **SOAP Type**: Required for SOAP APIs, defaults to `SOAP11` if not provided
- **Empty Array**: Empty array removes all routing addresses (routing will fail)
- **Load Balancing**: Configure load balancing algorithm separately (via routing settings)
- **Permissions**: Requires `ROLE_MANAGE_PROXIES` permission

## Related Documentation

- [Update Connection Settings](./update-connection-settings.md) - Update connection settings
- [Update Routing Status](./update-routing-status.md) - Update routing status
- [Get API Proxy](../crud/get-api-proxy.md) - Get API proxy details

