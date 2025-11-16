---
layout: default
permalink: /02-api-reference/05-policies/
---

# Policies API

## Overview

The Policies API provides endpoints for managing policies in API proxies. Policies are rules that can be applied to requests, responses, or errors to control behavior, security, transformation, and more.

## Endpoints

- [List Policies](/02-api-reference/05-policies/crud/list-policies/) - Get all policies for an API proxy
- [Add Policy](/02-api-reference/05-policies/crud/add-policy/) - Add a new policy to an API proxy
- [Update Policy](/02-api-reference/05-policies/crud/update-policy/) - Update an existing policy
- [Delete Policy](/02-api-reference/05-policies/crud/delete-policy/) - Delete a policy from an API proxy

## Policy Types

Policies are organized by type. Each policy type has its own documentation page with complete examples:

### Authentication Policies
- [Basic Authentication](/02-api-reference/05-policies/policies/policy-auth-basic/)
- [Clear Text Authentication](/02-api-reference/05-policies/policies/policy-auth-clear-text/)
- [Digest Authentication](/02-api-reference/05-policies/policies/policy-auth-digest/)
- [JWT Authentication](/02-api-reference/05-policies/policies/policy-auth-jwt/)
- [OAuth2 Authentication](/02-api-reference/05-policies/policies/policy-auth-oauth2/)
- [OIDC Authentication](/02-api-reference/05-policies/policies/policy-oidc/)
- [mTLS Authentication](/02-api-reference/05-policies/policies/policy-auth-mtls/)
- [API Authentication](/02-api-reference/05-policies/policies/policy-api-authentication/)
- [SAML Validation](/02-api-reference/05-policies/policies/policy-saml-validation/)

### Security Policies
- [WS-Security Encrypt](/02-api-reference/05-policies/policies/policy-ws-security-encrypt/)
- [WS-Security Decrypt](/02-api-reference/05-policies/policies/policy-ws-security-decrypt/)
- [WS-Security Sign](/02-api-reference/05-policies/policies/policy-ws-security-sign/)
- [WS-Security Sign Validation](/02-api-reference/05-policies/policies/policy-ws-security-sign-validation/)
- [WS-Security Username Token](/02-api-reference/05-policies/policies/policy-ws-security-username/)
- [WS-Security Timestamp](/02-api-reference/05-policies/policies/policy-ws-security-timestamp/)
- [WS-Security From Target](/02-api-reference/05-policies/policies/policy-ws-security-from-target/)
- [WS-Security To Target](/02-api-reference/05-policies/policies/policy-ws-security-to-target/)
- [JOSE Validation](/02-api-reference/05-policies/policies/policy-jose-validation/)
- [JOSE Implementation](/02-api-reference/05-policies/policies/policy-jose-implementation/)
- [Digital Sign](/02-api-reference/05-policies/policies/policy-digital-sign/)
- [Digital Sign Verification](/02-api-reference/05-policies/policies/policy-digital-sign-verification/)
- [Encryption](/02-api-reference/05-policies/policies/policy-encryption/)
- [Decryption](/02-api-reference/05-policies/policies/policy-decryption/)

### Rate Limiting & Quota Policies
- [API Based Throttling](/02-api-reference/05-policies/policies/policy-api-based-throttling/)
- [API Based Quota](/02-api-reference/05-policies/policies/policy-api-based-quota/)
- [Client Ban](/02-api-reference/05-policies/policies/policy-client-ban/)

### IP Filtering Policies
- [Blocked IP List](/02-api-reference/05-policies/policies/policy-black-ip/)
- [Allowed IP List](/02-api-reference/05-policies/policies/policy-white-ip/)

### Transformation Policies
- [JSON Transformation](/02-api-reference/05-policies/policies/policy-json-transformation/)
- [XML Transformation](/02-api-reference/05-policies/policies/policy-xml-transformation/)
- [Request Protocol Transformation](/02-api-reference/05-policies/policies/policy-request-protocol-transformation/)
- [Response Protocol Transformation](/02-api-reference/05-policies/policies/policy-response-protocol-transformation/)

### Validation Policies
- [JSON Schema Validation](/02-api-reference/05-policies/policies/policy-json-schema-validation/)
- [XML Schema Validation](/02-api-reference/05-policies/policies/policy-xml-schema-validation/)
- [Max Message Size](/02-api-reference/05-policies/policies/policy-max-message-size/)
- [Min Message Size](/02-api-reference/05-policies/policies/policy-min-message-size/)

### Content Policies
- [Content Filter](/02-api-reference/05-policies/policies/policy-content-filter/)
- [Redaction](/02-api-reference/05-policies/policies/policy-redaction/)

### Scripting Policies
- [Script](/02-api-reference/05-policies/policies/policy-script/)

### Integration Policies
- [API Call](/02-api-reference/05-policies/policies/policy-api-call/)

### Advanced Policies
- [Time Restriction](/02-api-reference/05-policies/policies/policy-time-restriction/)
- [Business Rule](/02-api-reference/05-policies/policies/policy-business-rule/)
- [Policy Group](/02-api-reference/05-policies/policies/policy-group/)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all policy operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](/02-api-reference/05-policies/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/02-api-reference/05-policies/01-getting-started/error-handling/) - Error response formats
