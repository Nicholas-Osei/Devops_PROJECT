#!/usr/bin/python3

import RPi.GPIO as GPIO
from flask import Flask,url_for,render_template
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPins = [5,6,16,17,21,22,23,24,26]

for index in ledPins:
 	GPIO.setup(index, GPIO.OUT)
 	GPIO.output(index, GPIO.LOW)

@app.route("/") 
def home(name=None):
    	return render_template('Nicholas_Flask.html', name=name)

@app.route("/rubens") 
def ruben(name=None):
	return render_template('rubens.html')

@app.route("/Leds/<int:number>") 
def leds(number):
	for index in ledPins:
		if index == number:
			continue
		GPIO.output(index, GPIO.LOW)
	if GPIO.input(ledPins[number])==GPIO.HIGH:
		GPIO.output(ledPins[number],GPIO.LOW)
	else:
		GPIO.output(ledPins[number],GPIO.HIGH)
	if number < 3 :
		return render_template('rubens.html')
	elif number < 6 :
		return render_template('van-hogh.html')
	else:
		return render_template('rembrandt.html')

@app.route("/van-hogh")
def vanhogh(name=None):
    return render_template('van-hogh.html', name=name)

@app.route("/rembrandt")
def rembrandt(name=None):
    return render_template('rembrandt.html', name=name)

if __name__ == '__main__': 
	app.run(host='0.0.0.0')
