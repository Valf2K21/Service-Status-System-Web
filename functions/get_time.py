# import dependencies
from datetime import datetime

# FIRST PART OF PROGRAM CODE: USER-DEFINED FUNCTION FOR CLOCK
# create class to provide real-time day, date, and time
def get_time():
    # get current time in this format: Monday, 12/31/2023 23:59:59
    currentTime = datetime.now().strftime('%A, %m/%d/%Y %H:%M:%S')
    
    # return currentTime to function that requests it
    return currentTime