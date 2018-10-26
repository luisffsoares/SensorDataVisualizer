#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizador dos dados do sensor de vibrações
Método:
    1 - abrir arquivo do datalogger ok
    2 - ler última linha do datalogger ok
    3 - tratar os dados ok
    4 - gerar freqs ok
    5 - plotar gráfico ok
    6 - infos
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
        listFreq = []
        #Lista das freqs
        for i in range (0, len(listFFT)):
            #i * 1.0 * samplingFrequency) / samples
            listFreq.append((i+3)*1*5000/1024)
        
            
        
        ax1.clear()
        plt.xlabel('Frequência (Hz)')
        plt.ylabel('Amplitude')
        plt.title('Dados Mic')    
        #plt.tight_layout()
        plt.subplots_adjust(bottom=.15, left=.17)
        ax1.annotate(horaFFT+ ' em ' +dataFFT , xy=(6.28, 1), xytext=(1200, 46000))
        ax1.set_ylim(0,50000)
        ax1.plot(listFreq,listFFT, linewidth=1.0)
    
ani = animation.FuncAnimation(fig, animate, interval=100)

plt.show()


    
    

