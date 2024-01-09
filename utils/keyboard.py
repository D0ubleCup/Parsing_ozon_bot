from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton



start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='/go', callback_data='go')]],
    resize_keyboard=True
)

exit_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Выйти')]],resize_keyboard=True,
    input_field_placeholder= 'Для выхода из функции, нажмите на кнопку ниже'
)