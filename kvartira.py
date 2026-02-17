from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from buttons import user_menu, k_v_menu, u_y_menu, humans_menu, xona_button, sotix_button, house_menu, tamir_button, create_price_keyboard, vosita_button, number_button
from state import KvartiraState

router = Router()

@router.message(F.text == "🏠 Kvartira")
async def kvartira_i(message: types.Message, state: FSMContext):
    await message.answer(
        """
        Qancha muddatga ijaraga berasiz?
        Tugmalardan birini tanlang 👇                
        """,
        reply_markup=k_v_menu
    )
    await state.set_state(KvartiraState.muddati)

@router.message(KvartiraState.muddati)
async def kvartira_muddati(message: types.Message, state: FSMContext):
    await state.update_data(muddati=message.text)
    await message.answer(
        "Qaysi tumanlarda kvartira ijaraga berasiz? 👇",
        reply_markup=u_y_menu
    )
    await state.set_state(KvartiraState.tuman)

@router.message(KvartiraState.tuman)
async def kvartira_tuman(message: types.Message, state: FSMContext):
    await state.update_data(tuman=message.text)
    await message.answer(
        "Kimga ijaraga berasiz? 👇",
        reply_markup=humans_menu
    )
    await state.set_state(KvartiraState.kimga)

@router.message(KvartiraState.kimga)
async def kvartira_kimga(message: types.Message, state: FSMContext):
    await state.update_data(kimga=message.text)
    await message.answer(
        "Nechta xona? 👇",
        reply_markup=xona_button
    )
    await state.set_state(KvartiraState.xona)

@router.message(KvartiraState.xona)
async def kvartira_xona(message: types.Message, state: FSMContext):
    await state.update_data(xona=message.text)
    await message.answer(
        "Nechta sotix? 👇",
        reply_markup=sotix_button
    )
    await state.set_state(KvartiraState.sotix)

@router.message(KvartiraState.sotix)
async def kvartira_sotix(message: types.Message, state: FSMContext):
    await state.update_data(sotix=message.text)
    await message.answer(
        "Qanday ta’mirda? 👇",
        reply_markup=tamir_button
    )
    await state.set_state(KvartiraState.tamir)

@router.message(KvartiraState.tamir)
async def kvartira_tamir(message: types.Message, state: FSMContext):
    await state.update_data(tamir=message.text)
    await message.answer(
        "Kvartira rasmini yuboring. 👇",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(KvartiraState.rasm)

@router.message(KvartiraState.rasm, F.photo)
async def kvartira_rasm(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(rasm=photo_id)
    await message.answer(
        "Kvartira narxini kiriting. 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(KvartiraState.narxi)

@router.message(KvartiraState.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    await state.update_data(narxi=message.text)
    await message.answer(
        "Vosita haqini kiriting. 👇",
        reply_markup=vosita_button
    )
    await state.set_state(KvartiraState.vosita_haqi)

@router.message(KvartiraState.vosita_haqi)
async def kvartira_vh(message: types.Message, state: FSMContext):
    await state.update_data(vosita_haqi=message.text)
    await message.answer(
        "Telefon raqamingizni yuboring:",
        reply_markup=number_button
    )
    await state.set_state(KvartiraState.number)

@router.message(KvartiraState.number, F.contact)
async def kvartira_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    
    text = f"""
🏠 Kvartira ijaraga berildi!

📅 Muddati: {data['muddati']}
📍 Tuman: {data['tuman']}
👥 Kimga: {data['kimga']}
🚪 Xona: {data['xona']}
📐 Maydon: {data['sotix']}
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

@router.message(KvartiraState.number)
async def kvartira_number_invalid(message: types.Message, state: FSMContext):
    await message.answer(
        "Iltimos, pastdagi tugma orqali telefon raqamingizni yuboring 📱",
        reply_markup=number_button
    )

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