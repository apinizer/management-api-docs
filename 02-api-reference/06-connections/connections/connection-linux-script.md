# Linux Script Connection

## General Information

### Connection Type
```
linuxscript
```

### UI Documentation
> 📖 **For detailed information:** [UI Documentation Link - Link will be added here]

### Description
Linux Script connection for executing scripts on remote Linux servers via SSH. Used by policies and connectors to run shell scripts, commands, or other operations on remote Linux systems. Provides secure SSH-based access to remote servers for script execution.

### Endpoints

#### List Connections
```
GET /apiops/projects/{projectName}/connections/
```

#### Get Connection
```
GET /apiops/projects/{projectName}/connections/{connectionName}/
```

#### Create Connection
```
POST /apiops/projects/{projectName}/connections/{connectionName}/
```

#### Update Connection
```
PUT /apiops/projects/{projectName}/connections/{connectionName}/
```

#### Delete Connection
```
DELETE /apiops/projects/{projectName}/connections/{connectionName}/
```

---

## List Connections

### Endpoint
```
GET /apiops/projects/{projectName}/connections/
```

### Request

#### Headers
| Header | Value |
|--------|-------|
| Authorization | Bearer {token} |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "resultList": [
    {
      "_class": "linuxscript",
      "id": "connection-id",
      "projectId": "project-id",
      "name": "my-linux-script-connection",
      "description": "Linux script connection via SSH",
      "deployToWorker": true,
      "enabled": true,
      "hostName": "linux.example.com",
      "sshPort": 22,
      "username": "apinizer",
      "password": null
    }
  ],
  "resultCount": 1
}
```

**Note:** In list operations, `password` is returned as `null` for security.

### cURL Example
```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/projects/MyProject/connections/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Get Connection

### Endpoint
```
GET /apiops/projects/{projectName}/connections/{connectionName}/
```

### Request

#### Headers
| Header | Value |
|--------|-------|
| Authorization | Bearer {token} |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| connectionName | string | Yes | Connection name |

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "resultList": [
    {
      "_class": "linuxscript",
      "id": "connection-id",
      "projectId": "project-id",
      "name": "my-linux-script-connection",
      "description": "Linux script connection via SSH",
      "deployToWorker": true,
      "enabled": true,
      "hostName": "linux.example.com",
      "sshPort": 22,
      "username": "apinizer",
      "password": null
    }
  ],
  "resultCount": 1
}
```

**Note:** Password is masked in get operations.

### cURL Example
```bash
curl -X GET \
  "https://demo.apinizer.com/apiops/projects/MyProject/connections/my-linux-script-connection/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Create Connection

### Endpoint
```
POST /apiops/projects/{projectName}/connections/{connectionName}/
```

### Request

#### Headers
| Header | Value |
|--------|-------|
| Authorization | Bearer {token} |
| Content-Type | application/json |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| connectionName | string | Yes | Connection name |

#### Request Body

##### Full JSON Body Example - Basic SSH Connection
```json
{
  "_class": "linuxscript",
  "name": "my-linux-script-connection",
  "description": "Linux script connection via SSH",
  "deployToWorker": true,
  "enabled": true,
  "hostName": "linux.example.com",
  "sshPort": 22,
  "username": "apinizer",
  "password": "password123"
}
```

##### Full JSON Body Example - Custom SSH Port
```json
{
  "_class": "linuxscript",
  "name": "my-linux-script-custom-port",
  "description": "Linux script connection with custom SSH port",
  "deployToWorker": true,
  "enabled": true,
  "hostName": "linux.example.com",
  "sshPort": 2222,
  "username": "apinizer",
  "password": "password123"
}
```

##### Request Body Fields

###### Common Fields
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| _class | string | Yes | - | Connection type: `linuxscript` |
| name | string | Yes | - | Connection name (must match path parameter) |
| description | string | No | - | Connection description |
| deployToWorker | boolean | No | true | Whether to deploy to worker |
| enabled | boolean | No | true | Whether connection is enabled |

###### Linux Script-Specific Fields
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| hostName | string | Yes | - | Linux server hostname or IP address |
| sshPort | integer | No | 22 | SSH port number (default: 22) |
| username | string | Yes | - | SSH username |
| password | string | Yes | - | SSH password (secret field) |

**Notes:**
- `hostName`, `username`, and `password` are required.
- `sshPort` defaults to 22 (standard SSH port).
- Connection uses SSH protocol for secure remote script execution.
- Password is stored securely and masked in responses.

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "deploymentResult": {
    "success": true,
    "deploymentResults": [
      {
        "environmentName": "production",
        "success": true,
        "message": "Deployment successful"
      }
    ]
  }
}
```

### cURL Example
```bash
curl -X POST \
  "https://demo.apinizer.com/apiops/projects/MyProject/connections/my-linux-script-connection/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "_class": "linuxscript",
    "name": "my-linux-script-connection",
    "description": "Linux script connection via SSH",
    "deployToWorker": true,
    "enabled": true,
    "hostName": "linux.example.com",
    "sshPort": 22,
    "username": "apinizer",
    "password": "password123"
  }'
```

---

## Update Connection

### Endpoint
```
PUT /apiops/projects/{projectName}/connections/{connectionName}/
```

### Request

#### Headers
| Header | Value |
|--------|-------|
| Authorization | Bearer {token} |
| Content-Type | application/json |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| connectionName | string | Yes | Connection name (must match name in body) |

#### Request Body

**Note:** The `id` field is required for update operations. Request body structure is the same as Create Connection. All fields should be provided for update.

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "deploymentResult": {
    "success": true,
    "deploymentResults": [...]
  }
}
```

---

## Delete Connection

### Endpoint
```
DELETE /apiops/projects/{projectName}/connections/{connectionName}/
```

### Request

#### Headers
| Header | Value |
|--------|-------|
| Authorization | Bearer {token} |

#### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| projectName | string | Yes | Project name |
| connectionName | string | Yes | Connection name |

### Response

#### Success Response (200 OK)
```json
{
  "success": true,
  "deploymentResult": {
    "success": true,
    "deploymentResults": [...]
  }
}
```

---

## Usage Scenarios

### Scenario 1: Standard SSH Connection

Basic SSH connection with default port.

**Request Body:**
```json
{
  "_class": "linuxscript",
  "name": "standard-ssh",
  "description": "Standard SSH connection",
  "deployToWorker": true,
  "enabled": true,
  "hostName": "linux.example.com",
  "sshPort": 22,
  "username": "apinizer",
  "password": "password123"
}
```

### Scenario 2: Custom SSH Port

SSH connection with non-standard port.

**Request Body:**
```json
{
  "_class": "linuxscript",
  "name": "custom-port-ssh",
  "description": "SSH connection with custom port",
  "deployToWorker": true,
  "enabled": true,
  "hostName": "linux.example.com",
  "sshPort": 2222,
  "username": "apinizer",
  "password": "password123"
}
```

---

## Notes and Warnings

- **SSH Protocol**: 
  - Connection uses SSH (Secure Shell) protocol for secure remote access
  - Standard SSH port is 22
  - Supports password-based authentication
- **Hostname**: 
  - `hostName` can be a hostname or IP address
  - Ensure hostname resolves correctly or use IP address
- **Port**: 
  - `sshPort` defaults to 22 (standard SSH port)
  - Use custom port if SSH server is configured on non-standard port
- **Authentication**: 
  - `username` and `password` are required
  - Password is stored securely and masked in responses
  - Consider using SSH key-based authentication (if supported)
- **Security**: 
  - Use strong passwords
  - Ensure SSH server is properly secured
  - Consider using non-standard ports for additional security
  - Use firewall rules to restrict SSH access
- **Script Execution**: 
  - Scripts are executed on the remote Linux server
  - Ensure user has necessary permissions to execute scripts
  - Scripts run with the privileges of the specified user
- **Network**: 
  - Ensure network connectivity between Apinizer worker and Linux server
  - Firewall rules must allow SSH connections
  - Consider VPN or private network for production
- **Performance**: 
  - SSH connections have overhead
  - Script execution time depends on script complexity and server performance
  - Consider timeout settings for long-running scripts
- **Deployment**: Connection changes require deployment to take effect. Set `deployToWorker: true` or deploy manually.

## Related Documentation

- [List Connections](../crud/list-connections.md) - List all connections
- [Get Connection](../crud/get-connection.md) - Get a specific connection
- [Create Connection](../crud/create-connection.md) - General connection creation guide
- [Update Connection](../crud/update-connection.md) - General connection update guide
- [Delete Connection](../crud/delete-connection.md) - General connection deletion guide

