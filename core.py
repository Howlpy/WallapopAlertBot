import api
import telebot
import threading

bot = telebot.TeleBot("TOKEN")



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
    cid= message.chat.id
    command = message.text.replace('/setalert','').split('-')
    if len(command) == 2:
        command = [x.strip(' ') for x in command]
        print(command)
        thread_alert = threading.Thread(target=wallasearch,args=(command[0],command[1],cid))
        thread_alert.start()
        #wallasearch(command[0],command[1])
    else:
        bot.reply_to(message,"Utiliza /help para aprender como usar los comandos.")

def arraypricelowest(array):
        return sorted(array, key=lambda x: x[1]) #ordena los array teniendo en cuenta el 2 elemento del array ( el precio en este caso )

def wallasearch(user_product,user_price,cid):
    text = []   
    res = api.basicSearch(user_product,user_price)
    array = arraypricelowest(res)    
    if len(array) >= 3:
        bot.send_message(cid,"Hay {} ofertas por menos de ese precio, aqui tienes las 3 primeras: ".format(len(array)))
        for i in array[:3]:
            bot.send_message(cid,"{} | Precio: {}€".format(i[0],i[1]))
    elif len(array) <= 3 and len(array) > 1:
        bot.send_message(cid,"Hay {} ofertas por menos de ese precio, aqui tienes la primera: ".format(len(array)))
        bot.send_message(cid,"{} | Precio: {}€".format(array[0][0],array[0][1]))
    else:
        bot.send_message(cid,"Hay 1 oferta por menos de ese precio, aqui la tienes: ")
        bot.send_message(cid,"{} | Precio: {}€".format(array[0][0],array[0][1]))





if __name__ == '__main__':
    bot.polling()
