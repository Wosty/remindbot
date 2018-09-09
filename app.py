import os
import sys
import json
import time
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request
app = Flask(__name__)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
if credentials.access_token_expired:
  gc.login()
  msg = '*'
  send_message(msg)
@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  
  sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1xmUic-CfN6tcUVfYfOS2nyHcyNHy8J5XfM5IVO0vStY/edit?usp=sharing')
  worksheet = sh.worksheet("Interview Staff Sign Ups")
  
  
  msg = data['text'] + ' Shifts\n'
  row = [int(worksheet.find((data['text']).strip()).row)]
  dv = [2, 3, 4]
  dv = [int(i) for i in dv]
  row = [int(i) for i in row]
  msg = msg + 'Chair/Exec:'
  for i in dv:
    msg = msg + ' ' + worksheet.cell(row, i).value
  msg = msg + '\n'
  row = [row[0]+1, row[0]+2]
  for i in dv:
    msg = msg + worksheet.cell(2, i) + ':'
    for j in row:
      msg = msg + ' ' + worksheet.cell(j, i).value
    msg = msg + '\n'
  faceList = open('faces.txt','r').readlines()
  msg = msg + random.choice(faceList).strip('\n')
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
