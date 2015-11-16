import json
import requests 
import six
import time
from six.moves.urllib import parse as urlparse

class Groupme:
    def __init__(self, config, logger):
	self = self
        self.config = config
        self.logger = logger

    def post_message(self, message, image=None):
	if image is None:
	    message = {
		"text": message,
		"bot_id": self.config.ConfigSectionMap('groupme')['bot_id'],
	    }
	else:
	    message = {
                "text": message,
                "bot_id": self.config.ConfigSectionMap('groupme')['bot_id'],
		"attachments": [
		    {
			"type": "image",
			"url": image
		    }
		]
            }
	try:
	    retry = 0
	    while retry < 20:
	    	content = requests.post(self.config.ConfigSectionMap('groupme')['url'], data=json.dumps(message))
	    	self.logger.info("Send groupme message: %s" % message)
	    	self.logger.info("Groupme response: %s" % content.status_code)

		if content.status_code != 202:
		    self.logger.info("Message not sent to groupme.  Retrying...")
		    retry += 1
		    time.sleep(5)
		else:
		    retry = 20
	    
	except:
	    self.logger.error("Cannot connect to groupme. The glory of trains will go unheard.")
