# Certificates API

## Overview

The Certificates API provides endpoints for managing SSL/TLS certificates in Apinizer. Certificates are used for secure communication, encryption, and authentication in API Proxies.

## Endpoints

- [List Certificates](./crud/list-certificates.md) - Get all certificates for a project
- [Get Certificate](./crud/get-certificate.md) - Get a specific certificate
- [Create Certificate](./crud/create-certificate.md) - Create a new certificate
- [Update Certificate](./crud/update-certificate.md) - Update an existing certificate
- [Delete Certificate](./crud/delete-certificate.md) - Delete a certificate
- [Export Certificate](./crud/export-certificate.md) - Export certificate as ZIP file
- [Get Truststore Certificates](./crud/get-truststore-certificates.md) - Get certificates from environment truststore

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all certificate operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats

