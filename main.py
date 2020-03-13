# github.com/eBind/LinuxCommands

import telebot
from os import path

bot = telebot.TeleBot('961827102:AAGKBTATdCQKrj1ZRu7CJzqcbhg9QQnuO2w')

@bot.message_handler(content_types=['text'])
def sent(message):
	msg = message.text
	chat = message.chat.id

	if msg[0] == '/':	
		if path.exists("commands/" + msg[1:].lower() + ".txt"):
			text = open("commands/" + msg[1:].lower() + ".txt").read()
			bot.send_message(chat, text)

		else:
			bot.send_message(chat, "Команда отсутствует в нашем реестре, для добавления отпишитесь @over_media")

bot.polling()