from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Asosiy menyu
user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔎 Ijaraga olaman"),
            KeyboardButton(text="🔑 Ijaraga beraman")
        ],
        [
            KeyboardButton(text="🌐 Tilni o‘zgartirish"),
            KeyboardButton(text="❓ Qanday ishlaydi")
        ],
        [
            KeyboardButton(text="📋 E'lonlarim")
        ]
    ],
    resize_keyboard=True
)

# Uy turlari menyusi
house_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠 Kvartira"),
            KeyboardButton(text="🏡 Uy Hovli")
        ],
        [
            KeyboardButton(text="🏘 Dacha"),
            KeyboardButton(text="🏙 Ofis")
        ],
        [
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

# Ijara muddati menyusi
k_v_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uzoq muddatga"),
            KeyboardButton(text="Kunlik")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

# Tumanlar menyusi
u_y_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌐 Boshqa viloyatni tanlash"),
        ],
        [
            KeyboardButton(text="Yakkasaroy"),
            KeyboardButton(text="Yashnobod")
        ],
        [
            KeyboardButton(text="Shayxontohur"),
            KeyboardButton(text="Chilonzor")
        ],
        [
            KeyboardButton(text="Bektemir"),
            KeyboardButton(text="Olmazor")
        ],
        [
            KeyboardButton(text="Mirobod"),
            KeyboardButton(text="Mirzo Ulug'bek")
        ],
        [
            KeyboardButton(text="Uchtepa"),
            KeyboardButton(text="Yunusobod")
        ],
        [
            KeyboardButton(text="Sergeli"),
            KeyboardButton(text="Yangihayot")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ],
    ],
    resize_keyboard=True
)

# Kimga ijaraga berish menyusi
humans_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Talabalarga"),
            KeyboardButton(text="Ishchilarga")
        ],
        [
            KeyboardButton(text="Sayyohlarga"),
            KeyboardButton(text="Oilaga")
        ],
        [
            KeyboardButton(text="Sheriklikka"),
            KeyboardButton(text="Barchaga")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ],
    ],
    resize_keyboard=True
)

# Xonalar soni menyusi
xona_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 xona"),
            KeyboardButton(text="2 xona"),
            KeyboardButton(text="3 xona"),
            KeyboardButton(text="4 xona"),
        ],
        [
            KeyboardButton(text="5 xona"),
            KeyboardButton(text="6 xona"),
            KeyboardButton(text="7 xona"),
            KeyboardButton(text="8 xona"),
        ],
        [
            KeyboardButton(text="9 xona"),
            KeyboardButton(text="10 xona"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

# Uy hovli sotix menyusi
uy_hovli_sotix_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
            KeyboardButton(text="4"),
        ],
        [
            KeyboardButton(text="5"),
            KeyboardButton(text="6"),
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
        ],
        [
            KeyboardButton(text="9"),
            KeyboardButton(text="10"),
            KeyboardButton(text="11"),
            KeyboardButton(text="12"),
        ],
        [
            KeyboardButton(text="13"),
            KeyboardButton(text="14"),
            KeyboardButton(text="15"),
            KeyboardButton(text="16"),
        ],
        [
            KeyboardButton(text="17"),
            KeyboardButton(text="18"),
            KeyboardButton(text="19"),
            KeyboardButton(text="20"),
        ],
        [
            KeyboardButton(text="25"),
            KeyboardButton(text="30"),
            KeyboardButton(text="35"),
            KeyboardButton(text="40"),
        ],
        [
            KeyboardButton(text="45"),
            KeyboardButton(text="50"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

# Kvadrat metr menyusi
sotix_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="20 m²"),
            KeyboardButton(text="22 m²"),
            KeyboardButton(text="25 m²"),
            KeyboardButton(text="28 m²"),
        ],
        [
            KeyboardButton(text="30 m²"),
            KeyboardButton(text="32 m²"),
            KeyboardButton(text="35 m²"),
            KeyboardButton(text="38 m²"),
        ],
        [
            KeyboardButton(text="40 m²"),
            KeyboardButton(text="42 m²"),
            KeyboardButton(text="45 m²"),
            KeyboardButton(text="48 m²"),
        ],
        [
            KeyboardButton(text="50 m²"),
            KeyboardButton(text="52 m²"),
            KeyboardButton(text="55 m²"),
            KeyboardButton(text="58 m²"),
        ],
        [
            KeyboardButton(text="60 m²"),
            KeyboardButton(text="62 m²"),
            KeyboardButton(text="65 m²"),
            KeyboardButton(text="68 m²"),
        ],
        [
            KeyboardButton(text="70 m²"),
            KeyboardButton(text="72 m²"),
            KeyboardButton(text="75 m²"),
            KeyboardButton(text="78 m²"),
        ],
        [
            KeyboardButton(text="80 m²"),
            KeyboardButton(text="82 m²"),
            KeyboardButton(text="85 m²"),
            KeyboardButton(text="88 m²"),
        ],
        [
            KeyboardButton(text="90 m²"),
            KeyboardButton(text="92 m²"),
            KeyboardButton(text="95 m²"),
            KeyboardButton(text="98 m²"),
        ],
        [
            KeyboardButton(text="100 m²"),
            KeyboardButton(text="105 m²"),
            KeyboardButton(text="110 m²"),
            KeyboardButton(text="115 m²"),
        ],
        [
            KeyboardButton(text="120 m²"),
            KeyboardButton(text="125 m²"),
            KeyboardButton(text="130 m²"),
            KeyboardButton(text="135 m²"),
        ],
        [
            KeyboardButton(text="140 m²"),
            KeyboardButton(text="145 m²"),
            KeyboardButton(text="150 m²"),
            KeyboardButton(text="155 m²"),
        ],
        [
            KeyboardButton(text="160 m²"),
            KeyboardButton(text="165 m²"),
            KeyboardButton(text="170 m²"),
            KeyboardButton(text="175 m²"),
        ],
        [
            KeyboardButton(text="180 m²"),
            KeyboardButton(text="185 m²"),
            KeyboardButton(text="190 m²"),
            KeyboardButton(text="195 m²"),
        ],
        [
            KeyboardButton(text="200 m²"),
            KeyboardButton(text="250 m²"),
            KeyboardButton(text="300 m²"),
            KeyboardButton(text="350 m²"),
        ],
        [
            KeyboardButton(text="400 m²"),
            KeyboardButton(text="450 m²"),
            KeyboardButton(text="500 m²"),
            KeyboardButton(text="550 m²"),
        ],
        [
            KeyboardButton(text="600 m²"),
            KeyboardButton(text="650 m²"),
            KeyboardButton(text="700 m²"),
            KeyboardButton(text="750 m²"),
        ],
        [
            KeyboardButton(text="800 m²"),
            KeyboardButton(text="850 m²"),
            KeyboardButton(text="900 m²"),
            KeyboardButton(text="950 m²"),
        ],
        [
            KeyboardButton(text="1000 m²"),
            KeyboardButton(text="1500 m²"),
            KeyboardButton(text="2000 m²"),
            KeyboardButton(text="2500 m²"),
        ],
        [
            KeyboardButton(text="3000 m²"),
            KeyboardButton(text="3500 m²"),
            KeyboardButton(text="4000 m²"),
            KeyboardButton(text="4500 m²"),
        ],
        [
            KeyboardButton(text="5000 m²"),
            KeyboardButton(text="5500 m²"),
            KeyboardButton(text="6000 m²"),
            KeyboardButton(text="6500 m²"),
        ],
        [
            KeyboardButton(text="7000 m²"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

# Ta'mir turi menyusi
tamir_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yevro ta'mir"),
            KeyboardButton(text="Ta'mirsiz"),
        ],
        [
            KeyboardButton(text="O'rtacha ta'mir"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

# Narx menyusini yaratuvchi funksiya
def create_price_keyboard(start=10, end=20000, step=10, buttons_per_row=2):
    """
    Narxlar uchun klaviatura yaratish funksiyasi
    start: boshlang'ich narx
    end: oxirgi narx
    step: qadam
    buttons_per_row: bir qatordagi tugmalar soni
    """
    keyboard = []
    row = []

    for i in range(start, end + 1, step):
        row.append(KeyboardButton(text=f"{i} y.e"))

        if len(row) == buttons_per_row:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )

# Vosita haqi menyusi
vosita_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yo'q")
        ],
        [
            KeyboardButton(text="50 %"),
            KeyboardButton(text="40 %")
        ],
        [
            KeyboardButton(text="30 %"),
            KeyboardButton(text="25 %")
        ],
        [
            KeyboardButton(text="20 %"),
            KeyboardButton(text="15 %")
        ],
        [
            KeyboardButton(text="10 %"),
            KeyboardButton(text="5 %")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

# Uy hovli qavat menyusi
uy_hovli_qavat_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
        ],
        [
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
            KeyboardButton(text="6"),
        ],
        [
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9"),
        ],
        [
            KeyboardButton(text="10"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

# Telefon raqam yuborish tugmasi
number_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)
        ]
    ],
    resize_keyboard=True
)