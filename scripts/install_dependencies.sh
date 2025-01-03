#!/bin/bash

# System dependencies
apt-get update
apt-get install -y python3-pip python3-venv git

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python requirements
pip install -r requirements.txt

# Create config directories
mkdir -p config
mkdir -p logs

# Copy example config
cp .env.example .env

echo "Please update .env with your configuration"
