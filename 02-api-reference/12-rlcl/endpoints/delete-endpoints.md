# Delete Endpoints from RLCL

## Overview

Removes specific endpoints from an RLCL. Only the specified endpoints are removed; other endpoints remain in the RLCL.

## Endpoint

```
DELETE /apiops/projects/{projectName}/rlcl/{rlclName}/endpoints/
```

## Authentication

Requires a Personal API Access Token.

**Header:**
```
Authorization: Bearer YOUR_TOKEN
```

## Request

Same structure as Add Endpoints. See [Add Endpoints](./add-endpoints.md#request-body-fields) for field descriptions.

**Important Notes:**
- Only the specified endpoints are removed
- Endpoints not in the RLCL are ignored (no error)
- Match is based on `apiProxyId` and `endpointId`

### Response

Same as Add Endpoints. See [Add Endpoints](./add-endpoints.md#response) for response format.

## cURL Example

```bash
curl -X DELETE \
  "https://demo.apinizer.com/apiops/projects/MyProject/rlcl/PremiumUserRLCL/endpoints/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "apiProxyId": "MyAPI",
      "endpointName": "GET /users"
    }
  ]'
```

## Notes and Warnings

- **Selective Removal**: 
  - Only the specified endpoints are removed
  - Other endpoints remain in the RLCL
- **Match Criteria**: 
  - Endpoints are matched by `apiProxyId` and `endpointId`
  - `endpointName` can be used to find `endpointId`

## Related Documentation

- [Add Endpoints](./add-endpoints.md) - Add endpoints to RLCL
- [Update Endpoints](./update-endpoints.md) - Replace all endpoints
