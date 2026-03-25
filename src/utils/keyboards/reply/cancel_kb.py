from aiogram import types

cancel_keyboard: list[list[types.KeyboardButton]] = [
    [types.KeyboardButton(text="❌ Отменить")],
]


async def cancel_button() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        keyboard=cancel_keyboard,
        resize_keyboard=True,
        input_field_placeholder="VELORA",
        one_time_keyboard=False,
    )
