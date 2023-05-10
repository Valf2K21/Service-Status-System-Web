# SEVENTH PART OF PROGRAM CODE: INITIALIZATION
# import dependencies
from flask import Flask, render_template, jsonify
import logging

# import user-created dependencies
from functions.get_time import get_time
from functions.plate_updater import plate_updater

# configure logging to only show error level messages
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# create a Flask web application instance
app = Flask(__name__)

# define path to function that will return current time as JSON object
@app.route('/time', methods = ['GET'])

# create user-defined function for current date grabber
def time_grab():
    # call get_time() function and return its result in time variable
    time = get_time()
    
    # return time to base template as json file using jsonify
    return jsonify(result = time)

# define path to function that will return current allPlates as JSON object
@app.route('/plates', methods = ['GET'])

# create user-defined function for current allPlates grabber
def plates_grab():
    # call plate_updater() function and return its result in plates variable
    allPlates = plate_updater()
    
    # return plates to base template as json file using jsonify
    return jsonify(allPlates)

# define path to activate function below
@app.route('/')

# create user-defined function for service board to return what to display at user
def service_board():
    # use render_template() function to grab HTML template and return to display said template
    return render_template('base.html')

# if-statement to run Flask web application instance
if __name__ == '__main__':
    print('Service Board Link: http://127.0.0.1:5000/')
    app.run()

