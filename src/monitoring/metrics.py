from prometheus_client import Counter, Gauge, start_http_server
import logging

logger = logging.getLogger(__name__)

class MetricsCollector:
    def __init__(self):
        self.missed_blocks = Counter('validator_missed_blocks_total', 
                                   'Total missed blocks', ['chain_id'])
        self.sync_height = Gauge('node_sync_height', 
                               'Current sync height', ['chain_id'])
        self.peer_count = Gauge('node_peer_count',
                              'Number of peers', ['chain_id'])
        
        # Start Prometheus HTTP server
        start_http_server(8000)
        
    def record_missed_block(self, chain_id: str):
        self.missed_blocks.labels(chain_id=chain_id).inc()
        
    def update_sync_height(self, chain_id: str, height: int):
        self.sync_height.labels(chain_id=chain_id).set(height)
        
    def update_peer_count(self, chain_id: str, count: int):
        self.peer_count.labels(chain_id=chain_id).set(count)
