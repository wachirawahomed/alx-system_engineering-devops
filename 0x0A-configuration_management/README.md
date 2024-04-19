# 0x0A-configuration_management
## Puppet Configuration Management

This repository contains Puppet manifests for managing configuration tasks.

## Tasks

### 0. Create a File

Creates a file named "school" in the `/tmp` directory with specific permissions, owner, group, and content.

Manifest file: [0-create_a_file.pp](0x0A-configuration_management/0-create_a_file.pp)

### 1. Install a Package

Installs Flask version 2.1.0 using pip3.

Manifest file: [1-install_a_package.pp](0x0A-configuration_management/1-install_a_package.pp)

### 2. Execute a Command

Executes a command to kill a process named "killmenow" using the `exec` resource.

Manifest file: [2-execute_a_command.pp](0x0A-configuration_management/2-execute_a_command.pp)

## Usage

To apply any of the manifests, run the following command:

```bash
puppet apply <manifest_file_name>
