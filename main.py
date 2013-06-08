from flask import Flask, render_template, jsonify
from random import random
from test import TempSensor
from datetime import datetime
app = Flask(__name__)
t = TempSensor()

@app.route('/')
def main():
    reading = t.read()
    time = datetime.now().time().strftime('%I:%M:%S %p')
    return render_template('main.html', time=time, reading=reading)

@app.route('/reload')
def reload():
    reading = t.read()
    time = datetime.now().time().strftime('%I:%M:%S %p')
    return jsonify(reading=reading, time=time)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
