from telebot import TeleBot

token = '5392783209:AAENp6hQs-MqFB9O8dzrQJ-By_HabDo3Ji8'
adminID = '882839892'

bot = TeleBot(token)


def sendMSG():
	msg = bot.send_message(adminID,"ЛОГ УСПЕШНО ОТПРАВЛЕН!")

sendMSG()