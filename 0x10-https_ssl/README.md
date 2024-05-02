# 0x10-https_ssl

## HTTPS SSL Configuration with HAProxy

This repository contains configurations and instructions for setting up HTTPS SSL termination and enforcing HTTPS traffic using HAProxy.

## Task 1: HAProxy SSL Termination

### Objective:
Configure HAProxy to terminate SSL traffic and serve encrypted traffic for the subdomain www.

### Steps:
1. Install HAProxy 1.5 or higher.
2. Create an SSL certificate using certbot for the subdomain www.
3. Configure HAProxy to listen on port TCP 443 and accept SSL traffic.
4. Ensure HAProxy serves encrypted traffic returning the root of your web server.
5. Verify that the root of your domain returns "Holberton School".
6. Share your HAProxy configuration as `/etc/haproxy/haproxy.cfg`.

## Task 2: Redirect HTTP to HTTPS

### Objective:
Configure HAProxy to automatically redirect HTTP traffic to HTTPS.

### Steps:
1. Edit HAProxy configuration to include a redirection rule for HTTP to HTTPS.
2. Ensure the redirection is transparent to the user and returns a 301 status code.
3. Verify that HTTP traffic is redirected to HTTPS.
4. Share your HAProxy configuration as `/etc/haproxy/haproxy.cfg`.

## Files:
- `0-haproxy_ssl_termination`: HAProxy configuration file for SSL termination.
- `100-redirect_http_to_https`: HAProxy configuration file for redirecting HTTP to HTTPS.

## Usage:
1. Ensure HAProxy is installed and configured as specified.
2. Replace placeholders with actual domain names, IP addresses, and file paths.
3. Restart HAProxy to apply the changes.

## Notes:
- HAProxy version 1.5 or higher is required for SSL termination.
- Certbot can be used to obtain SSL certificates for domains.
- Verify configurations and SSL certificate paths before deployment.
