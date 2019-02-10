/* 
@author: Gaurav Agarwal
@description: The main JS file.
@Date: 2nd Dec 2018. 
*/

var _streamCopy = null;     // used to stop the webcam video transmission
var video = null;
var foodItem = null;

function hasGetUserMedia() {
    return !!(navigator.mediaDevices &&
        navigator.mediaDevices.getUserMedia);
}

/**
 * Checks whether the browser supports the getUserMedia() function for WebCam access.
 */
function checkBrowserSupport() {
    if (hasGetUserMedia()) {
        // Good to go!
        getWebcamFeed();
    } else {
        alert('-----Please update your browser-----\nCertain features are not supported by your browser!');
    }
}

/**
 * Displays the web cam feed on the webpage.
 */
function getWebcamFeed() {
    // enable the screenshot button "Find calories"
    $("#btnFindCal").prop("disabled", false);
    // hide the previous screenshot
    $('#screenshotPreview').hide();
    // disable the add to database "consume it" button
    $("#btnConsumeCal").prop("disabled", true);

    const constraints = {
        video: true
    };

    video = document.querySelector('video');
    video.style.display = "block";
    if (_streamCopy) video.srcObject = _streamCopy;
    else
        navigator.mediaDevices.getUserMedia(constraints).
            then((stream) => {
                _streamCopy = stream;
                video.srcObject = stream
            });
}
/**
 * Displays the image captured from the video feed over the video box
 */
function showScreenshot() {
    // disable the screenshot button "Find calories"
    $("#btnFindCal").prop("disabled", true);
    // enable the add to database "consume it" button
    $("#btnConsumeCal").prop("disabled", false);

    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    // Other browsers will fall back to image/png
    const img = $('#screenshotPreview');
    img.show();
    img.attr("src", canvas.toDataURL('image/webp'));
    img.attr("width", video.videoWidth);
    disableWebcamFeed();
    sendImgToDetect(canvas.toDataURL('image/jpeg'));
}


/**
 * Disables the web cam feed displayed on the webpage
 */
function disableWebcamFeed() {
    try {
        // _streamCopy.stop(); // if this method doesn't exist, the catch will be executed.
    } catch (e) {
        // _streamCopy.getVideoTracks()[0].stop(); // then stop the first video track of the stream
    }
    finally {
        video.srcObject = null;
        video.style.display = "none";
    }
}

/**
 * resets the webcam and clears the screen.
 */
function resetFields() {
    disableWebcamFeed();
    $('#recognizedFood').text("");
    $('#itemCalories').text("");
    $('#count').text("");
    $('#totalCalories').text("");
    getWebcamFeed();
}

/**
 * update the consumption count in the datastore throught WS call.
 */
function consumeItem() {
    var jsonQuery = {
        foodItem: foodItem
    }
    $.ajax({
        // dataType is what you receive from the WS
        dataType: "json",
        url: "http://127.0.0.1:5000/updateCount",
        data: JSON.stringify(jsonQuery),
        method: 'POST',
        crossDomain: true,
        contentType: 'application/json; charset=utf-8',
        success: function () {
            alert("Successfully added");
            resetFields();
        },
        error: ajaxFailure
    });
}

/**
 * Calls web service over ajax to classify the image
 * @param {String} base64_img 
 */
function sendImgToDetect(base64_img) {
    base64_img = base64_img.replace('data:image/jpeg;base64,', '');
    var jsonQuery = {
        image: "" + base64_img
    }
    // console.log(base64_img);
    $.ajax({
        // dataType is what you receive from the WS
        dataType: "json",
        url: "http://127.0.0.1:5000/trackCalorie",
        data: JSON.stringify(jsonQuery),
        method: 'POST',
        // xhrFields: {
        //     withCredentials: true
        // },
        crossDomain: true,
        contentType: 'application/json; charset=utf-8',
        // timeout: 50000,
        success: classifyAjaxSuccess,
        error: ajaxFailure
    });
}

function classifyAjaxSuccess(result) {
    // result = JSON.parse(result);
    foodItem = result.foodItem; // don't remove this, it's a global variable
    $('#recognizedFood').text(foodItem);
    $('#itemCalories').text(result.calories);
    $('#count').text(result.count);
    $('#totalCalories').text(result.totalConsumed);

}

function ajaxFailure(jqXHR, textStatus, errorThrown) {
    disableWebcamFeed();
    alert(jqXHR.status + " : " + textStatus + " : " + errorThrown);
}