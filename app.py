import os
import sys
import json
import time
import gspread

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  msg = data['text'] + ' Shifts\n\n'
  # We don't want to reply to ourselves!
  if data['text'] == '8:00':
    #msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    time.sleep(2)
    msg = msg + 'MSC: Mark Thayer Cole \nCommons: Jackson Cameron \nHarrington: Wesley Noah Jacob'
    send_message(msg)
  elif data['text'] == '8:30':
    time.sleep(2)
    msg = msg + 'MSC: Cole Thayer Mark \nCommons: Jackson Gabi \nHarrington: Wesley Noah Jacob'
    send_message(msg)
  elif data['text'] == '9:00':
    time.sleep(2)
    msg = msg + 'MSC: Kourtnei Thayer Cole \nCommons: Jackson Gabi Torey \nHarrington: Noah Meg Lexi'
    send_message(msg)
  elif data['text'] == '9:30':
    time.sleep(2)
    msg = msg + 'MSC: Kourtnei Thayer Cole \nCommons: Jackson Mark Gabi Torey\nHarrington: Lexi Noah Meg'
    send_message(msg)
  elif data['text'] == '10:00':
    time.sleep(2)
    msg = msg + 'MSC: Cole Alec Torey \nCommons: Jackson Mark Danya \nHarrington: Addie Lexi Meg '
    send_message(msg)
  elif data['text'] == '10:30':
    time.sleep(2)
    msg = msg + 'MSC: Cole Cameron Torey \nCommons: Jackson Alec Danya \nHarrington: Addie Meg Wesley'
    send_message(msg)
  elif data['text'] == '11:00':
    time.sleep(2)
    msg = msg + 'MSC: Cole Cameron Torey \nCommons: Jackson Jonathan Lexi Danya\nSbisa: Jarrod Mary Kate Jacob'
    send_message(msg)
  elif data['text'] == '11:30':
    time.sleep(2)
    msg = msg + 'MSC: Torey Cole Cameron \nCommons: Jonathan Lexi Noah Danya\nSbisa: Jarrod Mary Kate Jacob'
    send_message(msg)
  elif data['text'] == '12:00':
    time.sleep(2)
    msg = msg + 'MSC: Thayer Cole \nCommons: Jonathan Lexi Sidney \nSbisa: Jarrod Mary Kate'
    send_message(msg)
  elif data['text'] == '12:30':
    time.sleep(2)
    msg = msg + 'MSC: Oriana Cole Thayer \nCommons: Jonathan Lexi Sidney \nSbisa: Addie Jarrod Mary Kate'
    send_message(msg)
  elif data['text'] == '1:00' or data['text'] == '13:00':
    time.sleep(2)
    msg = msg + 'MSC: Aly Thayer Oriana \nCommons: Mark Lexi Alec \nSbisa: Jarrod Mary Kate'
    send_message(msg)
  elif data['text'] == '1:30' or data['text'] == '13:30':
    time.sleep(2)
    msg = msg + 'MSC: Aly Thayer Oriana \nCommons: Mark Alec Sidney \nSbisa: Zac Jonathan Mary Kate'
    send_message(msg)
  elif data['text'] == '2:00' or data['text'] == '14:00':
    time.sleep(2)
    msg = msg + 'MSC: Aly Thayer Oriana \nCommons: Mark Noah Jacob \nHarrington: Creel Zac Saul Torey'
    send_message(msg)
  elif data['text'] == '2:30' or data['text'] == '14:30':
    time.sleep(2)
    msg = msg + 'MSC: Aly Thayer Oriana \nCommons: Alec Jonathan Jacob \nHarrington: Zac Creel Torey'
    send_message(msg)
  elif data['text'] == '3:00' or data['text'] == '15:00':
    time.sleep(2)
    msg = msg + 'MSC: Aly Thayer Sophia \nCommons: Wesley Jackon Sidney \nHarrington: Addie Zac Creel Torey'
    send_message(msg)
  elif data['text'] == '3:30' or data['text'] == '15:30':
    time.sleep(2)
    msg = msg + 'MSC: Thayer Sophia \nCommons: Wesley Jackson Sidney \nHarrington: Addie Zac Creel Torey'
    send_message(msg)
  elif data['text'] == '4:00' or data['text'] == '16:00':
    time.sleep(2)
    msg = msg + 'MSC: Kourtnei Thayer \nCommons: Addie Wesley Zac \nHarrington: Jarrod Creel'
    send_message(msg)
  elif data['text'] == '4:30' or data['text'] == '16:30':
    time.sleep(2)
    msg = msg + 'MSC: Kourtnei Thayer \nCommons: Addie Wesley \nHarrington: Jarrod Creel'
    send_message(msg)
  elif data['text'] == '5:00' or data['text'] == '17:00':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '5:30' or data['text'] == '17:30':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '6:00' or data['text'] == '18:00':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '6:30' or data['text'] == '18:30':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '7:00' or data['text'] == '19:00':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '7:30' or data['text'] == '19:30':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif  data['text'] == '20:00' or data['text'] == '20:30' or data['text'] == '21:00' or data['text'] == '21:30' or data['text'] == '22:00' or data['text'] == '22:30' or data['text'] == '23:00' or data['text'] == '23:30' or data['text'] == '0:00' or data['text'] == '0:30':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    if data['text'] == '21:00':
      msg = 'A A A A AAAAA\n' + msg
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
