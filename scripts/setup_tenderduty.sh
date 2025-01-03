#!/bin/bash

# Install Tenderduty
cd $HOME
git clone https://github.com/blockpane/tenderduty
cd tenderduty
docker-compose up -d

# Create config directory
mkdir -p $HOME/.tenderduty/config

# Copy example config
cp config.yml.example $HOME/.tenderduty/config/config.yml

echo "Tenderduty installation complete"
