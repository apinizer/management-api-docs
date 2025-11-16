---
layout: default
permalink: /02-api-reference/07-credentials/
---

# Credentials API

## Overview

The Credentials API provides endpoints for managing credentials in Apinizer. Credentials are used for authentication and authorization, allowing users or applications to access API Proxies and API Proxy Groups.

## Endpoints

- [List Credentials](./crud/list-credentials) - Get all credentials for a project
- [Create Credential](./crud/create-credential) - Create a new credential
- [Update Credential](./crud/update-credential) - Update an existing credential
- [Change Credential Password](./crud/change-credential-password) - Change credential password
- [Delete Credential](./crud/delete-credential) - Delete a credential
- [Get Granted Access List](./access/get-granted-access-list) - Get list of API Proxies/Groups granted to credential
- [Grant Access](./access/grant-access) - Grant access to API Proxy or API Proxy Group
- [Revoke Access](./access/revoke-access) - Revoke access from API Proxy or API Proxy Group

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all credential operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling) - Error response formats
