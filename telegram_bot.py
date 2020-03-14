import telebot
import time

bot_token = '994821392:AAGUZifqsQfw5jnIhjzekj4VHtw9YeRTSCg'
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola persona!')
    photon = open(r"C:\Users\sergi\OneDrive\Documentos\telegram\Saludos.jpg", 'rb')
    bot.send_sticker(message.chat.id, photon)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Hola, soy el bot de Sergi, de SIS 19-20. Mis comandos son /start y "Dime algo bonito".')

@bot.message_handler(func=lambda message: message.text == "Dime algo bonito")
def at_answer(message):
    audio = open(r'C:\Users\sergi\OneDrive\Documentos\telegram\Saludos.mp3','rb')
    bot.send_audio(message.chat.id, audio)

while True:
    try:
            bot.polling()
    except Exception:
    	time.sleep(15)