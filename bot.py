from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")
AUTHORIZED_USER_ID = int(os.environ.get("USER_ID"))

def authorized(update: Update):
    return update.effective_user.id == AUTHORIZED_USER_ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    await update.message.reply_text(
        "🤖 HamoudiTradeBot جاهز\n"
        "📊 إشارات: كريبتو – ذهب – ناسداك\n\n"
        "الأوامر:\n"
        "/btc\n"
        "/gold\n"
        "/nasdaq\n"
    )

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    await update.message.reply_text("🟢 BTCUSD\nإشارة قادمة")

async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    await update.message.reply_text("🟡 XAUUSD\nإشارة قادمة")

async def nasdaq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    await update.message.reply_text("🔵 NASDAQ\nإشارة قادمة")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))
app.add_handler(CommandHandler("gold", gold))
app.add_handler(CommandHandler("nasdaq", nasdaq))
app.run_polling()
