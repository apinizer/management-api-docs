# Get Environments by Project

## Overview

Retrieves all environments that are accessible from a specific project. This endpoint filters environments based on project associations and user permissions.

## Endpoint

```
GET /apiops/environments/{projectName}
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
| projectName | string | Yes | Project name |

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
    }
  ],
  "resultCount": 2
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Indicates if the request was successful |
| resultList | array | List of environment objects accessible from the project |
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

### EnumEnvironmentType

- `PRODUCTION` - Production environment
- `SANDBOX` - Sandbox environment
- `TEST` - Test environment

### EnumPublishStatus

- `PUBLISHED` - Environment is published and available
- `UNPUBLISHED` - Environment is unpublished
- `REPUBLISH_REQUIRED` - Environment requires republishing

### Error Response (400 Bad Request)

```json
{
  "error": "bad_request",
  "error_description": "Project not found for name: (MyProject) or user has not privilege to access it!"
}
```

### Causes

- Project name does not exist
- User does not have access to the project
- Invalid project name format

### Error Response (401 Unauthorized)

```json
{
  "error": "unauthorized_client",
  "error_description": "Invalid token"
}
```

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
  "https://demo.apinizer.com/apiops/environments/MyProject" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Full JSON Body Example

This endpoint does not require a request body.

## Notes and Warnings

- **Project Membership**: User must be a member of the project to access its environments
- **Filtered Results**: Only environments associated with or accessible from the project are returned
- **Case Sensitivity**: Project names are case-sensitive
- **Empty List**: If no environments are accessible, an empty `resultList` is returned

## Related Documentation

- [List Environments](./list-environments.md) - Get all environments (admin only)
- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Projects API](../02-projects/) - Project management
