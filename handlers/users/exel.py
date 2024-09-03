import xlsxwriter
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ContentType

from data.config import admin_user_id
from handlers.users.transliterate import to_cyrillic
from keyboards.default.keyboards import admin, admin_exel, admin_main
from loader import dp, bot
from utils.db_api.xisobot import Database_Xisob


@dp.message_handler(text="Hisobot", user_id=[admin_user_id, 984568970])
async def a366s(message: types.Message):
    workbook = xlsxwriter.Workbook(f'data/EXEL.xlsx')
    worksheet = workbook.add_worksheet()
    # worksheet.write('A1', "№")
    worksheet.write('A1', "Sana")
    worksheet.write('B1', "Operatsiya")
    worksheet.write('C1', "Qaysi qassa")
    worksheet.write('D1', "Kirim yoki xarajat turi")
    worksheet.write('E1', "Qaysi zakaz uchun")
    worksheet.write('F1', "Tafsilotlar")
    worksheet.write('G1', "Val")
    worksheet.write('H1', "Summa")
    worksheet.write('I1', "FIO")

    # son = await db.count_users()
    # print(son)
    f_1_oper = open("./data/Text/1_oper.txt", "r")
    msg = f_1_oper.read()
    son = msg.count(f'\n')+10
    f_1_oper.close()
    n = 2
    for i in range(1, son + 1):
        f_1_oper = open("./data/Text/1_oper.txt", "r")

        for j in range(i-1):
            f_1_oper.readline()
        oper_1 = f_1_oper.readline()
        f_1_oper.close()
        j=0


        f_2_kassa = open("./data/Text/2_kassa.txt", "r")
        for j in range(i-1):
            f_2_kassa.readline()
        kassa_2 = f_2_kassa.readline()
        f_2_kassa.close()
        j=0


        f_3_kyxt = open("./data/Text/3_kyxt.txt", "r")
        for j in range(i-1):
            f_3_kyxt.readline()
        kyxt_3 = f_3_kyxt.readline()
        f_3_kyxt.close()
        j=0


        f_4_qzu = open("./data/Text/4_qzu.txt", "r")
        for j in range(i-1):
            f_4_qzu.readline()
        qzu_4 = f_4_qzu.readline()
        f_4_qzu.close()
        j=0


        f_5_tafsil = open("./data/Text/5_tafsil.txt", "r")
        for j in range(i-1):
            f_5_tafsil.readline()
        tafsil_5 = f_5_tafsil.readline()
        f_5_tafsil.close()
        j=0


        f_6_val = open("./data/Text/6_val.txt", "r")
        for j in range(i-1):
            f_6_val.readline()
        val_6 = f_6_val.readline()
        f_6_val.close()
        j=0

        f_7_summa = open("./data/Text/7_summa.txt", "r")
        for j in range(i-1):
            f_7_summa.readline()
        summa_7 = f_7_summa.readline()
        f_7_summa.close()
        j=0


        f_8_fish = open("./data/Text/8_fish.txt", "r")
        for j in range(i-1):
            f_8_fish.readline()
        fish_8 = f_8_fish.readline()
        f_8_fish.close()
        j=0


        f_9_vaqt = open("./data/Text/9_vaqt.txt", "r")
        for j in range(i-1):
            f_9_vaqt.readline()
        vaqt_9 = f_9_vaqt.readline()
        f_9_vaqt.close()
        j=0


        worksheet.write(f'A{n}', (vaqt_9[:-1]))
        worksheet.write(f'B{n}', (oper_1[:-1]))
        worksheet.write(f'C{n}', (kassa_2[:-1]))
        worksheet.write(f'D{n}', (kyxt_3[:-1]))
        worksheet.write(f'E{n}', (qzu_4[:-1]))
        worksheet.write(f'F{n}', (tafsil_5[:-1]))
        worksheet.write(f'G{n}', (val_6[:-1]))
        worksheet.write(f'H{n}', (summa_7[:-1]))
        worksheet.write(f'I{n}', (fish_8[:-1]))
        n = n + 1
    workbook.close()
    son = 0
    n = 2
    with open(f"data/EXEL.xlsx", "rb") as photo_file:
        await bot.send_document(chat_id=message.from_user.id, document=photo_file)
    await message.answer(f"Hisobot jo'natildi", reply_markup=admin_main)



# @dp.message_handler(text="Hisobot", user_id=984568970)
# async def aewrwss(message: types.Message):
#     workbook = xlsxwriter.Workbook(f'data/EXEL.xlsx')
#     worksheet = workbook.add_worksheet()
#     # worksheet.write('A1', "№")
#     worksheet.write('A1', "Сана")
#     worksheet.write('B1', "Операция")
#     worksheet.write('C1', "Қайси касса")
#     worksheet.write('D1', "Kirim ёки харажат тури")
#     worksheet.write('E1', "Qaysi zakaz uchun")
#     worksheet.write('F1', "Tafsilotlari")
#     worksheet.write('G1', "Вал")
#     worksheet.write('H1', " Сумма ")
#     worksheet.write('I1', "ФИО")

#     # son = await db.count_users()
#     # print(son)
#     son = 1000
#     n = 2
#     for i in range(1, son + 1):
#         # print(i)
#         # try:
#         #     user = await db.select_user(id=i)
#         # except:
#         #     user = None

#         f_1_oper = open("./data/Text/1_oper.txt", "r")

#         for j in range(i-1):
#             f_1_oper.readline()[:-1]
#         oper_1 = f_1_oper.readline()
#         f_1_oper.close()
#         j=0


#         f_2_kassa = open("./data/Text/2_kassa.txt", "r")
#         for j in range(i-1):
#             f_2_kassa.readline()[:-1]
#         kassa_2 = f_2_kassa.readline()
#         f_2_kassa.close()
#         j=0


#         f_3_kyxt = open("./data/Text/3_kyxt.txt", "r")
#         for j in range(i-1):
#             f_3_kyxt.readline()[:-1]
#         kyxt_3 = f_3_kyxt.readline()
#         f_3_kyxt.close()
#         j=0


#         f_4_qzu = open("./data/Text/4_qzu.txt", "r")
#         for j in range(i-1):
#             f_4_qzu.readline()[:-1]
#         qzu_4 = f_4_qzu.readline()
#         f_4_qzu.close()
#         j=0


#         f_5_tafsil = open("./data/Text/5_tafsil.txt", "r")
#         for j in range(i-1):
#             f_5_tafsil.readline()[:-1]
#         tafsil_5 = f_5_tafsil.readline()
#         f_5_tafsil.close()
#         j=0


#         f_6_val = open("./data/Text/6_val.txt", "r")
#         for j in range(i-1):
#             f_6_val.readline()[:-1]
#         val_6 = f_6_val.readline()
#         f_6_val.close()
#         j=0

#         f_7_summa = open("./data/Text/7_summa.txt", "r")
#         for j in range(i-1):
#             f_7_summa.readline()[:-1]
#         summa_7 = f_7_summa.readline()
#         f_7_summa.close()
#         j=0


#         f_8_fish = open("./data/Text/8_fish.txt", "r")
#         for j in range(i-1):
#             f_8_fish.readline()[:-1]
#         fish_8 = f_8_fish.readline()
#         f_8_fish.close()
#         j=0


#         f_9_vaqt = open("./data/Text/9_vaqt.txt", "r")
#         for j in range(i-1):
#             f_9_vaqt.readline()[:-1]
#         vaqt_9 = f_9_vaqt.readline()
#         f_9_vaqt.close()
#         j=0


#         worksheet.write(f'A{n}', to_cyrillic(vaqt_9))
#         worksheet.write(f'B{n}', to_cyrillic(oper_1))
#         worksheet.write(f'C{n}', to_cyrillic(kassa_2))
#         worksheet.write(f'D{n}', to_cyrillic(kyxt_3))
#         worksheet.write(f'E{n}', to_cyrillic(qzu_4))
#         worksheet.write(f'F{n}', to_cyrillic(tafsil_5))
#         worksheet.write(f'G{n}', to_cyrillic(val_6))
#         worksheet.write(f'H{n}', to_cyrillic(summa_7))
#         worksheet.write(f'I{n}', to_cyrillic(fish_8))
#         n = n + 1
#     workbook.close()
#     son = 0
#     n = 2
#     with open(f"data/EXEL.xlsx", "rb") as photo_file:
#         await bot.send_document(chat_id=message.from_user.id, document=photo_file)
#     await message.answer(f"Hisobot жўнатилди", reply_markup=admin_main)
