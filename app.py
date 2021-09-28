# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.raw.functions.channels import GetLeftChannels

load_dotenv() #loading environment variables from .env file

client = Client(os.environ.get("SESSION_STRING"),os.environ.get("API_ID"),os.environ.get("API_HASH"),takeout=True)

client.start()
co = client.get_dialogs_count()
chats1 = client.iter_dialogs(co+(co//100)) #using this instead of 'client.iter_dialogs()' due to a bug in Pyrogram 1.2.9
for x in chats1:
    if x['chat']['type'] == 'channel' or x['chat']['type'] == 'supergroup':
        print(x['chat']['title'],'@{}'.format(x['chat']['username']),"---",x['chat']['id'])
    if x['chat']['type'] == 'bot':
        print(x['chat']['first_name'],'@{}'.format(x['chat']['username']),"---",x['chat']['id'])
    if x['chat']['type'] == 'private':
        print(x['chat']['first_name'],x['chat']['last_name'],'@{}'.format(x['chat']['username']),"---",x['chat']['id'])
print('\nContacts:')
for x in client.get_contacts():
    print(x['first_name'],x['last_name'],'@{}'.format(x['username']),"---",x['id'])
print('\nLeft Channels/supergroups:')
chats2 = client.send(GetLeftChannels(offset=0))
for x in chats2['chats']:
    print(x['title'],'@{}'.format(x['username']),"---",'-100{}'.format(x['id']))

client.stop()