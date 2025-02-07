import requests
import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandObject


def solve(variant):
    try:
        dct = requests.get(f"https://kompege.ru/api/v1/variant/kim/{variant}").json()
        tasks = dct["tasks"]
        k = 1
        res = ""
        for task in tasks:
            text = f"{k}) "
            if '\\n' in task['key']:
                text += '↓\n'
            text += f"{task["key"].replace("\\n", "\n")}\n"
            res += text
        return res
    except Exception:
        return "ERROR!!!"


async def solve_command(message: Message, command: CommandObject) -> None:
    await message.reply(solve(command.args))


async def main() -> None:
    bot_token = os.getenv("TOKEN")

    dp = Dispatcher()
    dp.message.register(solve_command, Command("kege"))

    bot = Bot(token=bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv()

    asyncio.run(main())
