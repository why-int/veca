from aiogram import Router, types
from aiogram.fsm.context import FSMContext

router = Router()


@router.callback_query()
async def cancel_button(
    callback: types.CallbackQuery, state: FSMContext
) -> bool:
    current_state: str | None = await state.get_state()

    if current_state is None:
        return await callback.answer(
            text="🧐 Хм.. Кажется активного действия для отмены нет."
        )

    return await callback.answer(
        text="❌ Вы отменили последнее активное действие."
    )
