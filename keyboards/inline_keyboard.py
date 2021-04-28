from telebot.types import InLineKeyboardMarkup, InLineKeyboardButton

inline_key = InLineKeyboardMarkup()
btn = InLineKeyboardButton('Yes', callback_data='yes')
btn1 = InLineKeyboardButton('No', callback_data='no')
inline_key.add(btn, btn1)