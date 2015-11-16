import os, json, sys
import time
import re

sys.path.append('/var/www/trainbot')
from groupme import Groupme

class TrainLogic:
    def __init__(self, config, logger):
	self.groupme = Groupme(config, logger)
	self.config = config
	self.logger = logger
	self.messages = []

    def process_message(self, message):
	if message['user_id'] != self.config.ConfigSectionMap('groupme')['bot_user_id']:
	    if not message['id'] in self.messages:
	        self.messages.append(message['id'])
		if self.checkMessage(message['text']):
		    responsetextfile = self.config.ConfigSectionMap('bot')['textfile']
		    f = open('/var/www/trainbot/traintext.txt', "r")
		    lines = f.readlines()
		    f.close()
		    time.sleep(1)

		    for line in lines:
			if 'jpeg' in line:
		  	    self.groupme.post_message('', line)
			else:
			    self.groupme.post_message(line)
			time.sleep(1.2)


    def checkMessage(self, text):
	dictionary = self.config.ConfigSectionMap('bot')['trigger_words'].split()

	sentence = text.split()
	sentence = [word.encode('utf-8') for word in sentence]
        sentence = [word.lower() for word in sentence]
	sentence = [word.replace(".", "") for word in sentence]
        sentence = [word.replace(",", "") for word in sentence]
  	if set(dictionary).intersection(sentence):
	    return True
