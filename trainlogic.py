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
		dictionary = self.config.ConfigSectionMap('bot')['trigger_words'].split()

		sentence = message['text'].split()
		sentence = [word.encode('utf-8') for word in sentence]
                sentence = [word.lower() for word in sentence]
		sentence = [word.replace(".", "") for word in sentence]
                sentence = [word.replace(",", "") for word in sentence]
		if set(dictionary).intersection(sentence):
		    time.sleep(1)
		    print "Received message: %s" % message
  		    self.logger.info("Received message: %s" % message)
	            self.groupme.post_message('HEEEEEERE THEY COME!', 'http://i.groupme.com/350x460.jpeg.91879800f84743648a947d7080d35380.large')
		    time.sleep(1.2)
		    self.groupme.post_message('CLICKETY-CLACK')
                    time.sleep(1.2)
                    self.groupme.post_message('D')
                    time.sleep(1.2)
                    self.groupme.post_message('O')
                    time.sleep(1.2)
                    self.groupme.post_message('W')
                    time.sleep(1.2)
                    self.groupme.post_message('N')
                    time.sleep(1.2)
                    self.groupme.post_message(' ')
                    time.sleep(1.2)
                    self.groupme.post_message('T')
                    time.sleep(1.2)
                    self.groupme.post_message('H')
                    time.sleep(1.2)
                    self.groupme.post_message('E')
                    time.sleep(1.2)
                    self.groupme.post_message(' ')
                    time.sleep(1.2)
                    self.groupme.post_message('T')
                    time.sleep(1.2)
                    self.groupme.post_message('R')
                    time.sleep(1.2)
                    self.groupme.post_message('A')
                    time.sleep(1.2)
                    self.groupme.post_message('C')
                    time.sleep(1.2)
                    self.groupme.post_message('K')
                    time.sleep(1.2)
                    self.groupme.post_message('S')
                    time.sleep(1.2)
                    self.groupme.post_message('!')
                    time.sleep(1.2)
                    self.groupme.post_message("IT'S LOTS & LOTS OF TRAINS!")
