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

  msg = data['text'] + ' Shifts\n\n'
  # We don't want to reply to ourselves!
  if data['text'] == '8:00':
    #msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    time.sleep(2)
    msg = msg + 'MSC: Landon Cameron Wesley \nCommons: Mark Jackson Gabi \nHarrington: Gracie Lexi sophia'
    send_message(msg)
  elif data['text'] == '8:30':
    time.sleep(2)
    msg = msg + 'MSC: Landon Jonathan Wesley \nCommons: Mark Jackson Gabi \nHarrington: Gracie Lexi sophia'
    send_message(msg)
  elif data['text'] == '9:00':
    time.sleep(2)
    msg = msg + 'MSC: Landon Jonathan Cole Danya\nCommons: Mark Gabi \nHarrington: Gracie Lexi sophia Torey'
    send_message(msg)
  elif data['text'] == '9:30':
    time.sleep(2)
    msg = msg + 'MSC: Cole Jonathan Danya Mary Kate\nCommons: Mark Gabi \nHarrington: Gracie Lexi sophia Torey'
    send_message(msg)
  elif data['text'] == '10:00':
    time.sleep(2)
    msg = msg + 'MSC: Danya Cole Mary Kate \nCommons: Meg Mark Jonathan \nHarrington: Addie Lexi Torey'
    send_message(msg)
  elif data['text'] == '10:30':
    time.sleep(2)
    msg = msg + 'MSC: Mary Kate Cole Danya \nCommons: Mark Jonathan Meg \nHarrington: Addie Torey Alec Cameron'
    send_message(msg)
  elif data['text'] == '11:00':
    time.sleep(2)
    msg = msg + 'MSC: Bre Mary Kate Cole Danya\nCommons: Mark Jonathan Alec \nSbisa: Cameron Jarrod '
    send_message(msg)
  elif data['text'] == '11:30':
    time.sleep(2)
    msg = msg + 'MSC: Andrew Bre Gabi Noah\nCommons: Mark Oriana Jonathan \n Sbisa: Creel Cameron Jarrod'
    send_message(msg)
  elif data['text'] == '12:00':
    time.sleep(2)
    msg = msg + 'MSC: Andrew Bre Gabi Noah\nCommons: Kourtnei Oriana Mark \n Sbisa: Creel Cameron Jarrod'
    send_message(msg)
  elif data['text'] == '12:30':
    time.sleep(2)
    msg = msg + 'MSC: Andrew Bre Gabi \nCommons: Kourtnei Oriana Mark \n Sbisa: Addie Jarrod'
    send_message(msg)
  elif data['text'] == '1:00' or data['text'] == '13:00':
    time.sleep(2)
    msg = msg + 'MSC: Andrew Landon Thayer Gabi \nCommons: Kourtnei Aly Oriana \n Sbisa: Lexi Haley Jonathan'
    send_message(msg)
  elif data['text'] == '1:30' or data['text'] == '13:30':
    time.sleep(2)
    msg = msg + 'MSC: Andrew Landon Thayer Gabi \nCommons: Kourtnei Aly Oriana \n Sbisa: Lexi Haley Sidney'
    send_message(msg)
  elif data['text'] == '2:00' or data['text'] == '14:00':
    time.sleep(2)
    msg = msg + 'MSC: Andrew Landon Thayer Gabi Jacob\nCommons: Kourtnei Aly Bre Oriana\nHarrington: Creel Wesley Lexi Torey'
    send_message(msg)
  elif data['text'] == '2:30' or data['text'] == '14:30':
    time.sleep(2)
    msg = msg + 'MSC: Mary Kate Landon Thayer Gabi Jacob\nCommons: Kourtnei Aly Bre Oriana\nHarrington: Creel Wesley Torey Saul'
    send_message(msg)
  elif data['text'] == '3:00' or data['text'] == '15:00':
    time.sleep(2)
    msg = msg + 'MSC: Oriana Landon Thayer Jacob Mary Kate\nCommons: Bre Cameron Gabi Sidney\nHarrington: Addie Gracie Wesley Saul'
    send_message(msg)
  elif data['text'] == '3:30' or data['text'] == '15:30':
    time.sleep(2)
    msg = msg + 'MSC: Oriana Landon Thayer Jonathan Mary Kate\nCommons: Bre Cameron Gabi Creel\nHarrington: Addie Gracie Wesley Saul'
    send_message(msg)
  elif data['text'] == '4:00' or data['text'] == '16:00':
    time.sleep(2)
    msg = msg + 'MSC: Addie Landon Thayer Jonathan Mary Kate\nCommons: Creel Cameron Gabi Noah\nHarrington: Oriana Jarrod Gracie Saul'
    if data['text'] == '16:00':
      msg = msg + '\nF*** you, Landon C.'
    send_message(msg)
  elif data['text'] == '4:30' or data['text'] == '16:30':
    time.sleep(2)
    msg = msg + 'MSC: Addie Landon Thayer Andrew Mary Kate\nCommons: Creel Cameron Gabi Noah\nHarrington: Oriana Jarrod Gracie Saul\n'
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
    if data['text'] == '21:00'
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
