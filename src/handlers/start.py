from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router(name="start_command_router")


@router.message(CommandStart())
async def start_command(message: types.Message) -> types.Message:
    return await message.answer(
        text="👋 <b>Приветствуем вас снова в Veca!</b>\n\n"
        "Для взаимодействия воспользуйтесь кнопками.\n"
        "При возникновении ошибок или вопросов сообщайте в поддержку.",
    )


@router.message(lambda c: c.data == "start")
async def start_button(message: types.Message) -> types.Message:
    return await start_command(message=message)
