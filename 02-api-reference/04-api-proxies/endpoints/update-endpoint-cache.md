---
layout: default
permalink: /02-api-reference/04-api-proxies/endpoints/update-endpoint-cache/
---

# Update Endpoint Cache Settings

## Overview

Updates cache settings for a specific endpoint/method. Endpoint-level cache settings override API Proxy-level cache settings for the specific endpoint.

## Endpoint

```
PATCH /apiops/projects/{projectName}/apiProxies/{apiProxyName}/endpoints/{endpointId}/cache/
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
| Content-Type | application/json | Yes |

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| apiProxyName | string | Yes | API Proxy name |
| endpointId | string | Yes | Endpoint ID (method ID) |

### Request Body

The request body uses the same `CacheSettings` structure as API Proxy-level cache settings. See [Update Cache Settings](../settings/update-cache-settings.md) for detailed field descriptions.

#### Full JSON Body Example - Basic Cache Configuration

```json
{
  "name": "Endpoint Cache Settings",
  "description": "Cache configuration for this endpoint",
  "cacheActive": true,
  "cacheOnlyHttpGetRequests": false,
  "cacheKeyType": "QUERY_PARAMS",
  "cacheStorageType": "LOCAL",
  "capacity": 1000,
  "ttl": 3600,
  "handlingAction": "STOP",
  "invalidationRequiresAuthn": false,
  "cacheNullValue": false,
  "variableList": []
}
```

#### Full JSON Body Example - Custom Cache Key

```json
{
  "name": "Endpoint Cache with Custom Key",
  "description": "Cache using custom variables",
  "cacheActive": true,
  "cacheOnlyHttpGetRequests": false,
  "cacheKeyType": "CUSTOM",
  "cacheStorageType": "DISTRIBUTED",
  "capacity": 5000,
  "ttl": 7200,
  "handlingAction": "CONTINUE",
  "invalidationRequiresAuthn": true,
  "cacheNullValue": true,
  "variableList": [
    {
      "name": "userId",
      "type": "HEADER",
      "dataType": "STRING"
    },
    {
      "name": "apiVersion",
      "type": "PARAMETER",
      "dataType": "STRING"
    }
  ]
}
```

#### Request Body Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| name | string | Yes | - | Cache settings name |
| description | string | No | - | Cache settings description |
| cacheActive | boolean | No | false | Enable/disable cache for this endpoint |
| cacheOnlyHttpGetRequests | boolean | No | true | Cache only GET requests (if false, caches all methods) |
| cacheKeyType | string | No | QUERY_PARAMS | Cache key type. See [EnumCacheKeyType](/#enumcachekeytype) |
| cacheStorageType | string | No | DISTRIBUTED | Cache storage type. See [EnumCacheStorageType](/#enumcachestoragetype) |
| capacity | integer | No | - | Maximum cache capacity (number of entries) |
| ttl | integer | No | - | Time to live in seconds |
| handlingAction | string | Yes | - | Cache handling action when cache hit occurs. See [EnumCacheHandlingAction](/#enumcachehandlingaction) |
| invalidationRequiresAuthn | boolean | No | false | Require authentication for cache invalidation |
| cacheNullValue | boolean | No | false | Cache null/empty responses |
| variableList | array | No | [] | List of variables for custom cache key (if cacheKeyType=CUSTOM). See [Variable Object](/#variable-object) |

### EnumCacheKeyType (cacheKeyType)

- `QUERY_PARAMS` - Use query parameters as cache key
- `CUSTOM` - Use custom variables as cache key (requires variableList)

### EnumCacheStorageType (cacheStorageType)

- `LOCAL` - Local cache (per worker instance)
- `DISTRIBUTED` - Distributed cache (shared across all workers)

### EnumCacheHandlingAction (handlingAction)
- `CONTINUE` - Return cached response and continue to backend (for logging/monitoring)
- `STOP` - Return cached response and stop (do not call backend)

### Variable Object (for variableList when cacheKeyType=CUSTOM)

See [Variable Definition](03-appendix/variable-definition) for complete variable documentation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Variable name |
| type | string | Yes | Variable type. See [Variable Types](03-appendix/variable-definition) |
| headerName | string | No* | Header name (required if type=HEADER) |
| paramType | string | No* | Parameter type (required if type=PARAMETER). See [EnumVariableParameterType](03-appendix/variable-definition) |
| paramName | string | No* | Parameter name (required if type=PARAMETER) |
| paramPath | string | No* | Parameter path template (required if type=PARAMETER and paramType=PATH) |
| messageContentType | string | No* | Message content type (required if type=BODY). See [EnumMessageContentType](03-appendix/variable-definition) |
| xpathValue | string | No* | XPath expression (required if type=BODY and messageContentType=XML) |
| jsonPathValue | string | No* | JsonPath expression (required if type=BODY and messageContentType=JSON) |
| contextValue | string | No* | Context value (required if type=CONTEXT_VALUES). See [EnumVariableContextValue](03-appendix/variable-definition) |
| zoneId | string | No* | Time zone ID (required for date/time context values) |
| scriptLanguage | string | No* | Script language (required if type=CUSTOM) |
| scriptBody | string | No* | Script body (required if type=CUSTOM) |

### Variable Types

- `HEADER` - Extract from HTTP header
- `PARAMETER` - Extract from query/path/form parameter
- `BODY` - Extract from request/response body (XML, JSON, or raw)
- `CONTEXT_VALUES` - Extract from system context values
- `CUSTOM` - Extract using custom script

### Response

#### Success Response (200 OK)
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
  "error_description": "handlingAction is required"
}
```

### Common Causes

- Missing required field `handlingAction`
- Invalid enum values
- Invalid cache configuration
- Invalid variableList when cacheKeyType=CUSTOM

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

or

```json
{
  "error": "not_found",
  "error_description": "Endpoint (id: endpoint-id) was not found!"
}
```

## cURL Example

### Example 1: Basic Endpoint Cache Configuration

```bash
curl -X PATCH \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/cache/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Endpoint Cache Settings",
    "cacheActive": true,
    "cacheOnlyHttpGetRequests": false,
    "cacheKeyType": "QUERY_PARAMS",
    "cacheStorageType": "LOCAL",
    "capacity": 1000,
    "ttl": 3600,
    "handlingAction": "STOP",
    "cacheNullValue": false
  }'
```

### Example 2: Custom Cache Key with Variables

```bash
curl -X PATCH \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/endpoints/endpoint-id/cache/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Endpoint Cache with Custom Key",
    "cacheActive": true,
    "cacheKeyType": "CUSTOM",
    "cacheStorageType": "DISTRIBUTED",
    "capacity": 5000,
    "ttl": 7200,
    "handlingAction": "CONTINUE",
    "invalidationRequiresAuthn": true,
    "variableList": [
      {
        "name": "userId",
        "type": "HEADER",
        "dataType": "STRING"
      },
      {
        "name": "apiVersion",
        "type": "PARAMETER",
        "dataType": "STRING"
      }
    ]
  }'
```

## Notes and Warnings

- **Endpoint-Level Override**: 
  - Endpoint cache settings override API Proxy-level cache settings
  - If endpoint cache is disabled, API Proxy-level cache still applies
- **handlingAction**: 
  - Required field
  - `CONTINUE` - Returns cached response but still calls backend (useful for logging/monitoring)
  - `STOP` - Returns cached response without calling backend (better performance)
- **Cache Key**: 
  - When `cacheKeyType=CUSTOM`, provide `variableList` to define cache key components
  - Variables are combined to create unique cache keys
- **Storage Type**: 
  - `LOCAL` cache is faster but not shared across workers
  - `DISTRIBUTED` cache is shared across all workers (recommended for multi-instance deployments)
- **TTL**: 
  - Cache entries expire after TTL seconds
  - Set appropriate TTL based on data freshness requirements
- **Capacity**: 
  - Maximum number of cache entries
  - Older entries are evicted when limit is reached (LRU eviction)
- **GET Only**: 
  - When `cacheOnlyHttpGetRequests=true`, only GET requests are cached
  - When `cacheOnlyHttpGetRequests=false`, all HTTP methods can be cached (use with caution)
- **Null Values**: 
  - When `cacheNullValue=false`, null/empty responses are not cached
  - When `cacheNullValue=true`, null/empty responses are cached (may cache error responses)
- **Permissions**: 
  - Requires `ROLE_MANAGE_PROXIES` permission
- **Endpoint Validation**: 
  - Endpoint must exist in the API Proxy
  - Endpoint ID must be valid

## Related Documentation

- [Update Cache Settings](../settings/update-cache-settings.md) - Update API Proxy-level cache settings
- [Get Endpoint](get-endpoint.md) - Get endpoint details
- [List Endpoints](list-endpoints.md) - List all endpoints
- [Update Endpoint](update-endpoint.md) - Update endpoint configuration
