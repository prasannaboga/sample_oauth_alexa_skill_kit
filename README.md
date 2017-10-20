### Setup

Install [pip](http://pip.readthedocs.org/en/stable/installing/). Then:
```commandline
pip install virtualenv
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Check installation successfully by running following commands are relative to the virtualenv:
```commandline
which python
which pip
```

### Test
Runs all tests
```commandline
python -m unittest discover
```

Runs tests for a specific module
```commandline
python -m unittest tests.test_utils
```

Runs tests a specific class
```commandline
python -m unittest tests.test_utils.TestUtils
```

Runs one specific test
```commandline
python -m unittest tests.test_utils.TestUtils.test_flatten
```

### Lambda Execution & Deploy
Copy config.sample.yaml file to cofig.yaml

```commandline
$ cp config.sample.yaml cofig.yaml 
```
Execute lambda function    
```commandline
$ lambda invoke -v
```
Deploy lambda function
```commandline
$ lambda deploy
```
    
