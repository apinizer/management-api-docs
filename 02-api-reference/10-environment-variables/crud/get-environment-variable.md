---
layout: default
permalink: /02-api-reference/10-environment-variables/crud/get-environment-variable/
---

# Get Environment Variable

## Overview

Retrieves a specific environment variable by name. Returns full details including values (secret values are masked if not visible).

## Endpoint

```
GET /apiops/projects/{projectName}/environmentVariables/{name}/
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
| projectName | string | Yes | Project name (can be "admin" for admin project) |
| name | string | Yes | Environment variable name |

### Query Parameters

None.

## Response

### Success Response (200 OK)

```json
{
  "success": true,
  "resultList": [
    {
      "projectId": "project-id",
      "name": "API_BASE_URL",
      "description": "Base URL for API calls",
      "global": false,
      "globalValue": null,
      "globalVisible": true,
      "projectName": "MyProject",
      "environmentValueList": [
        {
          "environmentName": "production",
          "value": "https://api.production.example.com",
          "visible": true
        },
        {
          "environmentName": "staging",
          "value": "https://api.staging.example.com",
          "visible": true
        }
      ]
    }
  ],
  "resultCount": 1
}
```

#### Response Fields

Same as List Environment Variables. See [List Environment Variables](/management-api-docs/02-api-reference/10-environment-variables/crud/list-environment-variables/) for field descriptions.

### Notes

- Secret values (`visible=false` or `globalVisible=false`) are masked (returned as `null`)
- Returns single environment variable matching the name

### Error Response (400 Bad Request)

```json
{
  "error": "bad_request",
  "error_description": "Environment variable (name: API_BASE_URL) was not found!"
}
```

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/projects/MyProject/environmentVariables/API_BASE_URL/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Related Documentation

- [List Environment Variables](/management-api-docs/02-api-reference/10-environment-variables/crud/list-environment-variables/) - List all environment variables
- [Create Environment Variable](/management-api-docs/02-api-reference/10-environment-variables/crud/create-environment-variable/) - Create a new environment variable
