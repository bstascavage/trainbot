import sys

from flask import Flask, request
from config import Config
from logger import Logger

sys.path.append('/var/www/trainbot')
from trainlogic import TrainLogic
app = Flask(__name__)

logger = Logger('trainlogger', '/var/log/trainbot.log')
config = Config('/var/www/trainbot/trainbot.conf', logger)
TrainLogic = TrainLogic(config, logger)

@app.route("/trainbot", methods=['POST'])
def trainbot():
    TrainLogic.process_message(request.json)
    return request.data

if __name__ == "__main__":
#    app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
