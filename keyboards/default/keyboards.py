from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kartalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Usmonjon Nematov"),
        ],
        [
            KeyboardButton(text="Karta Yanmin"),
            KeyboardButton(text="Karta Moy Gorod"),
        ],
        [
            KeyboardButton(text="Karta Xandamir"),
            KeyboardButton(text="Karta House Yasmin"),
        ],
        [
            KeyboardButton(text="Karta Saxovat"),
            KeyboardButton(text="🏠Bosh menu"),
        ],
    ], resize_keyboard=True
)

xisob_raqamlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bobomurod Sirojiddinov"),
        ],
        [
            KeyboardButton(text='"Yasmin Mebel New Group"'),
            KeyboardButton(text='"Moy Gorod Invest"'),
        ],
        [
            KeyboardButton(text='"Moy Gorod Invest"'),
            KeyboardButton(text='"Buyuk Sahovatli Zamin"'),
        ],
        [
            KeyboardButton(text='"House Yasmina"'),
            KeyboardButton(text='"Saxovat Madad Nur Fayz"'),
        ],
    ], resize_keyboard=True
)


chiqim_keyboard = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="Taʼminot"),
            KeyboardButton(text="Oylik"),
            KeyboardButton(text="Oshxona"),
        ],
        [
            KeyboardButton(text="Avtomobil"),
            KeyboardButton(text="Uskunalarga xarajat"),
            KeyboardButton(text="Marketing"),
        ],
        [
            KeyboardButton(text="Malaka oshirish"),
            KeyboardButton(text="Arenda"),
            KeyboardButton(text="Soliq"),
        ],
        [
            KeyboardButton(text="Safar xarajatlari"),
            KeyboardButton(text="Dvidend"),
            KeyboardButton(text="Boshqa xarajatlar"),
        ],
        [
            KeyboardButton(text="Kassalararo"),
            KeyboardButton(text="Dollar maydalash"),
            KeyboardButton(text="Turli shaxslar"),
        ],
        [
            KeyboardButton(text="🏠Bosh menu"),
        ],
    ], resize_keyboard=True
)


kirim_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mijozdan kirim"),
        ],
        [
            KeyboardButton(text="Turli shaxslar"),
        ],
        [
            KeyboardButton(text="Investitsiya"),
        ],
        [
            KeyboardButton(text="🏠Bosh menu"),
        ],
    ], resize_keyboard=True
)


bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Chiqim"),
            KeyboardButton(text="Kirim"),
        ],
        [
            KeyboardButton(text="🏠Bosh menu"),
        ],

    ], resize_keyboard=True
)

valyuta = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="sum"),
            KeyboardButton(text="$"),
        ],
        [
            KeyboardButton(text="🏠Bosh menu"),
        ],


    ], resize_keyboard=True
)


tasdik = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="qayta kiritish"),
            KeyboardButton(text="tasdiklash"),
        ],
        [
            KeyboardButton(text="🏠Bosh menu"),
        ],


    ], resize_keyboard=True
)


only_bosh_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="🏠Bosh menu"),
        ],
    ], resize_keyboard=True
)


admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hisobot"),
            KeyboardButton(text="Exelni almashtirish"),
        ],
        [
            KeyboardButton(text="/drop"),
        ],

    ], resize_keyboard=True
)


admin_exel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Avtamabillar.,"),
            KeyboardButton(text="FIO xodimlar.,"),
        ],
        [
            KeyboardButton(text="Kassalararo.,"),
            KeyboardButton(text="Turli shaxslar.,"),
        ],
        [
            KeyboardButton(text="Zakaz nomlari.,"),
        ],
        [
            KeyboardButton(text="/admin"),
        ],
    ], resize_keyboard=True
)


admin_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/admin"),
        ],
    ], resize_keyboard=True
)



tasdik_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/rad etish"),
            KeyboardButton(text="/tasdiklash"),
        ],
    ], resize_keyboard=True
)