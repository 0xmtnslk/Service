import asyncio
import logging
from bot.handlers import setup_handlers
from monitoring.node_status import NodeMonitor
from monitoring.alerts import AlertManager
from monitoring.metrics import MetricsCollector
from utils.database import Database

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Initialize components
    db = Database()
    node_monitor = NodeMonitor()
    alert_manager = AlertManager()
    metrics_collector = MetricsCollector()
    
    # Setup bot and handlers
    bot = setup_handlers()
    
    try:
        await bot.polling(non_stop=True)
    except Exception as e:
        logging.error(f"Bot error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
