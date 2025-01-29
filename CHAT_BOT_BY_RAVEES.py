#BY RAVEES PAPA 
#REMEMBER RAVEES PAPA

import subprocess
import sys
import openai
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os

os.system('pip install openai==0.28')


# Function to check and install missing packages
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Ensure the required packages are installed
required_packages = ["openai", "requests", "python-telegram-bot"]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        install_package(package)

# OpenAI API Key (Replace with your OpenAI API key)
OPENAI_API_KEY = "YOUR API TOKEN "

# Telegram Bot Token (Replace with your Telegram bot token)
TELEGRAM_BOT_TOKEN = "YOUR BOT TOKEN"


# Function to handle the "/start" command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Welcome! I am an AI intelligence created by RAVEES || @IISSECURITY || Channel @iisfreeshop. "
        "Send me a message, and I'll respond.")


# Function to process user messages and send response
async def process_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = openai_response(user_message)

    if response:
        await update.message.reply_text(response)
    else:
        await update.message.reply_text(
            "Sorry, I couldn't understand your input. Please try again.")


# Function to make API request to OpenAI
def openai_response(user_message):
    try:
        openai.api_key = OPENAI_API_KEY  # Set the API key

        # Make request to OpenAI API (use gpt-3.5-turbo instead of gpt-4)
        response = openai.Completion.create(
            model=
            "gpt-3.5-turbo",  # Use "gpt-3.5-turbo" if you don't have access to gpt-4
            prompt=user_message,  # Using 'prompt' instead of 'messages'
            temperature=0.7,
            max_tokens=200)

        return response["choices"][0]["text"].strip()

    except Exception as e:
        return f"Error while contacting OpenAI: {e}"


# Main function to start the bot
def main():
    # Initialize the bot application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

    # Start the bot
    application.run_polling()


if __name__ == '__main__':
    main()
