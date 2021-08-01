# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    #html = "<div style='text-align:center;margin:20px;'><h1>Greetings from AEM Technologies!</h1><img src='https://IP/aemtechlogo.png' width='40%' alt='Tuhin @ AEM Technologies'></div>"
    html = "<div style='text-align:center;margin:20px;'><h1>Greetings from AEM Technologies!</h1>'</div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
