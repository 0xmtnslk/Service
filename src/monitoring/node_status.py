import logging
import requests
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class NodeMonitor:
    def __init__(self):
        self.nodes: Dict[str, Dict] = {}
        
    def add_node(self, chain_id: str, rpc_endpoint: str):
        self.nodes[chain_id] = {
            'rpc_endpoint': rpc_endpoint,
            'status': None
        }
        
    def check_node_status(self, chain_id: str) -> Optional[Dict]:
        if chain_id not in self.nodes:
            logger.error(f"Chain {chain_id} not found")
            return None
            
        try:
            response = requests.get(f"{self.nodes[chain_id]['rpc_endpoint']}/status")
            status = response.json()
            self.nodes[chain_id]['status'] = status
            return status
        except Exception as e:
            logger.error(f"Error checking node status: {str(e)}")
            return None
