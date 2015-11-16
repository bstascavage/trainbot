import unittest
import sys

sys.path.append('/var/www/trainbot')
from trainlogic import TrainLogic as Trainlogic
from config import Config
from logger import Logger

# Here's our "unit tests".
class IsIncorrectStringTests(unittest.TestCase):
    def setUp(self):
        logger = Logger('trainlogger', '/var/log/trainbot.log')
        config = Config('/var/www/trainbot/trainbot.conf', logger)
        global TrainLogic
        TrainLogic = Trainlogic(config, logger)

    def testTraining(self):
        self.assertFalse(TrainLogic.checkMessage('training'))
