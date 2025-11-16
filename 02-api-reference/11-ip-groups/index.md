---
layout: default
permalink: /02-api-reference/11-ip-groups/
---

# IP Groups API

## Overview

The IP Groups API provides endpoints for managing IP Groups in Apinizer. IP Groups allow you to group multiple IP addresses or CIDR ranges together for use in policies (e.g., Black IP, White IP policies).

## Endpoints

### CRUD Operations
- [Create IP Group](./crud/create-ip-group.md) - Create a new IP Group
- [Update IP Group](./crud/update-ip-group.md) - Update an existing IP Group
- [Delete IP Group](./crud/delete-ip-group.md) - Delete an IP Group

### IP Management
- [Add IPs to Group](./ips/add-ips-to-group.md) - Add IP addresses to an IP Group
- [Update IPs in Group](./ips/update-ips-in-group.md) - Replace all IPs in an IP Group
- [Delete IPs from Group](./ips/delete-ips-from-group.md) - Remove IP addresses from an IP Group

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all IP Group operations

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats
- [Black IP Policy](../05-policies/policies/policy-black-ip.md) - Use IP Groups in Black IP policy
- [White IP Policy](../05-policies/policies/policy-white-ip.md) - Use IP Groups in White IP policy
