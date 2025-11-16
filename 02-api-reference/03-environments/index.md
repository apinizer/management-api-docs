---
layout: default
permalink: /02-api-reference/03-environments/
---

# Environments API

## Overview

The Environments API provides endpoints for managing deployment environments in Apinizer. Environments are deployment targets where API proxies can be deployed (e.g., production, staging, development).

## Endpoints

- [List Environments](/02-api-reference/03-environments/list-environments/) - Get all environments (admin only)
- [Get Environments by Project](/02-api-reference/03-environments/get-environments-by-project/) - Get environments accessible from a project

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- **List All Environments**: Requires admin role
- **Get Environments by Project**: Requires project membership

## Related Documentation

- [Authentication Guide](/02-api-reference/03-environments/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/02-api-reference/03-environments/01-getting-started/error-handling/) - Error response formats
