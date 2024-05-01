# 0x0E. Web stack debugging #1

## Description
This repository contains solutions to debugging tasks related to web stack configuration issues. The tasks involve identifying and fixing issues related to Nginx configuration to ensure it listens on port 80.

## Tasks

### Task 0: Nginx likes port 80
- Description: Identify and fix the issue preventing Nginx from listening on port 80.
- Requirements:
  - Nginx must be running and listening on port 80 of all the server’s active IPv4 IPs.
  - Write a Bash script to configure the server to meet the above requirements.

### Task 1: Debugging made short
- Description: Build a concise Bash script based on the solution from Task 0 to automate the fix for Nginx configuration.
- Requirements:
  - The Bash script must be 5 lines long or less.
  - Ensure there's a new line at the end of the file.
  - The script must meet usual Bash script requirements.
  - Do not use `;`, `&&`, or `wget`.
  - Ensure the `service` command reports that Nginx is not running.

## Usage
To use the provided scripts, follow these steps:
1. Clone this repository to your local machine.
2. Navigate to the directory containing the scripts.
3. Make sure all scripts have executable permissions using `chmod +x script_name`.
4. Run the desired script using `./script_name`.

## Author
This repository was created by Davis Wahome.
