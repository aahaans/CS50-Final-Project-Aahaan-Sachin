# CS50 Final Project - Aahaan Sachin

After enjoying and learning from this course I present to you
####	My CS50 final project

## About the Project

My project is **Web** *Application* / *Game* which measures the user's Words per minute.
It also has a deadline feature.

## Languages and Frameworks used

#### Languages used are Python, Javascript, HTML and CSS.
#### Framework used is Flask which a Python micro-framework for web development.

## Files and Folders in the Project

 1. application.py - The python file through which i give routes to my templates or HTML files.
 2. sentences.txt  - The text file which contains 20 sentences which end which the character "." .
 3. templates        - The folder which contains the HTML file(s)
 4. index.html 	  - The file in the folder templates which has the main web page.

## How the project works

In the route "/"
The application.py file reads from the file sentences.txt and stores all the sentences in an array.
It then randomly chooses 1 sentence  or 1 element of the array using the function randint from the random module.
The number of words and letters of the sentence are calculated.
The variable deadline is set to double of the number of words.
The template index.html is rendered.
The sentence, number of words, number of letters and he deadline is then displayed in the HTML file index.html.

The sentence appears at the centre of the page.
The number of words, number of letter, deadline appear in a table called information.
A form element is with a textarea element in it is shown below the sentence.
The user is expected to type the sentence in the textarea element and type full stop when he/she is done.
When the user types full stop the user's text and the sentence are then compared character by character and the results which are of 3 parts - Time taken , Accuracy, WPM (Words Per Minute)  are shown in a table called results.

When the Webpage first loads, a countdown from 5 to 1 is seen for dramatic effect.
The moment the user starts typing, the same countdown turns into a stopwatch incrementing at every 100 ms to give additional adrenaline rush.
If the stopwatch exceeds the deadline then the textarea field is disabled, the stopwatch has the value of "Time out!" and user failed in the game.
When the user types "." The textarea element is disabled and results are calculated.
The time taken is the value of the stop watch.
The users-text and the sentence are then compared to calculate the Accuracy.
The formula ((number of correctly typed words / time taken) * 60) is used to calculate the WPM.
The results are then displayed in table called results.

# Conclusion
## This project was made by Aahaan Sachin username - aahaans
## He is super happy to say that this was CS50.