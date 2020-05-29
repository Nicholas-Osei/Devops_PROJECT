# flask_web/app.py

#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hey, we have Flask in a Docker container!'


#if __name__ == '__main__': 
#	app.run(debug=True,host='0.0.0.0')







#import RPi.GPIO as GPIO
from flask import Flask,url_for,render_template
app = Flask(__name__)

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#ledPins = [5,6,16,17,21,22,23,24,26]

#for index in ledPins:
 #	GPIO.setup(index, GPIO.OUT)
 #	GPIO.output(index, GPIO.LOW)

@app.route("/") 
def home(name=None):
	output= """<style>
.flex-container {
  display: flex;
  justify-content: center;
}

.flex-container > button {
  background-color: #f1f1f1;
  width: 400px;
  margin: 50px;
  text-align: center;
  line-height: 275px;
  font-size: 30px;
  padding :0%;

}
h1
{
    text-align: center;
}
</style><h1>Maak een keuze</h1>
	<div class="flex-container"><button type="button" onclick="ruben()"onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#f1f1f1';">lol</button> <button type="button" onclick="window.location.href='{{ url_for('vanhogh')}}';"onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#f1f1f1';">Van-Hogh</button> <button type="button" onclick="window.location.href='{{ url_for('rembrandt')}}';"onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#f1f1f1';">Rembrandt</button> </div>"""
	return output
   	#return render_template('Nicholas_Flask.html', name=name)

@app.route("/rubens") 
def ruben():
	output = """<style>
.flex-container {
  display: flex;
  justify-content: center;
}

.flex-container > button {
  background-color: #f1f1f1;
  width: 400px;
  margin: 50px;
  text-align: center;
  line-height: 275px;
  font-size: 30px;
  padding :0%;

}
.Back
{
    background-color: #ffffff;
    position:absolute;
    width:400px;
    height:150px;
    background:#063;
    bottom:0px;
    right:25%;
    left:50%;
    margin-left:-150px;
    font-size: 30px;
    color:white
}

h1
{
    text-align: center;
}
</style>

<h1>Kies je Schilderij</h1>
<div class="flex-container">
<button type="button" onclick="window.location.href='{{ url_for('leds',number=0)}}';" onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#f1f1f1';">Sterrennacht</button>
<button type="button" onclick="window.location.href='{{ url_for('leds',number=1)}}';" onmouseover="this.style.background='lightblue';" onmouseout="this.style.background='#f1f1f1';">De Schreeuw</button>
<button type="button" onclick="window.location.href='{{ url_for('leds',number=2)}}';" onmouseover="this.style.background='lightblue';" onmouseout="this.style.background='#f1f1f1';">De volharding der herinnerin</button>  
</div>
<button class="Back" onclick="window.location.href='{{ url_for('home')}}';"onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#063';">Terug Naar HoofdPagina</button>"""
	return output

@app.route("/van-hogh")
def vanhogh(name=None):
	output = """<style>
.flex-container {
  display: flex;
  justify-content: center;
}

.flex-container > button {
  background-color: #f1f1f1;
  width: 400px;
  margin: 50px;
  text-align: center;
  line-height: 275px;
  font-size: 30px;
  padding :0%;

}
.Back
{
    background-color: #ffffff;
    position:absolute;
    width:400px;
    height:150px;
    background:#063;
    bottom:0px;
    right:25%;
    left:50%;
    margin-left:-150px;
    font-size: 30px;
    color:white
}

h1
{
    text-align: center;
}
</style>
<h1>Kies je Schilderij</h1>

<div class="flex-container">
  <button type="button" onclick="window.location.href='{{ url_for('leds',number=3)}}';" onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#f1f1f1';">Het meisje met de Parel</button>
  <button type="button" onclick="window.location.href='{{ url_for('leds',number=4)}}';" onmouseover="this.style.background='lightblue';" onmouseout="this.style.background='#f1f1f1';">De Nachtwacht</button>
  <button type="button" onclick="window.location.href='{{ url_for('leds',number=5)}}';" onmouseover="this.style.background='lightblue';" onmouseout="this.style.background='#f1f1f1';">De schepping van Adam</button>  
</div>
<button class="Back" onclick="window.location.href='{{ url_for('home')}}';"onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#063';">Terug Naar HoofdPagina</button>"""
	return output

@app.route("/rembrandt")
def rembrandt(name=None):
	output = """<style>
.flex-container {
  display: flex;
  justify-content: center;
}

.flex-container > button {
  background-color: #f1f1f1;
  width: 400px;
  margin: 50px;
  text-align: center;
  line-height: 275px;
  font-size: 30px;
  padding :0%;
}
.Back
{
    background-color: #ffffff;
    position:absolute;
    width:400px;
    height:150px;
    background:#063;
    bottom:0px;
    right:25%;
    left:50%;
    margin-left:-150px;
    font-size: 30px;
    color:white
}
h1
{
    text-align: center;
}
</style>
<h1>Kies je Schilderij</h1>

<div class="flex-container">
  <button type="button" onclick="window.location.href='{{ url_for('leds',number=6)}}';" onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#f1f1f1';">De Mona Lisa</button>
  <button type="button" onclick="window.location.href='{{ url_for('leds',number=7)}}';" onmouseover="this.style.background='lightblue';" onmouseout="this.style.background='#f1f1f1';">Het laatste Avondmaal</button>
  <button type="button" onclick="window.location.href='{{ url_for('leds',number=8)}}';" onmouseover="this.style.background='lightblue';" onmouseout="this.style.background='#f1f1f1';">De Nachtwacht</button>  
</div>
<button class="Back" onclick="window.location.href='{{ url_for('home')}}';"onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#063';">Terug Naar HoofdPagina</button> """
	return output

if __name__ == '__main__': 
	app.run(host='0.0.0.0')
