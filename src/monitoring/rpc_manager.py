import yaml
import random

class RPCManager:
    def __init__(self, backup_nodes_file='config/backup_nodes.yml'):
        with open(backup_nodes_file) as f:
            self.nodes = yaml.safe_load(f)
        self.current_nodes = {}
    
    def get_rpc_endpoint(self, chain):
        if chain not in self.current_nodes:
            self.current_nodes[chain] = self.nodes[chain][0]
        return self.current_nodes[chain]
    
    def rotate_endpoint(self, chain):
        available_nodes = self.nodes[chain]
        self.current_nodes[chain] = random.choice(available_nodes)
