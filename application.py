from flask import Flask, render_template, redirect, request, flash, session
from time import sleep
import random

app = Flask(__name__)


array = []
file = open("sentences.txt", "r")
for line in file:
	array.append(line)

@app.route("/", methods=["GET", "POST"])
def index():
	t = array[random.randint(0, 19)]
	text = []		

	lc = -1
	wc = 1

	for i in t:								
		text.append(i)
		lc += 1
		if i == " ":
			wc += 1

	dead = wc * 2 * 1000
	
	if request.method == "GET":
		timer = 5

		return render_template("index.html", timer = timer, text = t, wc = wc, lc = lc, deadline = dead)

	else:
		input_t = request.form.get(text_area)
		input_text = []

		a = 0

		for i in t:
			input_text.append(i)

		for i in range(len(t)):
			if i > len(input(t)):
				break
			a += 1

		return render_template("index.html")


# export FLASK_APP=application.py
# flask run