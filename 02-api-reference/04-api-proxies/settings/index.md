---
layout: default
permalink: /02-api-reference/04-api-proxies/settings/
---

# API Proxy Settings

This section contains endpoints for configuring various settings of API proxies.

## Settings Endpoints

### General Settings
- [Metadata](./update-metadata) - Update API proxy metadata (name, description, category, sharing)
- [Client Route](./update-client-route) - Configure client route metadata

### Security Settings
- [CORS Settings](./update-cors-settings) - Configure Cross-Origin Resource Sharing (CORS)
- [mTLS Settings](./update-mtls-settings) - Configure mutual TLS
- [NTLM Settings](./update-ntlm-settings) - Configure NTLM authentication
- [API Keys](./update-api-keys) - Configure API keys

### Routing Settings
- [Routing Addresses](./update-routing-addresses) - Configure backend routing addresses
- [Routing Status](./update-routing-status) - Enable or disable routing
- [Connection Settings](./update-connection-settings) - Configure connection settings
- [Proxy Server Settings](./update-proxy-server-settings) - Configure proxy server settings

### Performance Settings
- [Cache Settings](./update-cache-settings) - Configure caching behavior
- [Circuit Breaker Settings](./update-circuit-breaker-settings) - Configure circuit breaker

### Logging & Monitoring
- [Traffic Log Settings](./update-traffic-log-settings) - Configure traffic logging

### Error Handling
- [JSON Error Template](./update-json-error-template) - Configure JSON error response template
- [XML Error Template](./update-xml-error-template) - Configure XML error response template

### Other Settings
- [Forwarded IP Header](./update-forwarded-ip-header) - Configure forwarded IP header
- [Hide API Definition](./update-hide-spec-file) - Hide API specification file from public access

## Related Documentation

- [API Proxies Overview](../) - Complete API Proxy management documentation
- [CRUD Operations](../crud/) - Create, read, update, and delete API proxies
- [Deployment](../deployment/) - Deploy and undeploy API proxies
- [Endpoints](../endpoints/) - Manage API proxy endpoints

