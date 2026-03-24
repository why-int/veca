from aiogram import types
from aiogram.filters import CommandStart

from . import commands_router


@commands_router.message(CommandStart())
async def handler_command_start(message: types.Message) -> None:
    await message.answer(
        text="👋 <b>Приветствуем вас снова в Veca!</b>\n\n"
        "Для взаимодействия воспользуйтесь кнопками.\n"
        "При возникновении ошибок или вопросов сообщайте в поддержку.",
    )
