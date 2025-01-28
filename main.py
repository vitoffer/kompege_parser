import requests
import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message


def solve(variant):
    try:
        dct = requests.get(f"https://kompege.ru/api/v1/variant/kim/{variant}").json()
        tasks = dct["tasks"]
        k = 1
        res = ""
        for task in tasks:
            res += f'{k}) {task["key"]}\n'
            k += 1
        return res
    except Exception:
        return "ERROR!!!"


async def echo(message: Message) -> None:
    await message.answer(solve(message.text))


async def main() -> None:
    bot_token = os.getenv("TOKEN")

    dp = Dispatcher()
    dp.message.register(echo, F.text)

    bot = Bot(token=bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv()

    asyncio.run(main())
