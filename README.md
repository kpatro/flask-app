# flask-app
### Directory Structure <br>
    flask-app
        |__ my_app.py
        |__ app_logging.cfg
        |__ requirements.txt
        |__ tests
                |__ conftest.py
                |__ test_my_app.py
### Prerequisites
1. pip install pytest
2. pip install flask
3. pip install flask-accept

    
### Steps to Run
#### Create and activate the virtual environment by issuing below commands. <br> 
    a. virtualenv venv
    b. source venv/bin/activate
#### Install Below pre-requisites (requirements.txt) <br>
    a. pip install pytest
    b. pip install flask 
    c. pip install flask-accept
#### Start Application <br>
    a. python my_app.py

#### Change to Debug Mode to show logs
    a. Navigate to directory where app_logging.cfg lives. flask_app -> app_logging.cfg
    b. At line 22 change level=DEBUG instead of INFO.
    c. Save it, close the config file and RESTART your App.
    d. Retest using Curl Commands provided.

#### Test the Application <br>
    python -m pytest -v
    OR
    pytest -v tests/test_my_app.py

#### command to validate with and without Accept Header <br>
    curl http://localhost:5000/ -H "Accept: application/json"
    curl http://localhost:5000/

