# WS Security Timestamp Policy

## General Information

### Policy Type
```
policy-ws-security-timestamp
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
WS Security Timestamp policy adds WS-Security Timestamp element to SOAP requests before forwarding to the backend service. It provides timestamp-based replay attack prevention according to WS-Security standards.

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
            "type": "policy-ws-security-timestamp",
            "name": "ws-security-timestamp-policy",
            "description": "Add Timestamp to SOAP requests",
            "active": true,
            "mustUnderstand": true,
            "timeToLive": 300
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
| policyName | string | Yes | Policy name |

#### Request Body

##### Full JSON Body Example
```json
{
  "operationMetadata": {
    "targetScope": "ALL",
    "targetPipeline": "REQUEST",
    "deploy": true,
    "deployTargetEnvironmentNameList": ["production"],
    "order": 1
  },
  "policy": {
    "type": "policy-ws-security-timestamp",
    "description": "Add Timestamp to SOAP requests",
    "active": true,
    "mustUnderstand": true,
    "timeToLive": 300
  }
}
```

##### Request Body Fields

###### operationMetadata
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| targetScope | string | Yes | - | Policy scope: `ALL` or `ENDPOINT` |
| targetEndpoint | string | No* | - | Endpoint path (required if targetScope=ENDPOINT) |
| targetEndpointHTTPMethod | string | No* | - | HTTP method (required if targetScope=ENDPOINT) |
| targetPipeline | string | Yes | - | Pipeline: `REQUEST`, `RESPONSE`, or `ERROR` |
| deploy | boolean | No | true | Whether to deploy after adding policy |
| deployTargetEnvironmentNameList | array | No | [] | List of environment names to deploy to |
| order | integer | No | null | Policy execution order (starts from 1) |

**Enum: targetScope**
- `ALL` - Policy applies to all endpoints
- `ENDPOINT` - Policy applies only to specified endpoint

**Enum: targetPipeline**
- `REQUEST` - Executes in request pipeline (adds Timestamp to outgoing requests)
- `RESPONSE` - Executes in response pipeline (adds Timestamp to outgoing responses)
- `ERROR` - Executes in error pipeline

**Enum: targetEndpointHTTPMethod**
- `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`

###### policy
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| type | string | Yes | - | Policy type: `policy-ws-security-timestamp` |
| description | string | No | - | Policy description |
| active | boolean | No | true | Whether policy is active |
| mustUnderstand | boolean | No | true | WS-Security header mustUnderstand attribute |
| timeToLive | integer | Yes | - | Timestamp time to live in seconds (must be >= 0) |

**Note:**
- `timeToLive` is required and must be >= 0.
- `timeToLive` determines how long the timestamp is valid (in seconds).

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
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/ws-security-timestamp-policy/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "operationMetadata": {
      "targetScope": "ALL",
      "targetPipeline": "REQUEST",
      "deploy": true,
      "deployTargetEnvironmentNameList": ["production"],
      "order": 1
    },
    "policy": {
      "type": "policy-ws-security-timestamp",
      "description": "Add Timestamp to SOAP requests",
      "active": true,
      "mustUnderstand": true,
      "timeToLive": 300
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
| policyName | string | Yes | Policy name |

#### Request Body

**Note:** Request body structure is the same as Add Policy. All fields should be provided for update.

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
| Content-Type | application/json |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| apiProxyName | string | Yes | API Proxy name |
| policyName | string | Yes | Policy name |

#### Request Body

##### Full JSON Body Example
```json
{
  "operationMetadata": {
    "targetScope": "ALL",
    "targetPipeline": "REQUEST",
    "deploy": false
  }
}
```

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "deploymentResult": {
    "success": true,
    "deploymentResults": []
  }
}
```

---

## Usage Scenarios

### Scenario 1: Standard Timestamp

Add Timestamp with 5-minute time to live.

**Request Body:**
```json
{
  "operationMetadata": {
    "targetScope": "ALL",
    "targetPipeline": "REQUEST",
    "deploy": false,
    "order": 1
  },
  "policy": {
    "type": "policy-ws-security-timestamp",
    "description": "Add Timestamp with 5-minute TTL",
    "active": true,
    "mustUnderstand": true,
    "timeToLive": 300
  }
}
```

### Scenario 2: Short Time to Live

Add Timestamp with short time to live for high security.

**Request Body:**
```json
{
  "operationMetadata": {
    "targetScope": "ALL",
    "targetPipeline": "REQUEST",
    "deploy": false,
    "order": 1
  },
  "policy": {
    "type": "policy-ws-security-timestamp",
    "description": "Add Timestamp with short TTL",
    "active": true,
    "mustUnderstand": true,
    "timeToLive": 60
  }
}
```

---

## Notes and Warnings

- **Timestamp**: 
  - Adds Created and Expires timestamps to WS-Security header
  - Used for replay attack prevention
  - Backend validates timestamp expiration
- **Time to Live**: 
  - `timeToLive` is in seconds
  - Shorter TTL provides better security but may cause issues with clock skew
  - Typical values: 60-300 seconds (1-5 minutes)
  - Must be >= 0
- **Performance**: Timestamp adds minimal overhead. Use for necessary security.
- **Pipeline**: 
  - `REQUEST` pipeline adds Timestamp to outgoing requests
  - `RESPONSE` pipeline adds Timestamp to outgoing responses
- **Error Handling**: Invalid timeToLive causes policy validation to fail
- **Deployment**: Policy changes require deployment to take effect. Set `deploy: true` or deploy manually.

## Related Documentation

- [List Policies](../crud/list-policies.md) - List all policies
- [Add Policy](../crud/add-policy.md) - General policy addition guide
- [Update Policy](../crud/update-policy.md) - General policy update guide
- [Delete Policy](../crud/delete-policy.md) - General policy deletion guide
- [WS Security To Target Policy](./policy-ws-security-to-target.md) - Complete WS-Security configuration

