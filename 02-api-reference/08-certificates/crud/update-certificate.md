# Update Certificate

## Overview

Updates an existing certificate. The certificate name cannot be changed. Certificate is automatically deployed to all specified environments after update.

## Endpoint

```
PUT /apiops/projects/{projectName}/certificates/{certificateName}/
```

## Authentication

Requires a Personal API Access Token.

**Header:**
```
Authorization: Bearer YOUR_TOKEN
```

## Request

### Headers

| Header | Value | Required |
|--------|-------|----------|
| Authorization | Bearer {token} | Yes |
| Content-Type | multipart/form-data | Yes |

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| certificateName | string | Yes | Certificate name (cannot be changed) |

### Form Data

Same as Create Certificate. See [Create Certificate](./create-certificate.md#form-data) for field descriptions.

**Notes:**
- Certificate name in path must match existing certificate
- All form fields are required
- Old certificate is deleted and new one is created
- Certificate is automatically deployed after update

### Response

Same as Create Certificate. See [Create Certificate](./create-certificate.md#response) for response format.

## cURL Example

```bash
curl -X PUT \
  "https://demo.apinizer.com/apiops/projects/MyProject/certificates/my-certificate/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "alias=updated-cert-alias" \
  -F "certificateDescription=Updated SSL certificate" \
  -F "environmentList=production,staging" \
  -F "pemEncodedFile=@updated-certificate.pem"
```

## Notes and Warnings

- **Certificate Name**: 
  - Cannot be changed (specified in path)
  - Must match existing certificate
- **Replacement**: 
  - Old certificate is deleted and new one is created
  - This ensures clean update across all environments
- **All Fields Required**: 
  - All form fields must be provided
  - Same requirements as create

## Related Documentation

- [Create Certificate](./create-certificate.md) - Create a new certificate
- [Get Certificate](./get-certificate.md) - Get certificate details

