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

**Important:** This policy cannot be added manually. It is automatically added to the API Proxy when SOAP/REST transformation is enabled during API Proxy creation. Once added, this policy cannot be deleted but can be viewed and updated (update functionality is currently not implemented via API).

### Endpoints

#### List Policies
```
GET /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/
```

**Note:** Add Policy and Delete Policy endpoints are not supported for this policy type. Update Policy endpoint exists but functionality is not currently implemented.

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
            "policyCondition": null,
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

**Not Supported:** This policy cannot be added manually using the Add Policy endpoint. It is automatically created and added to the API Proxy when SOAP/REST transformation is enabled during API Proxy creation.

To enable this policy, configure SOAP/REST transformation settings when creating a new API Proxy.

---

## Update Policy

**Currently Not Implemented:** Update functionality for this policy is not yet implemented. While the policy can be viewed in the API Proxy, modifications cannot be made through the API at this time.

### Endpoint
```
PUT /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

**Note:** This endpoint exists but update functionality is not currently implemented. Future versions may support updating this policy.

---

## Delete Policy

**Not Supported:** This policy cannot be deleted. It is automatically managed by the system and is tied to the SOAP/REST transformation configuration of the API Proxy. To remove this policy, you would need to disable SOAP/REST transformation in the API Proxy configuration.

---

## Policy Condition

Policy condition allows you to specify when this policy should be applied. See [Policy Condition Documentation](/management-api-docs/02-api-reference/05-policies/crud/add-policy/) for detailed information.

---

## Error Messages

Error messages allow you to customize error responses when policy validation fails. See [Error Messages Documentation](/management-api-docs/02-api-reference/05-policies/crud/add-policy/) for detailed information.
