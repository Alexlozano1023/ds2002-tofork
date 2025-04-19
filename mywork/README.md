# EC2 Bootstrap Script – Lab 8 (DS 2002)

This repository contains a bootstrap script used for automatically configuring an EC2 instance during launch.

##  File: `bootstrap.sh`

### Purpose:
This script installs and configures the following tools automatically when launching an EC2 instance:
- `python3`
- `git`
- `nginx`

###  Key Commands:
- `apt update && apt upgrade`: Updates the system
- `apt install`: Installs required tools
- `systemctl start/enable`: Starts and auto-enables nginx

###  How to Use:
1. Copy the contents of `bootstrap.sh`
2. Paste it into the **User data** section when launching an EC2 instance
3. Ensure port 22 (SSH) and port 80 (HTTP) are open in your security group
4. After launch, verify installations by connecting via SSH and testing tool availability

###  Verification:
```bash
python3 --version
git --version
curl http://localhost

