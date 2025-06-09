import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests
import json

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Ваш Telegram Bot Token (получите у @BotFather)
TELEGRAM_BOT_TOKEN = '5811886937:AAGLRjIeNZJiLPLCw8D0unlvRkZCszslOaM'

# xAI API ключ
XAI_API_KEY = 'xai-8Hj6AazQwjys45xOI5kwKgqcWziFbkBnUHPjuoCLYqVeBOeTb7TzbmnT7EGkw5IgfSryVMopDW6FFODy'

# URL xAI API
XAI_API_URL = 'https://api.x.ai/v1/grok'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я бот с Grok. Задавай свои вопросы!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    try:
        # Запрос к xAI API
        headers = {
            'Authorization': f'Bearer {XAI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': 'grok-3',
            'messages': [
                {'role': 'user', 'content': user_message}
            ]
        }
        
        response = requests.post(XAI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        # Получение ответа от Grok
        response_data = response.json()
        grok_response = response_data['choices'][0]['message']['content']
        
        # Отправка ответа пользователю
        await update.message.reply_text(grok_response)
        
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Ошибка при обращении к API: {str(e)}')
    except (KeyError, IndexError) as e:
        await update.message.reply_text('Ошибка при обработке ответа от API.')
    except Exception as e:
        await update.message.reply_text(f'Произошла ошибка: {str(e)}')

def main():
    # Создание приложения Telegram
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Обработчики
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запуск бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()