from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from buttons import house_menu, u_y_menu, k_v_menu, uy_hovli_sotix_button, sotix_button, uy_hovli_qavat_button, tamir_button, create_price_keyboard, vosita_button, user_menu, number_button
from state import UyHovliState

router = Router()

@router.message(F.text == "🏡 Uy Hovli")
async def uyhovli_i(message: types.Message, state: FSMContext):
    await message.answer(
        """
        Qancha muddatga ijaraga berasiz?
        Tugmalardan birini tanlang 👇                
        """,
        reply_markup=k_v_menu
    )
    await state.set_state(UyHovliState.ijara)

@router.message(UyHovliState.ijara)
async def uyhovli_muddati(message: types.Message, state: FSMContext):
    await state.update_data(ijara=message.text)
    await message.answer(
        "Nechta sotix? 👇",
        reply_markup=uy_hovli_sotix_button
    )
    await state.set_state(UyHovliState.sotix)

@router.message(UyHovliState.sotix)
async def uyhovli_sotix(message: types.Message, state: FSMContext):
    await state.update_data(sotix=message.text)
    await message.answer(
        "Kvadrat metrini kiriting. 👇",
        reply_markup=sotix_button
    )
    await state.set_state(UyHovliState.kvadrat)

@router.message(UyHovliState.kvadrat)
async def uyhovli_kvadrat(message: types.Message, state: FSMContext):
    await state.update_data(kvadrat=message.text)
    await message.answer(
        "Nechta xona? 👇",
        reply_markup=u_y_menu
    )
    await state.set_state(UyHovliState.xona)

@router.message(UyHovliState.xona)
async def uyhovli_xona(message: types.Message, state: FSMContext):
    await state.update_data(xona=message.text)
    await message.answer(
        "Nechchi qavat? 👇",
        reply_markup=uy_hovli_qavat_button
    )
    await state.set_state(UyHovliState.qavat)

@router.message(UyHovliState.qavat)
async def uyhovli_qavat(message: types.Message, state: FSMContext):
    await state.update_data(qavat=message.text)
    await message.answer(
        "Qanday ta’mirda? 👇",
        reply_markup=tamir_button
    )
    await state.set_state(UyHovliState.tamir)

@router.message(UyHovliState.tamir)
async def uyhovli_tamir(message: types.Message, state: FSMContext):
    await state.update_data(tamir=message.text)
    await message.answer(
        "Uy hovli rasmini yuboring. 👇"
    )
    await state.set_state(UyHovliState.rasm)

@router.message(UyHovliState.rasm, F.photo)
async def uyhovli_rasm(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(rasm=photo_id)
    await message.answer(
        "Ijaraning narxini kiriting. 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(UyHovliState.narxi)

@router.message(UyHovliState.narxi)
async def uyhovli_narxi(message: types.Message, state: FSMContext):
    await state.update_data(narxi=message.text)
    await message.answer(
        "Vosita haqini kiriting. 👇",
        reply_markup=vosita_button
    )
    await state.set_state(UyHovliState.vosita_haqi)

@router.message(UyHovliState.vosita_haqi)
async def uyhovli_vosita(message: types.Message, state: FSMContext):
    await state.update_data(vosita_haqi=message.text)
    await message.answer(
        "Telefon raqamingizni yuboring:",
        reply_markup=number_button
    )
    await state.set_state(UyHovliState.number)

@router.message(UyHovliState.number, F.contact)
async def uyhovli_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    
    text = f"""
🏡 Uy Hovli ijaraga berildi!

📅 Muddat: {data['ijara']}
📐 Sotix: {data['sotix']}
📏 Kvadrat: {data['kvadrat']}
🚪 Xona: {data['xona']}
🏢 Qavat: {data['qavat']}
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