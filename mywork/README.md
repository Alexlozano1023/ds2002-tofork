# EC2 Bootstrap Script – Lab 8 (DS 2002)

This repository contains a bootstrap script used for automatically configuring an EC2 instance during launch as part of **Lab 8** in DS 2002.

## 🔧 File: `bootstrap.sh`

###  Purpose
This script bootstraps a new Ubuntu EC2 instance by automatically:
- Updating the system
- Installing essential tools:
  - `python3`
  - `git`
  - `nginx`
- Starting and enabling the nginx web server

## 💻Script Breakdown
```bash
#!/bin/bash
apt update -y
apt upgrade -y
apt install -y python3 git nginx
systemctl start nginx
systemctl enable nginx


