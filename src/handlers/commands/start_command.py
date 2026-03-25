from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router(name="start_command_router")

@router.message(CommandStart())
async def handler_command_start(message: types.Message) -> types.Message:
    return await message.answer(
        text="👋 <b>Приветствуем вас снова в Veca!</b>\n\n"
        "Для взаимодействия воспользуйтесь кнопками.\n"
        "При возникновении ошибок или вопросов сообщайте в поддержку.",
    )
