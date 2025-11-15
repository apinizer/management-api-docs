# Connections API

## Overview

The Connections API provides endpoints for managing connections to external systems such as databases, message queues, email servers, and logging systems. Connections are reusable configurations that can be used by policies and other components.

## Endpoints

### CRUD Operations
- [List Connections](./crud/list-connections.md) - Get all connections for a project
- [Get Connection](./crud/get-connection.md) - Get connection details
- [Create Connection](./crud/create-connection.md) - Create a new connection (general)
- [Update Connection](./crud/update-connection.md) - Update a connection (general)
- [Delete Connection](./crud/delete-connection.md) - Delete a connection

### Connection Types

Each connection type has its own documentation page with complete examples:

- [Email Connection](./connections/connection-email.md)
- [Kafka Connection](./connections/connection-kafka.md)
- [Elasticsearch Connection](./connections/connection-elasticsearch.md)
- [RabbitMQ Connection](./connections/connection-rabbitmq.md)
- [FTP Connection](./connections/connection-ftp.md)
- [Graylog Connection](./connections/connection-graylog.md)
- [Syslog Connection](./connections/connection-syslog.md)
- [Webhook Connection](./connections/connection-webhook.md)
- [Logback Connection](./connections/connection-logback.md)
- [Apache ActiveMQ Connection](./connections/connection-activemq.md)
- [SNMP Connection](./connections/connection-snmp.md)
- [Linux Script Connection](./connections/connection-linux-script.md)
- [Database Connection](./connections/connection-database.md)
- [LDAP Connection](./connections/connection-ldap.md)

## Authentication

All endpoints require authentication using a Personal API Access Token.

## Permissions

- `ROLE_API_SECURITY` - Required for all connection operations

## Secret Fields

- **List Operations**: Secret fields (passwords, API keys, etc.) are masked and returned as `null`
- **Get Single Connection**: Secret fields are returned in full
- **Security**: Never commit connection configurations with secrets to version control

## Related Documentation

- [Authentication Guide](../../01-getting-started/authentication.md) - How to obtain and use API tokens
- [Error Handling](../../01-getting-started/error-handling.md) - Error response formats

