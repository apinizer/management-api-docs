---
layout: default
permalink: /02-api-reference/05-policies/policies/policy-ws-security-encrypt/
---

# WS Security Encrypt Policy

## General Information

### Policy Type
```
policy-ws-security-encrypt
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
WS Security Encrypt policy encrypts SOAP message parts before forwarding to the backend service. It adds WS-Security Encryption elements to the SOAP message according to WS-Security standards.

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
            "type": "policy-ws-security-encrypt",
            "name": "ws-security-encrypt-policy",
            "description": "Encrypt SOAP message parts",
            "active": true,
            "mustUnderstand": true,
            "encPartList": [
              {
                "name": "Body",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
                "encodeType": "CONTENT"
              }
            ],
            "encEmbeddedKeyName": null,
            "encKeyIdType": "X509_CERTIFICATE",
            "encSymEncAlgorithm": "AES_128_CBC",
            "encKeyEncAlgorithm": "RSA",
            "encKeyStoreName": "encryption-keystore"
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

##### Full JSON Body Example - Standard Encryption
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
    "type": "policy-ws-security-encrypt",
    "description": "Encrypt SOAP message body",
    "active": true,
    "mustUnderstand": true,
    "encPartList": [
      {
        "name": "Body",
        "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        "encodeType": "CONTENT"
      }
    ],
    "encEmbeddedKeyName": null,
    "encKeyIdType": "X509_CERTIFICATE",
    "encSymEncAlgorithm": "AES_128_CBC",
    "encKeyEncAlgorithm": "RSA",
    "encKeyStoreName": "encryption-keystore"
  }
}
```

##### Full JSON Body Example - Multiple Parts
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
    "type": "policy-ws-security-encrypt",
    "description": "Encrypt multiple SOAP parts",
    "active": true,
    "mustUnderstand": true,
    "encPartList": [
      {
        "name": "Body",
        "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        "encodeType": "CONTENT"
      },
      {
        "name": "UsernameToken",
        "namespace": "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd",
        "encodeType": "ELEMENT"
      }
    ],
    "encEmbeddedKeyName": null,
    "encKeyIdType": "X509_CERTIFICATE",
    "encSymEncAlgorithm": "AES_256_CBC",
    "encKeyEncAlgorithm": "OAEP",
    "encKeyStoreName": "encryption-keystore"
  }
}
```

##### Full JSON Body Example - With Embedded Key
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
    "type": "policy-ws-security-encrypt",
    "description": "Encrypt with embedded key",
    "active": true,
    "mustUnderstand": true,
    "encPartList": [
      {
        "name": "Body",
        "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        "encodeType": "CONTENT"
      }
    ],
    "encEmbeddedKeyName": "embedded-key-alias",
    "encKeyIdType": "EMBEDDED_KEY_INFO",
    "encSymEncAlgorithm": "AES_128_CBC",
    "encKeyEncAlgorithm": "RSA",
    "encKeyStoreName": "encryption-keystore"
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
- `REQUEST` - Executes in request pipeline (encrypts outgoing requests)
- `RESPONSE` - Executes in response pipeline (encrypts outgoing responses)
- `ERROR` - Executes in error pipeline

**Enum: targetEndpointHTTPMethod**
- `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`

###### policy
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| type | string | Yes | - | Policy type: `policy-ws-security-encrypt` |
| description | string | No | - | Policy description |
| active | boolean | No | true | Whether policy is active |
| mustUnderstand | boolean | No | true | WS-Security header mustUnderstand attribute |
| encPartList | array | No | [] | Encryption parts list. See [WsSecurityToTargetPart](/#wssecuritytotargetpart) |
| encEmbeddedKeyName | string | No | null | Embedded key name for encryption (used when encKeyIdType=EMBEDDED_KEY_INFO) |
| encKeyIdType | string | No | null | Encryption key identifier type. See [EnumWsSecurityKeyIdentifierType](/#enumwssecuritykeyidentifiertype) |
| encSymEncAlgorithm | string | No | null | Symmetric encoding algorithm for encryption. See [EnumWsSecuritySymmetricEncodingAlgorithm](/#enumwssecuritysymmetricencodingalgorithm) |
| encKeyEncAlgorithm | string | No | null | Key encryption algorithm. See [EnumWsSecurityKeyEncryptionAlgorithm](/#enumwssecuritykeyencryptionalgorithm) |
| encKeyStoreName | string | Yes | - | Encryption keystore name |

### EnumWsSecurityKeyIdentifierType

- `BINARY_SECURITY_TOKEN` - Binary Security Token
- `ISSUER_NAME_AND_SERIAL_NUMBER` - Issuer Name and Serial Number
- `X509_CERTIFICATE` - X509 Certificate (recommended)
- `SUBJECT_KEY_IDENTIFIER` - Subject Key Identifier
- `THUMBPRINT_SHA1_IDENTIFIER` - Thumbprint SHA1 Identifier
- `EMBEDDED_KEY_INFO` - Embedded Key Info (requires encEmbeddedKeyName)
- `EMBED_SECURITY_TOKEN_REFERENCE` - Embed Security Token Reference
- `CUSTOM_KEY_INFO` - Custom Key Info

### EnumWsSecuritySymmetricEncodingAlgorithm

- `AES_128_CBC` - AES-128-CBC (http://www.w3.org/2001/04/xmlenc#aes128-cbc)
- `AES_192_CBC` - AES-192-CBC (http://www.w3.org/2001/04/xmlenc#aes192-cbc)
- `AES_256_CBC` - AES-256-CBC (http://www.w3.org/2001/04/xmlenc#aes256-cbc) (recommended)

### EnumWsSecurityKeyEncryptionAlgorithm

- `RSA` - RSA v1.5 (http://www.w3.org/2001/04/xmlenc#rsa-1_5) (legacy)
- `OAEP` - RSA-OAEP (http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p) (recommended, more secure)

### Note

- `encKeyStoreName` is required.
- If `encKeyIdType: EMBEDDED_KEY_INFO`, `encEmbeddedKeyName` should be provided.

### WsSecurityToTargetPart

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| name | string | Yes | - | Part name (e.g., "Body", "UsernameToken") |
| namespace | string | Yes | - | Part namespace URI |
| encodeType | string | Yes | - | Encode type. See [EnumWsSecurityEncryptionPartEncodeType](/#enumwssecurityencryptionpartencodetype) |

### EnumWsSecurityEncryptionPartEncodeType

- `CONTENT` - Encrypt content only
- `ELEMENT` - Encrypt entire element

### Common Part Names and Namespaces

- Body: `name: "Body"`, `namespace: "http://schemas.xmlsoap.org/soap/envelope/"`
- UsernameToken: `name: "UsernameToken"`, `namespace: "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"`
- Timestamp: `name: "Timestamp"`, `namespace: "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"`

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
  "https://demo.apinizer.com/apiops/projects/MyProject/apiProxies/MyAPI/policies/ws-security-encrypt-policy/" \
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
      "type": "policy-ws-security-encrypt",
      "description": "Encrypt SOAP message body",
      "active": true,
      "mustUnderstand": true,
      "encPartList": [
        {
          "name": "Body",
          "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
          "encodeType": "CONTENT"
        }
      ],
      "encKeyIdType": "X509_CERTIFICATE",
      "encSymEncAlgorithm": "AES_128_CBC",
      "encKeyEncAlgorithm": "RSA",
      "encKeyStoreName": "encryption-keystore"
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

- **Encryption Algorithms**: 
  - `AES_128_CBC`, `AES_192_CBC`, `AES_256_CBC` - Symmetric encryption algorithms
  - `AES_256_CBC` is recommended for stronger security
- **Key Encryption**: 
  - `RSA` - RSA v1.5 (legacy, less secure)
  - `OAEP` - RSA-OAEP (recommended, more secure)
- **Key Identifier Types**: 
  - `X509_CERTIFICATE` - Most common and recommended
  - `EMBEDDED_KEY_INFO` - Use embedded key (requires `encEmbeddedKeyName`)
- **Parts**: 
  - `CONTENT` - Encrypt only the content (preserves element structure)
  - `ELEMENT` - Encrypt entire element (more secure)
- **Key Store**: 
  - Encryption keystore must be configured in Apinizer
  - Keystore must contain appropriate certificates/keys
  - Key identifier type must match keystore content
- **Performance**: Encryption adds significant cryptographic processing overhead. Use for necessary security only.
- **Pipeline**: 
  - `REQUEST` pipeline encrypts outgoing requests
  - `RESPONSE` pipeline encrypts outgoing responses
- **Error Handling**: Invalid keystore, missing keys, or configuration errors cause policy to fail
- **Deployment**: Policy changes require deployment to take effect. Set `deploy: true` or deploy manually.

## Related Documentation

- [List Policies](../crud/list-policies.md) - List all policies
- [Add Policy](../crud/add-policy.md) - General policy addition guide
- [Update Policy](../crud/update-policy.md) - General policy update guide
- [Delete Policy](../crud/delete-policy.md) - General policy deletion guide
- [WS Security Decrypt Policy](policy-ws-security-decrypt.md) - Decrypt WS-Security content
