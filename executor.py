import json
from flask import Flask,jsonify
import requests
import time
import esecuzione
import threading
from os import getenv
from requests.auth import HTTPBasicAuth
from flask_httpauth import HTTPBasicAuth as log
from werkzeug.security import generate_password_hash, check_password_hash

username = "daniele" or "antonio"
password = "Cisco123" or "Dtlab123"
GET_TEMP = getenv("GET_TEMP") or "http://127.0.0.1:5000/temp"
SET_RELAY_1 =  getenv("SET_RELAY1") or "http://127.0.0.1:5001/set_relay/1"
SET_RELAY_2 = getenv("SET_RELAY2") or "http://127.0.0.1:5001/set_relay/2"
STATUS_RELAY = getenv("STATUS_RELAY") or "http://127.0.0.1:5001/status"

app = Flask(__name__)
# auth = HTTPBasicAuth()

# users = {
#     "daniele": generate_password_hash("Cisco123"),
#     "antonio": generate_password_hash("Dtlab123")
# }

# @auth.verify_password
# def verify_password(username, password):
#     if username in users and check_password_hash(users.get(username), password):
#         return username
        
x = None


@app.route('/executor')
#@auth.login_required
def get_data():
    response_temps = requests.get(GET_TEMP, auth=HTTPBasicAuth(username,password))
    temp = response_temps.json()
    global x    #per dichiarare di usare la variabile globale
    if x is not None:   #controlla che non è già in esecuzione
        return "thread già in esecuzione"
    x = threading.Thread(target=esecuzione.controllo_temp, args =(5,), daemon=True) #crea l'oggetto thread per la funzione di polling
    x.start()
    time.sleep(5)
    return (requests.get(STATUS_RELAY, auth=HTTPBasicAuth(username,password)).json())
    


@app.route('/stop')
#@auth.login_required
def stop_polling():
    global x
    esecuzione.stop_event.set() #setta l'evento per stoppare il ciclo while
    x.join()    #esegue la join con il main thread 
    esecuzione.stop_event.clear()
    x = None
    
    return "stopped polling"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5004)
