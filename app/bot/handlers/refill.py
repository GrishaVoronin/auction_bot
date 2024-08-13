from aiogram.types import Message
from aiogram import Router, F

import app.bot.messages as msg

from app.bot.states import Refill
from aiogram.fsm.context import FSMContext
from app.kafka_producer import produce_msg

router_refill = Router()

@router_refill.message(F.text == 'refill')
async def create_reminder(message: Message, state: FSMContext):
    await state.set_state(Refill.money)
    await message.answer(msg.refill)

@router_refill.message(Refill.money)
async def get_money(message: Message, state: FSMContext):
    try:
        int(message.text)
    except:
        await message.answer("Введено не число")
    finally:
        await produce_msg('balances', {'command': 'refill_balance',
                                       'tg_id': message.from_user.id, 'money': int(message.text)})
        await state.update_data(money=message.text)
        await message.answer("Баланс пополнен")