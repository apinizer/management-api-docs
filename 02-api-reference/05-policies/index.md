# Policies API

## Overview

The Policies API provides endpoints for managing policies in API proxies. Policies are rules that can be applied to requests, responses, or errors to control behavior, security, transformation, and more.

## Endpoints

- [List Policies](./crud/list-policies.md) - Get all policies for an API proxy
- [Add Policy](./crud/add-policy.md) - Add a new policy to an API proxy
- [Update Policy](./crud/update-policy.md) - Update an existing policy
- [Delete Policy](./crud/delete-policy.md) - Delete a policy from an API proxy

## Policy Types

Policies are organized by type. Each policy type has its own documentation page with complete examples:

### Authentication Policies
- [Basic Authentication](./policies/policy-auth-basic.md)
- [Clear Text Authentication](./policies/policy-auth-clear-text.md)
- [Digest Authentication](./policies/policy-auth-digest.md)
- [JWT Authentication](./policies/policy-auth-jwt.md)
- [OAuth2 Authentication](./policies/policy-auth-oauth2.md)
- [OIDC Authentication](./policies/policy-auth-oidc.md)
- [mTLS Authentication](./policies/policy-auth-mtls.md)
- [API Authentication](./policies/policy-api-authentication.md)
- [SAML Validation](./policies/policy-saml-validation.md)

### Security Policies
- [WS-Security Encrypt](./policies/policy-ws-security-encrypt.md)
- [WS-Security Decrypt](./policies/policy-ws-security-decrypt.md)
- [WS-Security Sign](./policies/policy-ws-security-sign.md)
- [WS-Security Sign Validation](./policies/policy-ws-security-sign-validation.md)
- [WS-Security Username Token](./policies/policy-ws-security-username.md)
- [WS-Security Timestamp](./policies/policy-ws-security-timestamp.md)
- [WS-Security From Target](./policies/policy-ws-security-from-target.md)
- [WS-Security To Target](./policies/policy-ws-security-to-target.md)
- [JOSE Validation](./policies/policy-jose-validation.md)
- [JOSE Implementation](./policies/policy-jose-implementation.md)
- [Digital Sign](./policies/policy-digital-sign.md)
- [Digital Sign Verification](./policies/policy-digital-sign-verification.md)
- [Encryption](./policies/policy-encryption.md)
- [Decryption](./policies/policy-decryption.md)

### Rate Limiting & Quota Policies
- [API Based Throttling](./policies/policy-api-based-throttling.md)
- [API Based Quota](./policies/policy-api-based-quota.md)
- [Endpoint Rate Limit](./policies/policy-endpoint-rate-limit.md)
- [Client Banner](./policies/policy-client-banner.md)

### IP Filtering Policies
- [Black IP](./policies/policy-black-ip.md)
- [White IP](./policies/policy-white-ip.md)

### Transformation Policies
- [JSON Transformation](./policies/policy-json-transformation.md)
- [XML Transformation](./policies/policy-xml-transformation.md)
- [Request Protocol Transformation](./policies/policy-request-protocol-transformation.md)
- [Response Protocol Transformation](./policies/policy-response-protocol-transformation.md)

### Validation Policies
- [JSON Schema Validation](./policies/policy-json-schema-validation.md)
- [XML Schema Validation](./policies/policy-xml-schema-validation.md)
- [Max Message Size](./policies/policy-max-message-size.md)
- [Min Message Size](./policies/policy-min-message-size.md)

### Content Policies
- [Content Filter](./policies/policy-content-filter.md)
- [Redaction](./policies/policy-redaction.md)

### Scripting Policies
- [Script](./policies/policy-script.md)

### Integration Policies
- [API Call](./policies/policy-api-call.md)

### Advanced Policies
- [Time Restriction](./policies/policy-time-restriction.md)
- [Business Rule](./policies/policy-business-rule.md)
- [Policy Group](./policies/policy-group.md)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all policy operations
- `ROLE_DEPLOY_UNDEPLOY_PROXIES` - Required for deployment operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats

