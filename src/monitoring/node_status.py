import aiohttp
import asyncio
from utils.database import Database

class NodeMonitor:
    def __init__(self):
        self.db = Database()
        
    async def check_validator_status(self, network: str, valoper_address: str):
        # Get RPC endpoints from config
        rpc_endpoints = self.get_network_endpoints(network)
        
        for endpoint in rpc_endpoints:
            try:
                async with aiohttp.ClientSession() as session:
                    # Check validator status
                    status = await self.get_validator_status(session, endpoint, valoper_address)
                    # Check block height
                    height = await self.get_block_height(session, endpoint)
                    return {"status": status, "height": height}
            except Exception as e:
                continue
        return {"status": "error", "height": 0}
    
    async def get_validator_status(self, session, endpoint: str, valoper_address: str):
        async with session.get(f"{endpoint}/validators") as response:
            data = await response.json()
            return data
