from aiogram.fsm.state import StatesGroup, State

class KvartiraState(StatesGroup):
    muddati = State()
    tuman = State()
    kimga = State()
    xona = State()
    sotix = State()
    tamir = State()
    rasm = State()
    narxi = State()
    vosita_haqi = State()
    number = State()  # Добавлено

class UyHovliState(StatesGroup):
    ijara = State()
    sotix = State()
    kvadrat = State()
    xona = State()
    qavat = State()
    tamir = State()
    rasm = State()
    narxi = State()
    vosita_haqi = State()
    number = State()

class DachaState(StatesGroup):
    ijara = State()
    xona = State()
    narxi = State()
    dam_narxi = State()
    rasm = State()
    number = State()

class OfisState(StatesGroup):
    ijara = State()
    xona = State()
    tamir = State()
    rasm = State()
    narxi = State()
    vosita_haqi = State()
    number = State()