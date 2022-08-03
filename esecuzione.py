import requests
import time

GET_TEMP = "http://127.0.0.1:5000/temp"
SET_RELAY_1 = "http://127.0.0.1:5001/set_relay/1"
SET_RELAY_2 = "http://127.0.0.1:5001/set_relay/2"


def controllo_temp():
    while(True):
        response_temps = requests.get(GET_TEMP)
        temp = response_temps.json()
        for chiave in temp:
            print(temp[chiave])
            if(temp[chiave] <= 20 and temp[chiave]>= 10 ):
                requests.get(SET_RELAY_1)
            elif(temp[chiave] >= 40): requests.get(SET_RELAY_2)
        time.sleep(2)
        #yield "ciao"


