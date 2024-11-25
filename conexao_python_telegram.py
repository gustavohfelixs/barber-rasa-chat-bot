
import telebot
import requests, uuid, json

def interacao_rasa(url_rasabot, chat_id, mensagem):
  # Cabeçalho para envio de informação via JSON para o RASA
  headers = {
      'Content-type':'application/json'
      }
  # Dados que serão enviados ao bot do RASA
  data = {
  "sender": chat_id, # Código que usamos para identificar o usuário que enviou a mensagem
  "message": mensagem # Mensagem do usuário
  }
  print("Mensagem do usuário: " +   str(chat_id) + " " + mensagem)
  request = requests.post(url_rasabot, headers=headers, json=data) # enviando a mensagem via POST
  response = request.json() # Recebendo a resposta num documento JSON
  print(response)
  if len(response)!=0:
    return response[0]['text'] # Retornando apenas a resposta de texto do bot ao usuário
  else:
    return "Favor reformular"


# --------- token telegrambot --------------
API_TOKEN = '7932613824:AAGtlE6y2N67Qv0yMr1tby-is_GgCwjhSjs'
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)
bot.set_webhook()
# --------- url Pinggy --------------
url = "https://5fe1-187-90-138-207.ngrok-free.app"
url_final = url + '/webhooks/rest/webhook'

# Lidando com mensagens de texto do usuário:
@bot.message_handler(content_types=['text'])
def text_processing(message):
  msg_usuario = message.text #Recebendo o atributo da mensagem de texto do usuário
  msg_bot = interacao_rasa(url_final, message.chat.id, msg_usuario) # Enviando a mensagem para o bot
  bot.reply_to(message, msg_bot) # Envia a resposta do bot ao usuári

@bot.message_handler(func=lambda message: True, content_types=['photo', 'audio', 'document', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact']) 
def handle_non_text(message): bot.reply_to(message, "Desculpe, ainda não sei processar esse tipo de informação.")
bot.infinity_polling()