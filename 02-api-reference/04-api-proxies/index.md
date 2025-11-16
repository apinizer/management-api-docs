---
layout: default
permalink: /02-api-reference/04-api-proxies/
---

# API Proxies API

## Overview

The API Proxies API provides endpoints for managing API proxies in Apinizer. API proxies act as intermediaries between clients and backend services, providing API management capabilities such as security, transformation, and monitoring.

## Endpoints

### CRUD Operations
- [List API Proxies](crud/list-api-proxies.md) - Get all API proxies for a project
- [Get API Proxy](crud/get-api-proxy.md) - Get API proxy details
- [Create API Proxy from URL](crud/create-api-proxy-from-url.md) - Create API proxy from OpenAPI/Swagger/WSDL URL
- [Create API Proxy from File](crud/create-api-proxy-from-file.md) - Create API proxy from uploaded file
- [Update API Proxy](crud/update-api-proxy.md) - Update API proxy
- [Delete API Proxy](crud/delete-api-proxy.md) - Delete API proxy

### Deployment
- [Deploy API Proxy](deployment/deploy.md) - Deploy API proxy to environments
- [Undeploy API Proxy](deployment/undeploy.md) - Undeploy API proxy from environments

### Endpoints Management
- [List Endpoints](endpoints/list-endpoints.md) - List all endpoints
- [Get Endpoint](endpoints/get-endpoint.md) - Get endpoint details
- [Create Endpoint](endpoints/create-endpoint.md) - Create new endpoint
- [Update Endpoint](endpoints/update-endpoint.md) - Update endpoint
- [Delete Endpoint](endpoints/delete-endpoint.md) - Delete endpoint
- [Update Endpoint Status](endpoints/update-endpoint-status.md) - Enable/disable endpoint
- [Update Endpoint WSA](endpoints/update-endpoint-wsa.md) - Update SOAP WSA settings
- [Update Endpoint Cache](endpoints/update-endpoint-cache.md) - Update endpoint cache settings

### Settings
- [CORS Settings](settings/update-cors-settings.md) - Configure CORS
- [Cache Settings](settings/update-cache-settings.md) - Configure caching
- [Routing Addresses](settings/update-routing-addresses.md) - Configure routing addresses
- [Routing Status](settings/update-routing-status.md) - Configure routing status
- [Connection Settings](settings/update-connection-settings.md) - Configure connection settings
- [Circuit Breaker Settings](settings/update-circuit-breaker-settings.md) - Configure circuit breaker
- [mTLS Settings](settings/update-mtls-settings.md) - Configure mTLS
- [NTLM Settings](settings/update-ntlm-settings.md) - Configure NTLM
- [Proxy Server Settings](settings/update-proxy-server-settings.md) - Configure proxy server
- [Traffic Log Settings](settings/update-traffic-log-settings.md) - Configure traffic logging
- [JSON Error Template](settings/update-json-error-template.md) - Configure JSON error template
- [XML Error Template](settings/update-xml-error-template.md) - Configure XML error template
- [Forwarded IP Header](settings/update-forwarded-ip-header.md) - Configure forwarded IP header
- [Hide API Definition](settings/update-hide-spec-file.md) - Hide API definition file
- [Client Route](settings/update-client-route.md) - Configure client route metadata
- [API Keys](settings/update-api-keys.md) - Configure API keys
- [Metadata](settings/update-metadata.md) - Update metadata (name, description, category, sharing)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all API proxy operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats
- [Policies API](../05-policies) - Policy management
- [Connections API](../06-connections) - Connection management
