# List Connections

## Overview

Retrieves all connections for a specific project. Secret fields (passwords, API keys, etc.) are masked and returned as `null` in list operations.

## Endpoint

```
GET /apiops/projects/{projectName}/connections/
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
      "_class": "email",
      "id": "connection-id-1",
      "projectId": "project-id",
      "name": "my-email-connection",
      "description": "Email connection for notifications",
      "deployToWorker": true,
      "enabled": true,
      "host": "smtp.example.com",
      "port": 587,
      "username": "user@example.com",
      "password": null,
      "enableStartTls": true,
      "auth": true,
      "defaultEncoding": "UTF-8",
      "from": "noreply@example.com"
    },
    {
      "_class": "kafka",
      "id": "connection-id-2",
      "projectId": "project-id",
      "name": "my-kafka-connection",
      "description": "Kafka connection for event streaming",
      "deployToWorker": true,
      "enabled": true,
      "topicName": "events",
      "keyStoreName": "my-keystore",
      "trustStoreName": "my-truststore"
    }
  ],
  "resultCount": 2
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Indicates if the request was successful |
| resultList | array | List of connection objects |
| resultCount | integer | Total number of connections |

#### Connection Object Fields (Common)

| Field | Type | Description |
|-------|------|-------------|
| _class | string | Connection type identifier |
| id | string | Connection unique identifier |
| projectId | string | Project ID |
| name | string | Connection name |
| description | string | Connection description |
| deployToWorker | boolean | Whether to deploy to worker |
| enabled | boolean | Whether connection is enabled |

**Note:** Connection-specific fields vary by connection type. Secret fields are returned as `null` in list operations.

### Error Response (401 Unauthorized)

```json
{
  "error": "unauthorized_client",
  "error_description": "Invalid token"
}
```

### Error Response (404 Not Found)

```json
{
  "error": "not_found",
  "error_description": "Project 'MyProject' not found"
}
```

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/projects/MyProject/connections/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Full JSON Body Example

This endpoint does not require a request body.

## Notes and Warnings

- **Secret Fields**: Secret fields (password, apiKey, etc.) are masked and returned as `null` in list operations
- **Get Single Connection**: Use [Get Connection](./get-connection.md) to retrieve full connection details including secrets
- **Connection Types**: Each connection type has different fields. See individual connection type documentation for details

## Related Documentation

- [Get Connection](./get-connection.md) - Get detailed connection information
- [Create Connection](./create-connection.md) - Create a new connection
- [Email Connection](../connections/connection-email.md) - Email connection details

