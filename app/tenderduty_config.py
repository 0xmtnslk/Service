import yaml
import os

def generate_tenderduty_config(validator_config):
    config = {
        "enable_dashboard": True,
        "listen_port": 8888,
        "hide_logs": True,
        "node_down_alert_minutes": 3,
        "prometheus_enabled": True,
        "prometheus_listen_port": 28686,
        "telegram": {
            "enabled": True,
            "api_key": os.getenv("TELEGRAM_BOT_TOKEN"),
            "chat_id": validator_config.telegram_id
        },
        "chains": {
            validator_config.network: {
                "chain_id": networks[validator_config.network].chain_id,
                "valoper_address": validator_config.valoper_address,
                "public_fallback": True,
                "alerts": {
                    "stalled_enabled": True,
                    "stalled_minutes": 10,
                    "consecutive_enabled": True,
                    "consecutive_missed": 1,
                    "percentage_enabled": True,
                    "percentage_missed": 10,
                    "alert_if_inactive": True,
                    "alert_if_no_servers": True
                },
                "nodes": [
                    {"url": url, "alert_if_down": False}
                    for url in networks[validator_config.network].rpc_endpoints
                ]
            }
        }
    }

    with open("config.yml", "w") as f:
        yaml.dump(config, f)
