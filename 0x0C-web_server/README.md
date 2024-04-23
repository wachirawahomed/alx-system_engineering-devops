# 0x0C. Web server  

This repository contains scripts and a Puppet manifest for configuring an Nginx web server on Ubuntu.  
Below are instructions for using each script and what they accomplish.  

## Scripts  

### 0-transfer_file  

This Bash script transfers a file from a client to a server using scp.
It accepts four parameters: the path to the file to be transferred, the IP address of the server, the username to connect with, and the path to the SSH private key to use with scp.  

_Usage:_   
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY  

### 1-install_nginx_web_server  

This Bash script installs Nginx on an Ubuntu server and configures it to listen on port 80.  
Additionally, it sets up a basic HTML page containing the string "Hello World!" to be served when querying Nginx at its root ("/") with a GET request using curl.  

_Usage:_  
./1-install_nginx_web_server  

### 2-setup_a_domain_name  

This Bash script configures a domain name for the server.  
It provides instructions for registering a free .tech domain from .TECH Domains and setting up DNS records to point the domain to the server's IP address.  
Additionally, it instructs how to update the Project website URL in the user's profile.  

### 3-redirection  

This Bash script configures Nginx to redirect requests to "/redirect_me" to another specified URL with a 301 Moved Permanently status code.  

_Usage:_  
./3-redirection  

### 4-not_found_page_404  

This Bash script configures Nginx to have a custom 404 page that contains the string "Ceci n'est pas une page".  

_Usage:_  
./4-not_found_page_404  

### 5-install_nginx_web_server.pp  

This Puppet manifest installs and configures Nginx on an Ubuntu server. 
It ensures that Nginx is installed, configured to listen on port 80, and set up to return "Hello World!" when queried at its root ("/"). 
Additionally, it configures redirection for "/redirect_me".  

_Usage:_  
sudo puppet apply 5-install_nginx_web_server.pp  
