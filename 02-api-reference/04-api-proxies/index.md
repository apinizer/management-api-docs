---
layout: default
permalink: /02-api-reference/04-api-proxies/
---

# API Proxies API

## Overview

The API Proxies API provides endpoints for managing API proxies in Apinizer. API proxies act as intermediaries between clients and backend services, providing API management capabilities such as security, transformation, and monitoring.

## Endpoints

### CRUD Operations
- [List API Proxies](/02-api-reference/04-api-proxies/crud/list-api-proxies) - Get all API proxies for a project
- [Get API Proxy](/02-api-reference/04-api-proxies/crud/get-api-proxy) - Get API proxy details
- [Create API Proxy from URL](/02-api-reference/04-api-proxies/crud/create-api-proxy-from-url) - Create API proxy from OpenAPI/Swagger/WSDL URL
- [Create API Proxy from File](/02-api-reference/04-api-proxies/crud/create-api-proxy-from-file) - Create API proxy from uploaded file
- [Update API Proxy](/02-api-reference/04-api-proxies/crud/update-api-proxy) - Update API proxy
- [Delete API Proxy](/02-api-reference/04-api-proxies/crud/delete-api-proxy) - Delete API proxy

### Deployment
- [Deploy API Proxy](/02-api-reference/04-api-proxies/deployment/deploy) - Deploy API proxy to environments
- [Undeploy API Proxy](/02-api-reference/04-api-proxies/deployment/undeploy) - Undeploy API proxy from environments

### Endpoints Management
- [List Endpoints](/02-api-reference/04-api-proxies/endpoints/list-endpoints) - List all endpoints
- [Get Endpoint](/02-api-reference/04-api-proxies/endpoints/get-endpoint) - Get endpoint details
- [Create Endpoint](/02-api-reference/04-api-proxies/endpoints/create-endpoint) - Create new endpoint
- [Update Endpoint](/02-api-reference/04-api-proxies/endpoints/update-endpoint) - Update endpoint
- [Delete Endpoint](/02-api-reference/04-api-proxies/endpoints/delete-endpoint) - Delete endpoint
- [Update Endpoint Status](/02-api-reference/04-api-proxies/endpoints/update-endpoint-status) - Enable/disable endpoint
- [Update Endpoint WSA](/02-api-reference/04-api-proxies/endpoints/update-endpoint-wsa) - Update SOAP WSA settings
- [Update Endpoint Cache](/02-api-reference/04-api-proxies/endpoints/update-endpoint-cache) - Update endpoint cache settings

### Settings
- [CORS Settings](/02-api-reference/04-api-proxies/settings/update-cors-settings) - Configure CORS
- [Cache Settings](/02-api-reference/04-api-proxies/settings/update-cache-settings) - Configure caching
- [Routing Addresses](/02-api-reference/04-api-proxies/settings/update-routing-addresses) - Configure routing addresses
- [Routing Status](/02-api-reference/04-api-proxies/settings/update-routing-status) - Configure routing status
- [Connection Settings](/02-api-reference/04-api-proxies/settings/update-connection-settings) - Configure connection settings
- [Circuit Breaker Settings](/02-api-reference/04-api-proxies/settings/update-circuit-breaker-settings) - Configure circuit breaker
- [mTLS Settings](/02-api-reference/04-api-proxies/settings/update-mtls-settings) - Configure mTLS
- [NTLM Settings](/02-api-reference/04-api-proxies/settings/update-ntlm-settings) - Configure NTLM
- [Proxy Server Settings](/02-api-reference/04-api-proxies/settings/update-proxy-server-settings) - Configure proxy server
- [Traffic Log Settings](/02-api-reference/04-api-proxies/settings/update-traffic-log-settings) - Configure traffic logging
- [JSON Error Template](/02-api-reference/04-api-proxies/settings/update-json-error-template) - Configure JSON error template
- [XML Error Template](/02-api-reference/04-api-proxies/settings/update-xml-error-template) - Configure XML error template
- [Forwarded IP Header](/02-api-reference/04-api-proxies/settings/update-forwarded-ip-header) - Configure forwarded IP header
- [Hide API Definition](/02-api-reference/04-api-proxies/settings/update-hide-spec-file) - Hide API definition file
- [Client Route](/02-api-reference/04-api-proxies/settings/update-client-route) - Configure client route metadata
- [API Keys](/02-api-reference/04-api-proxies/settings/update-api-keys) - Configure API keys
- [Metadata](/02-api-reference/04-api-proxies/settings/update-metadata) - Update metadata (name, description, category, sharing)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all API proxy operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](/01-getting-started/authentication) - How to obtain and use API tokens
- [Error Handling](/01-getting-started/error-handling) - Error response formats
- [Policies API](/02-api-reference/05-policies) - Policy management
- [Connections API](/02-api-reference/06-connections) - Connection management
