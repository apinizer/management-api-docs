---
layout: default
permalink: /02-api-reference/06-connections/
---

# Connections API

## Overview

The Connections API provides endpoints for managing connections to external systems such as databases, message queues, email servers, and logging systems. Connections are reusable configurations that can be used by policies and other components.

## Endpoints

### CRUD Operations
- [List Connections](./crud/list-connections) - Get all connections for a project
- [Get Connection](./crud/get-connection) - Get connection details
- [Create Connection](./crud/create-connection) - Create a new connection (general)
- [Update Connection](./crud/update-connection) - Update a connection (general)
- [Delete Connection](./crud/delete-connection) - Delete a connection

### Connection Types

Each connection type has its own documentation page with complete examples:

- [Email Connection](./connections/connection-email)
- [Kafka Connection](./connections/connection-kafka)
- [Elasticsearch Connection](./connections/connection-elasticsearch)
- [RabbitMQ Connection](./connections/connection-rabbitmq)
- [FTP Connection](./connections/connection-ftp)
- [Graylog Connection](./connections/connection-graylog)
- [Syslog Connection](./connections/connection-syslog)
- [Webhook Connection](./connections/connection-webhook)
- [Logback Connection](./connections/connection-logback)
- [Apache ActiveMQ Connection](./connections/connection-activemq)
- [SNMP Connection](./connections/connection-snmp)
- [Linux Script Connection](./connections/connection-linux-script)
- [Database Connection](./connections/connection-database)
- [LDAP Connection](./connections/connection-ldap)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_API_SECURITY` - Required for all connection operations

## Secret Fields

- **List Operations**: Secret fields (passwords, API keys, etc.) are masked and returned as `null`
- **Get Single Connection**: Secret fields are returned in full
- **Security**: Never commit connection configurations with secrets to version control

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling) - Error response formats
