---
layout: default
permalink: /02-api-reference/14-reports/organization-api-data-model-access-report/
---

# Organization API Data Model Access Report

## Overview

Retrieves an organization-level report showing API and data model access information. This report includes information about which APIs are shared externally or both internally and externally.

## Endpoint

```
GET /apiops/reports/organization-api-data-model-access
```

## Authentication

Requires a Personal API Access Token with admin or analyzer privileges.

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

None.

### Query Parameters

None.

## Response

### Success Response (200 OK)

```json
{
  "success": true,
  "result": {
    "apiProxyList": [
      {
        "apiProxyName": "MyAPI",
        "sharingType": "EXTERNAL",
        "accessList": []
      }
    ],
    "dataModelList": []
  }
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Indicates if the request was successful |
| result | object | Report result. See [Report Result Object](/#report-result-object) |

### Report Result Object (result)

| Field | Type | Description |
|-------|------|-------------|
| apiProxyList | array[object] | List of API Proxy access information |
| dataModelList | array[object] | List of data model access information |

### API Proxy Access Object (apiProxyList item)


| Field | Type | Description |
|-------|------|-------------|
| apiProxyName | string | API Proxy name |
| sharingType | string | Sharing type. See [EnumSharingType](/#enumsharingtype) |
| accessList | array[object] | List of access information |

### EnumSharingType (sharingType)

- `EXTERNAL` - Shared externally
- `INTERNAL` - Shared internally only
- `BOTH` - Shared both internally and externally
- `NONE` - Not shared

### Notes

- Report includes only APIs with `EXTERNAL` or `BOTH` sharing types
- Empty lists are returned if no data matches the criteria
- Only accessible by sysAdmin or sysAnalyzer users

### Error Response (401 Unauthorized)

```json
{
  "error": "unauthorized_client",
  "error_description": "Unauthorized API Access!"
}
```

## cURL Example

```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/reports/organization-api-data-model-access" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Notes and Warnings

- **Admin/Analyzer Only**: 
  - This endpoint requires sysAdmin or sysAnalyzer privileges
  - Regular users cannot access this endpoint
- **Sharing Types**: 
  - Report includes only APIs with EXTERNAL or BOTH sharing types
  - Internal-only APIs are excluded

## Related Documentation

- [API Report](api-report.md) - API Proxy report
- [Update Metadata](../04-api-proxies/settings/update-metadata.md) - Update API Proxy sharing type
