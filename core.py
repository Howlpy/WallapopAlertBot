import api
import telebot
import threading

bot = telebot.TeleBot("TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    cid = message.chat.id
    bot.reply_to(message, "Dame nombre del producto y el precio maximo que quieres pagar y este bot te avisara cuando alguien suba ese producto a wallapop por menos de tu precio maximo.")

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
        thread_alert = threading.Thread(target=wallasearch,args=(command[0],command[1]))
        thread_alert.start()
        #wallasearch(command[0],command[1])
    else:
        bot.reply_to(message,"Utiliza /help para aprender como usar los comandos.")


def wallasearch(user_product,user_price):   
    res = api.basicSearch(user_product,user_price)
    print (res)
    return res





if __name__ == '__main__':
    bot.polling()
