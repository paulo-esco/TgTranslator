import logging
import asyncio
import subprocess
import sys
from uuid import uuid4


THIRD_PARTY = ("aiogram>=3.5,<4.0", "googletrans==4.0.0-rc1")

try:
    # пробуем импортировать – если не выйдет, установим
    from aiogram import Bot, Dispatcher, types
    from aiogram.client.default import DefaultBotProperties
    from aiogram.filters import CommandStart
    from aiogram.types import (
        BotCommand,
        InlineQueryResultArticle,
        InputTextMessageContent,
    )
    from googletrans import Translator
except ImportError:          # сработает, если чего-то не хватает
    print("🔧 Устанавливаю/обновляю зависимости… (может занять около минуты)")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--upgrade", *THIRD_PARTY]
    )
    # пробуем ещё раз
    try:
        from aiogram import Bot, Dispatcher, types
        from aiogram.client.default import DefaultBotProperties
        from aiogram.filters import CommandStart
        from aiogram.types import (
            BotCommand,
            InlineQueryResultArticle,
            InputTextMessageContent,
        )
        from googletrans import Translator
    except ImportError:
        print("Библиотеки подгружены. Перезапустите бота командой: python main.py")
        exit()

TOKEN = ''

dp = Dispatcher()

bot = Bot(
    TOKEN or input(
        "Введите токен бота(чтобы не вводить каждый раз, впишите его меж кавычек в 4 строке): "
    ),
    default=DefaultBotProperties(
        link_preview_is_disabled=True,
    ),
)


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    me = await message.bot.get_me()
    await message.answer(f"Привет. Введи @{me.username} <Твой текст>\n И нажми Enter")

uk_flag_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/" \
              "Flag_of_the_United_Kingdom_%281-2%29.svg/" \
              "1200px-Flag_of_the_United_Kingdom_%281-2%29.svg.png"

es_flag_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/" \
              "Bandera_de_Espa%C3%B1a.svg/1200px-Bandera_de_Espa%C3%B1a.svg.png"

cn_flag_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/" \
              "Flag_of_the_People%27s_Republic_of_China.svg/" \
              "800px-Flag_of_the_People%27s_Republic_of_China.svg.png"


@dp.inline_query()
async def query_handler(inline_query: types.InlineQuery):

    async with Translator() as translator:
        eng = await translator.translate(text=inline_query.query, dest='en')
        esp = await translator.translate(text=inline_query.query, dest='es')
        ukr = await translator.translate(text=inline_query.query, dest='uk')

    await inline_query.answer(results=[
        InlineQueryResultArticle(
            id=uuid4().hex,
            title="English",
            description=eng.text,
            input_message_content=InputTextMessageContent(
                message_text=eng.text),
            thumbnail_url=uk_flag_url
        ),
        InlineQueryResultArticle(
            id=uuid4().hex,
            title="Espanol",
            description=esp.text,
            input_message_content=InputTextMessageContent(
                message_text=esp.text),
            thumbnail_url=es_flag_url

        ),
        InlineQueryResultArticle(
            id=uuid4().hex,
            title="Ukrainian",
            description=ukr.text,
            input_message_content=InputTextMessageContent(
                message_text=ukr.text),
            thumbnail_url=cn_flag_url

        ),
    ])


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.set_my_commands([
        BotCommand(command="/start", description="Запуск бота")
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
