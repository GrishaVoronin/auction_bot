import asyncio
from aiogram import Bot, Dispatcher

import logging

import os
from dotenv import load_dotenv

from handlers.start import router_start
from handlers.refill import router_refill

from database.models import run_db

async def main():
    await run_db()

    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router_start, router_refill)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())