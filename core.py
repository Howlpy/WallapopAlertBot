import apireqs
import telebot


bot = telebot.TeleBot("1614218850:AAGTVzKOqEpZm0ow0upXJuOrJ3K15AcAgmg")


@bot.message_handler(commands=['start'])
def start(message):
    cid = message.chat.id
    bot.reply_to(message, "Dame nombre de lo que deseas y el precio maximo que quieres pagar y este bot te avisara cuando alguien suba ese producto por menos de tu precio maximo.")

@bot.message_handler(commands=['help'])
def help(message):
    cid= message.chat.id
    bot.send_message(cid,"Utiliza /setalert producto - preciomaximo | Ejemplo:\n/setalert nintendo switch - 150")

@bot.message_handler(commands=['setalert'])
def setalert(message):
    command = message.text.replace('/setalert','').split('-')
    if len(command) == 2:
        command = [x.strip(' ') for x in command]
        print(command)
    else:
        bot.reply_to(message,"Utiliza /help para aprender como usar los comandos.")


bot.polling()
