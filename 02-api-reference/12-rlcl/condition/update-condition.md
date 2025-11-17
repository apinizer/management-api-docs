---
layout: default
permalink: /02-api-reference/12-rlcl/condition/update-condition/
---

# Update Condition in RLCL

## Overview

Updates the condition in an RLCL. Replaces the existing condition with the new one.

## Endpoint

```
PUT /apiops/projects/{projectName}/rlcl/{rlclName}/condition/
```

## Authentication

Requires a Personal API Access Token.

### Header

```
Authorization: Bearer YOUR_TOKEN
```

## Request

Same structure as Add Condition. See [Add Condition](/management-api-docs/02-api-reference/12-rlcl/condition/add-condition/) for field descriptions.

### Important Notes

- Replaces the existing condition completely
- Same structure as Add Condition

### Response

Same as Add Condition. See [Add Condition](/management-api-docs/02-api-reference/12-rlcl/condition/add-condition/) for response format.

## cURL Example

```bash
curl -X PUT \
  "https://demo.apinizer.com/apiops/projects/MyProject/rlcl/PremiumUserRLCL/condition/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "conditionRuleList": [
      {
        "conditionCriteria": "VALUE",
        "firstVariable": {
          "name": "userTypeHeader",
          "type": "HEADER",
          "headerName": "X-User-Type"
        },
        "variableDataType": "STRING",
        "valueComparisonOperator": "EQ",
        "secondValueSource": "VALUE",
        "secondValue": "VIP"
      }
    ]
  }'
```

## Related Documentation

- [Add Condition](/management-api-docs/02-api-reference/12-rlcl/condition/add-condition/) - Add condition to RLCL
- [Delete Condition](/management-api-docs/02-api-reference/12-rlcl/condition/delete-condition/) - Remove condition from RLCL
