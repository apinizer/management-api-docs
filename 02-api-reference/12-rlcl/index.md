---
layout: default
permalink: /02-api-reference/12-rlcl/
---

# RLCL API

## Overview

The RLCL (Rate Limit Control List) API provides endpoints for managing Rate Limit Control Lists in Apinizer. RLCLs allow you to define rate limiting rules for credentials and API endpoints, controlling how many requests can be made within a specific time period.

## Endpoints

### CRUD Operations
- [Create RLCL](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/crud/create-rlcl/) - Create a new RLCL
- [Update RLCL](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/crud/update-rlcl/) - Update an existing RLCL
- [Delete RLCL](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/crud/delete-rlcl/) - Delete an RLCL

### Credential Management
- [Add Credentials](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/credentials/add-credentials/) - Add credentials to an RLCL
- [Update Credentials](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/credentials/update-credentials/) - Replace all credentials in an RLCL
- [Delete Credentials](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/credentials/delete-credentials/) - Remove credentials from an RLCL

### Endpoint Management
- [Add Endpoints](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/endpoints/add-endpoints/) - Add API endpoints to an RLCL
- [Update Endpoints](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/endpoints/update-endpoints/) - Replace all endpoints in an RLCL
- [Delete Endpoints](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/endpoints/delete-endpoints/) - Remove endpoints from an RLCL

### Condition Management
- [Add Condition](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/condition/add-condition/) - Add condition to an RLCL
- [Update Condition](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/condition/update-condition/) - Update condition in an RLCL
- [Delete Condition](/02-api-reference/12-rlcl/02-api-reference/12-rlcl/condition/delete-condition/) - Remove condition from an RLCL

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all RLCL operations

## Related Documentation

- [Authentication Guide](/02-api-reference/12-rlcl/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/02-api-reference/12-rlcl/01-getting-started/error-handling/) - Error response formats
