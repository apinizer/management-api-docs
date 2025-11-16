---
layout: default
permalink: /02-api-reference/05-policies/policies/policy-request-protocol-transformation/
---

# Request Protocol Transformation Policy

## General Information

### Policy Type
```
policy-request-protocol-transformation
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
Request Protocol Transformation policy transforms REST requests to SOAP requests. This policy is used when you need to convert JSON/XML REST requests to SOAP format before forwarding to the backend service.

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
            "type": "policy-request-protocol-transformation",
            "name": "rest-to-soap-transformation",
            "description": "Transform REST requests to SOAP",
            "active": true,
            "policyCondition": {
              "conditionRuleList": []
            },
            "errorMessageList": []
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
  'https://api.apinizer.com/apiops/projects/my-project/apiProxies/my-api/policies/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN'
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
| policyName | string | Yes | Policy name (unique identifier) |

#### Request Body
```json
{
  "type": "policy-request-protocol-transformation",
  "description": "Transform REST requests to SOAP",
  "active": true,
  "policyCondition": {
    "conditionRuleList": []
  },
  "errorMessageList": []
}
```

#### Request Body Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| type | string | Yes | Policy type. Must be `"policy-request-protocol-transformation"` |
| description | string | No | Policy description |
| active | boolean | No | Whether the policy is active. Default: `true` |
| policyCondition | object | No | Policy condition configuration. See [Policy Condition](/management-api-docs/#policy-condition) |
| errorMessageList | array | No | List of error messages. See [Error Messages](/management-api-docs/#error-messages) |

**Note:** This policy currently only supports base policy fields. The actual REST-to-SOAP transformation configuration is managed through API Method settings in the API Proxy configuration.

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "result": {
    "type": "policy-request-protocol-transformation",
    "name": "rest-to-soap-transformation",
    "description": "Transform REST requests to SOAP",
    "active": true,
    "policyCondition": {
      "conditionRuleList": []
    },
    "errorMessageList": []
  }
}
```

### cURL Example
```bash
curl -X POST \
  'https://api.apinizer.com/apiops/projects/my-project/apiProxies/my-api/policies/rest-to-soap-transformation/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "policy-request-protocol-transformation",
    "description": "Transform REST requests to SOAP",
    "active": true,
    "policyCondition": {
      "conditionRuleList": []
    },
    "errorMessageList": []
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
| policyName | string | Yes | Policy name (unique identifier) |

#### Request Body
```json
{
  "type": "policy-request-protocol-transformation",
  "description": "Updated description for REST to SOAP transformation",
  "active": true,
  "policyCondition": {
    "conditionRuleList": []
  },
  "errorMessageList": []
}
```

#### Request Body Fields

Same as [Add Policy](/management-api-docs/#add-policy) request body fields.

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "result": {
    "type": "policy-request-protocol-transformation",
    "name": "rest-to-soap-transformation",
    "description": "Updated description for REST to SOAP transformation",
    "active": true,
    "policyCondition": {
      "conditionRuleList": []
    },
    "errorMessageList": []
  }
}
```

### cURL Example
```bash
curl -X PUT \
  'https://api.apinizer.com/apiops/projects/my-project/apiProxies/my-api/policies/rest-to-soap-transformation/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "policy-request-protocol-transformation",
    "description": "Updated description for REST to SOAP transformation",
    "active": true,
    "policyCondition": {
      "conditionRuleList": []
    },
    "errorMessageList": []
  }'
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
| policyName | string | Yes | Policy name (unique identifier) |

### Response

#### Success Response (200 OK)
```json
{
  "success": true
}
```

### cURL Example
```bash
curl -X DELETE \
  'https://api.apinizer.com/apiops/projects/my-project/apiProxies/my-api/policies/rest-to-soap-transformation/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

---

## Policy Condition

Policy condition allows you to specify when this policy should be applied. See [Policy Condition Documentation](/management-api-docs/02-api-reference/05-policies/crud/add-policy/) for detailed information.

---

## Error Messages

Error messages allow you to customize error responses when policy validation fails. See [Error Messages Documentation](/management-api-docs/02-api-reference/05-policies/crud/add-policy/) for detailed information.
