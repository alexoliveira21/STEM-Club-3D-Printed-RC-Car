$(document).ready(function(){

  var speedOutput = document.getElementById("speedValue");
  var steeringSlider = document.getElementById("steering");
  var steeringOutput = document.getElementById("steeringValue");
  var stopButton = document.getElementById("stopButton");
  var increaseSpeed = document.getElementById("increaseSpeed");
  var decreaseSpeed = document.getElementById("decreaseSpeed");
  var recordButton = document.getElementById("recordButton");
  var recordingOutput = document.getElementById("recordingValue");

  recordingOutput.innerHTML = "Not Recording";
  increaseSpeed.value = "90";
  decreaseSpeed.value = "90";
  steeringSlider.value = "100";

  stopButton.onclick = function(){

    recordingOutput.innerHTML = "Stopped Recording";

    increaseSpeed.value = "90";
    decreaseSpeed.value = "90";
    steeringSlider.value = "100";

    push_data(increaseSpeed.value, steeringSlider.value, "/stop");
    
    speedOutput.innerHTML = increaseSpeed.value;
    steeringOutput.innerHTML = steeringValue.value;
  };

  recordButton.onclick = function(){

    push_data(increaseSpeed.value, steeringSlider.value, "/record_data");
    if (recordingOutput.innerHTML == "Not Recording" || recordingOutput.innerHTML == "Stopped Recording"){
      recordingOutput.innerHTML = "Currently Recording";
    }
  }

  increaseSpeed.onclick = function(){

    increaseSpeed.value = String(parseInt(increaseSpeed.value)+2);
    decreaseSpeed.value = increaseSpeed.value;
    speedOutput.innerHTML = increaseSpeed.value;
    push_data(increaseSpeed.value, steeringSlider.value, "/change_speed");

  };

  decreaseSpeed.onclick = function(){

    increaseSpeed.value = String(parseInt(increaseSpeed.value)-2);
    decreaseSpeed.value = increaseSpeed.value;
    speedOutput.innerHTML = increaseSpeed.value;
    push_data(increaseSpeed.value, steeringSlider.value, "/change_speed");

  };

  steeringSlider.oninput = function() {

    steeringOutput.innerHTML = steeringSlider.value;
    push_data(increaseSpeed.value, steeringSlider.value, "/data_update");

  };

});

function push_data(speed, steering, url){

  var results = {"speed": speed, "steering": steering};
  console.log(results);

  $.ajax({
    type: "POST",
    url: url,
    crossDomain: true,
    data: results,
    contentType: "application/json",
    dataType: "jsonp",
    success: function(data, status){
      //alert("Data: " + data + "\nStatus: :" + status);
    }
  });

};
