import json
import requests 
import six
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
	    content = requests.post(self.config.ConfigSectionMap('groupme')['url'], data=json.dumps(message))
	except:
	    self.logger.error("Cannot connect to groupme. The glory of trains will go unheard.")
