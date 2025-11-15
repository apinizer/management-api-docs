# Endpoint Rate Limit Policy

## General Information

### Policy Type
```
policy-endpoint-rate-limit
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
Endpoint Rate Limit policy limits the number of requests per endpoint within a specified time interval. It applies rate limiting to specific API Proxy endpoints (methods) and uses a variable (such as API key, user ID, or IP address) to identify and throttle individual clients. This policy is similar to API Based Throttling but is scoped to specific endpoints.

### Endpoints

#### List Policies
```
GET /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/
```

#### Add Policy
```
POST /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

#### Update Policy
```
PUT /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

#### Delete Policy
```
DELETE /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

---

## List Policies

### Endpoint
```
GET /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/
```

### Request

#### Headers
| Header | Value |
|--------|-------|
| Authorization | Bearer {token} |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| apiProxyName | string | Yes | API Proxy name |

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "resultList": [
    {
      "apiProxy": {
        "name": "MyAPI",
        "requestPolicyList": [
          {
            "type": "policy-endpoint-rate-limit",
            "name": "endpoint-rate-limit-policy",
            "description": "Endpoint rate limit policy",
            "active": true,
            "apiProxyGroupId": "group-id",
            "apiProxyId": "api-proxy-id",
            "endpointId": "endpoint-id",
            "endpointName": "GET /users",
            "permittedMessageCount": 100,
            "timeIntervalPeriodLength": 1,
            "timeInterval": "ONE_MINUTE",
            "targetVariable": {
              "type": "HEADER",
              "headerName": "X-API-Key"
            },
            "cacheConnectionTimeoutInSeconds": 3,
            "cacheErrorHandlingType": "FAIL",
            "timeIntervalWindowType": "FIXED",
            "targetIdentityValue": null,
            "showRateLimitStatisticsInResponseHeader": false,
            "enabled": true
          }
        ],
        "responsePolicyList": [],
        "errorPolicyList": []
      }
    }
  ],
  "resultCount": 1
}
```

### cURL Example
```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Add Policy

### Endpoint
```
POST /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

### Request

#### Headers
| Header | Value |
|--------|-------|
| Authorization | Bearer {token} |
| Content-Type | application/json |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| apiProxyName | string | Yes | API Proxy name |
| policyName | string | Yes | Policy name (must match name in body) |

#### Request Body

##### Full JSON Body Example - Basic Endpoint Rate Limit
```json
{
  "type": "policy-endpoint-rate-limit",
  "name": "endpoint-rate-limit-policy",
  "description": "Endpoint rate limit policy",
  "active": true,
  "apiProxyGroupId": "group-id",
  "apiProxyId": "api-proxy-id",
  "endpointId": "endpoint-id",
  "endpointName": "GET /users",
  "permittedMessageCount": 100,
  "timeIntervalPeriodLength": 1,
  "timeInterval": "ONE_MINUTE",
  "targetVariable": {
    "type": "HEADER",
    "headerName": "X-API-Key"
  },
  "cacheConnectionTimeoutInSeconds": 3,
  "cacheErrorHandlingType": "FAIL",
  "timeIntervalWindowType": "FIXED",
  "targetIdentityValue": null,
  "showRateLimitStatisticsInResponseHeader": false,
  "enabled": true,
  "operationMetadata": {
    "targetScope": "ENDPOINT",
    "targetEndpoint": "GET /users",
    "targetEndpointHTTPMethod": "GET",
    "targetPipeline": "REQUEST",
    "deploy": true,
    "deployTargetEnvironmentNameList": ["production"],
    "order": 1
  },
  "condition": {
    "criteria": "ALWAYS",
    "rules": []
  }
}
```

##### Full JSON Body Example - IP-Based Rate Limit
```json
{
  "type": "policy-endpoint-rate-limit",
  "name": "endpoint-ip-rate-limit",
  "description": "Endpoint rate limit by IP address",
  "active": true,
  "apiProxyGroupId": "group-id",
  "apiProxyId": "api-proxy-id",
  "endpointId": "endpoint-id",
  "endpointName": "POST /orders",
  "permittedMessageCount": 50,
  "timeIntervalPeriodLength": 1,
  "timeInterval": "ONE_MINUTE",
  "targetVariable": {
    "type": "CLIENT_IP"
  },
  "cacheConnectionTimeoutInSeconds": 5,
  "cacheErrorHandlingType": "PASS",
  "timeIntervalWindowType": "SLIDING",
  "targetIdentityValue": null,
  "showRateLimitStatisticsInResponseHeader": true,
  "enabled": true,
  "operationMetadata": {
    "targetScope": "ENDPOINT",
    "targetEndpoint": "POST /orders",
    "targetEndpointHTTPMethod": "POST",
    "targetPipeline": "REQUEST",
    "deploy": true,
    "deployTargetEnvironmentNameList": ["production"],
    "order": 1
  },
  "condition": {
    "criteria": "ALWAYS",
    "rules": []
  }
}
```

##### Full JSON Body Example - User-Based Rate Limit with Sliding Window
```json
{
  "type": "policy-endpoint-rate-limit",
  "name": "endpoint-user-rate-limit",
  "description": "Endpoint rate limit by user ID with sliding window",
  "active": true,
  "apiProxyGroupId": "group-id",
  "apiProxyId": "api-proxy-id",
  "endpointId": "endpoint-id",
  "endpointName": "GET /products",
  "permittedMessageCount": 200,
  "timeIntervalPeriodLength": 1,
  "timeInterval": "ONE_HOUR",
  "targetVariable": {
    "type": "VARIABLE",
    "variableName": "userId"
  },
  "cacheConnectionTimeoutInSeconds": 3,
  "cacheErrorHandlingType": "FAIL",
  "timeIntervalWindowType": "SLIDING",
  "targetIdentityValue": null,
  "showRateLimitStatisticsInResponseHeader": true,
  "enabled": true,
  "operationMetadata": {
    "targetScope": "ENDPOINT",
    "targetEndpoint": "GET /products",
    "targetEndpointHTTPMethod": "GET",
    "targetPipeline": "REQUEST",
    "deploy": true,
    "deployTargetEnvironmentNameList": ["production"],
    "order": 1
  },
  "condition": {
    "criteria": "ALWAYS",
    "rules": []
  }
}
```

##### Request Body Fields

###### Common Policy Fields
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| type | string | Yes | - | Policy type: `policy-endpoint-rate-limit` |
| name | string | Yes | - | Policy name (must match path parameter) |
| description | string | No | - | Policy description |
| active | boolean | No | true | Whether policy is active |
| operationMetadata | object | Yes | - | Policy operation metadata. See [PolicyOperationMetadataDTO](#policyoperationmetadatadto) |
| condition | object | Yes | - | Policy condition. See [PolicyConditionDTO](#policyconditiondto) |

###### Endpoint Rate Limit Specific Fields
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| apiProxyGroupId | string | No | - | API Proxy Group ID |
| apiProxyId | string | No | - | API Proxy ID |
| endpointId | string | No | - | Endpoint ID (method ID) |
| endpointName | string | No | - | Endpoint name (e.g., "GET /users") |
| permittedMessageCount | integer | Yes | 100 | Maximum number of messages allowed per time interval |
| timeIntervalPeriodLength | integer | Yes | 1 | Length of time interval period |
| timeInterval | string | Yes | ONE_MINUTE | Time interval unit. See [EnumRateLimitTimeInterval](#enumratelimittimeinterval) |
| targetVariable | object | No | - | Variable used to identify clients for rate limiting. See [VariableDTO](#variabledto) |
| cacheConnectionTimeoutInSeconds | integer | No | 3 | Cache connection timeout in seconds |
| cacheErrorHandlingType | string | No | FAIL | Cache error handling type. See [EnumCacheErrorHandlingType](#enumcacheerrorhandlingtype) |
| timeIntervalWindowType | string | No | FIXED | Time interval window type. See [EnumIntervalWindowType](#enumintervalwindowtype) |
| targetIdentityValue | string | No | null | Target identity value (if not using targetVariable) |
| showRateLimitStatisticsInResponseHeader | boolean | No | false | Show rate limit statistics in response header |
| enabled | boolean | No | true | Enable rate limiting |

**EnumRateLimitTimeInterval (timeInterval)**
- `ONE_SECOND` - One second
- `ONE_MINUTE` - One minute (default)
- `ONE_HOUR` - One hour
- `ONE_DAY` - One day
- `ONE_MONTH` - One month

**EnumCacheErrorHandlingType (cacheErrorHandlingType)**
- `FAIL` - Fail request when cache error occurs (default)
- `PASS` - Pass request when cache error occurs

**EnumIntervalWindowType (timeIntervalWindowType)**
- `FIXED` - Fixed window (resets at fixed intervals)
- `SLIDING` - Sliding window (continuous rolling window)

**VariableDTO (targetVariable)**

See [Variable Definition](../../../03-appendix/variable-definition.md) for complete variable documentation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Variable name (e.g., "client.ip", "request.header.X-API-Key") |
| type | string | Yes | Variable type. See [Variable Types](../../../03-appendix/variable-definition.md#variable-types) |
| headerName | string | No* | Header name (required if type=HEADER) |
| paramType | string | No* | Parameter type (required if type=PARAMETER). See [EnumVariableParameterType](../../../03-appendix/variable-definition.md#enumvariableparametertype) |
| paramName | string | No* | Parameter name (required if type=PARAMETER) |
| paramPath | string | No* | Parameter path template (required if type=PARAMETER and paramType=PATH) |
| messageContentType | string | No* | Message content type (required if type=BODY). See [EnumMessageContentType](../../../03-appendix/variable-definition.md#enummessagecontenttype) |
| xpathValue | string | No* | XPath expression (required if type=BODY and messageContentType=XML) |
| jsonPathValue | string | No* | JsonPath expression (required if type=BODY and messageContentType=JSON) |
| contextValue | string | No* | Context value (required if type=CONTEXT_VALUES). See [EnumVariableContextValue](../../../03-appendix/variable-definition.md#enumvariablecontextvalue) |
| zoneId | string | No* | Time zone ID (required for date/time context values) |
| scriptLanguage | string | No* | Script language (required if type=CUSTOM) |
| scriptBody | string | No* | Script body (required if type=CUSTOM) |

**Variable Types:**
- `HEADER` - Extract from HTTP header
- `PARAMETER` - Extract from query/path/form parameter
- `BODY` - Extract from request/response body (XML, JSON, or raw)
- `CONTEXT_VALUES` - Extract from system context values (e.g., REQUEST_REMOTE_ADDRESS for client IP)
- `CUSTOM` - Extract using custom script

**PolicyOperationMetadataDTO (operationMetadata)**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| targetScope | string | Yes | Target scope. See [EnumPolicyTargetScope](#enumpolicytargetscope) |
| targetEndpoint | string | No | Target endpoint path (if targetScope is ENDPOINT) |
| targetEndpointHTTPMethod | string | No | Target endpoint HTTP method (if targetScope is ENDPOINT) |
| targetPipeline | string | Yes | Target pipeline. See [EnumPolicyTargetPipeline](#enumpolicytargetpipeline) |
| deploy | boolean | No | true | Whether to deploy immediately |
| deployTargetEnvironmentNameList | array | No | [] | List of environment names to deploy to |
| order | integer | No | - | Policy execution order |

**EnumPolicyTargetScope (operationMetadata.targetScope)**
- `API_PROXY` - Apply to entire API Proxy
- `ENDPOINT` - Apply to specific endpoint
- `GLOBAL` - Apply globally

**EnumPolicyTargetPipeline (operationMetadata.targetPipeline)**
- `REQUEST` - Request pipeline
- `RESPONSE` - Response pipeline
- `ERROR` - Error pipeline

**PolicyConditionDTO (condition)**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| criteria | string | Yes | Condition criteria. See [EnumConditionCriteria](#enumconditioncriteria) |
| rules | array | Yes | List of condition rules. See [ConditionRuleDTO](#conditionruledto) |

**EnumConditionCriteria (condition.criteria)**
- `ALWAYS` - Always execute policy
- `IF_ALL_MATCH` - Execute if all rules match
- `IF_ANY_MATCH` - Execute if any rule matches
- `IF_NONE_MATCH` - Execute if no rules match

**ConditionRuleDTO (condition.rules item)**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| variable | object | Yes | Variable to check. See [VariableDTO](#variabledto) |
| comparisonOperator | string | Yes | Comparison operator. See [EnumConditionValueComparisonOperator](#enumconditionvaluecomparisonoperator) |
| value | string | Yes | Value to compare against |
| valueSource | string | No | Value source. See [EnumConditionValueSource](#enumconditionvaluesource) |

**Notes:**
- `permittedMessageCount` must be greater than 0.
- `timeIntervalPeriodLength` must be greater than 0.
- `timeInterval` is required.
- `cacheConnectionTimeoutInSeconds` must be greater than 0.
- `cacheErrorHandlingType` is required.
- `timeIntervalWindowType` is required.
- `targetVariable` identifies clients for rate limiting (e.g., API key, IP address, user ID).
- `showRateLimitStatisticsInResponseHeader: true` adds rate limit headers to responses.
- `enabled: false` disables rate limiting without removing the policy.

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "deploymentResult": {
    "success": true,
    "deploymentResults": [
      {
        "environmentName": "production",
        "success": true,
        "message": "Deployment successful"
      }
    ]
  }
}
```

### cURL Example
```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/endpoint-rate-limit-policy/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "policy-endpoint-rate-limit",
    "name": "endpoint-rate-limit-policy",
    "description": "Endpoint rate limit policy",
    "active": true,
    "apiProxyGroupId": "group-id",
    "apiProxyId": "api-proxy-id",
    "endpointId": "endpoint-id",
    "endpointName": "GET /users",
    "permittedMessageCount": 100,
    "timeIntervalPeriodLength": 1,
    "timeInterval": "ONE_MINUTE",
    "targetVariable": {
      "type": "HEADER",
      "headerName": "X-API-Key"
    },
    "cacheConnectionTimeoutInSeconds": 3,
    "cacheErrorHandlingType": "FAIL",
    "timeIntervalWindowType": "FIXED",
    "showRateLimitStatisticsInResponseHeader": false,
    "enabled": true,
    "operationMetadata": {
      "targetScope": "ENDPOINT",
      "targetEndpoint": "GET /users",
      "targetEndpointHTTPMethod": "GET",
      "targetPipeline": "REQUEST",
      "deploy": true,
      "deployTargetEnvironmentNameList": ["production"],
      "order": 1
    },
    "condition": {
      "criteria": "ALWAYS",
      "rules": []
    }
  }'
```

---

## Update Policy

### Endpoint
```
PUT /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

### Request

#### Headers
| Header | Value |
|--------|-------|
| Authorization | Bearer {token} |
| Content-Type | application/json |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| apiProxyName | string | Yes | API Proxy name |
| policyName | string | Yes | Policy name (must match name in body) |

#### Request Body

**Note:** Request body structure is the same as Add Policy. All fields should be provided for update.

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "deploymentResult": {
    "success": true,
    "deploymentResults": [...]
  }
}
```

---

## Delete Policy

### Endpoint
```
DELETE /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

### Request

#### Headers
| Header | Value |
|--------|-------|
| Authorization | Bearer {token} |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| apiProxyName | string | Yes | API Proxy name |
| policyName | string | Yes | Policy name |

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "deploymentResult": {
    "success": true,
    "deploymentResults": [...]
  }
}
```

---

## Notes and Warnings

- **Rate Limiting**: 
  - Limits requests per endpoint within a time interval
  - Uses cache to track request counts
  - Applies to specific endpoints (methods)
- **Time Intervals**: 
  - `ONE_SECOND` - Per second
  - `ONE_MINUTE` - Per minute (default)
  - `ONE_HOUR` - Per hour
  - `ONE_DAY` - Per day
  - `ONE_MONTH` - Per month
- **Window Types**: 
  - `FIXED` - Fixed window (resets at fixed intervals, simpler)
  - `SLIDING` - Sliding window (continuous rolling window, more accurate)
- **Target Variable**: 
  - Identifies clients for rate limiting
  - Common: API key (HEADER), IP address (CLIENT_IP), user ID (VARIABLE)
  - Each unique value gets its own rate limit counter
- **Cache**: 
  - Uses cache to store rate limit counters
  - `cacheConnectionTimeoutInSeconds` - Timeout for cache operations
  - `cacheErrorHandlingType` - Behavior when cache fails:
    - `FAIL` - Reject request (default, more secure)
    - `PASS` - Allow request (more permissive)
- **Rate Limit Headers**: 
  - `showRateLimitStatisticsInResponseHeader: true` adds headers:
    - `X-RateLimit-Limit` - Maximum requests allowed
    - `X-RateLimit-Remaining` - Remaining requests
    - `X-RateLimit-Reset` - Reset time
- **Performance**: 
  - Cache performance affects rate limiting accuracy
  - Sliding window is more accurate but uses more resources
  - Fixed window is simpler but may allow bursts
- **Deployment**: Policy changes require deployment to take effect. Set `deploy: true` in `operationMetadata` or deploy manually.

## Related Documentation

- [List Policies](../crud/list-policies.md) - List all policies
- [Add Policy](../crud/add-policy.md) - General policy addition guide
- [Update Policy](../crud/update-policy.md) - General policy update guide
- [Delete Policy](../crud/delete-policy.md) - General policy deletion guide
- [API Based Throttling Policy](./policy-api-based-throttling.md) - Similar policy for API-level throttling
