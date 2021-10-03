# Metric Converter Web App

## Overview
This project was my first introduction into using Django to make a web app. 

This program converts metric measurements (namely milimeters, centimeters, and meters) into standard measurements (inches, feet, yards). 

**Note:** to run the program on Visual Studio Code on your computer, open up to the "conv_proj" directory. Then run the command, "python manage.py runserver". An http website url will appear with numbers. Hold down CTRL then press the link to open up the website page on your browser. 

[Web App Demo Video](https....)

## Web Pages
There are two web pages. One is the converter page, where the user can select the measurement types and type the metric number to be converted. When the submit button is pressed, the result page appears. This displays the calculated result. 
## Development Environment
I used Visual Studio Code with Django. I imported "views", "path", "render", "HttpResponse", "admin", "include", and "os" from the modules "shortcuts", "http", "urls", "contrib", and "pathlib".
## Useful Websites
- [Youtube Django for beginners with Telusko](https://www.youtube.com/watch?v=OTmQOjsl0eg)

- [Django tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-django)

- [W3Schools HTML style tutorials](https://www.w3schools.com/html/)

## Future Work

There are a few more things I would like to do to improve this app:

- Make more measurement options for conversions

- Give the user the option to convert standard to metric

- Have the result appear on the page, rather than on a seperate page
