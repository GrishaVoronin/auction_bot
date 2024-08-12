from aiokafka import AIOKafkaConsumer
import json

async def consume_msgs(topic, msg_handler):
    consumer = AIOKafkaConsumer(topic, bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    await consumer.start()
    async for msg in consumer:
        await msg_handler(msg)