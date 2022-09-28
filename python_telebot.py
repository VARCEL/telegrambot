import telebot

token = "TU-TOKEN-DE-BOTFATHER"

bot = telebot.TeleBot(token)

def handle_messages(messages):
	for message in messages:
		chatid = message.chat.id
		if message.content_type == 'text':
			text = message.text
			if text == "Hola":
				bot.send_message(chatid, "Hola, ¿Como podemos ayudarte?")
			if text == 'Info':
			   bot.send_message(chatid, "Nosotros somos una empresa comprometida con nuestros cliente ")
			if text == 'Productos':
				bot.send_message(chatid, "Estos son los productos que tenemos para ti: ")
				bot.send_photo(chatid, photo=open('TU-DIRECTORIO-DONDE-SE-VA-ENCONTRAR-LA-IMAGEN', 'rb'))
			if text == 'Catalogo':
				bot.send_message(chatid, "Claro te enviamos nuestro catalogo")
				bot.send_document(chatid,open('TU-DIRECTORIO-DONDE-SE-VA-ENCONTRAR-LA-ARCHIVO', 'rb'))



bot.set_update_listener(handle_messages) 

bot.infinity_polling()


