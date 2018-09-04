import os
import sys
import json
import time
import gspread

from oauth2client.service_account import ServiceAccountCredentials
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_p12_keyfile('remindboi@remindboi-1535675457929.iam.gserviceaccount.com', 'credentials.p12', scope, 'PASSWORD')

gc = gspread.authorize(credentials)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  
  sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1xmUic-CfN6tcUVfYfOS2nyHcyNHy8J5XfM5IVO0vStY/edit?usp=sharing')
  worksheet = sh.worksheet("Bannerz")
  
  
  msg = data['text'] + ' Shifts\n\n'
  dv = [21, 22, 23, 24]
  dv = [int(i) for i in dv]
  
  if data['text'] == '8:00':
    #msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    time.sleep(2)
    row = 10
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '8:30':
    time.sleep(2)
    row = 13
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '9:00':
    time.sleep(2)
    row = 16
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '9:30':
    time.sleep(2)
    row = 19
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '10:00':
    time.sleep(2)
    row = 22
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '10:30':
    time.sleep(2)
    row = 25
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '11:00':
    time.sleep(2)
    row = 28
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nSbisa: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '11:30':
    time.sleep(2)
    row = 31
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nSbisa: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '12:00':
    time.sleep(2)
    row = 34
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nSbisa: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '12:30':
    time.sleep(2)
    row = 37
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nSbisa: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '1:00' or data['text'] == '13:00':
    time.sleep(2)
    row = 40
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nSbisa: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '1:30' or data['text'] == '13:30':
    time.sleep(2)
    row = 43
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nSbisa: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '2:00' or data['text'] == '14:00':
    time.sleep(2)
    row = 46
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '2:30' or data['text'] == '14:30':
    time.sleep(2)
    row = 49
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '3:00' or data['text'] == '15:00':
    time.sleep(2)
    row = 52
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '3:30' or data['text'] == '15:30':
    time.sleep(2)
    row = 55
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '4:00' or data['text'] == '16:00':
    time.sleep(2)
    row = 58
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
    send_message(msg)
  elif data['text'] == '4:30' or data['text'] == '16:30':
    time.sleep(2)
    row = 61
    msg = msg + 'MSC: ' + worksheet.cell(row, dv[0]).value + ' ' + worksheet.cell(row, dv[1]).value + ' ' + worksheet.cell(row, dv[2]).value + ' ' + worksheet.cell(row, dv[3]).value
    msg = msg + '\nCommons: '  + worksheet.cell(row+1, dv[0]).value + ' ' + worksheet.cell(row+1, dv[1]).value + ' ' + worksheet.cell(row+1, dv[2]).value + ' ' + worksheet.cell(row+1, dv[3]).value
    msg = msg + '\nHarrington: '  + worksheet.cell(row+2, dv[0]).value + ' ' + worksheet.cell(row+2, dv[1]).value + ' ' + worksheet.cell(row+2, dv[2]).value + ' ' + worksheet.cell(row+2, dv[3]).value
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
  elif ':' in data['text'][:4] and data['sender_type'] != 'bot':
    faceList = open('faces.txt','r').readlines()
    msg = random.choice(faceList).strip('\n')
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
