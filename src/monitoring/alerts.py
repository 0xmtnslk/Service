from typing import Dict, List
import logging
import time

logger = logging.getLogger(__name__)

class AlertManager:
    def __init__(self):
        self.alert_history: Dict[str, List[float]] = {}
        self.alert_cooldown = 300  # 5 minutes
        
    def can_send_alert(self, alert_key: str) -> bool:
        if alert_key not in self.alert_history:
            self.alert_history[alert_key] = []
            return True
            
        now = time.time()
        self.alert_history[alert_key] = [t for t in self.alert_history[alert_key] 
                                       if now - t < self.alert_cooldown]
                                       
        if len(self.alert_history[alert_key]) == 0:
            return True
            
        return False
        
    def record_alert(self, alert_key: str):
        if alert_key not in self.alert_history:
            self.alert_history[alert_key] = []
        self.alert_history[alert_key].append(time.time())
