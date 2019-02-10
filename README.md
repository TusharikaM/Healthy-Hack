# Healthy-Hack
Currently in many apps it's tedious task where you are asked to manually input calories for the food item to keep track of your health. We thought of an idea to reduce this manual work to a great extent by incorporating image detection and calorie finder. Our app allows "click photo - track calories" kind of functionality. As simple as that.

## What it is does?
We have designed a system integrating Webpage and Alexa UI.
A User can find the calories for a food item and add it to their calorie count using the webpage. They can invoke our skill designed in alexa which will give details about their calorie consumption. Both these UI are linked to the same datastore at the end, so you get similar result either way whichever is more convenient to the user.

## What's in here?
This repo contains the code for the Front-End Webpage, Web Service API, Image classification using CNN, and the Alexa lambda function for alexa skills.

( Note: Our pretrained model file can be found at: https://drive.google.com/open?id=1u317FicYXRoL4QPXVAZwn6maTu8n_S5U )

## Overview of how it works?
1. The Webpage is where the user has the functionality to take a picture of the food item.
2. This image is sent asynchronously to our API
3. Our API classifies the image, finds it's calorie related data and sends back to the user. It then updates this in the datastore and updates this datastore to Amazon S3 cloud.
4. The user can add these food items detected into the datastore to keep a track of their calorie consumption.
5. When a user invokes our app on alexa, they can hear back these details stored in the datastore.

## How to run this?
1. On a Server, host the API and the webpage
2. Make sure the server has all the required libraries and languages support used here. I may upload an extensive wiki documentation for the same later.
3. Start the web service api using python command.
4. Access the web page and you can start to use it.
