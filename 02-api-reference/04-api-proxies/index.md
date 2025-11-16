---
layout: default
permalink: /02-api-reference/04-api-proxies/
---

# API Proxies API

## Overview

The API Proxies API provides endpoints for managing API proxies in Apinizer. API proxies act as intermediaries between clients and backend services, providing API management capabilities such as security, transformation, and monitoring.

## Endpoints

### CRUD Operations
- [List API Proxies](crud/list-api-proxies/) - Get all API proxies for a project
- [Get API Proxy](crud/get-api-proxy/) - Get API proxy details
- [Create API Proxy from URL](crud/create-api-proxy-from-url/) - Create API proxy from OpenAPI/Swagger/WSDL URL
- [Create API Proxy from File](crud/create-api-proxy-from-file/) - Create API proxy from uploaded file
- [Update API Proxy](crud/update-api-proxy/) - Update API proxy
- [Delete API Proxy](crud/delete-api-proxy/) - Delete API proxy

### Deployment
- [Deploy API Proxy](deployment/deploy/) - Deploy API proxy to environments
- [Undeploy API Proxy](deployment/undeploy/) - Undeploy API proxy from environments

### Endpoints Management
- [List Endpoints](endpoints/list-endpoints/) - List all endpoints
- [Get Endpoint](endpoints/get-endpoint/) - Get endpoint details
- [Create Endpoint](endpoints/create-endpoint/) - Create new endpoint
- [Update Endpoint](endpoints/update-endpoint/) - Update endpoint
- [Delete Endpoint](endpoints/delete-endpoint/) - Delete endpoint
- [Update Endpoint Status](endpoints/update-endpoint-status/) - Enable/disable endpoint
- [Update Endpoint WSA](endpoints/update-endpoint-wsa/) - Update SOAP WSA settings
- [Update Endpoint Cache](endpoints/update-endpoint-cache/) - Update endpoint cache settings

### Settings
- [CORS Settings](settings/update-cors-settings/) - Configure CORS
- [Cache Settings](settings/update-cache-settings/) - Configure caching
- [Routing Addresses](settings/update-routing-addresses/) - Configure routing addresses
- [Routing Status](settings/update-routing-status/) - Configure routing status
- [Connection Settings](settings/update-connection-settings/) - Configure connection settings
- [Circuit Breaker Settings](settings/update-circuit-breaker-settings/) - Configure circuit breaker
- [mTLS Settings](settings/update-mtls-settings/) - Configure mTLS
- [NTLM Settings](settings/update-ntlm-settings/) - Configure NTLM
- [Proxy Server Settings](settings/update-proxy-server-settings/) - Configure proxy server
- [Traffic Log Settings](settings/update-traffic-log-settings/) - Configure traffic logging
- [JSON Error Template](settings/update-json-error-template/) - Configure JSON error template
- [XML Error Template](settings/update-xml-error-template/) - Configure XML error template
- [Forwarded IP Header](settings/update-forwarded-ip-header/) - Configure forwarded IP header
- [Hide API Definition](settings/update-hide-spec-file/) - Hide API definition file
- [Client Route](settings/update-client-route/) - Configure client route metadata
- [API Keys](settings/update-api-keys/) - Configure API keys
- [Metadata](settings/update-metadata/) - Update metadata (name, description, category, sharing)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all API proxy operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](../01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](../01-getting-started/error-handling/) - Error response formats
- [Policies API](05-policies/) - Policy management
- [Connections API](06-connections/) - Connection management
