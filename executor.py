import json
from flask import Flask,jsonify
import requests
import time
import esecuzione

GET_TEMP = "http://127.0.0.1:5000/temp"
SET_RELAY_1 = "http://127.0.0.1:5001/set_relay/1"
SET_RELAY_2 = "http://127.0.0.1:5001/set_relay/2"
STATUS_RELAY = "http://127.0.0.1:5001/status"

app = Flask(__name__)

@app.route('/')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/executor')
def get_data():
    response_temps = requests.get(GET_TEMP)
    temp = response_temps.json()
    #print(response_temps.json()["T1"]
    esecuzione.controllo_temp()
    #return (requests.get(STATUS_RELAY).json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5004)
