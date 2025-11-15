# Add Endpoints to RLCL

## Overview

Adds API endpoints to an existing RLCL. Endpoints added to the RLCL will be subject to the rate limiting rules defined in the RLCL.

## Endpoint

```
POST /apiops/projects/{projectName}/rlcl/{rlclName}/endpoints/
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
| rlclName | string | Yes | RLCL name |

### Request Body

#### Full JSON Body Example - Single Endpoint

```json
[
  {
    "apiProxyId": "MyAPI",
    "endpointName": "GET /users",
    "permittedMessageCount": 100,
    "timeIntervalPeriodLength": 1,
    "timeInterval": "ONE_MINUTE",
    "cacheConnectionTimeoutInSeconds": 3,
    "cacheErrorHandlingType": "FAIL",
    "timeIntervalWindowType": "FIXED",
    "showRateLimitStatisticsInResponseHeader": false,
    "enabled": true
  }
]
```

#### Full JSON Body Example - Multiple Endpoints

```json
[
  {
    "apiProxyId": "MyAPI",
    "endpointName": "GET /users",
    "permittedMessageCount": 100,
    "timeIntervalPeriodLength": 1,
    "timeInterval": "ONE_MINUTE",
    "cacheConnectionTimeoutInSeconds": 3,
    "cacheErrorHandlingType": "FAIL",
    "timeIntervalWindowType": "FIXED",
    "showRateLimitStatisticsInResponseHeader": false,
    "enabled": true
  },
  {
    "apiProxyId": "MyAPI",
    "endpointName": "POST /orders",
    "permittedMessageCount": 50,
    "timeIntervalPeriodLength": 1,
    "timeInterval": "ONE_MINUTE",
    "cacheConnectionTimeoutInSeconds": 3,
    "cacheErrorHandlingType": "FAIL",
    "timeIntervalWindowType": "SLIDING",
    "showRateLimitStatisticsInResponseHeader": true,
    "enabled": true
  }
]
```

#### Full JSON Body Example - All Endpoints

```json
[
  {
    "apiProxyId": "MyAPI",
    "endpointName": "ALL",
    "permittedMessageCount": 200,
    "timeIntervalPeriodLength": 1,
    "timeInterval": "ONE_HOUR",
    "cacheConnectionTimeoutInSeconds": 3,
    "cacheErrorHandlingType": "FAIL",
    "timeIntervalWindowType": "FIXED",
    "showRateLimitStatisticsInResponseHeader": false,
    "enabled": true
  }
]
```

#### Request Body Fields

The request body is an array of endpoint rate limit objects.

**Endpoint Rate Limit Object:**

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| apiProxyId | string | Yes | - | API Proxy name (not ID) |
| endpointName | string | Yes | - | Endpoint name (e.g., "GET /users") or "ALL" for all endpoints |
| endpointId | string | No | - | Endpoint ID (auto-filled if endpointName is provided) |
| permittedMessageCount | integer | Yes | - | Maximum number of messages allowed per time interval |
| timeIntervalPeriodLength | integer | Yes | - | Length of time interval period |
| timeInterval | string | Yes | - | Time interval unit. See [EnumRateLimitTimeInterval](#enumratelimittimeinterval) |
| targetVariable | object\|null | No | null | Variable used to identify clients. See [Variable Object](#variable-object) |
| cacheConnectionTimeoutInSeconds | integer | Yes | - | Cache connection timeout in seconds |
| cacheErrorHandlingType | string | Yes | - | Cache error handling type. See [EnumCacheErrorHandlingType](#enumcacheerrorhandlingtype) |
| timeIntervalWindowType | string | Yes | - | Time interval window type. See [EnumIntervalWindowType](#enumintervalwindowtype) |
| targetIdentityValue | string\|null | No | null | Target identity value (if not using targetVariable) |
| showRateLimitStatisticsInResponseHeader | boolean | No | false | Show rate limit statistics in response header |
| enabled | boolean | No | true | Enable rate limiting for this endpoint |

**EnumRateLimitTimeInterval (timeInterval):**
- `ONE_SECOND` - One second
- `ONE_MINUTE` - One minute
- `ONE_HOUR` - One hour
- `ONE_DAY` - One day
- `ONE_MONTH` - One month

**EnumCacheErrorHandlingType (cacheErrorHandlingType):**
- `FAIL` - Fail request when cache error occurs
- `CONTINUE` - Continue processing when cache error occurs

**EnumIntervalWindowType (timeIntervalWindowType):**
- `FIXED` - Fixed window (resets at fixed intervals)
- `SLIDING` - Sliding window (continuous rolling window)

**Variable Object (targetVariable):**

See [Variable Definition](../../../../03-appendix/variable-definition.md) for complete variable documentation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Variable name (e.g., "client.ip", "request.header.X-User-ID") |
| type | string | Yes | Variable type. See [Variable Types](../../../../03-appendix/variable-definition.md#variable-types) |
| headerName | string | No* | Header name (required if type=HEADER) |
| paramType | string | No* | Parameter type (required if type=PARAMETER) |
| paramName | string | No* | Parameter name (required if type=PARAMETER) |
| paramPath | string | No* | Parameter path template (required if type=PARAMETER and paramType=PATH) |
| messageContentType | string | No* | Message content type (required if type=BODY) |
| xpathValue | string | No* | XPath expression (required if type=BODY and messageContentType=XML) |
| jsonPathValue | string | No* | JsonPath expression (required if type=BODY and messageContentType=JSON) |
| contextValue | string | No* | Context value (required if type=CONTEXT_VALUES) |
| zoneId | string | No* | Time zone ID (required for date/time context values) |

**Notes:**
- Request body must be an array (even for single endpoint)
- `apiProxyId` is the API Proxy name (not ID)
- `endpointName` can be specific endpoint (e.g., "GET /users") or "ALL" for all endpoints
- `endpointId` is auto-filled if `endpointName` is provided
- Duplicate endpoints are ignored (not added twice)
- Endpoints are added to the existing list

### Response

#### Success Response (200 OK)
```json
{
  "success": true
}
```

### Error Response (400 Bad Request)

```json
{
  "error": "bad_request",
  "error_description": "endpointRateLimits value can not be empty!"
}
```

or

```json
{
  "error": "bad_request",
  "error_description": "API Proxy with name (MyAPI) is not found in project!"
}
```

or

```json
{
  "error": "bad_request",
  "error_description": "API Endpoint with name (GET /users) is not found in API Proxy!"
}
```

## cURL Example

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/rlcl/PremiumUserRLCL/endpoints/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "apiProxyId": "MyAPI",
      "endpointName": "GET /users",
      "permittedMessageCount": 100,
      "timeIntervalPeriodLength": 1,
      "timeInterval": "ONE_MINUTE",
      "cacheConnectionTimeoutInSeconds": 3,
      "cacheErrorHandlingType": "FAIL",
      "timeIntervalWindowType": "FIXED",
      "showRateLimitStatisticsInResponseHeader": false,
      "enabled": true
    }
  ]'
```

## Notes and Warnings

- **Array Format**: 
  - Request body must be an array
  - Even for single endpoint, use array format
- **API Proxy Name**: 
  - Use API Proxy name (not ID) in `apiProxyId`
  - API Proxy must exist in the project
- **Endpoint Name**: 
  - Use endpoint name format: "HTTP_METHOD /path" (e.g., "GET /users")
  - Use "ALL" to apply to all endpoints
- **Duplicate Handling**: 
  - Duplicate endpoints are ignored
  - No error is thrown for duplicates
- **RLCL Must Exist**: 
  - RLCL must exist before adding endpoints

## Related Documentation

- [Update Endpoints](./update-endpoints.md) - Replace all endpoints
- [Delete Endpoints](./delete-endpoints.md) - Remove endpoints
- [Endpoint Rate Limit Policy](../../05-policies/policies/policy-endpoint-rate-limit.md) - Related policy documentation
