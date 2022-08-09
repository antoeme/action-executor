import re
import requests
import time

GET_TEMP = "http://127.0.0.1:5000/temp"
SET_RELAY_1 = "http://127.0.0.1:5001/set_relay/1"
SET_RELAY_2 = "http://127.0.0.1:5001/set_relay/2"
STATUS_RELAY = "http://127.0.0.1:5001/status"

RUN = True

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
    
def controllo_temp():
    while(RUN):
        temp = requests.get(GET_TEMP).json()
        stato_r = requests.get(STATUS_RELAY).json()
        if (temp['T1'] >= 40.0 and stato_r["Relay1"] == 0 ): 
            requests.get(SET_RELAY_1)
            print(temp['T1'])
        elif(temp['T2'] >= 25.0 and True ): 
            requests.get(SET_RELAY_2)
            print(temp['T2'])

        print(stato_r)
        time.sleep(10)


