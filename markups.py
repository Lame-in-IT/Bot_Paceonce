from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- Main Menu ---
btnprice = KeyboardButton('1. Отзыв уже оставил(а)')
btnreviews = KeyboardButton('2. Узнать условия получения бонуса')
btnsale = KeyboardButton('3. У меня возник вопрос или проблема')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnprice).add(btnreviews).add(btnsale)

# ---Back Menu ---
backmenu = KeyboardButton('1. Вернуться в начало')
backerMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(backmenu)

# ---Back1 Menu ---
backmenu1 = KeyboardButton('1. Вернуться в начало')
backmenu2 = KeyboardButton('Поделиться номером телефона', request_contact=True)
backerMenu1 = ReplyKeyboardMarkup(resize_keyboard=True).add(backmenu1).add(backmenu2)