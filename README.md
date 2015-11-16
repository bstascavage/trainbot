trainbot
========

Dumbass bot that spams a groupme group when someone mentions a trigger word.

## Installation

1.  Create a bot on groupme (https://dev.groupme.com/bots).  Make sure your Callback URL is set to 'http://<YOUR_FQDN>:8080/trainbot'
2.  Clone this repo:

    `git clone https://github.com/bstascavage/trainbot.git`

3.  Change to the trainbot directory
4.  Rename `trainbot.conf.example` to `trainbot.conf` and make sure the config file is complete.
5.  Run the webapp:

    `python trainbot.wsgi`

## Test cases
All test cases are located in the `test_cases` directory.  You can add your own test_cases files, or add your own to the existing files.

To run the test_cases, run:

`python -m unittest discover -v -p 'test*.py' -s 'test_cases/'`
