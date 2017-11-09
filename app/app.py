import urllib2
from flask import Flask, render_template

app = Flask(__name__)


url = "https://api.nasa.gov/planetary/apod?api_key=JgfRHHASa1UjyzXkVEgwEBboEhjVH8QGAQVhA4cb"

uResp = urllib2.urlopen( url ) 
contentsraw = uResp.read()
print uResp.info()


if __name__ == '__main__':
    app.debug = True
    app.run()
