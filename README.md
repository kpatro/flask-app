# flask-app
### Directory Structure <br>
    flask-app
        |__ my_app.py
        |__ app_logging.cfg
        |__ requirements.txt
        |__ tests
                |__ conftest.py
                |__ test_my_app.py
        |-- [venv-flask-app] --> need to be configured locally

### Prerequisites
    a. python3
    b. pytest
    c. flask
    d. flask-accept

    
### Steps to Run
#### Create and activate the virtual environment by issuing below commands. 
    a. python3 -m venv venv-flask-app && source venv-flask-app/bin/activate

#### Install Below pre-requisites (requirements.txt).
    b. pip install pytest
    c. pip install flask 
    d. pip install flask-accept

#### Start & Stop Application
    e. python my_app.py ( At any time hit [ctrl+c] to stop the app )

#### command to validate with and without Accept Header. 
    f. Ensure app is running as per above step, Issue below commands in a different terminal.
        curl http://localhost:5000/ -H "Accept: application/json"
        curl http://localhost:5000/
    g. At any time hit [ctrl+c] to stop the app

#### Change to Debug Mode to show logs
    a. Navigate to directory where app_logging.cfg lives. flask_app -> app_logging.cfg
    b. At line 22 change level=DEBUG instead of INFO in [handler_consoleHandler]
    c. Save it, close the config file and RESTART your App.
    d. Retest using Curl Commands provided above.

#### Test the Application
    python -m pytest -v OR
    pytest -v tests/test_my_app.py