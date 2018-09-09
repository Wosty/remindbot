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
  
  if ':' not in data['text']:
    return "ok", 200
  
  msg = data['text'] + ' Shifts\n'
  given = data['text'].strip().split(':')
  given = [int(i) for i in given]
  if given[0] != 12:
    given[0] = given[0]%12
  time = given[0] + ':' + given[1]
  row = [int(worksheet.find(time).row)]
  dv = [2, 3, 4]
  dv = [int(i) for i in dv]
  msg = msg + 'Chair/Exec:'
  for i in dv:
    msg = msg + ' ' + worksheet.cell(row[0], i).value
  msg = msg + '\n'
  row = [row[0]+1, row[0]+2]
  for i in dv:
    msg = msg + worksheet.cell(2, i).value + ':'
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
