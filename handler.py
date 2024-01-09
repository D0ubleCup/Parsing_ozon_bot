from aiogram import Router

from aiogram import Bot,  F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from utils import keyboard as kb
from utils.FSLclasses import Data 



router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer('Добро пожаловать в бота для определение цены товара на озон!', reply_markup=kb.start_keyboard)

@router.callback_query(F.data=='go')
async def go_work(message: Message, state: FSMContext):
    await message.answer('Пришлите ссылку на товар на озоне')
    await state.set_state(Data.ozon_url)

@router.message(Data.ozon_url, F.text[:27].in_(['https://www.ozon.ru/product']))
async def parsing_url(message: Message, state: FSMContext):
    await state.update_data(ozon_url=message.text)
    data = await state.get_data()
    print('123')
    #парсинг озон
    

@router.message(Data.ozon_url)
async def incorent_parsing_url(message: Message, state: FSMContext):
    if message.text == 'Выйти':
        await state.clear()
        await message.answer('Добро пожаловать в бота для определение цены товара на озон!', reply_markup=kb.start_keyboard)

    else:
        print(message.text[:27])
        await message.answer('Введите сылку на товар на озон!!! \nИли же для выхода введите или нажмите кнопку "Выйти"', reply_markup=kb.exit_keyboard)
