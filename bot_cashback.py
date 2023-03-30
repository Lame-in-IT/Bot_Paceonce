from tokin_bot import TOKIN, id_user
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

from database import read_bd, create_user, create_appeal_True, read_appeal_True, create_appeal
from database import create_screenshot, create_telephon

bot = Bot(token=TOKIN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo_file_id(message: types.Message):
    id_photo = create_screenshot(str(message.from_user.id), str(message.photo[-1].file_id))
    if id_photo[0] != "No":
        await bot.send_message(message.from_user.id, 'Отлично {0.first_name}!\nВаш скриншот принят в обработку и скоро с вами свяжется менеджер'.format(message.from_user), reply_markup=nav.backerMenu)
        await bot.send_message(chat_id=id_user[0], text=f"Покупатель https://t.me/{message.from_user.username} с номером телефона {id_photo[1]} отправил скриншот.\nНеобходимо посмотреть его на соответствие.".format(message.from_user))
        await bot.send_message(chat_id=id_user[1], text=f"Покупатель https://t.me/{message.from_user.username} с номером телефона {id_photo[1]} отправил скриншот.\nНеобходимо посмотреть его на соответствие.".format(message.from_user))
        await bot.send_photo(chat_id=id_user[0], photo=id_photo[0])
        await bot.send_photo(chat_id=id_user[1], photo=id_photo[0])
    elif id_photo[0] == "No":
        await bot.send_message(message.from_user.id, 'Простите {0.first_name}, но вы еще не оставили ваш номер телефона.\nПожалуйста нажмите на кнопку "Поделиться номером телефона" и после это отправьте нам свой скриншот. Только после этого вы получите свою вознаграждение.'.format(message.from_user), reply_markup=nav.backerMenu1)
        
@dp.message_handler(content_types=["document"])
async def send_photo_file(message: types.Message):
    id_photo = create_screenshot(str(message.from_user.id), str(message.document.file_id))
    if id_photo[0] != "No":
        await bot.send_message(message.from_user.id, 'Отлично {0.first_name}!\nВаш скриншот принят в обработку и скоро с вами свяжется менеджер'.format(message.from_user), reply_markup=nav.backerMenu)
        await bot.send_message(chat_id=id_user[0], text=f"Покупатель https://t.me/{message.from_user.username} с номером телефона {id_photo[1]} отправил скриншот.\nНеобходимо посмотреть его на соответствие.".format(message.from_user))
        await bot.send_document(chat_id=id_user[0], document=id_photo[0])
        await bot.send_message(chat_id=id_user[1], text=f"Покупатель https://t.me/{message.from_user.username} с номером телефона {id_photo[1]} отправил скриншот.\nНеобходимо посмотреть его на соответствие.".format(message.from_user))
        await bot.send_document(chat_id=id_user[1], document=id_photo[0])
    elif id_photo[0] == "No":
        await bot.send_message(message.from_user.id, 'Простите {0.first_name}, но вы еще не оставили ваш номер телефона.\nПожалуйста нажмите на кнопку "Поделиться номером телефона" и после это отправьте нам свой скриншот. Только после этого вы получите свою вознаграждение.'.format(message.from_user), reply_markup=nav.backerMenu1)
        
@dp.message_handler(content_types=['contact'])
async def message_contact_handler(message: types.Message):
    file_id = message.contact
    create_telephon(message.from_user.id, file_id.phone_number)
    
@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    user_id = read_bd(str(message.from_user.id))
    if user_id == True:
        mass_text = "start"
        create_appeal_True(message.from_user.id, mass_text)
    elif user_id == False:
        create_user(message.from_user)
    await bot.send_message(message.from_user.id, 'Здравствуйте {0.first_name}!\nДля начала, хотим сказать спасибо за выбор Faсio. Это нас очень радует!\nА еще, для нас важно ваше впечатление о нашем продукте.\nМы подарим 150 руб. за отзыв о купленном нашем товаре "Facio" оставленный на Wildberries.\nЕсли вы уже оставили свой отзыв, то наш денежный бонус уже готов прилететь к вам😉\n1. Пришлите цифру 1, если уже оставили отзыв\n2. Пришлите цифру 2, чтобы узнать условия получения бонуса\n3. Пришлите цифру 3, если возник вопрос или проблема.'.format(message.from_user), reply_markup=nav.mainMenu)
    
    
@dp.message_handler(text="1. Отзыв уже оставил(а)")
async def bot_message(message: types.Message):
    mass_text = "1. Отзыв уже оставил(а)"
    create_appeal_True(message.from_user.id, mass_text)
    await bot.send_message(message.from_user.id, 'Отлично {0.first_name}. Спасибо вам!\nВ таком случае:1. Нажмите конпку "Поделиться номером телефона" и ждем от вас скриншот: вашего отзыва о покупки, и 150 руб. очень скоро будут у вас.\n\nПосле их отправки, пожалуйста, дождитесь ответа наших менеджеров\n\nВ Личном кабинете Wildberries все оставленные отзывы можно найти в разделе "Профиль ➡️ “Отзывы и вопросы".\n\nЧто бы вернуться в начало, нажмите 1. Вернуться в начало'.format(message.from_user), reply_markup=nav.backerMenu1)
    
@dp.message_handler(text="2. Узнать условия получения бонуса")
async def bot_message(message: types.Message):
    mass_text = "2. Узнать условия получения бонуса"
    create_appeal_True(message.from_user.id, mass_text)
    await bot.send_message(message.from_user.id, 'Для того, чтобы получить свой денежный бонус, вам нужно оставить отзыв о покупке нашего товара на Wildberries.\nРасскажите, что вам понравилось в Facio: товар, упаковка, сервис, доставка.\nПошаговая инструкция для получения денежного вознаграждения:\n1️⃣ Зайдите в Личный кабинет Wildberries\n2️⃣ Найдите раздел “Покупки”\n3️⃣ Выберите товар Facio, который вы приобрели\n4️⃣ Кликните на “Отзыв” ➡️ “Оставить отзыв”\n5️⃣ Загрузите фото полученного товара и напишите, чем вам понравился наш бренд\n6️⃣ Кликните “Опубликовать отзыв”\n7️⃣ Сделайте скриншот готового отзыва и прикрепите в наш чат-бот\n\nЧто бы вернуться в начало, нажмите 1. Вернуться в начало', reply_markup=nav.backerMenu)

@dp.message_handler(text="3. У меня возник вопрос или проблема")
async def bot_message(message: types.Message):
    mass_text = "3. У меня возник вопрос или проблема"
    create_appeal_True(message.from_user.id, mass_text)
    await bot.send_message(message.from_user.id, 'Если у вас возник вопрос или проблема, вы можете написать тут и менеджер получит ваше сообщение.\n\n1. Пришлите цифру 1, если уже оставили отзыв\n2. Пришлите цифру 2, чтобы узнать условия получения бонуса\n3. Пришлите цифру 3, если возник вопрос или проблема.', reply_markup=nav.backerMenu) #0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟


@dp.message_handler(text="1. Вернуться в начало")
async def bot_message(message: types.Message):
    mass_text = "1. Вернуться в начало"
    create_appeal_True(message.from_user.id, mass_text)
    await command_start(message)
       
@dp.message_handler()
async def bot_message(message: types.Message):
    read_appeal_text = read_appeal_True(message.from_user.id)
    if read_appeal_text == "3. У меня возник вопрос или проблема":
        create_appeal(message.from_user.id, message.text)
        await bot.send_message(chat_id=id_user[0], text=f"Пользователь с именем https://t.me/{message.from_user.username} отправил сообщение.\n\n{message.text}".format(message.from_user))
        await bot.send_message(chat_id=id_user[1], text=f"Пользователь с именем https://t.me/{message.from_user.username} отправил сообщение.\n\n{message.text}".format(message.from_user))
        await bot.send_message(message.from_user.id, 'Ваше обращение принято в работу. В ближайшее время наш менеджер свяжется с Вами😊 Также у нашего менеджера есть рабочий график и на выходных он отдыхает😜', reply_markup=nav.backerMenu)
    elif read_appeal_text == "1. Отзыв уже оставил(а)":
        await bot.send_message(message.from_user.id, 'Ждём от вас именно картинку скриншота Вашего отзыва😉', reply_markup=nav.backerMenu1)   
    elif read_appeal_text == "2. Узнать условия получения бонуса":
        await bot.send_message(message.from_user.id, 'Ждём от вас именно картинку скриншота Вашего отзыва😉', reply_markup=nav.backerMenu)   
    else:
        await bot.send_message(message.from_user.id, 'Я вас не понял.\n\nЖдём от вас именно картинку скриншота Вашего отзыва😉\n1. Пришлите цифру 1, если уже оставили отзыв\n2. Пришлите цифру 2, чтобы узнать условия получения бонуса\n3. Пришлите цифру 3, если возник вопрос или проблема.', reply_markup=nav.backerMenu)   
       
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)