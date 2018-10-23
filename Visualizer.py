#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizador dos dados do sensor de vibrações

@author: luisffs
"""
    
#import datetime
#import csv
import paho.mqtt.client as mqtt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("/Sensor1/#")
    client.subscribe("/Sensor1/Mic")
    #client.subscribe("/Sensor1/Accel")

# Evento: recebimento de mensagem servidor
def on_message(t1, userdata, msg):
    #print(msg.topic)    
    msg_payload = str(msg.payload)#.split(';')
    msg_list = msg_payload.split(';')
    msg_list = msg_list[2:]
    msg_list = msg_list[:-1]
    lenL = len(msg_list)
    #print(lenL)
    #print(float(msg_list[52]))
    #print(msg_list) 
    
    dataFloat =  [float(i) for i in msg_list]
    
    for j in range(0 , lenL):
        
        data_mic[j,0] = dataFloat
    
        
    #print((dataFloat))
    
    



client = mqtt.Client("Viz1")#must be unique
client.username_pw_set("vizulizerOne", "")
client.on_connect = on_connect
client.on_message = on_message


#client.connect('test.mosquitto.org', 1883, 120) #Just for testing purposes

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
