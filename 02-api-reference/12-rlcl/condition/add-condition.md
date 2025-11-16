---
layout: default
permalink: /02-api-reference/12-rlcl/condition/add-condition/
---

# Add Condition to RLCL

## Overview

Adds a condition to an RLCL. Conditions determine when the RLCL should be applied. If a condition is set, the RLCL is only applied when the condition evaluates to true.

## Endpoint

```
POST /apiops/projects/{projectName}/rlcl/{rlclName}/condition/
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
| Content-Type | application/json | Yes |

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| rlclName | string | Yes | RLCL name |

### Request Body

#### Full JSON Body Example - Simple Condition

```json
{
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
      "secondValue": "PREMIUM"
    }
  ]
}
```

#### Full JSON Body Example - Complex Condition with Multiple Rules

```json
{
  "conditionRuleList": [
    {
      "conditionCriteria": "OR",
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
          "secondValue": "PREMIUM"
        },
        {
          "conditionCriteria": "AND",
          "firstVariable": {
            "name": "request.header.X-API-Version",
            "type": "HEADER",
            "dataType": "STRING"
          },
          "variableDataType": "STRING",
          "valueComparisonOperator": "EQUALS",
          "secondValueSource": "STATIC",
          "secondValue": "v2"
        }
      ]
    }
  ]
}
```

#### Request Body Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| conditionRuleList | array[object] | Yes | - | List of condition rules. See [ConditionRuleDTO](../../...md#conditionruledto) |

### ConditionRuleDTO (conditionRuleList item)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| conditionRuleList | array[object] | No | Nested condition rules (for complex conditions) |
| conditionCriteria | string | Yes | Condition criteria. See [EnumConditionCriteria](../../...md#enumconditioncriteria) |
| firstVariable | object | Yes | First variable for comparison. See [Variable Object](../../...md#variable-object) |
| variableDataType | string | Yes | Variable data type. See [EnumConditionVariableDataType](../../...md#enumconditionvariabledatatype) |
| dateFormat | string | No | Date format for date comparisons |
| valueComparisonOperator | string | Yes | Comparison operator. See [EnumConditionValueComparisonOperator](../../...md#enumconditionvaluecomparisonoperator) |
| secondValueSource | string | Yes | Second value source. See [EnumConditionValueSource](../../...md#enumconditionvaluesource) |
| secondValue | string | No | Static value for comparison (if secondValueSource is STATIC) |
| secondVariable | object | No | Second variable for comparison (if secondValueSource is VARIABLE) |

### EnumConditionCriteria (conditionCriteria)

- `AND` - All conditions must match
- `OR` - Any condition must match
- `NOT` - Condition must not match

### EnumConditionVariableDataType (variableDataType)

- `STRING` - String data type
- `NUMBER` - Number data type
- `BOOLEAN` - Boolean data type
- `DATE` - Date data type

### EnumConditionValueComparisonOperator (valueComparisonOperator)

- `EQUALS` - Equal to
- `NOT_EQUALS` - Not equal to
- `CONTAINS` - Contains
- `NOT_CONTAINS` - Does not contain
- `STARTS_WITH` - Starts with
- `ENDS_WITH` - Ends with
- `GREATER_THAN` - Greater than
- `GREATER_THAN_OR_EQUAL` - Greater than or equal
- `LESS_THAN` - Less than
- `LESS_THAN_OR_EQUAL` - Less than or equal
- `REGEX_MATCH` - Regular expression match
- `REGEX_NOT_MATCH` - Regular expression does not match

### EnumConditionValueSource (secondValueSource)

- `STATIC` - Static value (use `secondValue`)
- `VARIABLE` - Variable value (use `secondVariable`)

### Variable Object (firstVariable/secondVariable)

See [Variable Definition](../../../03-appendix/variable-definition.md) for complete variable documentation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Variable name (e.g., "request.header.X-User-Type", "client.ip") |
| type | string | Yes | Variable type. See [Variable Types](../../../03-appendix/variable-definition.md) |
| headerName | string | No* | Header name (required if type=HEADER) |
| paramType | string | No* | Parameter type (required if type=PARAMETER) |
| paramName | string | No* | Parameter name (required if type=PARAMETER) |
| paramPath | string | No* | Parameter path template (required if type=PARAMETER and paramType=PATH) |
| messageContentType | string | No* | Message content type (required if type=BODY) |
| xpathValue | string | No* | XPath expression (required if type=BODY and messageContentType=XML) |
| jsonPathValue | string | No* | JsonPath expression (required if type=BODY and messageContentType=JSON) |
| contextValue | string | No* | Context value (required if type=CONTEXT_VALUES). See [EnumVariableContextValue](../../../03-appendix/variable-definition.md) |
| zoneId | string | No* | Time zone ID (required for date/time context values) |

### Notes

- Conditions are evaluated before applying rate limiting
- If condition evaluates to false, RLCL is not applied
- Nested conditions are supported for complex logic
- If conditionRuleList is empty, default AND rule is used

### Response

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
  "error_description": "condition value can not be empty!"
}
```

## cURL Example

```bash
curl -X POST \
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
        "secondValue": "PREMIUM"
      }
    ]
  }'
```

## Notes and Warnings

- **Condition Evaluation**: 
  - Condition is evaluated before applying rate limiting
  - If condition is false, RLCL is not applied
- **Nested Conditions**: 
  - Complex conditions can be created using nested rules
  - Use conditionRuleList for nested logic
- **RLCL Must Exist**: 
  - RLCL must exist before adding condition

## Related Documentation

- [Update Condition](update-condition.md) - Update condition in RLCL
- [Delete Condition](delete-condition.md) - Remove condition from RLCL
- [Policy Conditions](../../05-policies/crud/add-policy.md) - Detailed condition documentation
