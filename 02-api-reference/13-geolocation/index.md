---
layout: default
permalink: /02-api-reference/13-geolocation/
---

# Geolocation API

## Overview

The Geolocation API provides endpoints for managing Geolocation settings in Apinizer. Geolocation allows you to determine the geographic location of API clients based on their IP addresses using MaxMind GeoIP2 database (MMDB) files.

## Endpoints

- [Upload MMDB File](upload-mmdb-file.md) - Upload MaxMind GeoIP2 database file
- [Enable Geolocation](enable-geolocation.md) - Enable geolocation functionality
- [Disable Geolocation](disable-geolocation.md) - Disable geolocation functionality

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- **Admin Only** - All endpoints require admin privileges (sysAdmin user)

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats
