# 0x12. Web stack debugging #2

This repository contains solutions for web stack debugging tasks. Each task addresses a specific issue related to web stack configuration and debugging.

## Tasks

### Task 0: Run software as another user
- **Description**: Write a Bash script that runs a command as another user.
- **File**: [0-iamsomeoneelse](./0-iamsomeoneelse)
- **Requirements**: The script should accept one argument, run the `whoami` command under the specified user, and pass Shellcheck without errors.

### Task 1: Run Nginx as Nginx
- **Description**: Configure Nginx to run as the nginx user and listen on port 8080.
- **File**: [1-run_nginx_as_nginx](./1-run_nginx_as_nginx)
- **Requirements**: Nginx must be running as the nginx user, listening on all active IPs on port 8080, and the script must be executable and pass Shellcheck without errors.

### Task 2: 7 lines or less
- **Description**: Shorten the fix from Task 1 to 7 lines or less.
- **File**: [100-fix_in_7_lines_or_less](./100-fix_in_7_lines_or_less)
- **Requirements**: The Bash script must be 7 lines long or less, respecting Bash script requirements, and cannot use certain characters or execute previous answer files.

## Usage
1. Clone the repository to your local machine.
2. Navigate to the directory containing the task files.
3. Run each Bash script individually according to the task requirements.
4. Verify the changes and functionality of the web stack components after running the scripts.
