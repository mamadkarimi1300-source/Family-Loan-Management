
from telegram.ext import Application, CommandHandler
from app.config.settings import BOT_TOKEN


async def start(update, context):
    await update.message.reply_text(
        "به ربات مدیریت وام خانوادگی خوش آمدید."
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("FamilyFund Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
