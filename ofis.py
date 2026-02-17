from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from buttons import user_menu, u_y_menu, xona_button, create_price_keyboard, house_menu, tamir_button, vosita_button, number_button
from state import OfisState

router = Router()

@router.message(F.text == "🏙 Ofis")
async def ofis_i(message: types.Message, state: FSMContext):
    await message.answer(
        """           
        Qaysi tumanda?
        Tugmalardan birini tanlang 👇                
        """,
        reply_markup=u_y_menu
    )
    await state.set_state(OfisState.ijara)

@router.message(OfisState.ijara)
async def ofis_muddati(message: types.Message, state: FSMContext):
    await state.update_data(ijara=message.text)
    await message.answer(
        "Maydoni necha kvadrat bo'lsin? (m²) Tugmalardan birini tanlang 👇",
        reply_markup=xona_button
    )
    await state.set_state(OfisState.xona)

@router.message(OfisState.xona)
async def ofis_xona(message: types.Message, state: FSMContext):
    await state.update_data(xona=message.text)
    await message.answer(
        "Ta'miri qanday? Tugmalardan birini tanlang 👇",
        reply_markup=tamir_button
    )
    await state.set_state(OfisState.tamir)

@router.message(OfisState.tamir)
async def ofis_tamir(message: types.Message, state: FSMContext):
    await state.update_data(tamir=message.text)
    await message.answer(
        "Ofis rasmini yuboring. 👇"
    )
    await state.set_state(OfisState.rasm)

@router.message(OfisState.rasm, F.photo)
async def ofis_rasm(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(rasm=photo_id)
    await message.answer(
        "Ijaraning narxini kiriting. 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(OfisState.narxi)

@router.message(OfisState.narxi)
async def ofis_narxi(message: types.Message, state: FSMContext):
    await state.update_data(narxi=message.text)
    await message.answer(
        "Vositachilik haqi bormi? Agar bo'lsa, necha foiz? Tugmalardan birini tanlang 👇",
        reply_markup=vosita_button
    )
    await state.set_state(OfisState.vosita_haqi)

@router.message(OfisState.vosita_haqi)
async def ofis_vosita_haqi(message: types.Message, state: FSMContext):
    await state.update_data(vosita_haqi=message.text)
    await message.answer(
        "Telefon raqamingizni yuboring:",
        reply_markup=number_button
    )
    await state.set_state(OfisState.number)

@router.message(OfisState.number, F.contact)
async def ofis_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    
    text = f"""
🏙 Ofis ijaraga berildi!

📍 Tuman: {data['ijara']}
📏 Maydon: {data['xona']}
🛠️ Ta'mir: {data['tamir']}
💵 Narxi: {data['narxi']}
🤝 Vosita haqi: {data['vosita_haqi']}
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