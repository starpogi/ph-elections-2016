# Which Philippine Presidential Candidate Are You
[![Build Status](https://travis-ci.org/starpogi/ph-elections-2016.svg?branch=master)](https://travis-ci.org/starpogi/ph-elections-2016)

Simple quiz to figure out which 2016 Presidential Candidate are you.

## Environment setup
To setup the environment, run this script
```
$ tools/setup.sh
```

Once the environment has been setup, don't forget to activate your virtual
environment when doing dev work
```
$ source tools/venv/bin/activate
```

Then, activate the web server by running
```
$ python web_server.py
```

This will spin up a Flask web server. For local development, it will create
a Web server at port `5000`, and is accessible by going to `http://127.0.0.1:5000`

For live deployment, Heroku will take care of spinning up the web server.

To add more module dependencies, modify `tools/requirements.txt`. Add the version
when you can so that you can stick with the version that works with your current
program. If not, a new module version might break your code.

## Testing
To run unit tests, do

```
$ nosetests
```

at the root directory. This repo is also connected to Travis CI
