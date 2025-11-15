# API Proxies API

## Overview

The API Proxies API provides endpoints for managing API proxies in Apinizer. API proxies act as intermediaries between clients and backend services, providing API management capabilities such as security, transformation, and monitoring.

## Endpoints

### CRUD Operations
- [List API Proxies](./crud/list-api-proxies.md) - Get all API proxies for a project
- [Get API Proxy](./crud/get-api-proxy.md) - Get API proxy details
- [Create API Proxy from URL](./crud/create-api-proxy-from-url.md) - Create API proxy from OpenAPI/Swagger/WSDL URL
- [Create API Proxy from File](./crud/create-api-proxy-from-file.md) - Create API proxy from uploaded file
- [Update API Proxy](./crud/update-api-proxy.md) - Update API proxy
- [Delete API Proxy](./crud/delete-api-proxy.md) - Delete API proxy

### Deployment
- [Deploy API Proxy](./deployment/deploy.md) - Deploy API proxy to environments
- [Undeploy API Proxy](./deployment/undeploy.md) - Undeploy API proxy from environments
- [Deployment Status](./deployment/deployment-status.md) - Get deployment status

### Endpoints Management
- [List Endpoints](./endpoints/list-endpoints.md) - List all endpoints
- [Get Endpoint](./endpoints/get-endpoint.md) - Get endpoint details
- [Create Endpoint](./endpoints/create-endpoint.md) - Create new endpoint
- [Update Endpoint](./endpoints/update-endpoint.md) - Update endpoint
- [Delete Endpoint](./endpoints/delete-endpoint.md) - Delete endpoint
- [Update Endpoint Status](./endpoints/update-endpoint-status.md) - Enable/disable endpoint
- [Update Endpoint WSA](./endpoints/update-endpoint-wsa.md) - Update SOAP WSA settings
- [Update Endpoint Cache](./endpoints/update-endpoint-cache.md) - Update endpoint cache settings

### Settings
- [CORS Settings](./settings/cors-settings.md) - Configure CORS
- [Cache Settings](./settings/cache-settings.md) - Configure caching
- [Routing Settings](./settings/routing-settings.md) - Configure routing
- [Connection Settings](./settings/connection-settings.md) - Configure connection settings
- [Circuit Breaker](./settings/circuit-breaker.md) - Configure circuit breaker
- [mTLS Settings](./settings/mtls-settings.md) - Configure mTLS
- [NTLM Settings](./settings/ntlm-settings.md) - Configure NTLM
- [Proxy Server Settings](./settings/proxy-server-settings.md) - Configure proxy server
- [Traffic Log Settings](./settings/traffic-log-settings.md) - Configure traffic logging
- [Error Response Templates](./settings/error-response-templates.md) - Configure error templates
- [Forwarded IP Header](./settings/forwarded-ip-header.md) - Configure forwarded IP header
- [Hide API Definition](./settings/hide-api-definition.md) - Hide API definition file
- [Client Route](./settings/client-route.md) - Configure client route metadata
- [Keys Settings](./settings/keys-settings.md) - Configure API keys
- [Metadata](./settings/metadata.md) - Update metadata (name, description, category, sharing)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all API proxy operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats
- [Policies API](../05-policies/) - Policy management
- [Connections API](../06-connections/) - Connection management
