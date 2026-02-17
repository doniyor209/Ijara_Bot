from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from buttons import user_menu, u_y_menu, xona_button, create_price_keyboard, house_menu, number_button
from state import DachaState

router = Router()

@router.message(F.text == "🏘 Dacha")
async def dacha_i(message: types.Message, state: FSMContext):
    await message.answer(
        """
        Qaysi tumanda?
        Tugmalardan birini tanlang 👇                
        """,
        reply_markup=u_y_menu
    )
    await state.set_state(DachaState.ijara)

@router.message(DachaState.ijara)
async def dacha_muddati(message: types.Message, state: FSMContext):
    await state.update_data(ijara=message.text)
    await message.answer(
        "Yotoqxonalar soni nechta? Tugmalardan birini tanlang 👇",
        reply_markup=xona_button
    )
    await state.set_state(DachaState.xona)

@router.message(DachaState.xona)
async def dacha_xona(message: types.Message, state: FSMContext):
    await state.update_data(xona=message.text)
    await message.answer(
        "Ijaraning narxini kiriting. 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(DachaState.narxi)

@router.message(DachaState.narxi)
async def dacha_narxi(message: types.Message, state: FSMContext):
    await state.update_data(narxi=message.text)
    await message.answer(
        "Dam olish kunlari narxi qancha? Tugmalardan birini tanlang👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(DachaState.dam_narxi)

@router.message(DachaState.dam_narxi)
async def dacha_dam_narxi(message: types.Message, state: FSMContext):
    await state.update_data(dam_narxi=message.text)
    await message.answer(
        "Dacha rasmini yuboring. 👇"
    )
    await state.set_state(DachaState.rasm)

@router.message(DachaState.rasm, F.photo)
async def dacha_rasm(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(rasm=photo_id)
    await message.answer(
        "Telefon raqamingizni yuboring:",
        reply_markup=number_button
    )
    await state.set_state(DachaState.number)

@router.message(DachaState.number, F.contact)
async def dacha_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    
    text = f"""
🏘 Dacha ijaraga berildi!

📍 Tuman: {data['ijara']}
🚪 Xona: {data['xona']}
💵 Narxi: {data['narxi']}
🏖 Dam olish narxi: {data['dam_narxi']}
📞 Tel: {data['number']}
    """
    
    await message.answer_photo(
        photo=data['rasm'],
        caption=text,
        reply_markup=user_menu
    )
    await state.clear()

@router.message(F.text == "⬅️ Orqaga")
async def orqaga(message: types.Message, state: FSMContext):
    await message.answer(
        "Oldingi bo‘limga qaytildi. Kerakli bo‘limni tanlang. 👇",
        reply_markup=house_menu
    )
    await state.clear()

@router.message(F.text == "🏠 Bosh sahifa")
async def bosh_sahifa(message: types.Message, state: FSMContext):
    await message.answer(
        "Bosh sahifaga qaytildi. Kerakli bo‘limni tanlang. 👇",
        reply_markup=user_menu
    )
    await state.clear()