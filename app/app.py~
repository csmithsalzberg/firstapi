#Caleb Smith-Salzberg
#SoftDev1 pd7
#HW 13 -- A RESTful Journey Skyward
#2017-11-09
import urllib2
import json
from flask import Flask, render_template

app = Flask(__name__)




@app.route("/")
def apifun():
    url = "https://api.nasa.gov/planetary/apod?api_key=JgfRHHASa1UjyzXkVEgwEBboEhjVH8QGAQVhA4cb"
    uResp = urllib2.urlopen( url ) 
    contentsraw = uResp.read()
    dat = json.loads(contentsraw)
    image = dat["url"]
    description = dat["explanation"]
    return render_template("display.html", img = image, desc = description)

if __name__ == '__main__':
    app.debug = True
    app.run()
apifun()
