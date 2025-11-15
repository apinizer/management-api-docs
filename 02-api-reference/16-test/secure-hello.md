# Secure Hello

## Overview

Returns a personalized greeting message if the user is authenticated. This endpoint is useful for testing authentication tokens and verifying API access.

## Endpoint

```
GET /apiops/test/hello/{name}
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

**Example:**
```
Hello John
```

**Notes:**
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

## Usage Scenarios

### Scenario 1: Test Authentication Token

Verify that your authentication token is working correctly.

**Request:**
```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/test/hello/TestUser" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Response:**
```
Hello TestUser
```

## Notes and Warnings

- **Authentication Required**: 
  - This endpoint requires a valid authentication token
  - Invalid tokens will return 401 Unauthorized
- **Simple Test**: 
  - Useful for quick authentication verification
  - Does not perform any complex operations

## Related Documentation

- [Healthcheck](./healthcheck.md) - Check API availability
- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain tokens

