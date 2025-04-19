#!/bin/bash

apt update -y
apt upgrade -y


apt install -y python3 git nginx


systemctl start nginx
systemctl enable ngin
