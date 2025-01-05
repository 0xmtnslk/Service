from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml
from typing import Dict, List
import os

app = FastAPI()

class Network:
    def __init__(self, name: str, chain_id: str, logo_png: str, rpc_endpoints: List[str]):
        self.name = name
        self.chain_id = chain_id
        self.logo_png = logo_png
        self.rpc_endpoints = rpc_endpoints

class ValidatorConfig:
    def __init__(self, network: str, valoper_address: str, telegram_id: str):
        self.network = network
        self.valoper_address = valoper_address
        self.telegram_id = telegram_id

with open("app/networks.yaml") as f:
    networks_config = yaml.safe_load(f)

networks = {}
for net_key, net_data in networks_config["networks"].items():
    networks[net_key] = Network(
        name=net_data["name"],
        chain_id=net_data["chain_id"],
        logo_png=net_data["logo_png"],
        rpc_endpoints=net_data["rpc_endpoints"]
    )

@app.get("/networks")
def get_networks():
    return networks_config

@app.post("/validator")
def add_validator(network: str, valoper_address: str, telegram_id: str):
    if network not in networks:
        raise HTTPException(status_code=404, detail="Network not found")
    config = ValidatorConfig(network, valoper_address, telegram_id)
    generate_tenderduty_config(config)
    return {"status": "success"}
