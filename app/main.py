from fastapi import FastAPI
from pydantic import BaseModel
import yaml

app = FastAPI()

@app.get("/networks")
def get_networks():
    with open("networks.yaml") as f:
        networks = yaml.safe_load(f)
    return networks
