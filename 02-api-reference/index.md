---
layout: default
permalink: /02-api-reference/
---

# API Reference

This section contains comprehensive documentation for all Management API endpoints organized by functionality.

## Overview

The Management API provides endpoints for managing all aspects of your Apinizer deployment, including projects, API proxies, policies, connections, credentials, certificates, and more.

## API Sections

### Authentication
- [Create Token](01-auth/create-token/) - Generate API access tokens

### Projects
- [List Projects](02-projects/list-projects/) - Get all projects

### Environments
- [List Environments](03-environments/list-environments/) - Get all environments
- [Get Environments by Project](03-environments/get-environments-by-project/) - Get environments for a specific project

### API Proxies
- [API Proxies Overview](04-api-proxies/) - Complete API Proxy management documentation
- Create, update, delete, import, export API proxies
- Manage endpoints, policies, and settings
- Deploy and undeploy API proxies

### Policies
- [Policies Overview](05-policies/) - Complete policy management documentation
- Authentication policies (Basic, JWT, OAuth2, OIDC, etc.)
- Security policies (WS-Security, JOSE, Encryption, etc.)
- Rate limiting and quota policies
- Transformation and validation policies
- Scripting and integration policies

### Connections
- [Connections Overview](06-connections/) - Complete connection management documentation
- Database, ActiveMQ, Kafka, RabbitMQ connections
- Email, FTP, LDAP connections
- Webhook, SNMP, Syslog connections
- And more...

### Credentials
- [Credentials Overview](07-credentials/) - Complete credential management documentation
- Create, update, delete credentials
- Manage credential access and passwords

### Certificates
- [Certificates Overview](08-certificates/) - Complete certificate management documentation
- Create, update, delete certificates
- Export certificates and manage truststore

### API Proxy Groups
- [API Proxy Groups Overview](09-api-proxy-groups/) - Complete API Proxy Group management documentation
- Create, update, delete groups
- Add/remove API proxies to groups
- Deploy and undeploy groups

### Environment Variables
- [Environment Variables Overview](10-environment-variables/) - Complete environment variable management documentation
- Create, update, delete environment variables

### IP Groups
- [IP Groups Overview](11-ip-groups/) - Complete IP group management documentation
- Create, update, delete IP groups
- Manage IP addresses in groups

### RLCL (Rate Limit, Connection Limit)
- [RLCL Overview](12-rlcl/) - Complete RLCL management documentation
- Manage rate limits and connection limits
- Configure conditions, credentials, and endpoints

### GeoLocation
- [GeoLocation Overview](13-geolocation/) - Complete geolocation management documentation
- Enable/disable geolocation
- Upload MMDB files

### Reports
- [Reports Overview](14-reports/) - Complete reporting documentation
- API reports
- Organization API data model access reports

### Test
- [Test Overview](16-test/) - Test endpoints
- Health check
- Secure hello

## Authentication

All endpoints (except test endpoints) require authentication using a Personal API Access Token. Include the token in the `Authorization` header:

```
Authorization: Bearer YOUR_TOKEN
```

See [Authentication Guide](../01-getting-started/authentication/) for details.

## Base URL

The Management API base URL is constructed by appending `/apiops` to your Apinizer Manager application URL.

For example:
- If Manager application runs at `https://demo.apinizer.com`, the API base URL is `https://demo.apinizer.com/apiops/`

See [Base URL](/02-api-reference/01-getting-started/base-url/) for more details.

## Error Handling

All endpoints follow a consistent error response format. See [Error Handling](../01-getting-started/error-handling/) for details.

## Related Documentation

- [Getting Started](../01-getting-started/overview/) - Overview and quick start guide
- [Appendix](../03-appendix/) - Glossary, variable definitions, enum references, and OpenAPI spec

