import yaml

def generate_config(network_id: str, valoper_address: str):
    with open("networks.yaml") as f:
        networks = yaml.safe_load(f)
    
    network = networks["networks"][network_id]
    
    config = {
        "enable_dashboard": True,
        "listen_port": 8888,
        "hide_logs": True,
        "node_down_alert_minutes": 3,
        "prometheus_enabled": True,
        "prometheus_listen_port": 28686,
        "chains": {
            network["name"]: {
                "chain_id": network["chain_id"],
                "valoper_address": valoper_address,
                "nodes": [{"url": url, "alert_if_down": False} for url in network["rpc_endpoints"]]
            }
        }
    }
    
    return yaml.dump(config)
