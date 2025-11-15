# Delete IP Group

## Overview

Deletes an IP Group specified by name. The group and all its IP addresses are permanently removed.

## Endpoint

```
DELETE /apiops/projects/{projectName}/ipGroups/{ipGroupName}/
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
| ipGroupName | string | Yes | IP Group name |

### Request Body

None.

## Response

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
  "error_description": "IP Group (AllowedIPs) is not found!"
}
```

## cURL Example

```bash
curl -X DELETE \
  "https://demo.apinizer.com/apiops/projects/MyProject/ipGroups/AllowedIPs/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Notes and Warnings

- **Permanent Deletion**: 
  - IP Group is permanently deleted
  - This action cannot be undone
- **IP Addresses**: 
  - All IP addresses in the group are also removed
- **Policy References**: 
  - Policies using this IP Group may need to be updated
  - Check for policy references before deletion

## Related Documentation

- [Create IP Group](./create-ip-group.md) - Create a new IP Group
- [Update IP Group](./update-ip-group.md) - Update an IP Group
