from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "7230429992:AAG1nWNErWxmkDL5BuMtk_7lqiY6mOkcBO8"

BUTTON_ASK = "🔮 Кнопка 1 — Задать вопрос"
BUTTON_SPACE = "🌿 Кнопка 2 — О пространстве"
BUTTON_REVIEW = "💳 Кнопка 3 — Как проходит разбор"

ASK_RESPONSE = (
    "Напишите, что волнует вас сейчас.\n"
    "Можно коротко — главное по сути.\n\n"
    "Я передам запрос для индивидуального разбора."
)

SPACE_RESPONSE = (
    "Это закрытое пространство для людей в периоде перемен.\n\n"
    "Здесь не дают обещаний и не пугают прогнозами.\n"
    "Здесь помогают понять причины происходящего\n"
    "и увидеть точки роста и выхода из кризисов."
)

REVIEW_RESPONSE = (
    "Разбор — это анализ текущего жизненного периода\n"
    "через принципы джйотиш и повторяющиеся сценарии.\n\n"
    "Вы получаете понимание:\n"
    "— почему сейчас именно так\n"
    "— что завершилось\n"
    "— куда лучше направлять энергию\n\n"
    "Оплата проходит через эквайренговый сервис, все безопасно"
)


def _main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [[BUTTON_ASK], [BUTTON_SPACE], [BUTTON_REVIEW]],
        resize_keyboard=True,
        one_time_keyboard=False,
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Выберите пункт в меню ниже.",
        reply_markup=_main_keyboard(),
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()

    if text == BUTTON_ASK:
        response = ASK_RESPONSE
    elif text == BUTTON_SPACE:
        response = SPACE_RESPONSE
    elif text == BUTTON_REVIEW:
        response = REVIEW_RESPONSE
    else:
        response = "Пожалуйста, выберите один из пунктов меню ниже."

    await update.message.reply_text(response, reply_markup=_main_keyboard())


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == "__main__":
    main()
