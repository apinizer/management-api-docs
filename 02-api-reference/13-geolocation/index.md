---
layout: default
permalink: /02-api-reference/13-geolocation/
---

# Geolocation API

## Overview

The Geolocation API provides endpoints for managing Geolocation settings in Apinizer. Geolocation allows you to determine the geographic location of API clients based on their IP addresses using MaxMind GeoIP2 database (MMDB) files.

## Endpoints

- [Upload MMDB File](/02-api-reference/13-geolocation/upload-mmdb-file/) - Upload MaxMind GeoIP2 database file
- [Enable Geolocation](/02-api-reference/13-geolocation/enable-geolocation/) - Enable geolocation functionality
- [Disable Geolocation](/02-api-reference/13-geolocation/disable-geolocation/) - Disable geolocation functionality

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- **Admin Only** - All endpoints require admin privileges (sysAdmin user)

## Related Documentation

- [Authentication Guide](/01-getting-started/authentication/) - How to obtain and use API tokens
- [Error Handling](/01-getting-started/error-handling/) - Error response formats
