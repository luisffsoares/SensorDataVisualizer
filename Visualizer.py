#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizador dos dados do sensor de vibrações

Método:
    1 - abrir arquivo do datalogger
    2 - ler última linha do datalogger
    3 - tratar os dados
    4 - gerar freqs
    5 - plotar gráfico


@author: luisffs
"""
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    
    with open('Mic.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter='\n')
        lista = list(plots)
        a = len(lista)
        
        ult_lin = lista[a-1]
        stringFFT = (ult_lin[0])
        listFFT = stringFFT.split(";")
        listFFT = listFFT[2:]
        global dataFFT
        global horaFFT
        dataFFT = listFFT[len(listFFT)-1]
        horaFFT = listFFT[len(listFFT)-2]
        listFFT = listFFT[:-3]
        listFFT = [float(i) for i in listFFT]
    
        ax1.clear()
        ax1.plot(listFFT)
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()


    
    
    
#plt.plot(listFFT)  
#print(listFFT)    
print(dataFFT)
print(horaFFT)
    
