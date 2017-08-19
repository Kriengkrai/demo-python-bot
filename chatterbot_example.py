#!/usr/bin/env python
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("PYTHON BOT")
conversation = [
  u"สวัสดี",
  u"ดีจ้า",
  u"ทำไรอยู่",
  u"กินข้าว"
]
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
print "\nReady!"
while(True):
  raw = raw_input('> ')
  decoded = raw.decode("utf-8")
  response = chatbot.get_response(decoded)
  print unicode(response)