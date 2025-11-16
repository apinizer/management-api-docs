---
layout: default
permalink: /02-api-reference/16-test/healthcheck/
---

# Healthcheck

## Overview

Returns a simple "OK" response if the Management API is up and accessible. This endpoint does not require authentication and can be used for monitoring and health checks.

## Endpoint

```
GET /apiops/test/healthcheck
```

## Authentication

No authentication required.

## Request

### Headers

None required.

### Path Parameters

None.

### Query Parameters

None.

## Response

### Success Response (200 OK)

**Content-Type:** `text/plain`

```
OK
```

### Notes

- Returns plain text "OK" if API is accessible
- No authentication required
- Useful for load balancer health checks

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/test/healthcheck"
```

## Notes and Warnings

- **No Authentication**: 
  - This endpoint does not require authentication
  - Can be used for public health checks
- **Simple Response**: 
  - Returns only "OK" text
  - No additional information is provided

## Related Documentation

- [Secure Hello](/02-api-reference/16-test/02-api-reference/16-test/secure-hello/) - Test authentication
