---
layout: default
permalink: /02-api-reference/05-policies/
---

# Policies API

## Overview

The Policies API provides endpoints for managing policies in API proxies. Policies are rules that can be applied to requests, responses, or errors to control behavior, security, transformation, and more.

## Endpoints

- [List Policies](./crud/list-policies) - Get all policies for an API proxy
- [Add Policy](./crud/add-policy) - Add a new policy to an API proxy
- [Update Policy](./crud/update-policy) - Update an existing policy
- [Delete Policy](./crud/delete-policy) - Delete a policy from an API proxy

## Policy Types

Policies are organized by type. Each policy type has its own documentation page with complete examples:

### Authentication Policies
- [Basic Authentication](./policies/policy-auth-basic)
- [Clear Text Authentication](./policies/policy-auth-clear-text)
- [Digest Authentication](./policies/policy-auth-digest)
- [JWT Authentication](./policies/policy-auth-jwt)
- [OAuth2 Authentication](./policies/policy-auth-oauth2)
- [OIDC Authentication](./policies/policy-oidc)
- [mTLS Authentication](./policies/policy-auth-mtls)
- [API Authentication](./policies/policy-api-authentication)
- [SAML Validation](./policies/policy-saml-validation)

### Security Policies
- [WS-Security Encrypt](./policies/policy-ws-security-encrypt)
- [WS-Security Decrypt](./policies/policy-ws-security-decrypt)
- [WS-Security Sign](./policies/policy-ws-security-sign)
- [WS-Security Sign Validation](./policies/policy-ws-security-sign-validation)
- [WS-Security Username Token](./policies/policy-ws-security-username)
- [WS-Security Timestamp](./policies/policy-ws-security-timestamp)
- [WS-Security From Target](./policies/policy-ws-security-from-target)
- [WS-Security To Target](./policies/policy-ws-security-to-target)
- [JOSE Validation](./policies/policy-jose-validation)
- [JOSE Implementation](./policies/policy-jose-implementation)
- [Digital Sign](./policies/policy-digital-sign)
- [Digital Sign Verification](./policies/policy-digital-sign-verification)
- [Encryption](./policies/policy-encryption)
- [Decryption](./policies/policy-decryption)

### Rate Limiting & Quota Policies
- [API Based Throttling](./policies/policy-api-based-throttling)
- [API Based Quota](./policies/policy-api-based-quota)
- [Client Ban](./policies/policy-client-ban)

### IP Filtering Policies
- [Blocked IP List](./policies/policy-black-ip)
- [Allowed IP List](./policies/policy-white-ip)

### Transformation Policies
- [JSON Transformation](./policies/policy-json-transformation)
- [XML Transformation](./policies/policy-xml-transformation)
- [Request Protocol Transformation](./policies/policy-request-protocol-transformation)
- [Response Protocol Transformation](./policies/policy-response-protocol-transformation)

### Validation Policies
- [JSON Schema Validation](./policies/policy-json-schema-validation)
- [XML Schema Validation](./policies/policy-xml-schema-validation)
- [Max Message Size](./policies/policy-max-message-size)
- [Min Message Size](./policies/policy-min-message-size)

### Content Policies
- [Content Filter](./policies/policy-content-filter)
- [Redaction](./policies/policy-redaction)

### Scripting Policies
- [Script](./policies/policy-script)

### Integration Policies
- [API Call](./policies/policy-api-call)

### Advanced Policies
- [Time Restriction](./policies/policy-time-restriction)
- [Business Rule](./policies/policy-business-rule)
- [Policy Group](./policies/policy-group)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all policy operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling) - Error response formats
