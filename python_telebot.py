import telebot

token = 5674277039:AAEamO3PNcESjgXmTa3VtUZKVOx0av9ioFg

bot = telebot.TeleBot(token)

def handle_messages(messages):
	for message in messages:
		chatid = message.chat.id
		if message.content_type == 'text':
			text = message.text
			if text == "Hola":
				bot.send_message(chatid, "Hola, ¿Como podemos ayudarte?")
			elif text == 'Info':
			   bot.send_message(chatid, "Nosotros somos una empresa comprometida con nuestros cliente ")
			elif text == 'Productos':
				bot.send_message(chatid, "Estos son los productos que tenemos para ti: ")
				bot.send_photo(chatid, photo=open('C:\Users\victor.arcel\Pictures', 'rb'))
			elif text == 'Catalogo':
				bot.send_message(chatid, "Claro te enviamos nuestro catalogo")
				bot.send_document(chatid,open('C:\Users\victor.arcel\Pictures', 'rb'))

bot.set_update_listener(handle_messages) 
bot.infinity_polling()




'''

# SI QUIERES QUE UNICAMENTE TE CONTESTE A TI TU BOT IMPEMENTA ESTE CODIGO


token = "TU-TOKEN-DE-BOTFATHER"
bot = telebot.TeleBot(token)
mychatid = "TU-CHAT-ID" 

def handle_messages(messages):
	for message in messages:
		chatid = message.chat.id
		if chatid == int(mychatid):
			if message.content_type == 'text':
				text = message.text
				if text == "Hola":
					bot.send_message(chatid, "Hola, ¿Como podemos ayudarte?")
				
bot.set_update_listener(handle_messages) 
bot.infinity_polling()



'''
