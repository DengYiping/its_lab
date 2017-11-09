from flask import Flask
from flask import request
from flask import render_template
import serial
ser_addr = '/dev/cu.usbmodem1411'
ser = serial.Serial(ser_addr, 9600, timeout=1) 
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("main.html")

@app.route('/', methods=['POST'])
def my_form_post():

    password = request.form['pwd']
    if password == 'nopassword':
        ser.write(b'1')
        return "Welcome"
    else:
        return 'Go Away'

if __name__ == '__main__':
    app.run()
