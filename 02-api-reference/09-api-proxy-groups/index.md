# API Proxy Groups API

## Overview

The API Proxy Groups API provides endpoints for managing API Proxy Groups in Apinizer. API Proxy Groups allow you to group multiple API Proxies together and manage them as a single unit, including shared client routes, CORS settings, cache settings, and deployment.

## Endpoints

### CRUD Operations
- [List API Proxy Groups](./crud/list-api-proxy-groups.md) - Get all API Proxy Groups for a project
- [Create API Proxy Group](./crud/create-api-proxy-group.md) - Create a new API Proxy Group
- [Update API Proxy Group](./crud/update-api-proxy-group.md) - Update an existing API Proxy Group
- [Delete API Proxy Group](./crud/delete-api-proxy-group.md) - Delete an API Proxy Group

### API Proxy Management
- [Add API Proxy to Group](./api-proxies/add-api-proxy-to-group.md) - Add an API Proxy to a group
- [Remove API Proxy from Group](./api-proxies/remove-api-proxy-from-group.md) - Remove an API Proxy from a group

### Deployment
- [List Environments](./deployment/list-environments.md) - Get all environments of an API Proxy Group
- [Deploy API Proxy Group](./deployment/deploy-api-proxy-group.md) - Deploy an API Proxy Group to an environment
- [Undeploy API Proxy Group](./deployment/undeploy-api-proxy-group.md) - Undeploy an API Proxy Group from an environment

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXY_GROUPS` - Required for all API Proxy Group operations
- `ROLE_MANAGE_PROXIES` - Required for adding/removing API Proxies
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats
- [API Proxies API](../04-api-proxies/index.md) - API Proxy management

