# Policy Group

## General Information

### Policy Type
```
policy-group
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
Policy Group is a container policy that groups multiple policies together. It allows organizing and managing related policies as a single unit. This policy type is currently in development and may have limited functionality.

**Note:** This policy type is currently under development. The implementation may be incomplete or subject to change.

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
            "type": "policy-group",
            "name": "policy-group-1",
            "description": "Group of related policies",
            "active": true
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

##### Full JSON Body Example - Basic Policy Group
```json
{
  "type": "policy-group",
  "name": "policy-group-1",
  "description": "Group of related policies",
  "active": true,
  "operationMetadata": {
    "targetScope": "API_PROXY",
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
| type | string | Yes | - | Policy type: `policy-group` |
| name | string | Yes | - | Policy name (must match path parameter) |
| description | string | No | - | Policy description |
| active | boolean | No | true | Whether policy is active |
| operationMetadata | object | Yes | - | Policy operation metadata. See [PolicyOperationMetadataDTO](#policyoperationmetadatadto) |
| condition | object | Yes | - | Policy condition. See [PolicyConditionDTO](#policyconditiondto) |

### PolicyOperationMetadataDTO (operationMetadata)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| targetScope | string | Yes | Target scope. See [EnumPolicyTargetScope](#enumpolicytargetscope) |
| targetEndpoint | string | No | Target endpoint path (if targetScope is ENDPOINT) |
| targetEndpointHTTPMethod | string | No | Target endpoint HTTP method (if targetScope is ENDPOINT) |
| targetPipeline | string | Yes | Target pipeline. See [EnumPolicyTargetPipeline](#enumpolicytargetpipeline) |
| deploy | boolean | No | true | Whether to deploy immediately |
| deployTargetEnvironmentNameList | array | No | [] | List of environment names to deploy to |
| order | integer | No | - | Policy execution order |

### EnumPolicyTargetScope (operationMetadata.targetScope)

- `API_PROXY` - Apply to entire API Proxy
- `ENDPOINT` - Apply to specific endpoint
- `GLOBAL` - Apply globally

### EnumPolicyTargetPipeline (operationMetadata.targetPipeline)

- `REQUEST` - Request pipeline
- `RESPONSE` - Response pipeline
- `ERROR` - Error pipeline

### PolicyConditionDTO (condition)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| criteria | string | Yes | Condition criteria. See [EnumConditionCriteria](#enumconditioncriteria) |
| rules | array | Yes | List of condition rules. See [ConditionRuleDTO](#conditionruledto) |

### EnumConditionCriteria (condition.criteria)

- `ALWAYS` - Always execute policy
- `IF_ALL_MATCH` - Execute if all rules match
- `IF_ANY_MATCH` - Execute if any rule matches
- `IF_NONE_MATCH` - Execute if no rules match

### ConditionRuleDTO (condition.rules item)

See [Add Policy](../crud/add-policy.md#conditionrulelist-item) for detailed documentation. The structure matches the `ConditionRuleDTO` defined in the Add Policy documentation.

### Notes

- This policy type is currently under development.
- Policy Group specific fields may be added in future versions.
- Currently, Policy Group acts as a container for organizing policies.

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
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/policy-group-1/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "policy-group",
    "name": "policy-group-1",
    "description": "Group of related policies",
    "active": true,
    "operationMetadata": {
      "targetScope": "API_PROXY",
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

- **Development Status**: 
  - This policy type is currently under development
  - Implementation may be incomplete
  - Functionality may change in future versions
- **Purpose**: 
  - Policy Group is intended to group multiple policies together
  - Allows organizing and managing related policies as a single unit
  - May provide additional functionality in future versions
- **Usage**: 
  - Currently acts as a container for organizing policies
  - Specific group functionality may be added later
  - Check latest documentation for updates
- **Deployment**: Policy changes require deployment to take effect. Set `deploy: true` in `operationMetadata` or deploy manually.

## Related Documentation

- [List Policies](../crud/list-policies) - List all policies
- [Add Policy](../crud/add-policy) - General policy addition guide
- [Update Policy](../crud/update-policy) - General policy update guide
- [Delete Policy](../crud/delete-policy) - General policy deletion guide
