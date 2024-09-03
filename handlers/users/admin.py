from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ContentType

from data.config import admin_user_id
from keyboards.default.keyboards import admin, admin_exel, admin_main
from loader import dp, bot


@dp.message_handler(text="/admin", user_id=admin_user_id)
async def adminmes(message: types.Message):
    await message.answer(f"Admin", reply_markup=admin)\

    
@dp.message_handler(text="/admin", user_id=984568970)
async def ad213mes(message: types.Message):
    await message.answer(f"Admin", reply_markup=admin)


@dp.message_handler(text="Exelni almashtirish")
async def adminmes(message: types.Message):
    await message.answer(f"Admin", reply_markup=admin_exel)


class AvtamabilState(StatesGroup):
    exel = State()


@dp.message_handler(text="Avtamabillar.,")
async def admiaves(message: types.Message):
    await message.answer(f"Avtamabillar exelini yuboring", reply_markup=admin_main)
    await AvtamabilState.exel.set()


@dp.message_handler(content_types=ContentType.DOCUMENT, state=AvtamabilState.exel)
async def advames(message: types.Message, state: FSMContext):
    file_id_doc = message.document.file_id
    file = await bot.get_file(file_id_doc)
    file_path = file.file_path
    await bot.download_file(file_path, "./data/Exel/Avtamabillar.xlsx")
    await message.answer(f"Avtamabillarga  exel yuklandi", reply_markup=admin_exel)
    await state.finish()


class FIOstate(StatesGroup):
    exel = State()


@dp.message_handler(text="FIO xodimlar.,")
async def ad213miaves(message: types.Message):
    await message.answer(f"FIO xodimlar exelini yuboring", reply_markup=admin_main)
    await FIOstate.exel.set()


@dp.message_handler(content_types=ContentType.DOCUMENT, state=FIOstate.exel)
async def advam23es(message: types.Message, state: FSMContext):
    file_id_doc = message.document.file_id
    file = await bot.get_file(file_id_doc)
    file_path = file.file_path
    await bot.download_file(file_path, "./data/Exel/FISHxodimlar.xlsx")
    await message.answer(f"FIO xodimlarга  exel yuklandi", reply_markup=admin_exel)
    await state.finish()


class Kassastate(StatesGroup):
    exel = State()


@dp.message_handler(text="Kassalararo.,")
async def ad213m3123iaves(message: types.Message):
    await message.answer(f"Kassalararo exelini yuboring", reply_markup=admin_main)
    await Kassastate.exel.set()


@dp.message_handler(content_types=ContentType.DOCUMENT, state=Kassastate.exel)
async def advam21323es(message: types.Message, state: FSMContext):
    file_id_doc = message.document.file_id
    file = await bot.get_file(file_id_doc)
    file_path = file.file_path
    await bot.download_file(file_path, "./data/Exel/Kassalararo.xlsx")
    await message.answer(f"Kassalararoга  exel yuklandi", reply_markup=admin_exel)
    await state.finish()


class Turlistate(StatesGroup):
    exel = State()


@dp.message_handler(text="Turli shaxslar.,")
async def ad213m3213123iaves(message: types.Message):
    await message.answer(f"Turli shaxslar exelini yuboring", reply_markup=admin_main)
    await Turlistate.exel.set()


@dp.message_handler(content_types=ContentType.DOCUMENT, state=Turlistate.exel)
async def advam2132133es(message: types.Message, state: FSMContext):
    file_id_doc = message.document.file_id
    file = await bot.get_file(file_id_doc)
    file_path = file.file_path
    await bot.download_file(file_path, "./data/Exel/Turli_shaxslar.xlsx")
    await message.answer(f"Turli shaxslarга  exel yuklandi", reply_markup=admin_exel)
    await state.finish()


class Zakazstate(StatesGroup):
    exel = State()


@dp.message_handler(text="Zakaz nomlari.,")
async def ad213m3213123iaves(message: types.Message):
    await message.answer(f"Zakaz nomlari exelini yuboring", reply_markup=admin_main)
    await Zakazstate.exel.set()


@dp.message_handler(content_types=ContentType.DOCUMENT, state=Zakazstate.exel)
async def advam2132133es(message: types.Message, state: FSMContext):
    file_id_doc = message.document.file_id
    file = await bot.get_file(file_id_doc)
    file_path = file.file_path
    await bot.download_file(file_path, "./data/Exel/Zakaz_nomlari.xlsx")
    await message.answer(f"Zakaz nomlariга exel yuklandi", reply_markup=admin_exel)
    await state.finish()


@dp.message_handler(text="/admin", state=[AvtamabilState.exel, FIOstate.exel, Kassastate.exel,
                                          Turlistate.exel, Zakazstate.exel])
async def admi213131nmes(message: types.Message, state: FSMContext):
    await message.answer(f"Admin", reply_markup=admin)
    await state.finish()
