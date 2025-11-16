---
layout: default
permalink: /
---

# Apinizer Management API Documentation

Welcome to the Apinizer Management API documentation. This documentation provides comprehensive information about all available endpoints, request/response formats, and usage examples.

The Management API allows you to perform many operations without needing the web interface, enabling integration of Apinizer into your DevOps environment.

## Base URL

The Management API base URL is constructed by appending `/apiops` to your Apinizer Manager application URL.

### Example

- If Manager application runs at `https://demo.apinizer.com`, the API base URL is `https://demo.apinizer.com/apiops/`

For more details, see [Base URL](../01-getting-started/base-url.md).

## OpenAPI Specification

You can view the OpenAPI specification files online:
- Interactive documentation: `https://{management_console_url}/apiops/openapi`
- YAML specification: `https://{management_console_url}/apiops/openapi.yaml`

For example:
- `https://demo.apinizer.com/apiops/openapi`
- `https://demo.apinizer.com/apiops/openapi.yaml`

See [OpenAPI Spec](../03-appendix/openapi-spec.md) for more information.

## 📚 Table of Contents

- [Getting Started](../01-getting-started.md)
  - [Overview](../01-getting-started/overview.md)
  - [Authentication](../01-getting-started/authentication.md)
  - [Base URL](../01-getting-started/base-url.md)
  - [Error Handling](../01-getting-started/error-handling.md)

- [API Reference](../02-api-reference.md)
  - [Authentication](../02-api-reference/01-auth.md)
  - [Projects](../02-api-reference/02-projects.md)
  - [Environments](../02-api-reference/03-environments.md)
  - [API Proxies](../02-api-reference/04-api-proxies.md)
  - [Policies](../02-api-reference/05-policies.md)
  - [Connections](../02-api-reference/06-connections.md)
  - [Credentials](../02-api-reference/07-credentials.md)
  - [Certificates](../02-api-reference/08-certificates.md)
  - [API Proxy Groups](../02-api-reference/09-api-proxy-groups.md)
  - [Environment Variables](../02-api-reference/10-environment-variables.md)
  - [IP Groups](../02-api-reference/11-ip-groups.md)
  - [RLCL](../02-api-reference/12-rlcl.md)
  - [GeoLocation](../02-api-reference/13-geolocation.md)
  - [Reports](../02-api-reference/14-reports.md)
  - [Test](../02-api-reference/16-test.md)

- [Appendix](../03-appendix.md)
  - [Glossary](../03-appendix/glossary.md)
  - [Variable Definition](../03-appendix/variable-definition.md)
  - [Enum Reference](../03-appendix/enum-reference.md)
  - [OpenAPI Spec](../03-appendix/openapi-spec.md)

## 🚀 Quick Start

1. **Get Your API Token**: See [Authentication](../01-getting-started/authentication.md) for details on obtaining a Personal API Access Token.

2. **Make Your First Request**: 
   ```bash
   curl -X GET \
     "https://demo.apinizer.com/apiops/projects/" \
     -H "Authorization: Bearer YOUR_TOKEN"
   ```

3. **Explore the APIs**: Start with [Projects](../02-api-reference/02-projects.md) to list available projects.

## 📖 Documentation Structure

Each API endpoint documentation includes:
- **Endpoint URL** and HTTP method
- **Authentication** requirements
- **Request** parameters, headers, and body structure
- **Response** formats (success and error)
- **Full JSON examples** for all operations
- **cURL examples** for quick testing

## 🔑 Authentication

All endpoints (except the test endpoint) require authentication using a **Personal API Access Token**. Include the token in the `Authorization` header:

```
Authorization: Bearer YOUR_TOKEN
```

**Note:** Each endpoint may require different permissions based on the operation it performs.

See [Authentication Guide](../01-getting-started/authentication.md) for details on obtaining and using API tokens.

## 📄 License

[Add license information here]

## 🔗 Related Resources

- [Apinizer Documentation](https://docs.apinizer.com)
- [Apinizer Management Console](https://demo.apinizer.com)

## 📧 Support

For questions or issues, please contact support@apinizer.com

