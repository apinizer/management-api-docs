# Delete Credentials from RLCL

## Overview

Removes specific credentials from an RLCL. Only the specified credentials are removed; other credentials remain in the RLCL.

## Endpoint

```
DELETE /apiops/projects/{projectName}/rlcl/{rlclName}/credentials/
```

## Authentication

Requires a Personal API Access Token.

### Header

```
Authorization: Bearer YOUR_TOKEN
```

## Request

Same structure as Add Credentials. See [Add Credentials](./add-credentials) for field descriptions.

### Important Notes

- Only the specified credentials are removed
- Credentials not in the RLCL are ignored (no error)

### Response

Same as Add Credentials. See [Add Credentials](./add-credentials) for response format.

## cURL Example

```bash
curl -X DELETE \
  "https://demo.apinizer.com/apiops/projects/MyProject/rlcl/PremiumUserRLCL/credentials/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "credentialNameList": [
      "api-user-1"
    ]
  }'
```

## Notes and Warnings

- **Selective Removal**: 
  - Only the specified credentials are removed
  - Other credentials remain in the RLCL
- **Non-existent Credentials**: 
  - Credentials not in the RLCL are ignored (no error)

## Related Documentation

- [Add Credentials](./add-credentials) - Add credentials to RLCL
- [Update Credentials](./update-credentials) - Replace all credentials
