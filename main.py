import asyncio
import logging
import sqlite3
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from buttons import (
    user_menu, house_menu, k_v_menu, u_y_menu, humans_menu,
    xona_button, uy_hovli_sotix_button, sotix_button,
    uy_hovli_qavat_button, tamir_button, vosita_button,
    number_button, create_price_keyboard
)
from aiogram.client.session.aiohttp import AiohttpSession


PROXY_URL = 'http://proxy.server:3128'
session = AiohttpSession(proxy=PROXY_URL)
bot = Bot(token=TOKEN, session=session)

TOKEN = "7945234223:AAGyNAwRf1Rg8RTyQoxyrI5yV9DiUF_ovdA"

dp = Dispatcher()

# Ma'lumotlar bazasini yaratish
def init_database():
    conn = sqlite3.connect('ijara_bot.db')
    cursor = conn.cursor()
    
    # Foydalanuvchilar jadvali
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            phone TEXT,
            registered_date TEXT
        )
    ''')
    
    # E'lonlar jadvali
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ads (
            ad_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            ad_type TEXT,
            tuman TEXT,
            muddat TEXT,
            kimga TEXT,
            xona TEXT,
            maydon TEXT,
            tamir TEXT,
            narx TEXT,
            vosita TEXT,
            telefon TEXT,
            photo_id TEXT,
            status TEXT DEFAULT 'active',
            created_date TEXT,
            views_count INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Ma'lumotlar bazasi yaratildi")

# Holatlar
class AdState(StatesGroup):
    waiting_for_action = State()
    editing_ad = State()
    editing_field = State()

@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    
    # Foydalanuvchini bazaga qo'shish
    conn = sqlite3.connect('ijara_bot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR IGNORE INTO users (user_id, username, first_name, last_name, registered_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, username, first_name, last_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    
    conn.commit()
    conn.close()
    
    await message.answer(
        f"👋 Xush kelibsiz, {first_name}!\n\n"
        f"Ijara bot orqali siz uy-joylarni ijaraga berishingiz va olishingiz mumkin.\n\n"
        f"Kerakli bo‘limni tanlang 👇",
        reply_markup=user_menu
    )

@dp.message(F.text == "🔑 Ijaraga beraman")
async def rent_out(message: types.Message):
    await message.answer(
        "🏠 Qanday turdagi binoni ijaraga berasiz?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=house_menu
    )

@dp.message(F.text == "🔎 Ijaraga olaman")
async def rent_in(message: types.Message):
    await message.answer(
        "🔎 Qanday turdagi uy-joy qidiryapsiz?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=house_menu
    )

@dp.message(F.text == "🌐 Tilni o‘zgartirish")
async def change_language(message: types.Message):
    await message.answer(
        "🌐 Til o'zgartirish\n\n"
        "✅ O'zbek tili\n"
        "⏳ Русский язык (tez kunda)\n"
        "⏳ English (coming soon)",
        reply_markup=user_menu
    )

@dp.message(F.text == "❓ Qanday ishlaydi")
async def qanday_ishlaydi(message: types.Message):
    await message.answer("""
📋 **IJARACHI BOT ISHLASH TARTIBI**

**🏠 Ijaraga berish:**
1. "🔑 Ijaraga beraman" tugmasini bosing
2. Uy turini tanlang
3. Barcha ma'lumotlarni kiriting
4. Rasm va telefon raqam yuboring
5. E'lon avtomatik joylanadi

**🔎 Ijaraga olish:**
1. "🔎 Ijaraga olaman" tugmasini bosing
2. Uy turini tanlang
3. Filtrlarni o'rnating
4. Mos e'lonlarni ko'ring

**📋 E'lonlarim:**
Barcha e'lonlaringizni ko'rish va boshqarish

✏️ Taklif va murojaatlar: @TDD_199
    """, parse_mode="Markdown")

@dp.message(F.text == "📋 E'lonlarim")
async def my_ads(message: types.Message):
    """Mening e'lonlarim - rasm bilan"""
    user_id = message.from_user.id
    
    # Bazadan foydalanuvchi e'lonlarini olish
    conn = sqlite3.connect('ijara_bot.db')
    cursor = conn.cursor()
    
    # TO'G'RILANGAN SQL SO'ROVI - bir qatorda
    cursor.execute("SELECT ad_id, ad_type, tuman, narx, status, photo_id, created_date, muddat, kimga, xona, maydon, tamir, vosita, telefon FROM ads WHERE user_id = ? ORDER BY created_date DESC", (user_id,))
    
    ads = cursor.fetchall()
    conn.close()
    
    if not ads:
        # E'lonlar bo'lmasa
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="➕ Yangi e'lon qo'shish", callback_data="new_ad")]
            ]
        )
        
        await message.answer(
            "📋 **SIZNING E'LONLARINGIZ**\n\n"
            "Sizda hali e'lonlar yo'q.\n"
            "Yangi e'lon qo'shish uchun pastdagi tugmani bosing 👇",
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
        return
    
    # E'lonlar bor bo'lsa
    await message.answer(
        f"📋 **SIZNING E'LONLARINGIZ**\n\n"
        f"Jami: {len(ads)} ta e'lon\n"
        f"────────────────",
        parse_mode="Markdown"
    )
    
    for i, ad in enumerate(ads, 1):
        ad_id, ad_type, tuman, narx, status, photo_id, created_date, muddat, kimga, xona, maydon, tamir, vosita, telefon = ad
        
        # Statusga qarab belgi
        status_icon = "✅" if status == "active" else "⏳"
        status_text = "Faol" if status == "active" else "Kutishda"
        
        # E'lon matni
        ad_text = f"""
{status_icon} **E'LON #{i}**
────────────────
🏠 **Tur:** {ad_type}
📍 **Tuman:** {tuman}
💰 **Narx:** {narx}
📊 **Holat:** {status_text}
📅 **Sana:** {created_date[:10] if created_date else '—'}
────────────────
📝 **Ma'lumotlar:**
• Muddat: {muddat or '—'}
• Kimga: {kimga or '—'}
• Xona: {xona or '—'}
• Maydon: {maydon or '—'}
• Ta'mir: {tamir or '—'}
• Vosita: {vosita or '—'}
• Tel: {telefon or '—'}
        """
        
        # Inline tugmalar
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="👁 Ko'rish", callback_data=f"view_{ad_id}"),
                    InlineKeyboardButton(text="✏️ Tahrirlash", callback_data=f"edit_{ad_id}"),
                    InlineKeyboardButton(text="🗑 O'chirish", callback_data=f"delete_{ad_id}")
                ]
            ]
        )
        
        # Agar rasm bo'lsa, rasm bilan yuborish
        if photo_id and photo_id != "None" and photo_id != "" and photo_id is not None:
            try:
                await message.answer_photo(
                    photo=photo_id,
                    caption=ad_text,
                    reply_markup=keyboard,
                    parse_mode="Markdown"
                )
            except Exception as e:
                print(f"Rasm yuborishda xato: {e}")
                await message.answer(
                    ad_text + "\n🖼 (Rasm yuklanmadi)",
                    reply_markup=keyboard,
                    parse_mode="Markdown"
                )
        else:
            await message.answer(
                ad_text,
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
    
    # Umumiy tugmalar
    general_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➕ Yangi e'lon qo'shish", callback_data="new_ad")],
            [InlineKeyboardButton(text="🔄 Yangilash", callback_data="refresh_ads")]
        ]
    )
    
    # Faol e'lonlar sonini hisoblash
    active_count = 0
    for ad in ads:
        if ad[4] == 'active':
            active_count += 1
    
    await message.answer(
        f"📊 **Jami:** {len(ads)} ta e'lon\n"
        f"✅ Faol: {active_count} ta\n"
        f"⏳ Kutishda: {len(ads) - active_count} ta",
        reply_markup=general_keyboard,
        parse_mode="Markdown"
    )

@dp.message(F.text == "🏠 Bosh sahifa")
async def home_page(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "🏠 Bosh sahifaga qaytildi.",
        reply_markup=user_menu
    )

# Callback handlerlar
@dp.callback_query()
async def process_callback(callback_query: types.CallbackQuery, state: FSMContext):
    action = callback_query.data
    user_id = callback_query.from_user.id
    
    if action == "new_ad":
        await callback_query.message.answer(
            "➕ Yangi e'lon qo'shish uchun 'Ijaraga beraman' tugmasini bosing 👇",
            reply_markup=house_menu
        )
        await callback_query.answer()
        
    elif action.startswith("view_"):
        ad_id = action.replace("view_", "")
        await show_ad_details(callback_query.message, ad_id, user_id)
        await callback_query.answer()
        
    elif action.startswith("edit_"):
        ad_id = action.replace("edit_", "")
        await edit_ad_menu(callback_query.message, ad_id, state)
        await callback_query.answer()
        
    elif action.startswith("delete_"):
        ad_id = action.replace("delete_", "")
        
        # Confirm delete
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="✅ Ha, o'chir", callback_data=f"confirm_delete_{ad_id}"),
                    InlineKeyboardButton(text="❌ Yo'q", callback_data="cancel_delete")
                ]
            ]
        )
        
        await callback_query.message.answer(
            f"⚠️ **Diqqat!**\n\nBu e'lonni o'chirishni tasdiqlaysizmi?",
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
        await callback_query.answer()
        
    elif action.startswith("confirm_delete_"):
        ad_id = action.replace("confirm_delete_", "")
        
        # E'lonni o'chirish
        conn = sqlite3.connect('ijara_bot.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ads WHERE ad_id = ? AND user_id = ?", (ad_id, user_id))
        conn.commit()
        conn.close()
        
        await callback_query.message.answer(
            "✅ **E'lon muvaffaqiyatli o'chirildi!**",
            parse_mode="Markdown"
        )
        
        # E'lonlar ro'yxatini yangilash
        await my_ads(callback_query.message)
        await callback_query.answer()
        
    elif action == "cancel_delete":
        await callback_query.message.answer(
            "❌ O'chirish bekor qilindi"
        )
        await callback_query.answer()
        
    elif action == "refresh_ads":
        await callback_query.message.answer(
            "🔄 E'lonlar yangilanmoqda..."
        )
        await my_ads(callback_query.message)
        await callback_query.answer()

async def show_ad_details(message: types.Message, ad_id: str, user_id: int):
    """E'lon tafsilotlarini ko'rsatish"""
    conn = sqlite3.connect('ijara_bot.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT ad_type, tuman, muddat, kimga, xona, maydon, tamir, narx, vosita, telefon, photo_id, status, created_date FROM ads WHERE ad_id = ? AND user_id = ?", (ad_id, user_id))
    
    ad = cursor.fetchone()
    
    if ad:
        # Ko'rishlar sonini yangilash
        cursor.execute("UPDATE ads SET views_count = views_count + 1 WHERE ad_id = ?", (ad_id,))
        conn.commit()
    
    conn.close()
    
    if not ad:
        await message.answer("❌ E'lon topilmadi")
        return
    
    ad_type, tuman, muddat, kimga, xona, maydon, tamir, narx, vosita, telefon, photo_id, status, created_date = ad
    
    status_text = "✅ Faol" if status == "active" else "⏳ Kutishda"
    
    detail_text = f"""
📋 **E'LON TAFSILOTLARI**
────────────────
🏠 **Tur:** {ad_type}
📍 **Tuman:** {tuman}
💰 **Narx:** {narx}
📊 **Holat:** {status_text}
📅 **Qo'shilgan:** {created_date[:10] if created_date else '—'}
────────────────
📝 **BATAFSIL MA'LUMOTLAR:**
• 📅 Muddat: {muddat or '—'}
• 👥 Kimga: {kimga or '—'}
• 🚪 Xona: {xona or '—'}
• 📐 Maydon: {maydon or '—'}
• 🛠️ Ta'mir: {tamir or '—'}
• 🤝 Vosita: {vosita or '—'}
• 📞 Tel: {telefon or '—'}
────────────────
    """
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✏️ Tahrirlash", callback_data=f"edit_{ad_id}")],
            [InlineKeyboardButton(text="🗑 O'chirish", callback_data=f"delete_{ad_id}")],
            [InlineKeyboardButton(text="◀️ Orqaga", callback_data="refresh_ads")]
        ]
    )
    
    if photo_id and photo_id != "None" and photo_id != "" and photo_id is not None:
        try:
            await message.answer_photo(
                photo=photo_id,
                caption=detail_text,
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
        except:
            await message.answer(
                detail_text + "\n🖼 (Rasm yuklanmadi)",
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
    else:
        await message.answer(
            detail_text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

async def edit_ad_menu(message: types.Message, ad_id: str, state: FSMContext):
    """E'lonni tahrirlash menyusi"""
    await state.update_data(current_ad_id=ad_id)
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💰 Narx", callback_data="edit_field_narx")],
            [InlineKeyboardButton(text="📍 Tuman", callback_data="edit_field_tuman")],
            [InlineKeyboardButton(text="📅 Muddat", callback_data="edit_field_muddat")],
            [InlineKeyboardButton(text="👥 Kimga", callback_data="edit_field_kimga")],
            [InlineKeyboardButton(text="🚪 Xona", callback_data="edit_field_xona")],
            [InlineKeyboardButton(text="📐 Maydon", callback_data="edit_field_maydon")],
            [InlineKeyboardButton(text="🛠️ Ta'mir", callback_data="edit_field_tamir")],
            [InlineKeyboardButton(text="🤝 Vosita", callback_data="edit_field_vosita")],
            [InlineKeyboardButton(text="📞 Telefon", callback_data="edit_field_telefon")],
            [InlineKeyboardButton(text="◀️ Orqaga", callback_data="refresh_ads")]
        ]
    )
    
    await message.answer(
        "✏️ **Nimani o'zgartirmoqchisiz?**\n\n"
        "Kerakli bo'limni tanlang:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.callback_query(lambda c: c.data and c.data.startswith("edit_field_"))
async def edit_field_callback(callback_query: types.CallbackQuery, state: FSMContext):
    field = callback_query.data.replace("edit_field_", "")
    data = await state.get_data()
    ad_id = data.get('current_ad_id')
    
    await state.update_data(editing_field=field, editing_ad_id=ad_id)
    
    field_names = {
        'narx': '💰 Yangi narxni kiriting:',
        'tuman': '📍 Yangi tumanni kiriting:',
        'muddat': '📅 Yangi muddatni kiriting:',
        'kimga': '👥 Yangi ma\'lumotni kiriting:',
        'xona': '🚪 Yangi xona sonini kiriting:',
        'maydon': '📐 Yangi maydonni kiriting:',
        'tamir': '🛠️ Yangi ta\'mir ma\'lumotini kiriting:',
        'vosita': '🤝 Yangi vosita haqini kiriting:',
        'telefon': '📞 Yangi telefon raqamini kiriting:'
    }
    
    await callback_query.message.answer(
        field_names.get(field, "✏️ Yangi ma'lumotni kiriting:"),
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(AdState.editing_field)
    await callback_query.answer()

@dp.message(AdState.editing_field)
async def process_field_edit(message: types.Message, state: FSMContext):
    """Maydonni tahrirlash"""
    data = await state.get_data()
    field = data.get('editing_field')
    ad_id = data.get('editing_ad_id')
    user_id = message.from_user.id
    
    new_value = message.text
    
    # Bazani yangilash
    conn = sqlite3.connect('ijara_bot.db')
    cursor = conn.cursor()
    
    field_map = {
        'narx': 'narx',
        'tuman': 'tuman',
        'muddat': 'muddat',
        'kimga': 'kimga',
        'xona': 'xona',
        'maydon': 'maydon',
        'tamir': 'tamir',
        'vosita': 'vosita',
        'telefon': 'telefon'
    }
    
    if field in field_map:
        cursor.execute(f"UPDATE ads SET {field_map[field]} = ? WHERE ad_id = ? AND user_id = ?", 
                      (new_value, ad_id, user_id))
        conn.commit()
        
        await message.answer(
            f"✅ **Ma'lumot muvaffaqiyatli yangilandi!**",
            parse_mode="Markdown"
        )
    
    conn.close()
    await state.clear()
    
    # Yangilangan e'lonni ko'rsatish
    await show_ad_details(message, ad_id, user_id)

# E'lonni saqlash funksiyasi (boshqa fayllardan chaqirish uchun)
async def save_ad_to_db(user_id, ad_type, data_dict, photo_id):
    """E'lonni bazaga saqlash"""
    conn = sqlite3.connect('ijara_bot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO ads (
            user_id, ad_type, tuman, muddat, kimga, xona, maydon, 
            tamir, narx, vosita, telefon, photo_id, status, created_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        user_id, 
        ad_type,
        data_dict.get('tuman', ''),
        data_dict.get('muddat', ''),
        data_dict.get('kimga', ''),
        data_dict.get('xona', ''),
        data_dict.get('maydon', ''),
        data_dict.get('tamir', ''),
        data_dict.get('narx', ''),
        data_dict.get('vosita', ''),
        data_dict.get('telefon', ''),
        photo_id,
        'active',
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    
    ad_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return ad_id

async def main() -> None:
    # Ma'lumotlar bazasini ishga tushirish
    init_database()
    
    bot = Bot(token=TOKEN)
    
    # Import qilingan routerlarni ulash
    try:
        from kvartira import router as kvartira_router
        from Uyhovli import router as uy_hovli_router
        from dacha import router as dacha_router
        from ofis import router as ofis_router
        from handler import router as handler_router
        from ijaragaolaman import router as ijaraga_olaman_router
        
        dp.include_router(kvartira_router)
        dp.include_router(uy_hovli_router)
        dp.include_router(dacha_router)
        dp.include_router(ofis_router)
        dp.include_router(handler_router)
        dp.include_router(ijaraga_olaman_router)
    except Exception as e:
        print(f"Routerlarni ulashda xato: {e}")
    
    print("🤖 Bot ishga tushdi!")
    print("📋 E'lonlarim bo'limi faol")
    print("🖼 Rasm bilan ishlash yoqilgan")
    print("💾 Ma'lumotlar bazasi: ijara_bot.db")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main()) 