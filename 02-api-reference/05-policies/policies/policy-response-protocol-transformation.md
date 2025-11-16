---
layout: default
permalink: /02-api-reference/05-policies/policies/policy-response-protocol-transformation/
---

# Response Protocol Transformation Policy

## General Information

### Policy Type
```
policy-response-protocol-transformation
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
Response Protocol Transformation policy transforms SOAP responses to REST responses. This policy is used when you need to convert SOAP responses from the backend service to JSON/XML REST format.

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
        "requestPolicyList": [],
        "responsePolicyList": [
          {
            "type": "policy-response-protocol-transformation",
            "name": "soap-to-rest-transformation",
            "description": "Transform SOAP responses to REST",
            "active": true,
            "apiMethodList": [
              {
                "id": "method-1",
                "name": "getUser",
                "description": "Get user information",
                "active": true,
                "httpMethod": "GET",
                "backendResourceUrl": "/soap/UserService",
                "backendHttpMethod": "POST"
              }
            ],
            "policyCondition": {
              "conditionRuleList": []
            },
            "errorMessageList": []
          }
        ],
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
  "type": "policy-response-protocol-transformation",
  "description": "Transform SOAP responses to REST",
  "active": true,
  "apiMethodList": [
    {
      "id": "method-1",
      "name": "getUser",
      "description": "Get user information",
      "active": true,
      "httpMethod": "GET",
      "backendResourceUrl": "/soap/UserService",
      "backendHttpMethod": "POST"
    }
  ],
  "policyCondition": {
    "conditionRuleList": []
  },
  "errorMessageList": []
}
```

#### Request Body Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| type | string | Yes | Policy type. Must be `"policy-response-protocol-transformation"` |
| description | string | No | Policy description |
| active | boolean | No | Whether the policy is active. Default: `true` |
| apiMethodList | array | Yes | List of API methods for transformation. At least one API method must be provided. See [API Method](#api-method) |
| policyCondition | object | No | Policy condition configuration. See [Policy Condition](#policy-condition) |
| errorMessageList | array | No | List of error messages. See [Error Messages](#error-messages) |

### API Method

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | API Method ID (unique identifier) |
| name | string | Yes | API Method name |
| description | string | No | API Method description |
| active | boolean | No | Whether the API method is active. Default: `true` |
| httpMethod | string | Yes | HTTP method for the REST endpoint. See [EnumHttpRequestMethod](#enumhttprequestmethod) |
| backendResourceUrl | string | Yes | Backend SOAP service resource URL |
| backendHttpMethod | string | Yes | HTTP method for the backend SOAP service. See [EnumHttpRequestMethod](#enumhttprequestmethod) |

### EnumHttpRequestMethod

| Value | Description |
|-------|-------------|
| GET | HTTP GET method |
| POST | HTTP POST method |
| PUT | HTTP PUT method |
| DELETE | HTTP DELETE method |
| PATCH | HTTP PATCH method |
| HEAD | HTTP HEAD method |
| OPTIONS | HTTP OPTIONS method |

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "result": {
    "type": "policy-response-protocol-transformation",
    "name": "soap-to-rest-transformation",
    "description": "Transform SOAP responses to REST",
    "active": true,
    "apiMethodList": [
      {
        "id": "method-1",
        "name": "getUser",
        "description": "Get user information",
        "active": true,
        "httpMethod": "GET",
        "backendResourceUrl": "/soap/UserService",
        "backendHttpMethod": "POST"
      }
    ],
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
  'https://api.apinizer.com/apiops/projects/my-project/apiProxies/my-api/policies/soap-to-rest-transformation/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "policy-response-protocol-transformation",
    "description": "Transform SOAP responses to REST",
    "active": true,
    "apiMethodList": [
      {
        "id": "method-1",
        "name": "getUser",
        "description": "Get user information",
        "active": true,
        "httpMethod": "GET",
        "backendResourceUrl": "/soap/UserService",
        "backendHttpMethod": "POST"
      }
    ],
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
  "type": "policy-response-protocol-transformation",
  "description": "Updated description for SOAP to REST transformation",
  "active": true,
  "apiMethodList": [
    {
      "id": "method-1",
      "name": "getUser",
      "description": "Get user information",
      "active": true,
      "httpMethod": "GET",
      "backendResourceUrl": "/soap/UserService",
      "backendHttpMethod": "POST"
    },
    {
      "id": "method-2",
      "name": "createUser",
      "description": "Create a new user",
      "active": true,
      "httpMethod": "POST",
      "backendResourceUrl": "/soap/UserService",
      "backendHttpMethod": "POST"
    }
  ],
  "policyCondition": {
    "conditionRuleList": []
  },
  "errorMessageList": []
}
```

#### Request Body Fields

Same as [Add Policy](#add-policy) request body fields.

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "result": {
    "type": "policy-response-protocol-transformation",
    "name": "soap-to-rest-transformation",
    "description": "Updated description for SOAP to REST transformation",
    "active": true,
    "apiMethodList": [
      {
        "id": "method-1",
        "name": "getUser",
        "description": "Get user information",
        "active": true,
        "httpMethod": "GET",
        "backendResourceUrl": "/soap/UserService",
        "backendHttpMethod": "POST"
      },
      {
        "id": "method-2",
        "name": "createUser",
        "description": "Create a new user",
        "active": true,
        "httpMethod": "POST",
        "backendResourceUrl": "/soap/UserService",
        "backendHttpMethod": "POST"
      }
    ],
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
  'https://api.apinizer.com/apiops/projects/my-project/apiProxies/my-api/policies/soap-to-rest-transformation/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "policy-response-protocol-transformation",
    "description": "Updated description for SOAP to REST transformation",
    "active": true,
    "apiMethodList": [
      {
        "id": "method-1",
        "name": "getUser",
        "description": "Get user information",
        "active": true,
        "httpMethod": "GET",
        "backendResourceUrl": "/soap/UserService",
        "backendHttpMethod": "POST"
      },
      {
        "id": "method-2",
        "name": "createUser",
        "description": "Create a new user",
        "active": true,
        "httpMethod": "POST",
        "backendResourceUrl": "/soap/UserService",
        "backendHttpMethod": "POST"
      }
    ],
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
  'https://api.apinizer.com/apiops/projects/my-project/apiProxies/my-api/policies/soap-to-rest-transformation/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

---

## Policy Condition

Policy condition allows you to specify when this policy should be applied. See [Policy Condition Documentation](/02-api-reference/05-policies/crud/add-policy) for detailed information.

---

## Error Messages

Error messages allow you to customize error responses when policy validation fails. See [Error Messages Documentation](/02-api-reference/05-policies/crud/add-policy) for detailed information.
