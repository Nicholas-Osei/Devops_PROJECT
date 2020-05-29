from flask import Flask,url_for,render_template
app = Flask(__name__)

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
</style><h1>STALK ME EVERYWHERE !</h1>
	<div class="flex-container"><button type="button" onclick="window.open('https://www.youtube.com/channel/UC7k50BTEIlvYrbTQ4xf6gbQ')"onmouseover="this.style.background='red';"onmouseout="this.style.background='#f1f1f1';">YOUTUBE</button> <button type="button" onclick="window.open('https://www.youtube.com/channel/UC7k50BTEIlvYrbTQ4xf6gbQ')"onmouseover="this.style.background='red';"onmouseout="this.style.background='#f1f1f1';">YOUTUBE</button><button type="button" onclick="window.open('https://mobile.twitter.com/niconaldo_')"onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#f1f1f1';">TWITTER</button> </div>
<button class="Back" onclick="alert('Email: s107305@ap.be')"onmouseover="this.style.background='lightblue';"onmouseout="this.style.background='#063';">EMAIL ME NOW ! </button>"""
	return output



	

if __name__ == '__main__': 
	app.run(host='0.0.0.0')
