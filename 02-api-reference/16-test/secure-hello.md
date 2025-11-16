---
layout: default
permalink: /02-api-reference/16-test/secure-hello/
---

# Secure Hello

## Overview

Returns a personalized greeting message if the user is authenticated. This endpoint is useful for testing authentication tokens and verifying API access.

## Endpoint

```
GET /apiops/test/hello/{name}
```

## Authentication

Requires a Personal API Access Token.

### Header

```
Authorization: Bearer YOUR_TOKEN
```

## Request

### Headers

| Header | Value | Required |
|--------|-------|----------|
| Authorization | Bearer {token} | Yes |

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | string | Yes | Name to include in greeting |

### Query Parameters

None.

## Response

### Success Response (200 OK)

**Content-Type:** `text/plain`

```
Hello {name}
```

### Example

```
Hello John
```

### Notes

- Returns "Hello {name}" if authentication is successful
- Name is taken from path parameter
- Response is plain text

### Error Response (401 Unauthorized)

```json
{
  "error": "unauthorized_client",
  "error_description": "Invalid token"
}
```

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/test/hello/John" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Notes and Warnings

- **Authentication Required**: 
  - This endpoint requires a valid authentication token
  - Invalid tokens will return 401 Unauthorized
- **Simple Test**: 
  - Useful for quick authentication verification
  - Does not perform any complex operations

## Related Documentation

- [Healthcheck](/management-api-docs/02-api-reference/16-test/healthcheck/) - Check API availability
- [Authentication Guide](/management-api-docs/01-getting-started/authentication/) - How to obtain tokens
