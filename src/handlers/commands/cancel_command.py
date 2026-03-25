from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("cancel"))
async def cancel_command(
    message: types.Message, state: FSMContext
) -> types.Message:
    current_state: str | None = await state.get_state()

    if current_state is None:
        return await message.answer(
            text="🧐 Хм.. Кажется нет ни одного активного действия."
        )

    await state.clear()
    return await message.answer(text="❌ Вы отменили все активные действия.")
