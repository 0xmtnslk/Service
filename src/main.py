import logging
from bot.handlers import setup_handlers
from monitoring.alerts import AlertManager
from monitoring.node_status import NodeMonitor
from monitoring.metrics import MetricsCollector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    alert_manager = AlertManager()
    node_monitor = NodeMonitor()
    metrics = MetricsCollector()
    
    # Setup and start bot handlers
    setup_handlers(alert_manager, node_monitor, metrics)

if __name__ == "__main__":
    main()
