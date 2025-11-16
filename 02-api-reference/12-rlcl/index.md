# RLCL API

## Overview

The RLCL (Rate Limit Control List) API provides endpoints for managing Rate Limit Control Lists in Apinizer. RLCLs allow you to define rate limiting rules for credentials and API endpoints, controlling how many requests can be made within a specific time period.

## Endpoints

### CRUD Operations
- [Create RLCL](./crud/create-rlcl.md) - Create a new RLCL
- [Update RLCL](./crud/update-rlcl.md) - Update an existing RLCL
- [Delete RLCL](./crud/delete-rlcl.md) - Delete an RLCL

### Credential Management
- [Add Credentials](./credentials/add-credentials.md) - Add credentials to an RLCL
- [Update Credentials](./credentials/update-credentials.md) - Replace all credentials in an RLCL
- [Delete Credentials](./credentials/delete-credentials.md) - Remove credentials from an RLCL

### Endpoint Management
- [Add Endpoints](./endpoints/add-endpoints.md) - Add API endpoints to an RLCL
- [Update Endpoints](./endpoints/update-endpoints.md) - Replace all endpoints in an RLCL
- [Delete Endpoints](./endpoints/delete-endpoints.md) - Remove endpoints from an RLCL

### Condition Management
- [Add Condition](./condition/add-condition.md) - Add condition to an RLCL
- [Update Condition](./condition/update-condition.md) - Update condition in an RLCL
- [Delete Condition](./condition/delete-condition.md) - Remove condition from an RLCL

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all RLCL operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats
