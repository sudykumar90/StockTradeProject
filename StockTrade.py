import numpy as np
import urllib as urls
import re
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.finance import candlestick_ohlc as cndl
import os

if not os.path.exists('AllPrice'):
    os.mkdir('AllPrice')

def movingaverage(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas

# 1 day
def data1D(stock):
    list1D = stock.split('\n')
    for symbol in list1D:
        allfile1D = open('AllPrice/'+symbol+'1D.txt', 'w+')
        allfile1D.close()

        htmltext1D = urls.urlopen('http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1d/csv').read()
        data1D = htmltext1D.split('\n')

        for line1D in data1D:
             splitline1D = line1D.split(',')
             if len(splitline1D) == 6:
                if 'values' not in line1D:
                    allfile1D = open('AllPrice/' + symbol + '1D.txt', 'a')
                    linestowrite1D = line1D + '\n'
                    allfile1D.write(str(symbol) + ',' + linestowrite1D)
                    allfile1D.close()

#1 month

def data1M(stock):
    list1M = stock.split('\n')
    for symbol in list1M:
        allfile1M = open('AllPrice/'+symbol+'1M.txt', 'w+')
        allfile1M.close()

        htmltext1M = urls.urlopen('http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1m/csv').read()
        data1M = htmltext1M.split('\n')

        for line1M in data1M:
             splitline1M = line1M.split(',')
             if len(splitline1M) == 6:
                if 'values' not in line1M:
                    allfile1M = open('AllPrice/' + symbol + '1M.txt', 'a')
                    linestowrite1M = line1M + '\n'
                    allfile1M.write(str(symbol) + ',' + linestowrite1M)
                    allfile1M.close()

# 1 Year

def data1Y(stock):
    list1Y = stock.split('\n')
    for symbol in list1Y:
        allfile1Y = open('AllPrice/'+symbol+'1Y.txt', 'w+')
        allfile1Y.close()

        htmltext1Y = urls.urlopen('http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1y/csv').read()
        data1Y = htmltext1Y.split('\n')

        for line1Y in data1Y:
             splitline1Y = line1Y.split(',')
             if len(splitline1Y) == 6:
                if 'values' not in line1Y:
                    allfile1Y = open('AllPrice/' + symbol + '1Y.txt', 'a')
                    linestowrite1Y = line1Y + '\n'
                    allfile1Y.write(str(symbol) + ',' + linestowrite1Y)
                    allfile1Y.close()

#plot
def plot(stock):
    listplot = stock.split('\n')
    for symbol in listplot:
        # 1D plot
        datas1D = np.genfromtxt('AllPrice/' + symbol + '1D.txt', delimiter=',')
        #name1D = pd.read_csv('AllPrice/' + symbol + '1D.txt')
        close1D = tuple(datas1D[:,][:,2])
        high1D = tuple(datas1D[:,][:,3])
        low1D = tuple(datas1D[:,][:,4])
        open1D = tuple(datas1D[:,][:,5])
        volume1D = tuple(datas1D[:,][:,6])
        time1D = datas1D[:, ][:, 1]
        time1D = (time1D - time1D[0])/1000
        MV11D = int(len(close1D) * 0.01)
        MV21D = int(len(close1D) * 0.025)

        start1D=0
        end1D=len(close1D)
        candlesticks1D = []
        while start1D<end1D:
            append1D = time1D[start1D],open1D[start1D],close1D[start1D],high1D[start1D],low1D[start1D]
            candlesticks1D.append(append1D)
            start1D += 1

        if MV11D > 1:
            MV11D = MV11D
        else:
            MV11D = 2

        if MV21D > 1:
            MV21D = MV21D
        else:
            MV21D= 4


        mv3stock1D1 = (movingaverage(close1D, MV11D))
        mv3stock1D2 = (movingaverage(close1D, MV21D))

        SP1D1 = len(time1D[MV11D - 1:])
        SP1D2 = len(time1D[MV21D - 1:])

        close1D = datas1D[:, ][:, 2]

        # 1M plot
        datas1M = np.genfromtxt('AllPrice/'+symbol+'1M.txt', delimiter=',', converters={1: mdate.strpdate2num('%Y%m%d')})
        #name1M = pd.read_csv('AllPrice/'+symbol+'1M.txt')
        close1M = tuple(datas1M[:,][:,2])
        high1M = tuple(datas1M[:,][:,3])
        low1M = tuple(datas1M[:,][:,4])
        open1M = tuple(datas1M[:,][:,5])
        volume1M = tuple(datas1M[:,][:,6])
        time1M = datas1M[:, ][:, 1]
        time1M = time1M - time1M[0]
        MV11M = int(len(close1M) * 0.01)
        MV21M = int(len(close1M) * 0.025)

        start1M = 0
        end1M = len(close1M)
        candlesticks1M = []
        while start1M < end1M:
            append1M = time1M[start1M],open1M[start1M],close1M[start1M],high1M[start1M],low1M[start1M]
            candlesticks1M.append(append1M)
            start1M += 1

        if MV11M > 1:
            MV11M = MV11M
        else:
            MV11M = 2

        if MV21M > 1:
            MV21M = MV21M
        else:
            MV21M = 4



        mv3stock1M1 = (movingaverage(close1M, MV11M))
        mv3stock1M2 = (movingaverage(close1M, MV21M))

        SP1M1 = len(time1M[MV11M-1:])
        SP1M2 = len(time1M[MV21M - 1:])
        close1M = datas1M[:, ][:, 2]

        # 1Y plot
        datas1Y = np.genfromtxt('AllPrice/'+symbol+'1Y.txt', delimiter=',', converters={1: mdate.strpdate2num('%Y%m%d')})
        #name1Y = pd.read_csv('AllPrice/'+symbol+'1Y.txt')
        close1Y = tuple(datas1Y[:,][:,2])
        high1Y = tuple(datas1Y[:,][:,3])
        low1Y = tuple(datas1Y[:,][:,4])
        open1Y = tuple(datas1Y[:,][:,5])
        volume1Y = tuple(datas1Y[:,][:,6])
        time1Y = datas1Y[:, ][:, 1]
        time1Y = time1Y - time1Y[0]
        MV11Y = int(len(close1Y) * 0.01)
        MV21Y = int(len(close1Y) * 0.025)

        start1Y = 0
        end1Y = len(close1Y)
        candlesticks1Y = []
        while start1Y < end1Y:
            append1Y = time1Y[start1Y],open1Y[start1Y],close1Y[start1Y],high1Y[start1Y],low1Y[start1Y]
            candlesticks1Y.append(append1Y)
            start1Y += 1


        if MV11Y > 1:
            MV11Y = MV11Y
        else:
            MV11Y = 2

        if MV21Y > 1:
            MV21Y = MV21Y
        else:
            MV21Y = 4


        mv3stock1Y1 = (movingaverage(close1Y, MV11Y))
        mv3stock1Y2 = (movingaverage(close1Y, MV21Y))

        SP1Y1 = len(time1Y[MV11Y-1:])
        SP1Y2 = len(time1Y[MV21Y - 1:])
        close1Y = datas1Y[:, ][:, 2]

        mvavgplot11D = str(MV11D) + ' MA'
        mvavgplot21D = str(MV21D) + ' MA'

        fig = plt.figure(facecolor='black')
        fig1 = fig.add_subplot(2,2,1, axisbg='black')
        cndl(fig1, candlesticks1D, width=0.025, colorup='g', colordown='r')
        fig1.plot(time1D[-SP1D1:], mv3stock1D1[-SP1D1:], 'r-', label=mvavgplot11D)
        fig1.plot(time1D[-SP1D2:], mv3stock1D2[-SP1D2:], 'g-', label=mvavgplot21D)
        fig1.set_xlim(xmin=0)
        fig1.grid(True, color='w')
        fig1.spines['bottom'].set_color('w')
        fig1.spines['top'].set_color('w')
        fig1.spines['left'].set_color('w')
        fig1.spines['right'].set_color('w')
        fig1.tick_params(axis='x',colors='w')
        fig1.tick_params(axis='y', colors='w')
        plt.legend(loc=9,ncol=2, prop={'size':8})
        plt.xlabel('TimeFrame', color='w')
        plt.ylabel('StockPrice',color='w')
        plt.title(symbol+ ' Stock Price 1 Day',color='w')

        mvavgplot11M = str(MV11M) + ' MA'
        mvavgplot21M = str(MV21M) + ' MA'

        fig2 = fig.add_subplot(2,2,2, axisbg='black')
        cndl(fig2, candlesticks1M, width=0.1, colorup='g', colordown='r')
        fig2.plot(time1M[-SP1M1:],mv3stock1M1[-SP1M1:] , 'r-',label=mvavgplot11M)
        fig2.plot(time1M[-SP1M2:],mv3stock1M2[-SP1M2:], 'g-',label=mvavgplot21M)
        fig2.set_xlim(xmin=0)
        fig2.grid(True, color='w')
        fig2.spines['bottom'].set_color('w')
        fig2.spines['top'].set_color('w')
        fig2.spines['left'].set_color('w')
        fig2.spines['right'].set_color('w')
        fig2.tick_params(axis='x',colors='w')
        fig2.tick_params(axis='y', colors='w')
        plt.legend(loc=9,ncol=2, prop={'size':8})
        plt.xlabel('TimeFrame',color='w')
        plt.ylabel('StockPrice',color='w')
        plt.title(symbol + ' Stock Price 1 Month',color='w')


        mvavgplot11Y = str(MV11Y) + ' MA'
        mvavgplot21Y = str(MV21Y) + ' MA'
        fig3 = fig.add_subplot(2,1,2, axisbg='black')
        cndl(fig3, candlesticks1Y, width=0.5, colorup='g', colordown='r')
        fig3.plot(time1Y[-SP1Y1:],mv3stock1Y1[-SP1Y1:] , 'r-',label=mvavgplot11Y)
        fig3.plot(time1Y[-SP1Y2:], mv3stock1Y2[-SP1Y2:], 'g-',label=mvavgplot21Y)
        fig3.set_xlim(xmin=0)
        fig3.grid(True, color = 'w')
        fig3.spines['bottom'].set_color('w')
        fig3.spines['top'].set_color('w')
        fig3.spines['left'].set_color('w')
        fig3.spines['right'].set_color('w')
        fig3.tick_params(axis='x',colors='w')
        fig3.tick_params(axis='y', colors='w')
        plt.legend(loc=9,ncol=2, prop={'size':8})
        plt.xlabel('TimeFrame',color='w')
        plt.ylabel('StockPrice',color='w')
        plt.title(symbol + ' Stock Price 1 Year',color='w')
        plt.subplots_adjust(left=0.1,bottom=0.08,right=0.97,top=0.94,wspace=0.25,hspace=0.34)
        plt.show()


while True:
    stock = raw_input('Please Input Stock: ')
    data1D(stock)
    data1M(stock)
    data1Y(stock)
    plot(stock)
