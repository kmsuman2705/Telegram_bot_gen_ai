from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os
import logging

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
# print(API_TOKEN)

# Additional setup and bot logic here

# configure logging

logging.basicConfig(level=logging.INFO)

# Initialize bot

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    await message.reply("Hi \n I am Echo Bot \n Powered by Aiogram")


@dp.message_handler()
async def echo(message: types.Message):

    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    