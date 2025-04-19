#!/bin/bash

# Update system packages
apt update -y
apt upgrade -y

# Install selected tools
apt install -y python3 git nginx

# Start and enable nginx service
systemctl start nginx
systemctl enable nginx

