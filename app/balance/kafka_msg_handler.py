import database.requests as rq

async def kafka_handler(msg):
    data = msg.value
    if data['command'] == 'add_user':
        await rq.add_user(data['tg_id'])