---
layout: default
permalink: /02-api-reference/16-test/
---

# Test API

## Overview

The Test API provides simple endpoints for testing API connectivity and authentication. These endpoints are useful for verifying that the Management API is accessible and that your authentication token is working correctly.

## Endpoints

- [Healthcheck](../../../02-api-reference/16-test/healthcheck/) - Check if the API is up and accessible
- [Secure Hello](../../../02-api-reference/16-test/secure-hello/) - Test authentication with a simple greeting

## Authentication

Most endpoints require authentication using a Personal API Access Token. Healthcheck endpoint does not require authentication.

## Related Documentation

- [Authentication Guide](../../../01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](../../../01-getting-started/error-handling/) - Error response formats
