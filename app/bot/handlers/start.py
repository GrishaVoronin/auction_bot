from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

import app.bot.messages as msg

router_start = Router()

@router_start.message(CommandStart())
async def greeting(message: Message):
    await message.answer(msg.start)