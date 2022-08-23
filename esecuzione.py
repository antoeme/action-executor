import threading
import requests
import time
from os import getenv
from requests.auth import HTTPBasicAuth

GET_TEMP = getenv("GET_TEMP") or "http://127.0.0.1:5000/temp"
SET_RELAY_1 =  getenv("SET_RELAY1") or "http://127.0.0.1:5001/set_relay/1"
SET_RELAY_2 = getenv("SET_RELAY2") or "http://127.0.0.1:5001/set_relay/2"
STATUS_RELAY = getenv("STATUS_RELAY") or "http://127.0.0.1:5001/status"
username = "daniele" or "antonio"
password = "Cisco123" or "Dtlab123"


stop_event = threading.Event()  #variabile evento per lo stop 

# def controllo_temp():
#     while(RUN):
#         temp = requests.get(GET_TEMP).json()
#         stato_r = requests.get(STATUS_RELAY).json()
#         print(stato_r)
#         for chiave in temp:
#             print(temp[chiave])
#             if(temp[chiave] >= 20.0 and temp[chiave]<= 30.0 and stato_r["Relay1"] == 0 ): requests.get(SET_RELAY_1)
#             elif(temp[chiave] >= 40.0 and stato_r["Relay2"] == 0 ): requests.get(SET_RELAY_2)
#         time.sleep(10)
    
def controllo_temp(interval):
    count = 0
    while(not stop_event.is_set()):
        count +=1
        temp = requests.get(GET_TEMP,auth=HTTPBasicAuth(username,password)).json()    #estrae dizionario di temperature
        stato_r = requests.get(STATUS_RELAY, auth=HTTPBasicAuth(username,password)).json() #estrae dizionare di relays
        if (temp['T1'] >= 40.0 and stato_r["Relay1"] == 0 ): 
            requests.get(SET_RELAY_1,auth=HTTPBasicAuth(username,password))
            print(temp['T1'])
        elif(temp['T2'] >= 25.0 and True ):
        #elif(temp['T2'] >= 25.0 and stato_r["Relay2"] == 0 ): 
            requests.get(SET_RELAY_2,auth=HTTPBasicAuth(username,password))
            print(temp['T2'])

        print(stato_r)
        
        time.sleep(interval)
    print("thread stopped; count is", count)

