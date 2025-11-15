# List Environments

## Overview

Retrieves all environments in the system. This endpoint is only available to users with admin role.

## Endpoint

```
GET /apiops/environments/
```

## Authentication

Requires a Personal API Access Token with admin role.

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

None

### Query Parameters

None

## Response

### Success Response (200 OK)

```json
{
  "success": true,
  "resultList": [
    {
      "name": "production",
      "description": "Production environment",
      "type": "KUBERNETES",
      "status": "PUBLISHED",
      "accessUrl": "https://api.production.example.com"
    },
    {
      "name": "staging",
      "description": "Staging environment",
      "type": "KUBERNETES",
      "status": "PUBLISHED",
      "accessUrl": "https://api.staging.example.com"
    },
    {
      "name": "development",
      "description": "Development environment",
      "type": "DOCKER",
      "status": "DRAFT",
      "accessUrl": "http://localhost:8080"
    }
  ],
  "resultCount": 3
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Indicates if the request was successful |
| resultList | array | List of environment objects |
| resultCount | integer | Total number of environments |

#### Environment Object Fields

| Field | Type | Description |
|-------|------|-------------|
| name | string | Environment name |
| description | string | Environment description |
| type | string | Environment type |
| status | string | Publish status |
| accessUrl | string | Environment access URL |
| deployed | boolean | Whether API proxies are deployed (may be null) |
| redeployRequired | boolean | Whether redeployment is required (may be null) |

**Enum: type (EnumEnvironmentType)**
- `PRODUCTION` - Production environment
- `SANDBOX` - Sandbox environment
- `TEST` - Test environment

**Enum: status (EnumPublishStatus)**
- `PUBLISHED` - Environment is published and available
- `UNPUBLISHED` - Environment is unpublished
- `REPUBLISH_REQUIRED` - Environment requires republishing

### Error Response (401 Unauthorized)

```json
{
  "error": "unauthorized_client",
  "error_description": "Invalid token or insufficient permissions"
}
```

**Causes:**
- Missing or invalid Authorization header
- Token expired or revoked
- User does not have admin role

### Error Response (500 Internal Server Error)

```json
{
  "error": "internal_error",
  "error_description": "An unexpected error occurred"
}
```

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/environments/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Full JSON Body Example

This endpoint does not require a request body.

## Notes and Warnings

- **Admin Only**: This endpoint requires admin role. Regular users should use [Get Environments by Project](./get-environments-by-project.md)
- **All Environments**: Returns all environments in the system regardless of project associations
- **Null Fields**: Some fields (deployed, redeployRequired) may be null depending on context

## Related Documentation

- [Get Environments by Project](./get-environments-by-project.md) - Get environments for a specific project
- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens

