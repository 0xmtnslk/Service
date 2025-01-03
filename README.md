# Validator Monitor Bot

## Installation Guide

1. Install required packages:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
```

2. Clone repository:
```bash
git clone https://github.com/0xmtnslk/Service
cd Service
```

3. Install Python dependencies:
```bash
pip3 install -r requirements.txt
```

4. Configure Telegram Bot:
- Create a new bot with [@BotFather](https://t.me/BotFather)
- Save the bot token
- Edit `systemd/validator-bot.service` and replace `your_token_here` with your bot token

5. Install systemd service:
```bash
sudo cp systemd/validator-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable validator-bot
sudo systemctl start validator-bot
```

6. Install Tenderduty:
```bash
sudo addgroup --system tenderduty
sudo adduser --ingroup tenderduty --system --home /var/lib/tenderduty tenderduty
sudo -su tenderduty
cd ~
echo 'export PATH=$PATH:~/go/bin' >> .bashrc
. .bashrc
git clone https://github.com/blockpane/tenderduty
cd tenderduty
go install
```

7. Configure and start Tenderduty:
```bash
sudo cp systemd/tenderduty.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable tenderduty
sudo systemctl start tenderduty
```

8. Check logs:
```bash
# Bot logs
sudo journalctl -fu validator-bot

# Tenderduty logs
sudo journalctl -fu tenderduty
```
