from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

import app.bot.messages as msg

import app.bot.database.requests as rq

from app.kafka_producer import produce_msg

router_start = Router()

@router_start.message(CommandStart())
async def greeting(message: Message):
    await rq.add_user(message.from_user.id, message.from_user.first_name)
    await produce_msg('balances', {'command': 'add_user', 'tg_id': message.from_user.id})
    await message.answer(msg.start)