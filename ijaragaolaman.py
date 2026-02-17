from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from buttons import (
    user_menu, house_menu, k_v_menu, u_y_menu, humans_menu,
    xona_button, sotix_button, tamir_button, vosita_button,
    create_price_keyboard
)

router = Router()

# Holatlar (States)
class IjaragaOlamanState(StatesGroup):
    # Umumiy holatlar
    uy_turi = State()      # Uy turi
    muddat = State()       # Ijara muddati
    tuman = State()        # Tuman
    kimdan = State()       # Kimdan
    
    # Kvartira uchun filtrlar
    kvartira_xona = State()
    kvartira_sotix = State()
    kvartira_tamir = State()
    kvartira_narx_min = State()
    kvartira_narx_max = State()
    
    # Uy hovli uchun filtrlar
    uy_hovli_sotix = State()
    uy_hovli_kvadrat = State()
    uy_hovli_xona = State()
    uy_hovli_qavat = State()
    uy_hovli_tamir = State()
    uy_hovli_narx_min = State()
    uy_hovli_narx_max = State()
    
    # Dacha uchun filtrlar
    dacha_xona = State()
    dacha_narx_min = State()
    dacha_narx_max = State()
    
    # Ofis uchun filtrlar
    ofis_maydon = State()
    ofis_tamir = State()
    ofis_narx_min = State()
    ofis_narx_max = State()

@router.message(F.text == "🔎 Ijaraga olaman")
async def ijaraga_olaman_start(message: types.Message, state: FSMContext):
    """Ijara olish jarayonini boshlash"""
    await message.answer(
        "🏠 Qanday turdagi uy-joy qidiryapsiz?\n\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=house_menu
    )
    await state.set_state(IjaragaOlamanState.uy_turi)

@router.message(IjaragaOlamanState.uy_turi)
async def uy_turi_handler(message: types.Message, state: FSMContext):
    """Uy turini tanlash"""
    uy_turi = message.text
    
    # Uy turini saqlash
    await state.update_data(uy_turi=uy_turi)
    
    if uy_turi == "🏠 Kvartira":
        await message.answer(
            "📅 Qancha muddatga ijaraga olmoqchisiz?\n"
            "Tugmalardan birini tanlang 👇",
            reply_markup=k_v_menu
        )
        await state.set_state(IjaragaOlamanState.muddat)
        
    elif uy_turi == "🏡 Uy Hovli":
        await message.answer(
            "📅 Qancha muddatga ijaraga olmoqchisiz?\n"
            "Tugmalardan birini tanlang 👇",
            reply_markup=k_v_menu
        )
        await state.set_state(IjaragaOlamanState.muddat)
        
    elif uy_turi == "🏘 Dacha":
        await message.answer(
            "📍 Qaysi tumanda?\n"
            "Tugmalardan birini tanlang 👇",
            reply_markup=u_y_menu
        )
        await state.set_state(IjaragaOlamanState.tuman)
        
    elif uy_turi == "🏙 Ofis":
        await message.answer(
            "📍 Qaysi tumanda?\n"
            "Tugmalardan birini tanlang 👇",
            reply_markup=u_y_menu
        )
        await state.set_state(IjaragaOlamanState.tuman)
    
    elif uy_turi == "🏠 Bosh sahifa":
        await message.answer(
            "Bosh sahifaga qaytildi. Kerakli bo‘limni tanlang. 👇",
            reply_markup=user_menu
        )
        await state.clear()

@router.message(IjaragaOlamanState.muddat)
async def muddat_handler(message: types.Message, state: FSMContext):
    """Ijara muddatini saqlash"""
    await state.update_data(muddat=message.text)
    
    data = await state.get_data()
    uy_turi = data.get('uy_turi')
    
    await message.answer(
        "📍 Qaysi tumanda?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=u_y_menu
    )
    await state.set_state(IjaragaOlamanState.tuman)

@router.message(IjaragaOlamanState.tuman)
async def tuman_handler(message: types.Message, state: FSMContext):
    """Tumanni saqlash"""
    await state.update_data(tuman=message.text)
    
    data = await state.get_data()
    uy_turi = data.get('uy_turi')
    
    await message.answer(
        "👥 Kimdan ijaraga olmoqchisiz?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=humans_menu
    )
    await state.set_state(IjaragaOlamanState.kimdan)

@router.message(IjaragaOlamanState.kimdan)
async def kimdan_handler(message: types.Message, state: FSMContext):
    """Kimdan ijaraga olishini saqlash"""
    await state.update_data(kimdan=message.text)
    
    data = await state.get_data()
    uy_turi = data.get('uy_turi')
    
    # Uy turiga qarab turli holatlarga o'tish
    if uy_turi == "🏠 Kvartira":
        await message.answer(
            "🚪 Nechta xona kerak?\n"
            "Tugmalardan birini tanlang 👇",
            reply_markup=xona_button
        )
        await state.set_state(IjaragaOlamanState.kvartira_xona)
        
    elif uy_turi == "🏡 Uy Hovli":
        await message.answer(
            "📐 Necha sotix kerak?\n"
            "Tugmalardan birini tanlang 👇",
            reply_markup=xona_button  # Sotix uchun alohida button kerak
        )
        await state.set_state(IjaragaOlamanState.uy_hovli_sotix)
        
    elif uy_turi == "🏘 Dacha":
        await message.answer(
            "🚪 Yotoqxonalar soni nechta bo'lsin?\n"
            "Tugmalardan birini tanlang 👇",
            reply_markup=xona_button
        )
        await state.set_state(IjaragaOlamanState.dacha_xona)
        
    elif uy_turi == "🏙 Ofis":
        await message.answer(
            "📏 Maydoni necha kvadrat bo'lsin?\n"
            "Tugmalardan birini tanlang 👇",
            reply_markup=sotix_button
        )
        await state.set_state(IjaragaOlamanState.ofis_maydon)

# ==================== KVARTIRA FILTRLARI ====================

@router.message(IjaragaOlamanState.kvartira_xona)
async def kvartira_xona_handler(message: types.Message, state: FSMContext):
    """Kvartira xonalar soni"""
    await state.update_data(kvartira_xona=message.text)
    await message.answer(
        "📐 Necha sotix bo'lsin?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=sotix_button
    )
    await state.set_state(IjaragaOlamanState.kvartira_sotix)

@router.message(IjaragaOlamanState.kvartira_sotix)
async def kvartira_sotix_handler(message: types.Message, state: FSMContext):
    """Kvartira maydoni"""
    await state.update_data(kvartira_sotix=message.text)
    await message.answer(
        "🛠️ Qanday ta'mirda bo'lsin?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=tamir_button
    )
    await state.set_state(IjaragaOlamanState.kvartira_tamir)

@router.message(IjaragaOlamanState.kvartira_tamir)
async def kvartira_tamir_handler(message: types.Message, state: FSMContext):
    """Kvartira ta'miri"""
    await state.update_data(kvartira_tamir=message.text)
    await message.answer(
        "💵 Minimal narxni kiriting 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(IjaragaOlamanState.kvartira_narx_min)

@router.message(IjaragaOlamanState.kvartira_narx_min)
async def kvartira_narx_min_handler(message: types.Message, state: FSMContext):
    """Kvartira minimal narxi"""
    await state.update_data(kvartira_narx_min=message.text)
    await message.answer(
        "💵 Maksimal narxni kiriting 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(IjaragaOlamanState.kvartira_narx_max)

@router.message(IjaragaOlamanState.kvartira_narx_max)
async def kvartira_narx_max_handler(message: types.Message, state: FSMContext):
    """Kvartira maksimal narxi - natijalarni ko'rsatish"""
    await state.update_data(kvartira_narx_max=message.text)
    
    data = await state.get_data()
    
    # Bu yerda ma'lumotlar bazasidan kvartiralarni qidirish kerak
    # Hozircha namuna sifatida xabar chiqaramiz
    
    text = f"""
🔍 QIDIRUV NATIJALARI (KVARTIRA)

📅 Muddat: {data.get('muddat', '—')}
📍 Tuman: {data.get('tuman', '—')}
👥 Kimdan: {data.get('kimdan', '—')}
🚪 Xona: {data.get('kvartira_xona', '—')}
📐 Maydon: {data.get('kvartira_sotix', '—')}
🛠️ Ta'mir: {data.get('kvartira_tamir', '—')}
💵 Narx: {data.get('kvartira_narx_min', '—')} - {data.get('kvartira_narx_max', '—')}

Sizning so'rovingiz bo'yicha e'lonlar topilmadi.
Tez orada yangi e'lonlar qo'shiladi!
    """
    
    await message.answer(
        text,
        reply_markup=user_menu
    )
    await state.clear()

# ==================== UY HOVLI FILTRLARI ====================

@router.message(IjaragaOlamanState.uy_hovli_sotix)
async def uy_hovli_sotix_handler(message: types.Message, state: FSMContext):
    """Uy hovli sotix"""
    await state.update_data(uy_hovli_sotix=message.text)
    await message.answer(
        "📏 Kvadrat metri necha bo'lsin?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=sotix_button
    )
    await state.set_state(IjaragaOlamanState.uy_hovli_kvadrat)

@router.message(IjaragaOlamanState.uy_hovli_kvadrat)
async def uy_hovli_kvadrat_handler(message: types.Message, state: FSMContext):
    """Uy hovli kvadrati"""
    await state.update_data(uy_hovli_kvadrat=message.text)
    await message.answer(
        "🚪 Nechta xona bo'lsin?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=xona_button
    )
    await state.set_state(IjaragaOlamanState.uy_hovli_xona)

@router.message(IjaragaOlamanState.uy_hovli_xona)
async def uy_hovli_xona_handler(message: types.Message, state: FSMContext):
    """Uy hovli xonalar soni"""
    await state.update_data(uy_hovli_xona=message.text)
    await message.answer(
        "🏢 Necha qavat bo'lsin?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=xona_button  # Qavat uchun alohida button kerak
    )
    await state.set_state(IjaragaOlamanState.uy_hovli_qavat)

@router.message(IjaragaOlamanState.uy_hovli_qavat)
async def uy_hovli_qavat_handler(message: types.Message, state: FSMContext):
    """Uy hovli qavati"""
    await state.update_data(uy_hovli_qavat=message.text)
    await message.answer(
        "🛠️ Qanday ta'mirda bo'lsin?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=tamir_button
    )
    await state.set_state(IjaragaOlamanState.uy_hovli_tamir)

@router.message(IjaragaOlamanState.uy_hovli_tamir)
async def uy_hovli_tamir_handler(message: types.Message, state: FSMContext):
    """Uy hovli ta'miri"""
    await state.update_data(uy_hovli_tamir=message.text)
    await message.answer(
        "💵 Minimal narxni kiriting 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(IjaragaOlamanState.uy_hovli_narx_min)

@router.message(IjaragaOlamanState.uy_hovli_narx_min)
async def uy_hovli_narx_min_handler(message: types.Message, state: FSMContext):
    """Uy hovli minimal narxi"""
    await state.update_data(uy_hovli_narx_min=message.text)
    await message.answer(
        "💵 Maksimal narxni kiriting 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(IjaragaOlamanState.uy_hovli_narx_max)

@router.message(IjaragaOlamanState.uy_hovli_narx_max)
async def uy_hovli_narx_max_handler(message: types.Message, state: FSMContext):
    """Uy hovli maksimal narxi - natijalarni ko'rsatish"""
    await state.update_data(uy_hovli_narx_max=message.text)
    
    data = await state.get_data()
    
    text = f"""
🔍 QIDIRUV NATIJALARI (UY HOVLI)

📅 Muddat: {data.get('muddat', '—')}
📍 Tuman: {data.get('tuman', '—')}
👥 Kimdan: {data.get('kimdan', '—')}
📐 Sotix: {data.get('uy_hovli_sotix', '—')}
📏 Kvadrat: {data.get('uy_hovli_kvadrat', '—')}
🚪 Xona: {data.get('uy_hovli_xona', '—')}
🏢 Qavat: {data.get('uy_hovli_qavat', '—')}
🛠️ Ta'mir: {data.get('uy_hovli_tamir', '—')}
💵 Narx: {data.get('uy_hovli_narx_min', '—')} - {data.get('uy_hovli_narx_max', '—')}

Sizning so'rovingiz bo'yicha e'lonlar topilmadi.
Tez orada yangi e'lonlar qo'shiladi!
    """
    
    await message.answer(
        text,
        reply_markup=user_menu
    )
    await state.clear()

# ==================== DACHA FILTRLARI ====================

@router.message(IjaragaOlamanState.dacha_xona)
async def dacha_xona_handler(message: types.Message, state: FSMContext):
    """Dacha xonalar soni"""
    await state.update_data(dacha_xona=message.text)
    await message.answer(
        "💵 Minimal narxni kiriting 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(IjaragaOlamanState.dacha_narx_min)

@router.message(IjaragaOlamanState.dacha_narx_min)
async def dacha_narx_min_handler(message: types.Message, state: FSMContext):
    """Dacha minimal narxi"""
    await state.update_data(dacha_narx_min=message.text)
    await message.answer(
        "💵 Maksimal narxni kiriting 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(IjaragaOlamanState.dacha_narx_max)

@router.message(IjaragaOlamanState.dacha_narx_max)
async def dacha_narx_max_handler(message: types.Message, state: FSMContext):
    """Dacha maksimal narxi - natijalarni ko'rsatish"""
    await state.update_data(dacha_narx_max=message.text)
    
    data = await state.get_data()
    
    text = f"""
🔍 QIDIRUV NATIJALARI (DACHA)

📍 Tuman: {data.get('tuman', '—')}
👥 Kimdan: {data.get('kimdan', '—')}
🚪 Xona: {data.get('dacha_xona', '—')}
💵 Narx: {data.get('dacha_narx_min', '—')} - {data.get('dacha_narx_max', '—')}

Sizning so'rovingiz bo'yicha e'lonlar topilmadi.
Tez orada yangi e'lonlar qo'shiladi!
    """
    
    await message.answer(
        text,
        reply_markup=user_menu
    )
    await state.clear()

# ==================== OFIS FILTRLARI ====================

@router.message(IjaragaOlamanState.ofis_maydon)
async def ofis_maydon_handler(message: types.Message, state: FSMContext):
    """Ofis maydoni"""
    await state.update_data(ofis_maydon=message.text)
    await message.answer(
        "🛠️ Ta'miri qanday bo'lsin?\n"
        "Tugmalardan birini tanlang 👇",
        reply_markup=tamir_button
    )
    await state.set_state(IjaragaOlamanState.ofis_tamir)

@router.message(IjaragaOlamanState.ofis_tamir)
async def ofis_tamir_handler(message: types.Message, state: FSMContext):
    """Ofis ta'miri"""
    await state.update_data(ofis_tamir=message.text)
    await message.answer(
        "💵 Minimal narxni kiriting 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(IjaragaOlamanState.ofis_narx_min)

@router.message(IjaragaOlamanState.ofis_narx_min)
async def ofis_narx_min_handler(message: types.Message, state: FSMContext):
    """Ofis minimal narxi"""
    await state.update_data(ofis_narx_min=message.text)
    await message.answer(
        "💵 Maksimal narxni kiriting 👇",
        reply_markup=create_price_keyboard()
    )
    await state.set_state(IjaragaOlamanState.ofis_narx_max)

@router.message(IjaragaOlamanState.ofis_narx_max)
async def ofis_narx_max_handler(message: types.Message, state: FSMContext):
    """Ofis maksimal narxi - natijalarni ko'rsatish"""
    await state.update_data(ofis_narx_max=message.text)
    
    data = await state.get_data()
    
    text = f"""
🔍 QIDIRUV NATIJALARI (OFIS)

📍 Tuman: {data.get('tuman', '—')}
👥 Kimdan: {data.get('kimdan', '—')}
📏 Maydon: {data.get('ofis_maydon', '—')}
🛠️ Ta'mir: {data.get('ofis_tamir', '—')}
💵 Narx: {data.get('ofis_narx_min', '—')} - {data.get('ofis_narx_max', '—')}

Sizning so'rovingiz bo'yicha e'lonlar topilmadi.
Tez orada yangi e'lonlar qo'shiladi!
    """
    
    await message.answer(
        text,
        reply_markup=user_menu
    )
    await state.clear()

# ==================== UMUMIY BUYRUQLAR ====================

@router.message(F.text == "⬅️ Orqaga")
async def orqaga_handler(message: types.Message, state: FSMContext):
    """Orqaga qaytish"""
    current_state = await state.get_state()
    
    if current_state:
        await message.answer(
            "Oldingi bo‘limga qaytildi. Kerakli bo‘limni tanlang. 👇",
            reply_markup=house_menu
        )
        await state.clear()
    else:
        await message.answer(
            "Bosh menyuga qaytildi. Kerakli bo‘limni tanlang. 👇",
            reply_markup=user_menu
        )

@router.message(F.text == "🏠 Bosh sahifa")
async def bosh_sahifa_handler(message: types.Message, state: FSMContext):
    """Bosh sahifaga qaytish"""
    await message.answer(
        "Bosh sahifaga qaytildi. Kerakli bo‘limni tanlang. 👇",
        reply_markup=user_menu
    )
    await state.clear()