---
layout: default
permalink: /02-api-reference/14-reports/
---

# Reports API

## Overview

The Reports API provides endpoints for generating various reports about API Proxies, API Proxy Groups, and access control. These reports are useful for auditing, compliance, and understanding API usage patterns.

## Endpoints

- [API Report](/02-api-reference/14-reports/02-api-reference/14-reports/api-report/) - Get report of all API Proxies and API Proxy Groups
- [Organization API Data Model Access Report](/02-api-reference/14-reports/02-api-reference/14-reports/organization-api-data-model-access-report/) - Get organization-level API and data model access report

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- **Admin/Analyzer Only** - All endpoints require sysAdmin or sysAnalyzer privileges

## Related Documentation

- [Authentication Guide](/02-api-reference/14-reports/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/02-api-reference/14-reports/01-getting-started/error-handling/) - Error response formats
