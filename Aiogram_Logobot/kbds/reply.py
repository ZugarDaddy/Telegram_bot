from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📖О себе'),
         KeyboardButton(text='☎️Контакты')],
        [KeyboardButton(text='💵Тарифы'),
         KeyboardButton(text='🧸За кулисы')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Улыбайся ;)'
)

price_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📗Что входит в обследование?')],
        [KeyboardButton(text='🔙Назад'),
         KeyboardButton(text='🎬Фрагменты занятий')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Милый котёнок!'
)

contact_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📱Мобильный'),
         KeyboardButton(text='🔵Telegram'),
         KeyboardButton(text='🟢WhatsApp')],
        [KeyboardButton(text='🖼️Instagram'),
         KeyboardButton(text='🟣Viber')],
        [KeyboardButton(text='🔙Назад')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выходи на связь ;)'
)

gallery_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🎬Фрагменты занятий')],
        [KeyboardButton(text='📚Материал и учебное пособие')],
        [KeyboardButton(text='🔙Назад'),
         KeyboardButton(text='⭐️Отзывы')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Давай познакомимся!'
)
