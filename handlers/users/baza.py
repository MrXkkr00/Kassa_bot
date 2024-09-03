from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ContentType

from data.config import admin_user_id
from keyboards.default.keyboards import admin, admin_exel, admin_main, tasdik_main
from loader import dp, bot
from utils.db_api.xisobot import Database_Xisob


class DropState(StatesGroup):
    drop = State()


@dp.message_handler(text="/admin", state=[DropState.drop])
async def adqeqes(message: types.Message, state:FSMContext):
    await message.answer(f"Drop", reply_markup=tasdik_main)
    await state.finish()



@dp.message_handler(text="/admin")
async def adqeqes(message: types.Message, state : FSMContext):
    await message.answer(f"Admin", reply_markup=admin)


@dp.message_handler(text="/drop", user_id=984568970)
async def adqeqes(message: types.Message):
    await message.answer(f"Drop", reply_markup=tasdik_main)
    await DropState.drop.set()


@dp.message_handler(text="/drop", user_id=admin_user_id)
async def adq123es(message: types.Message):
    await message.answer(f"Drop", reply_markup=tasdik_main)
    await DropState.drop.set()


@dp.message_handler(text="/tasdiklash", state=DropState.drop)
async def ad213es(message: types.Message, state: FSMContext):
    try:
        f_oper = open("./data/Text/1_oper.txt", "w")
        f_oper.close()

        f_kassa = open("./data/Text/2_kassa.txt", "w")
        f_kassa.close()

        f_3_kyxt = open("./data/Text/3_kyxt.txt", "w")
        f_3_kyxt.close()

        f_4_qzu = open("./data/Text/4_qzu.txt", "w")
        f_4_qzu.close()

        f_5_tafsil = open("./data/Text/5_tafsil.txt", "w")
        f_5_tafsil.close()

        f_6_val = open("./data/Text/6_val.txt", "w")
        f_6_val.close()

        f_7_summa = open("./data/Text/7_summa.txt", "w")
        f_7_summa.close()

        f_8_fish = open("./data/Text/8_fish.txt", "w")
        f_8_fish.close()

        f_vaqt = open("./data/Text/9_vaqt.txt", "w")
        f_vaqt.close()

        await message.answer(f"Baza yangilandi", reply_markup=admin)
    except:
        await message.answer(f"Xatolik bo'ldi")
    await state.finish()


@dp.message_handler(text="/rad etish", state=DropState.drop)
async def a324234s(message: types.Message, state: FSMContext):
    await message.answer(f"Admin", reply_markup=admin)
    await state.finish()
