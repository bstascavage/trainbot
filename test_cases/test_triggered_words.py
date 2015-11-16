import unittest
import sys

sys.path.append('/var/www/trainbot')
from trainlogic import TrainLogic as Trainlogic
from config import Config
from logger import Logger

# Here's our "unit tests".
class IsCorrectStringTests(unittest.TestCase):
    def setUp(self):
	logger = Logger('trainlogger', '/var/log/trainbot.log')
	config = Config('/var/www/trainbot/trainbot.conf', logger)
	global TrainLogic
	TrainLogic = Trainlogic(config, logger)

    def testTrain(self):
        self.assertTrue(TrainLogic.checkMessage('train'))

    def testTrains(self):
        self.assertTrue(TrainLogic.checkMessage('trains'))
