import os, sys
import configparser

CONF = configparser.ConfigParser()

class Config:
    def __init__(self, config_path, logger):
        CONF.read(os.path.realpath(config_path))
	self.logger = logger

    def ConfigSectionMap(self, section):
        dict1 = {}
        options = CONF.options(section)
        for option in options:
            try:
                dict1[option] = CONF.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                self.logger.error("exception on %s!" % option)
                dict1[option] = None
        return dict1
