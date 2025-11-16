---
layout: default
permalink: /02-api-reference/02-projects/
---

# Projects API

## Overview

The Projects API provides endpoints for managing projects in Apinizer. Projects are containers for API proxies, policies, connections, and other resources.

## Endpoints

- [List Projects](/management-api-docs/02-api-reference/02-projects/list-projects/) - Get all projects accessible by the authenticated user

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

Users can only access projects where they are members. The API automatically filters projects based on the authenticated user's permissions.

## Related Documentation

- [Authentication Guide](/management-api-docs/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/management-api-docs/01-getting-started/error-handling/) - Error response formats
