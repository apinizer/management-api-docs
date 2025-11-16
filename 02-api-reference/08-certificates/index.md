---
layout: default
permalink: /02-api-reference/08-certificates/
---

# Certificates API

## Overview

The Certificates API provides endpoints for managing SSL/TLS certificates in Apinizer. Certificates are used for secure communication, encryption, and authentication in API Proxies.

## Endpoints

- [List Certificates](/management-api-docs/02-api-reference/08-certificates/crud/list-certificates/) - Get all certificates for a project
- [Get Certificate](/management-api-docs/02-api-reference/08-certificates/crud/get-certificate/) - Get a specific certificate
- [Create Certificate](/management-api-docs/02-api-reference/08-certificates/crud/create-certificate/) - Create a new certificate
- [Update Certificate](/management-api-docs/02-api-reference/08-certificates/crud/update-certificate/) - Update an existing certificate
- [Delete Certificate](/management-api-docs/02-api-reference/08-certificates/crud/delete-certificate/) - Delete a certificate
- [Export Certificate](/management-api-docs/02-api-reference/08-certificates/crud/export-certificate/) - Export certificate as ZIP file
- [Get Truststore Certificates](/management-api-docs/02-api-reference/08-certificates/crud/get-truststore-certificates/) - Get certificates from environment truststore

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all certificate operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](/management-api-docs/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/management-api-docs/01-getting-started/error-handling/) - Error response formats
