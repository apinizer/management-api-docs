# Update Condition in RLCL

## Overview

Updates the condition in an RLCL. Replaces the existing condition with the new one.

## Endpoint

```
PUT /apiops/projects/{projectName}/rlcl/{rlclName}/condition/
```

## Authentication

Requires a Personal API Access Token.

**Header:**
```
Authorization: Bearer YOUR_TOKEN
```

## Request

Same structure as Add Condition. See [Add Condition](./add-condition.md#request-body-fields) for field descriptions.

**Important Notes:**
- Replaces the existing condition completely
- Same structure as Add Condition

### Response

Same as Add Condition. See [Add Condition](./add-condition.md#response) for response format.

## cURL Example

```bash
curl -X PUT \
  "https://demo.apinizer.com/apiops/projects/MyProject/rlcl/PremiumUserRLCL/condition/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "conditionRuleList": [
      {
        "conditionCriteria": "AND",
        "firstVariable": {
          "name": "request.header.X-User-Type",
          "type": "HEADER",
          "dataType": "STRING"
        },
        "variableDataType": "STRING",
        "valueComparisonOperator": "EQUALS",
        "secondValueSource": "STATIC",
        "secondValue": "VIP"
      }
    ]
  }'
```

## Related Documentation

- [Add Condition](./add-condition.md) - Add condition to RLCL
- [Delete Condition](./delete-condition.md) - Remove condition from RLCL

