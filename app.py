import os
import sys
import json
import time

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  # We don't want to reply to ourselves!
  if data['text'] == '8:00':
    #msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    time.sleep(2)
    msg = 'MSC: Mark alec sophia \nCommons: Jackson Meg Wesley \nHarrington: Saul Cameron'
    send_message(msg)
  elif data['text'] == '8:30':
    time.sleep(2)
    msg = 'MSC: Mark alec sophia \nCommons: Jackson Meg Wesley \nHarrington: Sidney Saul Cameron '
    send_message(msg)
  elif data['text'] == '9:00':
    time.sleep(2)
    msg = 'MSC: Jacob  alec Cameron \nCommons: Meg Wesley Jackson \nHarrington: Lexi Zac Saul '
    send_message(msg)
  elif data['text'] == '9:30':
    time.sleep(2)
    msg = 'MSC: Aly Oriana Jacob Cameron\nCommons: Meg Jackson alec \nHarrington: Lexi Zac Noah Saul'
    send_message(msg)
  elif data['text'] == '10:00':
    time.sleep(2)
    msg = 'MSC: Aly Oriana Jacob Zac\nCommons: Meg Jackson alec Jarrod\nHarrington: Addie Gracie Noah Saul'
    send_message(msg)
  elif data['text'] == '10:30':
    time.sleep(2)
    msg = 'MSC: Aly Oriana  \nCommons: Meg alec Jarrod \nHarrington:  Addie Gracie Noah Cameron'
    send_message(msg)
  elif data['text'] == '11:00':
    time.sleep(2)
    msg = 'MSC: Aly Oriana Cole \nCommons: Meg Jarrod alec \nSbisa:  Gracie Cameron Danya'
    send_message(msg)
  elif data['text'] == '11:30':
    time.sleep(2)
    msg = 'MSC: Aly Oriana Sophia Cole\nCommons: Meg Jarrod Alec \nSbisa:  Gracie Cameron Danya'
    send_message(msg)
  elif data['text'] == '12:00':
    time.sleep(2)
    msg = 'MSC: Sophia Cole Mark \nCommons: Jarrod  Meg \nSbisa:  Gracie Danya Cameron'
    send_message(msg)
  elif data['text'] == '12:30':
    time.sleep(2)
    msg = 'MSC: Cole Mark Sophia \nCommons: Jarrod Meg  \nSbisa:  Gracie Danya Cameron'
    send_message(msg)
  elif data['text'] == '1:00':
    time.sleep(2)
    msg = 'MSC: Cole Jacob Mark \nCommons: Addie Jarrod Saul \nSbisa:  Haley Danya Noah Cameron'
    send_message(msg)
  elif data['text'] == '1:30':
    time.sleep(2)
    msg = 'MSC: Cole Jacob Sidney \nCommons: Addie Jarrod Saul \nSbisa:  Haley Danya Noah Cameron'
    send_message(msg)

  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
