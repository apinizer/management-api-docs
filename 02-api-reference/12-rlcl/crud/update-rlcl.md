# Update RLCL

## Overview

Updates an existing RLCL. The name cannot be changed (it's used as the identifier). All other fields can be updated.

## Endpoint

```
PUT /apiops/projects/{projectName}/rlcl/{rlclName}/
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
| Content-Type | application/json | Yes |

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| rlclName | string | Yes | RLCL name (cannot be changed) |

### Request Body

Same structure as Create RLCL. See [Create RLCL](./create-rlcl.md#request-body-fields) for field descriptions.

**Important Notes:**
- `name` must match the RLCL name in path (cannot be changed)
- All other fields can be updated
- Credentials and endpoints are not updated by this endpoint

### Response

#### Success Response (200 OK)
```json
{
  "success": true
}
```

### Error Response (400 Bad Request)

```json
{
  "error": "bad_request",
  "error_description": "RLCL (PremiumUserRLCL) is not found!"
}
```

## cURL Example

```bash
curl -X PUT \
  "https://demo.apinizer.com/apiops/projects/MyProject/rlcl/PremiumUserRLCL/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "PremiumUserRLCL",
    "description": "Updated rate limit for premium users",
    "enabled": true,
    "executionOrder": "FIRST",
    "cacheConnectionTimeoutInSeconds": 5,
    "cacheErrorHandlingType": "CONTINUE",
    "timeIntervalWindowType": "SLIDING",
    "showRateLimitStatisticsInResponseHeader": true
  }'
```

## Notes and Warnings

- **Name Cannot Change**: 
  - Name is used as identifier and cannot be changed
  - Use the existing name in the request
- **Credentials/Endpoints**: 
  - Credentials and endpoints are not updated by this endpoint
  - Use separate endpoints for managing credentials and endpoints

## Related Documentation

- [Create RLCL](./create-rlcl.md) - Create a new RLCL
- [Delete RLCL](./delete-rlcl.md) - Delete an RLCL

