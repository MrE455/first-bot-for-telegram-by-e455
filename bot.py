import telebot
import os

token = os.environ.get('TOKEN')

client = telebot.TeleBot(str(token)) # Передаём токен.

hi_words = ['hi', 'hello', 'привет', 'здравствуй', 'ку', 'бонжур', 'салам', 'дарова', 'здарова', 'утречка']
answer_words = ['info', 'information', 'инфа', 'инфо', 'информация']
bye_words = ['bye', 'goodbye', 'пока', 'увидимся', 'до встречи', 'до свидания', 'до завтра']
# Список слов на которые будет реагировать бот.

@client.message_handler(content_types = ['text'])
def words (message):
	if message.text.lower() in hi_words:
		client.send_message(message.chat.id, f"Hello {message.from_user.first_name} {message.from_user.last_name}.")
	elif message.text.lower() in answer_words:
		client.send_message(message.chat.id, "Author - Egor Kirillov @mr_e455")
	elif message.text.lower() in bye_words:
		client.send_message(message.chat.id, f"Goodbye {message.from_user.first_name} {message.from_user.last_name}.")
# Реакция на слова из списков.

client.polling(none_stop = True, interval = 0) # Запуск.
