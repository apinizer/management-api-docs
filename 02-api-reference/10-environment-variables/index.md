# Environment Variables API

## Overview

The Environment Variables API provides endpoints for managing environment variables in Apinizer. Environment variables allow you to store configuration values that can vary between environments (e.g., API endpoints, database URLs, API keys).

## Endpoints

- [List Environment Variables](./crud/list-environment-variables.md) - Get all environment variables for a project
- [Get Environment Variable](./crud/get-environment-variable.md) - Get a specific environment variable
- [Create Environment Variable](./crud/create-environment-variable.md) - Create a new environment variable
- [Update Environment Variable](./crud/update-environment-variable.md) - Update an existing environment variable
- [Delete Environment Variable](./crud/delete-environment-variable.md) - Delete an environment variable

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_API_SECURITY` - Required for all environment variable operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats
