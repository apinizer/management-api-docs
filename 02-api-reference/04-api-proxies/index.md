---
layout: default
permalink: /02-api-reference/04-api-proxies/
---

# API Proxies API

## Overview

The API Proxies API provides endpoints for managing API proxies in Apinizer. API proxies act as intermediaries between clients and backend services, providing API management capabilities such as security, transformation, and monitoring.

## Endpoints

### CRUD Operations
- [List API Proxies](/management-api-docs/02-api-reference/04-api-proxies/crud/list-api-proxies/) - Get all API proxies for a project
- [Get API Proxy](/management-api-docs/02-api-reference/04-api-proxies/crud/get-api-proxy/) - Get API proxy details
- [Create API Proxy from URL](/management-api-docs/02-api-reference/04-api-proxies/crud/create-api-proxy-from-url/) - Create API proxy from OpenAPI/Swagger/WSDL URL
- [Create API Proxy from File](/management-api-docs/02-api-reference/04-api-proxies/crud/create-api-proxy-from-file/) - Create API proxy from uploaded file
- [Update API Proxy](/management-api-docs/02-api-reference/04-api-proxies/crud/update-api-proxy/) - Update API proxy
- [Delete API Proxy](/management-api-docs/02-api-reference/04-api-proxies/crud/delete-api-proxy/) - Delete API proxy

### Deployment
- [Deploy API Proxy](/management-api-docs/02-api-reference/04-api-proxies/deployment/deploy/) - Deploy API proxy to environments
- [Undeploy API Proxy](/management-api-docs/02-api-reference/04-api-proxies/deployment/undeploy/) - Undeploy API proxy from environments

### Endpoints Management
- [List Endpoints](/management-api-docs/02-api-reference/04-api-proxies/endpoints/list-endpoints/) - List all endpoints
- [Get Endpoint](/management-api-docs/02-api-reference/04-api-proxies/endpoints/get-endpoint/) - Get endpoint details
- [Create Endpoint](/management-api-docs/02-api-reference/04-api-proxies/endpoints/create-endpoint/) - Create new endpoint
- [Update Endpoint](/management-api-docs/02-api-reference/04-api-proxies/endpoints/update-endpoint/) - Update endpoint
- [Delete Endpoint](/management-api-docs/02-api-reference/04-api-proxies/endpoints/delete-endpoint/) - Delete endpoint
- [Update Endpoint Status](/management-api-docs/02-api-reference/04-api-proxies/endpoints/update-endpoint-status/) - Enable/disable endpoint
- [Update Endpoint WSA](/management-api-docs/02-api-reference/04-api-proxies/endpoints/update-endpoint-wsa/) - Update SOAP WSA settings
- [Update Endpoint Cache](/management-api-docs/02-api-reference/04-api-proxies/endpoints/update-endpoint-cache/) - Update endpoint cache settings

### Settings
- [CORS Settings](/management-api-docs/02-api-reference/04-api-proxies/settings/update-cors-settings/) - Configure CORS
- [Cache Settings](/management-api-docs/02-api-reference/04-api-proxies/settings/update-cache-settings/) - Configure caching
- [Routing Addresses](/management-api-docs/02-api-reference/04-api-proxies/settings/update-routing-addresses/) - Configure routing addresses
- [Routing Status](/management-api-docs/02-api-reference/04-api-proxies/settings/update-routing-status/) - Configure routing status
- [Connection Settings](/management-api-docs/02-api-reference/04-api-proxies/settings/update-connection-settings/) - Configure connection settings
- [Circuit Breaker Settings](/management-api-docs/02-api-reference/04-api-proxies/settings/update-circuit-breaker-settings/) - Configure circuit breaker
- [mTLS Settings](/management-api-docs/02-api-reference/04-api-proxies/settings/update-mtls-settings/) - Configure mTLS
- [NTLM Settings](/management-api-docs/02-api-reference/04-api-proxies/settings/update-ntlm-settings/) - Configure NTLM
- [Proxy Server Settings](/management-api-docs/02-api-reference/04-api-proxies/settings/update-proxy-server-settings/) - Configure proxy server
- [Traffic Log Settings](/management-api-docs/02-api-reference/04-api-proxies/settings/update-traffic-log-settings/) - Configure traffic logging
- [JSON Error Template](/management-api-docs/02-api-reference/04-api-proxies/settings/update-json-error-template/) - Configure JSON error template
- [XML Error Template](/management-api-docs/02-api-reference/04-api-proxies/settings/update-xml-error-template/) - Configure XML error template
- [Forwarded IP Header](/management-api-docs/02-api-reference/04-api-proxies/settings/update-forwarded-ip-header/) - Configure forwarded IP header
- [Hide API Definition](/management-api-docs/02-api-reference/04-api-proxies/settings/update-hide-spec-file/) - Hide API definition file
- [Client Route](/management-api-docs/02-api-reference/04-api-proxies/settings/update-client-route/) - Configure client route metadata
- [API Keys](/management-api-docs/02-api-reference/04-api-proxies/settings/update-api-keys/) - Configure API keys
- [Metadata](/management-api-docs/02-api-reference/04-api-proxies/settings/update-metadata/) - Update metadata (name, description, category, sharing)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all API proxy operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](/management-api-docs/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/management-api-docs/01-getting-started/error-handling/) - Error response formats
- [Policies API](/management-api-docs/05-policies/) - Policy management
- [Connections API](/management-api-docs/06-connections/) - Connection management
