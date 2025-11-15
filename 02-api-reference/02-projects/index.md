# Projects API

## Overview

The Projects API provides endpoints for managing projects in Apinizer. Projects are containers for API proxies, policies, connections, and other resources.

## Endpoints

- [List Projects](./list-projects.md) - Get all projects accessible by the authenticated user

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

Users can only access projects where they are members. The API automatically filters projects based on the authenticated user's permissions.

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats
