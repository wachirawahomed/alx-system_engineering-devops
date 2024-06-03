#!/usr/bin/env bash

# Update the package list
sudo apt-get update

# Add the MySQL APT repository key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C

# Add the MySQL APT repository
echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" | sudo tee /etc/apt/sources.list.d/mysql.list

# Update the package list again with the new repository
sudo apt-get update

# Install MySQL 5.7 packages
sudo apt-get install -f -y mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

# Verify the installation
mysql --version
