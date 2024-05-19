# 0x13. Firewall

This repository contains solutions to tasks related to configuring a firewall using `ufw` on web servers.

## Task 0: Block All Incoming Traffic Except Specific Ports

### Description
Configure the firewall on web-01 to block all incoming traffic except for SSH (port 22), HTTPS SSL (port 443), and HTTP (port 80).

### Solution
The solution involves setting up `ufw` firewall rules to block incoming traffic on all ports except the specified ones.

#### Steps
1. Install `ufw` if not already installed.
2. Set the default incoming policy to deny.
3. Allow incoming traffic for SSH (port 22), HTTPS SSL (port 443), and HTTP (port 80).
4. Enable `ufw` to apply the rules.
5. Verify the `ufw` status to ensure correct configuration.

## Task 1: Port Forwarding

### Description
Configure port forwarding on web-01 to redirect traffic from port 8080/TCP to port 80/TCP.

### Solution
The solution involves modifying the `ufw` configuration file to implement port forwarding.

#### Steps
1. Open the `ufw` configuration file (`before.rules`) for editing.
2. Add a port forwarding rule to redirect traffic from port 8080 to port 80.
3. Save the changes and reload the `ufw` firewall.
4. Verify that the port forwarding rule has been applied correctly.

## Repository Structure
- `0-block_all_incoming_traffic_but`: Contains the `ufw` configuration file modified for Task 0.
- `100-port_forwarding`: Contains the `ufw` configuration file modified for Task 1.
