from aiogram import Router, F, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from buttons import u_y_menu, humans_menu

router = Router()

tumanlar = [
    "Yakkasaroy", "Yashnobod", "Shayxontohur", "Chilonzor", 
    "Bektemir", "Olmazor", "Mirobod", "Mirzo Ulug'bek", 
    "Uchtepa", "Yunusobod", "Sergeli", "Yangihayot"
]

@router.message(F.text == "Uzoq muddatga")
async def uzoq_muddat_handler(message: types.Message):
    await message.answer(
        "Uzoq muddatga ijarani tanladingiz 🏠",
        reply_markup=u_y_menu
    )

@router.message(F.text.in_(tumanlar))
async def tuman_bosilganda(message: types.Message):
    await message.answer(
        text="Kimlarga ijaraga bermoqchisiz?\n\nTugmalardan birini tanlang 👇",
        reply_markup=humans_menu
    )