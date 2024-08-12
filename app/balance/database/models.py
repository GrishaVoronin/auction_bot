from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from sqlalchemy import BigInteger

import os
from dotenv import load_dotenv

load_dotenv()
engine = create_async_engine(os.getenv('BALANCES_DB_URL'))

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Balance(Base):
    __tablename__ = 'balances'

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    balance: Mapped[int] = mapped_column(BigInteger)
    in_slots: Mapped[int] = mapped_column(BigInteger)

async def run_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)