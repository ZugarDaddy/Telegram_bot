from aiogram import types, Router, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile, CallbackQuery
from aiogram.utils.media_group import MediaGroupBuilder
import aiogram
from kbds import reply

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    image_from_pc = FSInputFile('photo/Start_photo.jpeg')
    await message.answer_photo(
        image_from_pc,
        caption='Я рада вас видеть! 🤗\nМеня зовут Светлана Владимировна и я онлайн-логопед',
        reply_markup=reply.start_kb)

# контакты и их вызовы
@user_private_router.message(F.text=='☎️Контакты')
async def contact_main(message: types.Message):
    await message.answer('Все мои контакты!\nВыбери удобный для себя вариант 😃',
                         reply_markup=reply.contact_kb)

@user_private_router.message(F.text=='📱Мобильный')
async def contact_cmd_mobile(message: types.Message):
    await message.answer('Мой номер мобильного телефона:')
    await message.answer('89047515140')

@user_private_router.message(F.text=='🟢WhatsApp')
async def contact_cmd_whatsapp(message: types.Message):
    await message.answer('https://api.whatsapp.com/send?phone=79047515140')

@user_private_router.message(F.text=='🟣Viber')
async def contact_cmd_viber(message: types.Message):
    await message.answer('https://tinyurl.com/bdzfa2f5')

@user_private_router.message(F.text=='🖼️Instagram')
async def contact_cmd_insta(message: types.Message):
    await message.answer('https://www.instagram.com/svetlanavladimirovnalogo?igsh=bnU2OHA4NmVpZG0=')
    await message.answer('(Может не запускаться, следует включить VPN-сервис на вашем телефоне)')

@user_private_router.message(F.text=='🔵Telegram')
async def contact_cmd_tg(message: types.Message):
    await message.answer('@Svetlana_logos')

# вызовы материалов "за кулисы"
@user_private_router.message(F.text=='🧸За кулисы')
async def gallery_main(message: types.Message):
    await message.answer('Здесь Вы можете узнать о моих занятиях чуть больше!',
                         reply_markup=reply.gallery_kb)

@user_private_router.message(F.text=='🎬Фрагменты занятий')
async def gallery_video(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='1️⃣Занятие с язычком - "Штанга"', url="https://youtube.com/shorts/k42JTYFUqZQ"))
    builder.row(types.InlineKeyboardButton(
        text='2️⃣Задание - "Разведчик"', url='https://youtube.com/shorts/T8wv76dk01M?feature=share'))
    builder.row(types.InlineKeyboardButton(
        text='3️⃣Задание - Найди букву "Ш"', url='https://youtube.com/shorts/EqaPhNNHguc?feature=share'))
    builder.row(types.InlineKeyboardButton(
        text='4️⃣Задание - "Змейка"', url='https://youtu.be/PfVs_nZOOEg'))
    builder.row(types.InlineKeyboardButton(
        text='5️⃣Рекомендация родителю', url='https://youtube.com/shorts/YkfUm3KgAAw?feature=share'))
    await message.answer(
        'Вот немного фрагментов занятий 😃',
        reply_markup=builder.as_markup())

@user_private_router.message(F.text=='📚Материал и учебное пособие')
async def gallery_photo(message: types.Message):
    album_builder = MediaGroupBuilder()
    album_builder.add_photo(media=FSInputFile('photo/thing_1.jpg'))
    album_builder.add_photo(media=FSInputFile('photo/thing_2.jpg'))
    album_builder.add_photo(media=FSInputFile('photo/thing_3.jpg'))
    album_builder.add_photo(media=FSInputFile('photo/thing_4.jpg'))
    album_builder.add_photo(media=FSInputFile('photo/thing_5.jpg'))
    await message.answer_media_group(media=album_builder.build())
    await message.answer(
        'Для достижения положительных результатов на занятии, для поддержания интереса и внимания моих учеников я использую различные наглядные пособия и обучающий материал 😃')


@user_private_router.message(F.text=='📖О себе')
async def about_me_cmd(message: types.Message):
    await message.answer('''
        ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️🌤️☁️☁️☁️☁️
        
        Меня зовут Хлюстова Светлана Владимировна.
        Мой стаж в логопедии 30 лет, 4 из которых я совмещаю с онлайн-занятиями . 
        Цель моей работы - коррекция речевых нарушений у детей, развитие всех мыслительных процессов, обогащение словарного запаса и подготовка к школе.

   🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷''')
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='⭐️Отзывы',
        callback_data='star_reaction')
    )
    await message.answer('👨‍👩‍👦Отзывы родителей моих учеников👨‍👩‍👦', reply_markup=builder.as_markup())

# все кнопки тарифов
@user_private_router.message(F.text=='💵Тарифы')
async def price_main(message: types.Message):
    image_from_pc = FSInputFile('photo/cat_money.jpg')
    await message.answer_photo(image_from_pc,
                               caption='''
➖ Онлайн-обследование  (длительность: 1,5 часа) - 2000₽.
➖ Занятие (длительность: 40 мин) - 1200₽.
▫️  Действуют скидки.''',
                         reply_markup=reply.price_kb)

@user_private_router.message(F.text=='📗Что входит в обследование?')
async def price_review(message: types.Message):
    await message.answer('''
➖ выявление уровня и тяжести нарушения звуковой стороны речи;
➖ выявление наличия/отсутствия  грубых видимых дефектов в строении артикуляционного аппарата;
➖ определение уровня словарного запаса;
➖ проверка состояния фразовой речи и её грамматического оформления;
➖ наблюдение за темпом, интонацией и плавностью речи;
➖ сбор анамнеза развития ребёнка (со слов родителей).
▫️  После этого дается логопедическое заключение и определяется план коррекционной работы.
        ''')

@user_private_router.message(F.text=='🔙Назад')
async def back_btn(message: types.Message):
    await message.answer('🤗')
    await message.answer('Переходи в мой канал и узнавай много полезного и интересного!\nhttps://t.me/logoped_sv',
                         reply_markup=reply.start_kb)

album_builder = MediaGroupBuilder()
album_builder.add_photo(media=FSInputFile('photo/reviewes_1.jpg'))
album_builder.add_photo(media=FSInputFile('photo/reviewes_2.jpg'))
album_builder.add_photo(media=FSInputFile('photo/reviewes_3.jpg'))
album_builder.add_photo(media=FSInputFile('photo/reviewes_4.jpg'))
album_builder.add_photo(media=FSInputFile('photo/reviewes_5.jpg'))
album_builder.add_photo(media=FSInputFile('photo/reviewes_6.jpg'))
album_builder.add_photo(media=FSInputFile('photo/reviewes_7.jpg'))
album_builder.add_photo(media=FSInputFile('photo/reviewes_8.jpg'))
album_builder.add_photo(media=FSInputFile('photo/reviewes_9.jpg'))
album_builder.add_photo(media=FSInputFile('photo/reviewes_10.jpg'))

@user_private_router.message(F.text=='⭐️Отзывы')
async def star(message: types.Message):
    await message.answer_media_group(media=album_builder.build())
@user_private_router.callback_query(F.data == "star_reaction")
async def callback_star(callback: types.CallbackQuery):
    await callback.message.answer_media_group(media=album_builder.build())
