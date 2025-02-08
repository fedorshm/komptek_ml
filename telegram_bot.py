import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "Gnider/kompt_distil_v1" 
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

QUESTIONS = [
    "What is your gender?",
    "What is your age?",
    "What is your city?",
    "Are you a Working Professional or a Student?",
    "What is your profession? (Type 'nan' if you don't have one)",
    "What is your academic pressure from 0 to 5? (Type 'nan' if you are not a student)",
    "What is your work pressure from 0 to 5? (Type 'nan' if you do not work)",
    "What is your CGPA?(Type 'nan' if you are not a student)",
    "What is your study satisfaction from 0 to 5? (Type 'nan' if you are not a student)",
    "What is your job satisfaction from 0 to 5? (Type 'nan' if you do not have a job)",
    "What is your sleep duration?",
    "What are your dietary habits?",
    "What is your degree? (Type 'nan' if you don't have one)",
    "Have you ever had suicidal thoughts?",
    "What are you work/study hours?",
    "What is your financial stress from 1 to 5? (Type 'nan' if you don't experience financial stress)",
    "Do you have family history of mental illness?",
    
]

ASKING_QUESTIONS, PREDICTING = range(2)

user_responses = {}

async def start(update: Update, context):
    await update.message.reply_text(
        "Hello! I'm here to help you. I'll ask you a few questions to understand your situation. If you can't or don't want to answer some questions, type and send 'nan'. "
        "Let's begin. What is your gender?"
    )
    return ASKING_QUESTIONS

async def handle_response(update: Update, context):
    user_id = update.message.from_user.id
    text = update.message.text

    if user_id not in user_responses:
        user_responses[user_id] = []
    user_responses[user_id].append(text)

    if len(user_responses[user_id]) < len(QUESTIONS):
        await update.message.reply_text(QUESTIONS[len(user_responses[user_id])])
        return ASKING_QUESTIONS
    else:
        combined_text = " ".join(user_responses[user_id])
        await update.message.reply_text("Thank you! Analyzing your responses...")

        inputs = tokenizer(combined_text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            logits = model(**inputs).logits
        prediction = torch.argmax(logits, dim=-1).item()

        if prediction == 1:
            await update.message.reply_text("Based on your responses, you may be experiencing depression. Please seek professional help.")
        else:
            await update.message.reply_text("Based on your responses, you do not seem to be experiencing depression. Take care!")

        del user_responses[user_id]
        return ConversationHandler.END

async def cancel(update: Update, context):
    await update.message.reply_text("Conversation canceled.")
    return ConversationHandler.END

def main():
    application = ApplicationBuilder().token(" ").build() #сюда идет токен бота

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASKING_QUESTIONS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
