# SAML Validation Policy

## General Information

### Policy Type
```
policy-saml-validation
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
SAML Validation policy validates SAML assertions in request messages. It verifies SAML assertion signatures using certificates from KeyStore and optionally clears SAML assertions after validation. This policy is used for SAML-based SSO (Single Sign-On) authentication and authorization.

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
            "type": "policy-saml-validation",
            "name": "saml-validation-policy",
            "description": "Validate SAML assertions",
            "active": true,
            "keyStoreId": "saml-keystore-id",
            "allowUnknownSigner": false,
            "clearSaml": false,
            "clearSamlPath": null
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

##### Full JSON Body Example - Full Validation
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
    "type": "policy-saml-validation",
    "description": "Validate SAML assertions with signature verification",
    "active": true,
    "keyStoreId": "saml-keystore-id",
    "allowUnknownSigner": false,
    "clearSaml": false,
    "clearSamlPath": null
  }
}
```

##### Full JSON Body Example - Clear SAML After Validation
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
    "type": "policy-saml-validation",
    "description": "Validate and clear SAML assertions",
    "active": true,
    "keyStoreId": "saml-keystore-id",
    "allowUnknownSigner": false,
    "clearSaml": true,
    "clearSamlPath": "/soap:Envelope/soap:Header/wsse:Security/saml:Assertion"
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
- `REQUEST` - Executes in request pipeline (validates request SAML)
- `RESPONSE` - Executes in response pipeline (validates response SAML)
- `ERROR` - Executes in error pipeline

**Enum: targetEndpointHTTPMethod**
- `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`

###### policy
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| type | string | Yes | - | Policy type: `policy-saml-validation` |
| description | string | No | - | Policy description |
| active | boolean | No | true | Whether policy is active |
| keyStoreId | string | Yes | - | Keystore ID for SAML signature validation |
| allowUnknownSigner | boolean | No | false | Allow unknown signer for SAML validation |
| clearSaml | boolean | No | false | Clear SAML assertion after validation |
| clearSamlPath | string | No* | null | XPath to SAML assertion to clear (required if clearSaml=true) |

### Note

- `keyStoreId` is required and must reference a valid KeyStore containing SAML signing certificates.
- If `clearSaml: true`, `clearSamlPath` is required (XPath expression to locate SAML assertion).

### XPath Examples

- `/soap:Envelope/soap:Header/wsse:Security/saml:Assertion` - SOAP header SAML assertion
- `//saml:Assertion` - Anywhere in document
- `/root/saml:Assertion` - Root element SAML assertion

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
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/saml-validation-policy/" \
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
      "type": "policy-saml-validation",
      "description": "Validate SAML assertions",
      "active": true,
      "keyStoreId": "saml-keystore-id",
      "allowUnknownSigner": false,
      "clearSaml": false
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

## Notes and Warnings

- **KeyStore**: 
  - `keyStoreId` must reference a valid KeyStore containing SAML signing certificates
  - KeyStore must contain public keys or certificates for signature validation
  - Certificates must match the signer's certificate used in SAML assertion
- **Signature Validation**: 
  - Validates SAML assertion signature using certificates from KeyStore
  - Signature must be valid and certificate must be trusted
  - Assertion must not be expired
- **Unknown Signer**: 
  - When `allowUnknownSigner: false`, only signers with certificates in KeyStore are allowed
  - When `allowUnknownSigner: true`, validation proceeds even if signer is not in KeyStore (less secure)
- **Clear SAML**: 
  - When `clearSaml: true`, SAML assertion is removed after validation
  - `clearSamlPath` must be a valid XPath expression pointing to SAML assertion
  - Useful for removing sensitive SAML data before forwarding request
- **XPath**: 
  - `clearSamlPath` must be a valid XPath expression
  - Supports namespaces (e.g., `soap:Envelope`, `saml:Assertion`)
  - Use absolute paths for precise location
- **SAML Format**: 
  - Supports SAML 1.1 and SAML 2.0 assertions
  - Supports SAML assertions in SOAP headers (WS-Security)
  - Supports SAML assertions in HTTP headers or body
- **Performance**: SAML validation adds processing overhead. Use for necessary validation only.
- **Pipeline**: 
  - `REQUEST` pipeline validates SAML in request before processing
  - `RESPONSE` pipeline validates SAML in response before sending to client
  - Validation failure results in 401 Unauthorized or 403 Forbidden response
- **Error Handling**: Invalid SAML assertion or signature causes validation to fail
- **Deployment**: Policy changes require deployment to take effect. Set `deploy: true` or deploy manually.

## Related Documentation

- [List Policies](../crud/list-policies) - List all policies
- [Add Policy](../crud/add-policy) - General policy addition guide
- [Update Policy](../crud/update-policy) - General policy update guide
- [Delete Policy](../crud/delete-policy) - General policy deletion guide
- [OIDC Authentication Policy](./policy-oidc) - OIDC Authentication
- [JWT Authentication Policy](./policy-auth-jwt) - JWT Token Authentication
