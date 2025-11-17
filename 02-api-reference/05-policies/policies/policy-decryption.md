---
layout: default
permalink: /02-api-reference/05-policies/policies/policy-decryption/
---

# Decryption Policy

## General Information

### Policy Type
```
policy-decryption
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
Decryption policy decrypts encrypted data using cryptographic keys. It reads encrypted data from source variables, decrypts them using specified cipher algorithms, and stores the decrypted data in target variables. This policy provides data confidentiality capabilities by reversing encryption operations.

**⚠️ Implementation Status:** This policy is **currently not implemented** in Management API. This policy cannot be created or managed through the Management API at this time. This documentation is provided for reference purposes and will be updated when full API support is added in a future release.

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
            "type": "policy-decryption",
            "name": "decryption-policy",
            "description": "Decrypt encrypted data",
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

**Note:** The current DTO implementation is empty. The following JSON structure is based on the underlying `PolicyDecryption` and `PolicyDecryptionDef` classes and represents the expected structure when full API support is added.

##### Full JSON Body Example - Basic Decryption

```json
{
  "type": "policy-decryption",
  "description": "Decrypt encrypted data",
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
  "policyDecryptionDefList": [
    {
      "id": "decryption-def-1",
      "description": "Decrypt request body",
      "sourceVar": {
        "name": "encryptedBody",
        "type": "CONTEXT_VALUES",
        "dataType": "STRING"
      },
      "targetVar": {
        "name": "decryptedBody",
        "type": "BODY",
        "dataType": "STRING"
      },
      "cipherAlgorithm": "AES_CBC_PKCS5Padding",
      "cipherAlgorithmVar": null,
      "cryptoKeyInfoId": "decryption-key-id",
      "certificateId": null,
      "enumKeyCertificateType": "KEY",
      "ivExists": true,
      "ivVar": {
        "name": "iv",
        "type": "CONTEXT_VALUES",
        "dataType": "STRING"
      },
      "ivEncodingType": "BASE64",
      "inputEncodingType": "BASE64"
    }
  ]
}
```

##### Full JSON Body Example - Dynamic Cipher Algorithm

```json
{
  "type": "policy-decryption",
  "description": "Decrypt with dynamic algorithm",
  "active": true,
  "policyCondition": null,
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
  "policyDecryptionDefList": [
    {
      "id": "decryption-def-1",
      "description": "Decrypt with algorithm from variable",
      "sourceVar": {
        "name": "encryptedData",
        "type": "HEADER",
        "headerName": "X-Encrypted-Data",
        "dataType": "STRING"
      },
      "targetVar": {
        "name": "decryptedData",
        "type": "CONTEXT_VALUES",
        "dataType": "STRING"
      },
      "cipherAlgorithm": null,
      "cipherAlgorithmVar": {
        "name": "algorithm",
        "type": "HEADER",
        "headerName": "X-Cipher-Algorithm",
        "dataType": "STRING"
      },
      "cryptoKeyInfoId": "decryption-key-id",
      "certificateId": null,
      "enumKeyCertificateType": "KEY",
      "ivExists": true,
      "ivVar": {
        "name": "iv",
        "type": "HEADER",
        "headerName": "X-IV",
        "dataType": "STRING"
      },
      "ivEncodingType": "BASE64",
      "inputEncodingType": "BASE64"
    }
  ]
}
```

##### Full JSON Body Example - Multiple Decryption Definitions

```json
{
  "type": "policy-decryption",
  "description": "Decrypt multiple fields",
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
  "policyDecryptionDefList": [
    {
      "id": "decryption-def-1",
      "description": "Decrypt request body",
      "sourceVar": {
        "name": "encryptedBody",
        "type": "CONTEXT_VALUES",
        "dataType": "STRING"
      },
      "targetVar": {
        "name": "decryptedBody",
        "type": "BODY",
        "dataType": "STRING"
      },
      "cipherAlgorithm": "AES_CBC_PKCS5Padding",
      "cipherAlgorithmVar": null,
      "cryptoKeyInfoId": "aes-key-id",
      "certificateId": null,
      "enumKeyCertificateType": "KEY",
      "ivExists": true,
      "ivVar": {
        "name": "iv",
        "type": "CONTEXT_VALUES",
        "dataType": "STRING"
      },
      "ivEncodingType": "BASE64",
      "inputEncodingType": "BASE64"
    },
    {
      "id": "decryption-def-2",
      "description": "Decrypt header value",
      "sourceVar": {
        "name": "encryptedHeader",
        "type": "HEADER",
        "headerName": "X-Encrypted-Header",
        "dataType": "STRING"
      },
      "targetVar": {
        "name": "decryptedHeader",
        "type": "HEADER",
        "headerName": "X-Decrypted-Header",
        "dataType": "STRING"
      },
      "cipherAlgorithm": "RSA_ECB_PKCS1Padding",
      "cipherAlgorithmVar": null,
      "cryptoKeyInfoId": null,
      "certificateId": "rsa-cert-id",
      "enumKeyCertificateType": "CERTIFICATE",
      "ivExists": false,
      "ivVar": null,
      "ivEncodingType": null,
      "inputEncodingType": "BASE64"
    }
  ]
}
```

#### Request Body Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| type | string | Yes | - | Must be `"policy-decryption"` |
| description | string | No | - | Policy description |
| active | boolean | No | true | Whether the policy is active |
| policyCondition | object | No | null | Policy condition. See [Policy Condition](/management-api-docs/#policy-condition) |
| errorMessageList | array | No | [] | List of error messages. See [Error Messages](/management-api-docs/#error-messages) |
| operationMetadata | object | Yes | - | Operation metadata. See [Policy Operation Metadata](/management-api-docs/#policy-operation-metadata) |
| policyDecryptionDefList | array | Yes | - | List of decryption definitions. See [Decryption Definition](/management-api-docs/#decryption-definition) |

### Decryption Definition (policyDecryptionDefList)


| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| id | string | No | - | Definition ID |
| description | string | No | - | Definition description |
| sourceVar | object | Yes | - | Source variable containing encrypted data. See [Variable Object](/management-api-docs/#variable-object) |
| targetVar | object | Yes | - | Target variable for decrypted data. See [Variable Object](/management-api-docs/#variable-object) |
| cipherAlgorithm | string | No | null | Cipher algorithm (if static). See [EnumCipherAlgorithm](/management-api-docs/#enumcipheralgorithm) |
| cipherAlgorithmVar | object | No | null | Variable containing cipher algorithm name (if dynamic) |
| cryptoKeyInfoId | string | No | null | Crypto key info ID (for symmetric algorithms or asymmetric with KEY type) |
| certificateId | string | No | null | Certificate ID (for asymmetric algorithms with CERTIFICATE type) |
| enumKeyCertificateType | string | No | KEY | Key/certificate type. See [EnumKeyCertificateType](/management-api-docs/#enumkeycertificatetype) |
| ivExists | boolean | No | false | Whether initialization vector (IV) exists |
| ivVar | object | No | null | Variable containing IV (if ivExists=true) |
| ivEncodingType | string | No | null | IV encoding type (if ivExists=true). See [EnumEncodingType](/management-api-docs/#enumencodingtype) |
| inputEncodingType | string | Yes | - | Input encoding type of encrypted data. See [EnumEncodingType](/management-api-docs/#enumencodingtype) |

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

### EnumEncodingType (inputEncodingType, ivEncodingType)

- `BASE64` - Base64 encoding
- `HEXADECIMAL` - Hexadecimal encoding

### EnumKeyCertificateType (enumKeyCertificateType)

- `KEY` - Use cryptographic key (from cryptoKeyInfoId)
- `CERTIFICATE` - Use certificate (from certificateId)

### Variable Object (sourceVar, targetVar, ivVar, cipherAlgorithmVar)

See [Variable Definition](/management-api-docs/03-appendix/variable-definition/) for complete variable documentation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Variable name |
| type | string | Yes | Variable type. See [Variable Types](/management-api-docs/03-appendix/variable-definition/) |
| headerName | string | No* | Header name (required if type=HEADER) |
| paramType | string | No* | Parameter type (required if type=PARAMETER). See [EnumVariableParameterType](/management-api-docs/03-appendix/variable-definition/) |
| paramName | string | No* | Parameter name (required if type=PARAMETER) |
| paramPath | string | No* | Parameter path template (required if type=PARAMETER and paramType=PATH) |
| messageContentType | string | No* | Message content type (required if type=BODY). See [EnumMessageContentType](/management-api-docs/03-appendix/variable-definition/) |
| xpathValue | string | No* | XPath expression (required if type=BODY and messageContentType=XML) |
| jsonPathValue | string | No* | JsonPath expression (required if type=BODY and messageContentType=JSON) |
| contextValue | string | No* | Context value (required if type=CONTEXT_VALUES). See [EnumVariableContextValue](/management-api-docs/03-appendix/variable-definition/) |
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

See [Policy Condition Documentation](/management-api-docs/02-api-reference/05-policies/crud/add-policy/) for detailed information.

### Policy Operation Metadata (operationMetadata)

See [Policy Operation Metadata Documentation](/management-api-docs/02-api-reference/05-policies/crud/add-policy/) for detailed information.

### Error Messages (errorMessageList)

See [Error Messages Documentation](/management-api-docs/02-api-reference/05-policies/crud/add-policy/) for detailed information.

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
  "error_description": "policyDecryptionDefList cannot be empty"
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

### Example 1: Add Basic Decryption Policy

```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/decryption-policy/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "policy-decryption",
    "description": "Decrypt encrypted data",
    "active": true,
    "operationMetadata": {
      "targetScope": "API_PROXY",
      "targetPipeline": "REQUEST",
      "deploy": false,
      "order": 1
    },
    "policyDecryptionDefList": [
      {
        "sourceVar": {
          "name": "encryptedBody",
          "type": "CONTEXT_VALUES",
          "dataType": "STRING"
        },
        "targetVar": {
          "name": "decryptedBody",
          "type": "BODY",
          "dataType": "STRING"
        },
        "cipherAlgorithm": "AES_CBC_PKCS5Padding",
        "cryptoKeyInfoId": "decryption-key-id",
        "enumKeyCertificateType": "KEY",
        "ivExists": true,
        "ivVar": {
          "name": "iv",
          "type": "CONTEXT_VALUES",
          "dataType": "STRING"
        },
        "ivEncodingType": "BASE64",
        "inputEncodingType": "BASE64"
      }
    ]
  }'
```

### Example 2: Update Decryption Policy

```bash
curl -X PUT \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/decryption-policy/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "policy-decryption",
    "description": "Updated decryption policy",
    "active": true,
    "operationMetadata": {
      "targetScope": "API_PROXY",
      "targetPipeline": "REQUEST",
      "deploy": false,
      "order": 1
    },
    "policyDecryptionDefList": [
      {
        "sourceVar": {
          "name": "encryptedBody",
          "type": "CONTEXT_VALUES",
          "dataType": "STRING"
        },
        "targetVar": {
          "name": "decryptedBody",
          "type": "BODY",
          "dataType": "STRING"
        },
        "cipherAlgorithm": "AES_CBC_PKCS5Padding",
        "cryptoKeyInfoId": "new-decryption-key-id",
        "enumKeyCertificateType": "KEY",
        "ivExists": true,
        "ivVar": {
          "name": "iv",
          "type": "CONTEXT_VALUES",
          "dataType": "STRING"
        },
        "ivEncodingType": "BASE64",
        "inputEncodingType": "BASE64"
      }
    ]
  }'
```

### Example 3: Delete Decryption Policy

```bash
curl -X DELETE \
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/decryption-policy/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Notes and Warnings

- **⚠️ Implementation Status**: 
  - **This policy is currently NOT IMPLEMENTED in Management API**
  - **Attempting to create or update this policy via Management API will fail**
  - This documentation is provided for reference purposes only
  - Full API support will be added in a future release
- **Cipher Algorithm**: 
  - Can be specified statically via `cipherAlgorithm` or dynamically via `cipherAlgorithmVar`
  - If both are null, decryption will be skipped (data returned as-is)
  - Algorithm must match the one used for encryption
- **Initialization Vector (IV)**: 
  - Required for CBC mode algorithms
  - Set `ivExists: true` if IV is present
  - IV must be provided in `ivVar` with correct `ivEncodingType`
  - IV encoding must match the encoding used during encryption
  - ECB mode algorithms do not require IV
- **Input Encoding**: 
  - Must match the output encoding used during encryption
  - `BASE64` - For Base64-encoded encrypted data
  - `HEXADECIMAL` - For hexadecimal-encoded encrypted data
- **Key/Certificate Management**: 
  - Keys must be configured in Key Store before use
  - Certificates must be configured in Certificate Store before use
  - Use `enumKeyCertificateType` to specify key or certificate source
  - Key/certificate must match the one used for encryption
- **Variable Types**: 
  - Source and target variables can be from headers, parameters, body, or context
  - Use appropriate variable types based on data location
  - Encrypted data is typically stored in context or headers
- **Multiple Definitions**: 
  - Multiple decryption definitions can be configured in one policy
  - Each definition decrypts a different source variable
  - Definitions are executed in order
- **Decryption Order**: 
  - Decryption should be performed before other policies that need plaintext data
  - Consider policy order when configuring decryption policies
- **Error Handling**: 
  - Decryption failures will throw exceptions
  - Configure error messages for better error handling
  - Invalid keys or algorithms will cause decryption to fail
- **Permissions**: 
  - Requires `ROLE_MANAGE_PROXIES` permission
  - Deployment requires `ROLE_DEPLOY_UNDEPLOY_PROXIES` permission

## Related Documentation

- [List Policies](/management-api-docs/02-api-reference/05-policies/crud/list-policies/) - List all policies
- [Add Policy](/management-api-docs/02-api-reference/05-policies/crud/add-policy/) - Add a policy
- [Update Policy](/management-api-docs/02-api-reference/05-policies/crud/update-policy/) - Update a policy
- [Delete Policy](/management-api-docs/02-api-reference/05-policies/crud/delete-policy/) - Delete a policy
- [Encryption Policy](/management-api-docs/02-api-reference/05-policies/policies/policy-encryption/) - Encrypt data
