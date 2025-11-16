---
layout: default
permalink: /02-api-reference/05-policies/policies/policy-encryption/
---

# Encryption Policy

## General Information

### Policy Type
```
policy-encryption
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
Encryption policy encrypts data using cryptographic keys or certificates. It reads data from source variables, encrypts them using specified cipher algorithms, and stores the encrypted data in target variables. This policy provides data confidentiality capabilities.

**Note:** This policy is currently not fully implemented in Management API. The DTO structure exists but `convertToPolicy` returns null. This documentation is based on the underlying policy structure (`PolicyEncryption` and `PolicyEncryptionDef`) and will be updated when full API support is added.

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
            "type": "policy-encryption",
            "name": "encryption-policy",
            "description": "Encrypt sensitive data",
            "active": true
          }
        ],
        "responsePolicyList": [],
        "errorPolicyList": []
      }
    }
  ]
}
```

---

## Add Policy

### Endpoint
```
POST /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

### Request

#### Headers
| Header | Value | Required |
|--------|-------|----------|
| Authorization | Bearer {token} | Yes |
| Content-Type | application/json | Yes |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| apiProxyName | string | Yes | API Proxy name |
| policyName | string | Yes | Policy name (unique identifier) |

#### Request Body

**Note:** The current DTO implementation is empty. The following JSON structure is based on the underlying `PolicyEncryption` and `PolicyEncryptionDef` classes and represents the expected structure when full API support is added.

##### Full JSON Body Example - Basic Encryption

```json
{
  "type": "policy-encryption",
  "description": "Encrypt sensitive data",
  "active": true,
  "policyCondition": null,
  "errorMessageList": [],
  "operationMetadata": {
    "targetScope": "API_PROXY",
    "targetPipeline": "REQUEST",
    "deploy": false,
    "deployTargetEnvironmentNameList": [],
    "order": 1
  },
  "policyEncryptionDefList": [
    {
      "id": "encryption-def-1",
      "description": "Encrypt request body",
      "sourceVar": {
        "name": "requestBody",
        "type": "BODY",
        "dataType": "STRING"
      },
      "targetVar": {
        "name": "encryptedBody",
        "type": "CONTEXT_VALUES",
        "dataType": "STRING"
      },
      "cipherAlgorithm": "AES_CBC_PKCS5Padding",
      "cryptoKeyInfoId": "encryption-key-id",
      "certificateId": null,
      "enumKeyCertificateType": "KEY",
      "createIV": true,
      "ivEncodingType": "BASE64",
      "ivVar": {
        "name": "iv",
        "type": "CONTEXT_VALUES",
        "dataType": "STRING"
      },
      "cipherAlgorithmVar": null,
      "outputEncodingType": "BASE64"
    }
  ]
}
```

##### Full JSON Body Example - Multiple Encryption Definitions

```json
{
  "type": "policy-encryption",
  "description": "Encrypt multiple fields",
  "active": true,
  "policyCondition": {
    "criteria": "ALL",
    "conditionRuleList": [
      {
        "variable": {
          "name": "contentType",
          "type": "HEADER",
          "dataType": "STRING"
        },
        "valueComparisonOperator": "EQUALS",
        "valueSource": "STATIC",
        "value": "application/json"
      }
    ]
  },
  "errorMessageList": [],
  "operationMetadata": {
    "targetScope": "ENDPOINT",
    "targetEndpoint": "endpoint-id",
    "targetEndpointHTTPMethod": "POST",
    "targetPipeline": "REQUEST",
    "deploy": false,
    "deployTargetEnvironmentNameList": [],
    "order": 1
  },
  "policyEncryptionDefList": [
    {
      "id": "encryption-def-1",
      "description": "Encrypt request body",
      "sourceVar": {
        "name": "requestBody",
        "type": "BODY",
        "dataType": "STRING"
      },
      "targetVar": {
        "name": "encryptedBody",
        "type": "CONTEXT_VALUES",
        "dataType": "STRING"
      },
      "cipherAlgorithm": "AES_CBC_PKCS5Padding",
      "cryptoKeyInfoId": "aes-key-id",
      "certificateId": null,
      "enumKeyCertificateType": "KEY",
      "createIV": true,
      "ivEncodingType": "BASE64",
      "ivVar": {
        "name": "iv",
        "type": "CONTEXT_VALUES",
        "dataType": "STRING"
      },
      "cipherAlgorithmVar": null,
      "outputEncodingType": "BASE64"
    },
    {
      "id": "encryption-def-2",
      "description": "Encrypt header value",
      "sourceVar": {
        "name": "sensitiveHeader",
        "type": "HEADER",
        "dataType": "STRING"
      },
      "targetVar": {
        "name": "encryptedHeader",
        "type": "HEADER",
        "dataType": "STRING"
      },
      "cipherAlgorithm": "RSA_ECB_PKCS1Padding",
      "cryptoKeyInfoId": null,
      "certificateId": "rsa-cert-id",
      "enumKeyCertificateType": "CERTIFICATE",
      "createIV": false,
      "ivEncodingType": null,
      "ivVar": null,
      "cipherAlgorithmVar": null,
      "outputEncodingType": "BASE64"
    }
  ]
}
```

#### Request Body Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| type | string | Yes | - | Must be `"policy-encryption"` |
| description | string | No | - | Policy description |
| active | boolean | No | true | Whether the policy is active |
| policyCondition | object | No | null | Policy condition. See [Policy Condition](/#policy-condition) |
| errorMessageList | array | No | [] | List of error messages. See [Error Messages](/#error-messages) |
| operationMetadata | object | Yes | - | Operation metadata. See [Policy Operation Metadata](/#policy-operation-metadata) |
| policyEncryptionDefList | array | Yes | - | List of encryption definitions. See [Encryption Definition](/#encryption-definition) |

### Encryption Definition (policyEncryptionDefList)


| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| id | string | No | - | Definition ID |
| description | string | No | - | Definition description |
| sourceVar | object | Yes | - | Source variable to encrypt. See [Variable Object](/#variable-object) |
| targetVar | object | Yes | - | Target variable for encrypted data. See [Variable Object](/#variable-object) |
| cipherAlgorithm | string | Yes | - | Cipher algorithm. See [EnumCipherAlgorithm](/#enumcipheralgorithm) |
| cipherAlgorithmVar | object | No | null | Variable containing cipher algorithm name (if dynamic) |
| cryptoKeyInfoId | string | No | null | Crypto key info ID (for symmetric algorithms or asymmetric with KEY type) |
| certificateId | string | No | null | Certificate ID (for asymmetric algorithms with CERTIFICATE type) |
| enumKeyCertificateType | string | No | KEY | Key/certificate type. See [EnumKeyCertificateType](/#enumkeycertificatetype) |
| createIV | boolean | No | false | Whether to create initialization vector (IV) |
| ivEncodingType | string | No | null | IV encoding type (if createIV=true). See [EnumEncodingType](/#enumencodingtype) |
| ivVar | object | No | null | Variable to store IV (if createIV=true) |
| outputEncodingType | string | Yes | - | Output encoding type. See [EnumEncodingType](/#enumencodingtype) |

### EnumCipherAlgorithm (cipherAlgorithm)


Symmetric Algorithms:
- `AES_CBC_NoPadding` - AES/CBC/NoPadding
- `AES_CBC_PKCS5Padding` - AES/CBC/PKCS5Padding (requires IV)
- `AES_ECB_NoPadding` - AES/ECB/NoPadding
- `AES_ECB_PKCS5Padding` - AES/ECB/PKCS5Padding
- `DES_CBC_NoPadding` - DES/CBC/NoPadding
- `DES_CBC_PKCS5Padding` - DES/CBC/PKCS5Padding (requires IV)
- `DES_ECB_NoPadding` - DES/ECB/NoPadding
- `DES_ECB_PKCS5Padding` - DES/ECB/PKCS5Padding
- `DESede_CBC_NoPadding` - DESede/CBC/NoPadding
- `DESede_CBC_PKCS5Padding` - DESede/CBC/PKCS5Padding (requires IV)
- `DESede_ECB_NoPadding` - DESede/ECB/NoPadding
- `DESede_ECB_PKCS5Padding` - DESede/ECB/PKCS5Padding

Asymmetric Algorithms:
- `RSA_ECB_PKCS1Padding` - RSA/ECB/PKCS1Padding
- `RSA_ECB_OAEPWithSHA_1AndMGF1Padding` - RSA/ECB/OAEPWithSHA-1AndMGF1Padding
- `RSA_ECB_OAEPWithSHA_256AndMGF1Padding` - RSA/ECB/OAEPWithSHA-256AndMGF1Padding

### EnumEncodingType (outputEncodingType, ivEncodingType)

- `BASE64` - Base64 encoding
- `HEXADECIMAL` - Hexadecimal encoding

### EnumKeyCertificateType (enumKeyCertificateType)

- `KEY` - Use cryptographic key (from cryptoKeyInfoId)
- `CERTIFICATE` - Use certificate (from certificateId)

### Variable Object (sourceVar, targetVar, ivVar, cipherAlgorithmVar)

See [Variable Definition](/02-api-reference/05-policies/policies/03-appendix/variable-definition/) for complete variable documentation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Variable name |
| type | string | Yes | Variable type. See [Variable Types](/02-api-reference/05-policies/policies/03-appendix/variable-definition/) |
| headerName | string | No* | Header name (required if type=HEADER) |
| paramType | string | No* | Parameter type (required if type=PARAMETER). See [EnumVariableParameterType](/02-api-reference/05-policies/policies/03-appendix/variable-definition/) |
| paramName | string | No* | Parameter name (required if type=PARAMETER) |
| paramPath | string | No* | Parameter path template (required if type=PARAMETER and paramType=PATH) |
| messageContentType | string | No* | Message content type (required if type=BODY). See [EnumMessageContentType](/02-api-reference/05-policies/policies/03-appendix/variable-definition/) |
| xpathValue | string | No* | XPath expression (required if type=BODY and messageContentType=XML) |
| jsonPathValue | string | No* | JsonPath expression (required if type=BODY and messageContentType=JSON) |
| contextValue | string | No* | Context value (required if type=CONTEXT_VALUES). See [EnumVariableContextValue](/02-api-reference/05-policies/policies/03-appendix/variable-definition/) |
| zoneId | string | No* | Time zone ID (required for date/time context values) |
| scriptLanguage | string | No* | Script language (required if type=CUSTOM) |
| scriptBody | string | No* | Script body (required if type=CUSTOM) |

### Variable Types

- `HEADER` - Extract from HTTP header
- `PARAMETER` - Extract from query/path/form parameter
- `BODY` - Extract from request/response body (XML, JSON, or raw)
- `CONTEXT_VALUES` - Extract from system context values
- `CUSTOM` - Extract using custom script

### Policy Condition (policyCondition)

See [Policy Condition Documentation](/02-api-reference/05-policies/crud/add-policy/) for detailed information.

### Policy Operation Metadata (operationMetadata)

See [Policy Operation Metadata Documentation](/02-api-reference/05-policies/crud/add-policy/) for detailed information.

### Error Messages (errorMessageList)

See [Error Messages Documentation](/02-api-reference/05-policies/crud/add-policy/) for detailed information.

### Response

#### Success Response (200 OK)
```json
{
  "success": true
}
```

#### Error Response (400 Bad Request)
```json
{
  "error": "bad_request",
  "error_description": "policyEncryptionDefList cannot be empty"
}
```

---

## Update Policy

### Endpoint
```
PUT /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

### Request

Same as Add Policy. All fields can be updated.

### Response

Same as Add Policy.

---

## Delete Policy

### Endpoint
```
DELETE /apiops/projects/{projectName}/apiProxies/{apiProxyName}/policies/{policyName}/
```

### Request

#### Headers
| Header | Value | Required |
|--------|-------|----------|
| Authorization | Bearer {token} | Yes |

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
  "success": true
}
```

---

## cURL Examples

### Example 1: Add Basic Encryption Policy

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/encryption-policy/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "policy-encryption",
    "description": "Encrypt sensitive data",
    "active": true,
    "operationMetadata": {
      "targetScope": "API_PROXY",
      "targetPipeline": "REQUEST",
      "deploy": false,
      "order": 1
    },
    "policyEncryptionDefList": [
      {
        "sourceVar": {
          "name": "requestBody",
          "type": "BODY",
          "dataType": "STRING"
        },
        "targetVar": {
          "name": "encryptedBody",
          "type": "CONTEXT_VALUES",
          "dataType": "STRING"
        },
        "cipherAlgorithm": "AES_CBC_PKCS5Padding",
        "cryptoKeyInfoId": "encryption-key-id",
        "enumKeyCertificateType": "KEY",
        "createIV": true,
        "ivEncodingType": "BASE64",
        "outputEncodingType": "BASE64"
      }
    ]
  }'
```

### Example 2: Update Encryption Policy

```bash
curl -X PUT \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/encryption-policy/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "policy-encryption",
    "description": "Updated encryption policy",
    "active": true,
    "operationMetadata": {
      "targetScope": "API_PROXY",
      "targetPipeline": "REQUEST",
      "deploy": false,
      "order": 1
    },
    "policyEncryptionDefList": [
      {
        "sourceVar": {
          "name": "requestBody",
          "type": "BODY",
          "dataType": "STRING"
        },
        "targetVar": {
          "name": "encryptedBody",
          "type": "CONTEXT_VALUES",
          "dataType": "STRING"
        },
        "cipherAlgorithm": "AES_CBC_PKCS5Padding",
        "cryptoKeyInfoId": "new-encryption-key-id",
        "enumKeyCertificateType": "KEY",
        "createIV": true,
        "ivEncodingType": "BASE64",
        "outputEncodingType": "BASE64"
      }
    ]
  }'
```

### Example 3: Delete Encryption Policy

```bash
curl -X DELETE \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/encryption-policy/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Notes and Warnings

- **Implementation Status**: 
  - This policy is currently not fully implemented in Management API
  - The DTO structure exists but `convertToPolicy` returns null
  - This documentation is based on the underlying policy structure
- **Cipher Algorithms**: 
  - Symmetric algorithms (AES, DES, DESede) require `cryptoKeyInfoId`
  - Asymmetric algorithms (RSA) can use either `cryptoKeyInfoId` (KEY) or `certificateId` (CERTIFICATE)
  - CBC mode algorithms require IV (set `createIV: true`)
  - ECB mode algorithms do not require IV
- **Initialization Vector (IV)**: 
  - Required for CBC mode algorithms
  - Set `createIV: true` to generate IV automatically
  - IV is stored in `ivVar` with specified `ivEncodingType`
  - IV must be provided for decryption
- **Encoding Types**: 
  - `BASE64` - Common encoding for encrypted data
  - `HEXADECIMAL` - Alternative encoding format
  - Output encoding must match input encoding for decryption
- **Key/Certificate Management**: 
  - Keys must be configured in Key Store before use
  - Certificates must be configured in Certificate Store before use
  - Use `enumKeyCertificateType` to specify key or certificate source
- **Variable Types**: 
  - Source and target variables can be from headers, parameters, body, or context
  - Use appropriate variable types based on data location
- **Multiple Definitions**: 
  - Multiple encryption definitions can be configured in one policy
  - Each definition encrypts a different source variable
  - Definitions are executed in order
- **Permissions**: 
  - Requires `ROLE_MANAGE_PROXIES` permission
  - Deployment requires `ROLE_DEPLOY_UNDEPLOY_PROXIES` permission

## Related Documentation

- [List Policies](/02-api-reference/05-policies/crud/list-policies/) - List all policies
- [Add Policy](/02-api-reference/05-policies/crud/add-policy/) - Add a policy
- [Update Policy](/02-api-reference/05-policies/crud/update-policy/) - Update a policy
- [Delete Policy](/02-api-reference/05-policies/crud/delete-policy/) - Delete a policy
- [Decryption Policy](/02-api-reference/05-policies/policies/policy-decryption/) - Decrypt encrypted data
