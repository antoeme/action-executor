import json
from flask import Flask,jsonify
import requests
import sys
sys.path.append('../')

GET_TEMP = "http://127.0.0.1:5003/executor"

app = Flask(__name__)

@app.route('/')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/executor')
def get_data():
    response_temps = requests.get(GET_TEMP)
    print(response_temps) 
    return ("ciao")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5004)

