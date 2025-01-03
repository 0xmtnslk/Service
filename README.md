# Validator Monitor Bot

## Installation Guide

1. Clone the repository:
```bash
git clone https://github.com/0xmtnslk/Service.git
cd Service
```

2. Install Python dependencies:
```bash
pip3 install -r requirements.txt
```

3. Create .env file:
```bash
echo "TELEGRAM_BOT_TOKEN=your_bot_token" > .env
```

4. Install systemd service:
```bash
sudo cp systemd/validator-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable validator-bot
sudo systemctl start validator-bot
```

5. Check service status:
```bash
sudo systemctl status validator-bot
```
