---
layout: default
permalink: /02-api-reference/07-credentials/
---

# Credentials API

## Overview

The Credentials API provides endpoints for managing credentials in Apinizer. Credentials are used for authentication and authorization, allowing users or applications to access API Proxies and API Proxy Groups.

## Endpoints

- [List Credentials](/management-api-docs/02-api-reference/07-credentials/crud/list-credentials/) - Get all credentials for a project
- [Create Credential](/management-api-docs/02-api-reference/07-credentials/crud/create-credential/) - Create a new credential
- [Update Credential](/management-api-docs/02-api-reference/07-credentials/crud/update-credential/) - Update an existing credential
- [Change Credential Password](/management-api-docs/02-api-reference/07-credentials/crud/change-credential-password/) - Change credential password
- [Delete Credential](/management-api-docs/02-api-reference/07-credentials/crud/delete-credential/) - Delete a credential
- [Get Granted Access List](/management-api-docs/02-api-reference/07-credentials/access/get-granted-access-list/) - Get list of API Proxies/Groups granted to credential
- [Grant Access](/management-api-docs/02-api-reference/07-credentials/access/grant-access/) - Grant access to API Proxy or API Proxy Group
- [Revoke Access](/management-api-docs/02-api-reference/07-credentials/access/revoke-access/) - Revoke access from API Proxy or API Proxy Group

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all credential operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](/management-api-docs/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/management-api-docs/01-getting-started/error-handling/) - Error response formats
