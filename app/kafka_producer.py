from aiokafka import AIOKafkaProducer
import json

async def produce_msg(topic, msg):
    # requires python dict as msg
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    await producer.start()
    try:
        await producer.send_and_wait(topic, msg)
    finally:
        await producer.stop()