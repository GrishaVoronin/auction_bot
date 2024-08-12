import asyncio
from database.models import run_db

async def main():
    await run_db()

if __name__ == '__main__':
    asyncio.run(main())