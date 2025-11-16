---
layout: default
permalink: /02-api-reference/11-ip-groups/
---

# IP Groups API

## Overview

The IP Groups API provides endpoints for managing IP Groups in Apinizer. IP Groups allow you to group multiple IP addresses or CIDR ranges together for use in policies (e.g., Black IP, White IP policies).

## Endpoints

### CRUD Operations
- [Create IP Group](/02-api-reference/11-ip-groups/02-api-reference/11-ip-groups/crud/create-ip-group/) - Create a new IP Group
- [Update IP Group](/02-api-reference/11-ip-groups/02-api-reference/11-ip-groups/crud/update-ip-group/) - Update an existing IP Group
- [Delete IP Group](/02-api-reference/11-ip-groups/02-api-reference/11-ip-groups/crud/delete-ip-group/) - Delete an IP Group

### IP Management
- [Add IPs to Group](/02-api-reference/11-ip-groups/02-api-reference/11-ip-groups/ips/add-ips-to-group/) - Add IP addresses to an IP Group
- [Update IPs in Group](/02-api-reference/11-ip-groups/02-api-reference/11-ip-groups/ips/update-ips-in-group/) - Replace all IPs in an IP Group
- [Delete IPs from Group](/02-api-reference/11-ip-groups/02-api-reference/11-ip-groups/ips/delete-ips-from-group/) - Remove IP addresses from an IP Group

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_MANAGE_PROXIES` - Required for all IP Group operations

## Related Documentation

- [Authentication Guide](/02-api-reference/11-ip-groups/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/02-api-reference/11-ip-groups/01-getting-started/error-handling/) - Error response formats
- [Black IP Policy](/02-api-reference/11-ip-groups/02-api-reference/05-policies/policies/policy-black-ip/) - Use IP Groups in Black IP policy
- [White IP Policy](/02-api-reference/11-ip-groups/02-api-reference/05-policies/policies/policy-white-ip/) - Use IP Groups in White IP policy
