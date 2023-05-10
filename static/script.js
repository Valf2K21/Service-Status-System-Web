console.log('script.js imported successfully')

// a variable to hold root url for web app
var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};

// create a function to update time value every 200ms
var timeInterval = setInterval(update_time,1000);

// create a function to get current time value from server and update display
function update_time() {
  $.getJSON($SCRIPT_ROOT + '/time',
    function(currentTime) {
      $('#result').text(currentTime.result);
    });
};

// create a function to update plates every 5 minutes
var platesInterval = setInterval(update_plates,5000);

// create a function to get current allPlates dictionary from server and update display
// idea: since currentTime is a dictionary from get_time() function, I can replace it with allPlates
// idea2: also, I think I can replace result into column name (counter, in progress, completed)
// to-do: the goal for this function is to turn it into something like plate_generator of my tkinter prototype
// add: also, check if the order of the plates in the json file is the same as the order in my tkinter prototype
function update_plates() {
  // for counter column
  $.getJSON($SCRIPT_ROOT + '/plates',
    function(allPlates) {
      // put list of lists of counter key in a new variable
      var counterList = allPlates.counter;

      // create an empty array to store generated plates later
      var generated = [];

      // flush all existing elements in this id
      $('#counter').empty();

      // for-loop to loop through every list of counterList list of lists
      for (var i = 0; i < counterList.length; i++) {
        // put content in their respective variables
        var currentList = counterList[i];
        var plateNo = currentList[0];
        var appoint = currentList[2];

        // if plateNo is empty or N/A...
        if (!plateNo || plateNo === 'N/A') {
          // use csno as plateNo instead
          var plateNo = currentList[1];
        }

        // if appoint of plateNo is 1 and plateNo is not yet generated...
        if (appoint === '1' && !generated.includes(plateNo)) {
          // display plateNo using <p> element that uses walk-in_plate CSS class
          $('#counter').append('<p class="walk-in_plate">' + plateNo + '</p>' + '<br>');

          // add used plateNo in generated variable
          generated.push(plateNo)
        }

        // else if appoint of plateNo is 2-4 and plateNo is not yet generated...
        else if (appoint >= '1' && appoint <= '5' && !generated.includes(plateNo)) {
          // display plateNo using <p> element that uses booking_plate CSS class
          $('#counter').append('<p class="booking_plate">' + plateNo + '</p>' + '<br>');

          // add used plateNo in generated variable
          generated.push(plateNo)
        }
      }

      // append generated plates in the counter column via <div> with counter as its id
      $('#counter').append('<br>');
    });

  // for progress column
  $.getJSON($SCRIPT_ROOT + '/plates',
    function(allPlates) {
      // put list of lists of progress key in a new variable
      var progressList = allPlates.progress;

      // create an empty array to store generated plates later
      var generated = [];

      // flush all existing elements in this id
      $('#progress').empty();

      // for-loop to loop through every list of progressList list of lists
      for (var i = 0; i < progressList.length; i++) {
        // put content in their respective variables
        var currentList = progressList[i];
        var plateNo = currentList[0];
        var appoint = currentList[2];

        // if plateNo is empty or N/A...
        if (!plateNo || plateNo === 'N/A') {
          // use csno as plateNo instead
          var plateNo = currentList[1];
        }

        // if appoint of plateNo is 1 and plateNo is not yet generated...
        if (appoint === '1' && !generated.includes(plateNo)) {
          // display plateNo using <p> element that uses walk-in_plate CSS class
          $('#progress').append('<p class="walk-in_plate">' + plateNo + '</p>' + '<br>');

          // add used plateNo in generated variable
          generated.push(plateNo)
        }

        // else if appoint of plateNo is 2-4 and plateNo is not yet generated...
        else if (appoint >= '1' && appoint <= '5' && !generated.includes(plateNo)) {
          // display plateNo using <p> element that uses booking_plate CSS class
          $('#progress').append('<p class="booking_plate">' + plateNo + '</p>' + '<br>');

          // add used plateNo in generated variable
          generated.push(plateNo)
        }
      }

      // append generated plates in the in progress column via <div> with progress as its id
      $('#progress').append('<br>');
    });

  // for completed column
  $.getJSON($SCRIPT_ROOT + '/plates',
    function(allPlates) {
      // put list of lists of completed key in a new variable
      var completedList = allPlates.completed;

      // create an empty array to store generated plates later
      var generated = [];

      // flush all existing elements in this id
      $('#completed').empty();

      // for-loop to loop through every list of completedList list of lists
      for (var i = 0; i < completedList.length; i++) {
        // put content in their respective variables
        var currentList = completedList[i];
        var plateNo = currentList[0];
        var appoint = currentList[2];

        // if plateNo is empty or N/A...
        if (!plateNo || plateNo === 'N/A') {
          // use csno as plateNo instead
          var plateNo = currentList[1];
        }

        // if appoint of plateNo is 1 and plateNo is not yet generated...
        if (appoint === '1' && !generated.includes(plateNo)) {
          // display plateNo using <p> element that uses walk-in_plate CSS class
          $('#completed').append('<p class="walk-in_plate">' + plateNo + '</p>' + '<br>');

          // add used plateNo in generated variable
          generated.push(plateNo)
        }

        // else if appoint of plateNo is 2-4 and plateNo is not yet generated...
        else if (appoint >= '1' && appoint <= '5' && !generated.includes(plateNo)) {
          // display plateNo using <p> element that uses booking_plate CSS class
          $('#completed').append('<p class="booking_plate">' + plateNo + '</p>' + '<br>');

          // add used plateNo in generated variable
          generated.push(plateNo)
        }
      }
      // append generated plates in the completed column via <div> with completed as its id
      $('#completed').append('<br>');
    });
};