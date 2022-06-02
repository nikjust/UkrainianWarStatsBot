"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

import config
from info import *

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config.token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
def format_date(date):
    if "2022" in date:
        date = date.replace("2022","22")

    if "." in date:
        date = datetime.strptime(date, "%d.%m.%y")
    elif " " in date:
        date = datetime.strptime(date, "%d %m %y")
    elif "_" in date:
        date = datetime.strptime(date, "%d_%m_%y")
    elif "-" in date:
        date = datetime.strptime(date, "%d-%m-%y")
    elif "/" in date:
        date = datetime.strptime(date, "%d/%m/%y")
    else:
        date = datetime.now()
    date_time = date.strftime("%d_%m_20%y")
    return date_time

@dp.message_handler(commands=['инфа',"info"])
async def today_command(message: types.Message):
    date_time = format_date(message.get_args())
    print(date_time)


    await message.reply(info_day(date_time), parse_mode="markdown")
    await bot.send_photo(message.chat.id, f"https://opermap.mash.ru/tiles/{date_time}/l1/01/l1_01_01.jpg")

@dp.message_handler(commands=['start'])
async def today_command(message: types.Message):
    await message.reply("", parse_mode="markdown")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)