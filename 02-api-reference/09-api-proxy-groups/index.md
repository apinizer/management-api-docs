---
layout: default
permalink: /02-api-reference/09-api-proxy-groups/
---

# API Proxy Groups API

## Overview

The API Proxy Groups API provides endpoints for managing API Proxy Groups in Apinizer. API Proxy Groups allow you to group multiple API Proxies together and manage them as a single unit, including shared client routes, CORS settings, cache settings, and deployment.

## Endpoints

### CRUD Operations
- [List API Proxy Groups](/management-api-docs/02-api-reference/09-api-proxy-groups/crud/list-api-proxy-groups/) - Get all API Proxy Groups for a project
- [Create API Proxy Group](/management-api-docs/02-api-reference/09-api-proxy-groups/crud/create-api-proxy-group/) - Create a new API Proxy Group
- [Update API Proxy Group](/management-api-docs/02-api-reference/09-api-proxy-groups/crud/update-api-proxy-group/) - Update an existing API Proxy Group
- [Delete API Proxy Group](/management-api-docs/02-api-reference/09-api-proxy-groups/crud/delete-api-proxy-group/) - Delete an API Proxy Group

### API Proxy Management
- [Add API Proxy to Group](/management-api-docs/02-api-reference/09-api-proxy-groups/api-proxies/add-api-proxy-to-group/) - Add an API Proxy to a group
- [Remove API Proxy from Group](/management-api-docs/02-api-reference/09-api-proxy-groups/api-proxies/remove-api-proxy-from-group/) - Remove an API Proxy from a group

### Deployment
- [List Environments](/management-api-docs/02-api-reference/09-api-proxy-groups/deployment/list-environments/) - Get all environments of an API Proxy Group
- [Deploy API Proxy Group](/management-api-docs/02-api-reference/09-api-proxy-groups/deployment/deploy-api-proxy-group/) - Deploy an API Proxy Group to an environment
- [Undeploy API Proxy Group](/management-api-docs/02-api-reference/09-api-proxy-groups/deployment/undeploy-api-proxy-group/) - Undeploy an API Proxy Group from an environment

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXY_GROUPS` - Required for all API Proxy Group operations
- `ROLE_MANAGE_PROXIES` - Required for adding/removing API Proxies
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](/management-api-docs/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/management-api-docs/01-getting-started/error-handling/) - Error response formats
- [API Proxies API](/management-api-docs/02-api-reference/04-api-proxies/) - API Proxy management
