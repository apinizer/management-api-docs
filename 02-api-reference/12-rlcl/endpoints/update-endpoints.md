# Update Endpoints in RLCL

## Overview

Replaces all endpoints in an RLCL with the provided list. This completely replaces the existing endpoint list.

## Endpoint

```
PUT /apiops/projects/{projectName}/rlcl/{rlclName}/endpoints/
```

## Authentication

Requires a Personal API Access Token.

### Header

```
Authorization: Bearer YOUR_TOKEN
```

## Request

Same structure as Add Endpoints. See [Add Endpoints](./add-endpoints) for field descriptions.

### Important Notes

- This endpoint replaces ALL existing endpoints with the provided list
- If you want to add endpoints without removing existing ones, use Add Endpoints endpoint

### Response

Same as Add Endpoints. See [Add Endpoints](./add-endpoints) for response format.

## cURL Example

```bash
curl -X PUT \
  "https://demo.apinizer.com/apiops/projects/MyProject/rlcl/PremiumUserRLCL/endpoints/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "endpointRateLimitList": [
      {
        "apiProxyName": "MyAPI",
        "endpointName": "/users",
        "endpointHTTPMethod": "GET",
        "permittedMessageCount": 200,
        "timeIntervalPeriodLength": 1,
        "timeInterval": "ONE_HOUR",
        "cacheConnectionTimeoutInSeconds": 3,
        "cacheErrorHandlingType": "FAIL",
        "timeIntervalWindowType": "FIXED",
        "showRateLimitStatisticsInResponseHeader": false,
        "enabled": true
      }
    ]
  }'
```

## Notes and Warnings

- **Complete Replacement**: 
  - Replaces ALL existing endpoints with the provided list
  - Existing endpoints not in the new list are removed
- **Use Add Endpoints for Addition**: 
  - If you want to add endpoints without removing existing ones, use Add Endpoints endpoint

## Related Documentation

- [Add Endpoints](./add-endpoints) - Add endpoints without removing existing ones
- [Delete Endpoints](./delete-endpoints) - Remove specific endpoints
