import asyncio
from aiogram import Bot, Dispatcher

import logging

import os
from dotenv import load_dotenv

from handlers.start import router_start

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router_start)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())