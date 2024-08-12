import asyncio
from database.models import run_db

from app.kafka_consumer import consume_msgs
from app.balance.kafka_msg_handler import kafka_handler

async def main():
    await consume_msgs('balances', kafka_handler)
    await run_db()

if __name__ == '__main__':
    asyncio.run(main())