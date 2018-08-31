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
    msg = 'MSC: Landon Cameron Wesley \nCommons: Mark Jackson Gabi \nHarrington: Gracie Lexi sophia'
    send_message(msg)
  elif data['text'] == '8:30':
    time.sleep(2)
    msg = 'MSC: Landon Jonathan Wesley \nCommons: Mark Jackson Gabi \nHarrington: Gracie Lexi sophia'
    send_message(msg)
  elif data['text'] == '9:00':
    time.sleep(2)
    msg = 'MSC: Landon Jonathan Cole Danya\nCommons: Mark Gabi \nHarrington: Gracie Lexi sophia Torey'
    send_message(msg)
  elif data['text'] == '9:30':
    time.sleep(2)
    msg = 'MSC: Cole Jonathan Danya Mary Kate\nCommons: Mark Gabi \nHarrington: Gracie Lexi sophia Torey'
    send_message(msg)
  elif data['text'] == '10:00':
    time.sleep(2)
    msg = 'MSC: Danya Cole Mary Kate \nCommons: Meg Mark Jonathan \nHarrington: Addie Lexi Torey'
    send_message(msg)
  elif data['text'] == '10:30':
    time.sleep(2)
    msg = 'MSC: Mary Kate Cole Danya \nCommons: Mark Jonathan Meg \nHarrington: Addie Torey Alec Cameron'
    send_message(msg)
  elif data['text'] == '11:00':
    time.sleep(2)
    msg = 'MSC: Bre Mary Kate Cole Danya\nCommons: Mark Jonathan Alec \nSbisa: Cameron Jarrod '
    send_message(msg)
  elif data['text'] == '11:30':
    time.sleep(2)
    msg = 'MSC: Andrew Bre Gabi Noah\nCommons: Mark Oriana Jonathan \n Sbisa: Creel Cameron Jarrod'
    send_message(msg)
  elif data['text'] == '12:00':
    time.sleep(2)
    msg = 'MSC: Andrew Bre Gabi Noah\nCommons: Kourtnei Oriana Mark \n Sbisa: Creel Cameron Jarrod'
    send_message(msg)
  elif data['text'] == '12:30':
    time.sleep(2)
    msg = 'MSC: Andrew Bre Gabi \nCommons: Kourtnei Oriana Mark \n Sbisa: Addie Jarrod'
    send_message(msg)
  elif data['text'] == '1:00':
    time.sleep(2)
    msg = 'MSC: Andrew Landon Thayer Gabi \nCommons: Kourtnei Aly Oriana \n Sbisa: Lexi Haley Jonathan'
    send_message(msg)
  elif data['text'] == '1:30':
    time.sleep(2)
    msg = 'MSC: Andrew Landon Thayer Gabi \nCommons: Kourtnei Aly Oriana \n Sbisa: Lexi Haley Sidney'
    send_message(msg)
  elif data['text'] == '2:00':
    time.sleep(2)
    msg = 'MSC: Andrew Landon Thayer Gabi Jacob\nCommons: Kourtnei Aly Bre Oriana\nHarrington: Creel Wesley Lexi Torey'
    send_message(msg)
  elif data['text'] == '2:30':
    time.sleep(2)
    msg = 'MSC: Mary Kate Landon Thayer Gabi Jacob\nCommons: Kourtnei Aly Bre Oriana\nHarrington: Creel Wesley Torey Saul'
    send_message(msg)
  elif data['text'] == '3:00':
    time.sleep(2)
    msg = 'MSC: Oriana Landon Thayer Jacob Mary Kate\nCommons: Bre Cameron Gabi Sidney\nHarrington: Addie Gracie Wesley Saul'
    send_message(msg)
  elif data['text'] == '3:30':
    time.sleep(2)
    msg = 'MSC: Oriana Landon Thayer Jonathan Mary Kate\nCommons: Bre Cameron Gabi Creel\nHarrington: Addie Gracie Wesley Saul'
    send_message(msg)
  elif data['text'] == '4:00':
    time.sleep(2)
    msg = 'MSC: Addie Landon Thayer Jonathan Mary Kate\nCommons: Creel Cameron Gabi Noah\nHarrington: Oriana Jarrod Gracie Saul'
    send_message(msg)
  elif data['text'] == '4:30':
    time.sleep(2)
    msg = 'MSC: Addie Landon Thayer Andrew Mary Kate\nCommons: Creel Cameron Gabi Noah\nHarrington: Oriana Jarrod Gracie Saul\n'
    send_message(msg)
  elif data['text'] == '5:00':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '5:30':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '6:00':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '6:30':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '7:00':
    time.sleep(2)
    msg = 'Y\'all done hoes'
    send_message(msg)
  elif data['text'] == '7:30':
    time.sleep(2)
    msg = 'Y\'all done hoes'
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
