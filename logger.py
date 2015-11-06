import os
import logging 

class Logger:
    def __init__(self, type, logging_path):
	self.logger = logging.getLogger(type)

	hdlr = logging.FileHandler(logging_path)
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)

	self.logger.addHandler(hdlr) 
	self.logger.setLevel(logging.INFO)

    def error(self, message):
	self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def warn(self, message):
        self.logger.warn(message)

    def info(self, message):
        self.logger.info(message)
