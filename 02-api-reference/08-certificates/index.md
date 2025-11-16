---
layout: default
permalink: /02-api-reference/08-certificates/
---

# Certificates API

## Overview

The Certificates API provides endpoints for managing SSL/TLS certificates in Apinizer. Certificates are used for secure communication, encryption, and authentication in API Proxies.

## Endpoints

- [List Certificates](/02-api-reference/08-certificates/02-api-reference/08-certificates/crud/list-certificates/) - Get all certificates for a project
- [Get Certificate](/02-api-reference/08-certificates/02-api-reference/08-certificates/crud/get-certificate/) - Get a specific certificate
- [Create Certificate](/02-api-reference/08-certificates/02-api-reference/08-certificates/crud/create-certificate/) - Create a new certificate
- [Update Certificate](/02-api-reference/08-certificates/02-api-reference/08-certificates/crud/update-certificate/) - Update an existing certificate
- [Delete Certificate](/02-api-reference/08-certificates/02-api-reference/08-certificates/crud/delete-certificate/) - Delete a certificate
- [Export Certificate](/02-api-reference/08-certificates/02-api-reference/08-certificates/crud/export-certificate/) - Export certificate as ZIP file
- [Get Truststore Certificates](/02-api-reference/08-certificates/02-api-reference/08-certificates/crud/get-truststore-certificates/) - Get certificates from environment truststore

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all certificate operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](/02-api-reference/08-certificates/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/02-api-reference/08-certificates/01-getting-started/error-handling/) - Error response formats
