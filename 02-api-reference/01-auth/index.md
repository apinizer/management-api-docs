---
layout: default
permalink: /02-api-reference/01-auth/
---

# Authentication API

## Overview

The Authentication API provides endpoints for obtaining Personal API Access Tokens, which are required for accessing all other Management API endpoints.

## Endpoints

- [Create Token](./create-token) - Create a Personal API Access Token

## Authentication

The token creation endpoint does not require authentication. However, you must provide valid Apinizer credentials (username and password) to obtain a token.

## Token Usage

Once you have obtained a token, include it in the `Authorization` header of all subsequent API requests:

```
Authorization: Bearer YOUR_TOKEN
```

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication) - Detailed authentication information
- [Error Handling](../../01-getting-started/error-handling) - Error response formats
