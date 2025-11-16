---
layout: default
permalink: /02-api-reference/12-rlcl/condition/delete-condition/
---

# Delete Condition from RLCL

## Overview

Removes the condition from an RLCL. After deletion, the RLCL will be applied unconditionally (always).

## Endpoint

```
DELETE /apiops/projects/{projectName}/rlcl/{rlclName}/condition/
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
| rlclName | string | Yes | RLCL name |

### Request Body

None.

## Response

#### Success Response (200 OK)
```json
{
  "success": true
}
```

## cURL Example

```bash
curl -X DELETE \
  "https://demo.apinizer.com/apiops/projects/MyProject/rlcl/PremiumUserRLCL/condition/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Notes and Warnings

- **Unconditional Application**: 
  - After deletion, RLCL is applied unconditionally (always)
  - No condition evaluation is performed

## Related Documentation

- [Add Condition](../../../../02-api-reference/12-rlcl/condition/add-condition/) - Add condition to RLCL
- [Update Condition](../../../../02-api-reference/12-rlcl/condition/update-condition/) - Update condition in RLCL
