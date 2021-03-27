# flask-app
##Directory Structure <br>
    |--> my_app.py
    |--> app_logging.cfg
    |--> requirements.txt
    |--> tests
    ****|--> conftest.py
    ****|--> test_my_app.py
## Prerequisites
1. pip install pytest
2. pip install flask
3. pip install flask-accept

    
## Steps to Run
###Create and activate the virtual environment by issuing below commands. <br> 
    a. virtualenv venv
    b. source venv/bin/activate
###Install Below pre-requisites (requirements.txt) <br>
    a. pip install pytest
    b. pip install flask 
    c. pip install flask-accept
###Start Application <br>
    a. python my_app.py

### Change to Debug Mode to show logs
1. Navigate to directory where app_logging.cfg lives. flask_app -> app_logging.cfg
2. At line 22 change level=DEBUG instead of INFO.
3. Save it, close the config file and restart your App.
4. Retest using Curl Commands provided.

### Test the Application <br>
python -m pytest -v <br>
OR <br>
pytest -v tests/test_my_app.py

### Sample command to Validate with and without Accept Header <br>
curl -XGET http://localhost:5000/ -H "Accept: application/json"
curl -XGET http://localhost:5000/

