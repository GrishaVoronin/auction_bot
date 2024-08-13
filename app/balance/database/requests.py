from app.balance.database.models import async_session
from app.balance.database.models import Balance
from sqlalchemy import select, update

async def add_user(tg_id):
    async with async_session() as session:
        balance = await session.scalar(select(Balance).where(Balance.tg_id == tg_id))

        if not balance:
            session.add(Balance(tg_id=tg_id, balance=0, in_slots=0))
            await session.commit()

async def refill_balance(tg_id, money):
    async with async_session() as session:
        balance = await session.scalar(select(Balance).where(Balance.tg_id == tg_id))
        balance.balance += money
        await session.commit()