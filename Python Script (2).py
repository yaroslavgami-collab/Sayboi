import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
import asyncio

TOKEN = "8954124854:AAGczlEeHPxiT1saoytPzrXHhLHPhXWia6A"

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
    text="🚀 Open App",
    web_app=WebAppInfo(
        url="https://6a569eb8b226e43363f384d8--monumental-florentine-5a6ccd.netlify.app/"
    )
)
            ]
        ]
    )

    await message.answer(
        "Добро пожаловать!",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

app.run(debug=True)
