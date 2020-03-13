# github.com/eBind/LinuxCommands

import telebot
from os import path

bot = telebot.TeleBot('id:token')

@bot.message_handler(content_types=['text'])
def sent(message):
	msg = message.text
	chat = message.chat.id

	if msg[0] == '/':	
		if path.exists("commands/" + msg[1:].lower() + ".txt"):
			text = open("commands/" + msg[1:].lower() + ".txt", encoding='utf-8').read()
			bot.send_message(chat, text)

		else:
			bot.send_message(chat, "Команда отсутствует в нашем реестре, для добавления отпишитесь ...")

bot.polling()
