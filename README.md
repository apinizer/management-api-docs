# Apinizer Management API Documentation

Welcome to the Apinizer Management API documentation. This documentation provides comprehensive information about all available endpoints, request/response formats, and usage examples.

The Management API allows you to perform many operations without needing the web interface, enabling integration of Apinizer into your DevOps environment.

## Base URL

The Management API base URL is constructed by appending `/apiops` to your Apinizer Manager application URL.

### Example

- If Manager application runs at `https://demo.apinizer.com`, the API base URL is `https://demo.apinizer.com/apiops/`

For more details, see [Base URL](/01-getting-started/base-url).

## OpenAPI Specification

You can view the OpenAPI specification files online:
- Interactive documentation: `https://{management_console_url}/apiops/openapi`
- YAML specification: `https://{management_console_url}/apiops/openapi.yaml`

For example:
- `https://demo.apinizer.com/apiops/openapi`
- `https://demo.apinizer.com/apiops/openapi.yaml`

See [OpenAPI Spec](/03-appendix/openapi-spec) for more information.

## 📚 Table of Contents

- [Getting Started](/01-getting-started)
  - [Overview](/01-getting-started/overview)
  - [Authentication](/01-getting-started/authentication)
  - [Base URL](/01-getting-started/base-url)
  - [Error Handling](/01-getting-started/error-handling)

- [API Reference](/02-api-reference)
  - [Authentication](/02-api-reference/01-auth)
  - [Projects](/02-api-reference/02-projects)
  - [Environments](/02-api-reference/03-environments)
  - [API Proxies](/02-api-reference/04-api-proxies)
  - [Policies](/02-api-reference/05-policies)
  - [Connections](/02-api-reference/06-connections)
  - [Credentials](/02-api-reference/07-credentials)
  - [Certificates](/02-api-reference/08-certificates)
  - [API Proxy Groups](/02-api-reference/09-api-proxy-groups)
  - [Environment Variables](/02-api-reference/10-environment-variables)
  - [IP Groups](/02-api-reference/11-ip-groups)
  - [RLCL](/02-api-reference/12-rlcl)
  - [GeoLocation](/02-api-reference/13-geolocation)
  - [Reports](/02-api-reference/14-reports)
  - [Test](/02-api-reference/16-test)

- [Appendix](/03-appendix)
  - [Glossary](/03-appendix/glossary)
  - [Variable Definition](/03-appendix/variable-definition)
  - [Enum Reference](/03-appendix/enum-reference)
  - [OpenAPI Spec](/03-appendix/openapi-spec)

## 🚀 Quick Start

1. **Get Your API Token**: See [Authentication](/01-getting-started/authentication) for details on obtaining a Personal API Access Token.

2. **Make Your First Request**: 
   ```bash
   curl -X GET \
     "https://demo.apinizer.com/apiops/projects/" \
     -H "Authorization: Bearer YOUR_TOKEN"
   ```

3. **Explore the APIs**: Start with [Projects](/02-api-reference/02-projects) to list available projects.

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

See [Authentication Guide](/01-getting-started/authentication) for details on obtaining and using API tokens.

## 📄 License

[Add license information here]

## 🔗 Related Resources

- [Apinizer Documentation](https://docs.apinizer.com)
- [Apinizer Management Console](https://demo.apinizer.com)

## 📧 Support

For questions or issues, please contact support@apinizer.com
