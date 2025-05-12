import os
import asyncio

from aiogram.filters import CommandStart
from aiogram.types import BotCommand

try:
    from aiogram import Dispatcher, Bot, types
except ModuleNotFoundError:
    os.system("pip install aiogram")
    from aiogram import Dispatcher, Bot

TOKEN = '7744896116:AAHZG6ak7ctbsQQ127DU-qO-pcIz05PcEds'

dp = Dispatcher()

bot = Bot(
    TOKEN or input(
        "Введите токен бота(чтобы не вводить каждый раз, впишите его меж кавычек в 4 строке): "
    )
)


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет")


@dp.inline_query()
async def query_handler(inline_query: types.InlineQuery):
    print(inline_query)


async def main():
    await bot.set_my_commands([
        BotCommand(command="/start", description="Запуск бота")
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
