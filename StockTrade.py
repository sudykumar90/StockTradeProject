import numpy as np
import urllib as urls
import re
import json
import matplotlib.pyplot as plt


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

        htmltext1D = urls.urlopen('http://www.bloomberg.com/markets/chart/data/1D/'+symbol+':US')
        data1D = json.load(htmltext1D)
        datapoints1D = data1D["data_values"]

        allfile1D = open('AllPrice/' +symbol+ '1D.txt', 'a')

        for point in datapoints1D:
            allfile1D.write(str(symbol) + ',' + str(point[0]) + ',' + str(point[1]) + '\n')
        allfile1D.close()

#1 month

def data1M(stock):
    list1M = stock.split('\n')
    for symbol in list1M:
        allfile1M = open('AllPrice/'+symbol+'1M.txt', 'w+')
        allfile1M.close()

        htmltext1M = urls.urlopen('http://www.bloomberg.com/markets/chart/data/1M/'+symbol+':US')
        data1M = json.load(htmltext1M)
        datapoints1M = data1M["data_values"]

        allfile1M = open('AllPrice/' +symbol+ '1M.txt', 'a')

        for point in datapoints1M:
            allfile1M.write(str(symbol) + ',' + str(point[0]) + ',' + str(point[1]) + '\n')
        allfile1M.close()

# 1 Year

def data1Y(stock):
    list1Y = stock.split('\n')
    for symbol in list1Y:
        allfile1Y = open('AllPrice/'+symbol+'1Y.txt', 'w+')
        allfile1Y.close()

        htmltext1Y = urls.urlopen('http://www.bloomberg.com/markets/chart/data/1Y/'+symbol+':US')
        data1Y = json.load(htmltext1Y)
        datapoints1Y = data1Y["data_values"]

        allfile1Y = open('AllPrice/' +symbol+ '1Y.txt', 'a')

        for point in datapoints1Y:
            allfile1Y.write(str(symbol) + ',' + str(point[0]) + ',' + str(point[1]) + '\n')
        allfile1Y.close()

#plot
def plot(stock):
    listplot = stock.split('\n')
    for symbol in listplot:
        # 1D plot
        datas1D = np.genfromtxt('AllPrice/' + symbol + '1D.txt', delimiter=',')
        #name1D = pd.read_csv('AllPrice/' + symbol + '1D.txt')
        stocks1D = tuple(datas1D[:,][:,2])
        time1D = datas1D[:, ][:, 1]
        time1D = time1D - time1D[0]
        MV11D = int(len(stocks1D) * 0.01)
        MV21D = int(len(stocks1D) * 0.025)


        if MV11D > 1:
            MV11D = MV11D
        else:
            MV11D = 2

        if MV21D > 1:
            MV21D = MV21D
        else:
            MV21D= 4


        mv3stock1D1 = (movingaverage(stocks1D, MV11D))
        mv3stock1D2 = (movingaverage(stocks1D, MV21D))

        SP1D1 = len(time1D[MV11D - 1:])
        SP1D2 = len(time1D[MV21D - 1:])

        stock1D = datas1D[:, ][:, 2]

        # 1M plot
        datas1M = np.genfromtxt('AllPrice/'+symbol+'1M.txt', delimiter=',')
        #name1M = pd.read_csv('AllPrice/'+symbol+'1M.txt')
        stocks1M = tuple(datas1M[:,][:,2])
        time1M = datas1M[:, ][:, 1]
        time1M = time1M - time1M[0]
        MV11M = int(len(stocks1M) * 0.01)
        MV21M = int(len(stocks1M) * 0.025)

        if MV11M > 1:
            MV11M = MV11M
        else:
            MV11M = 2

        if MV21M > 1:
            MV21M = MV21M
        else:
            MV21M = 4


        mv3stock1M1 = (movingaverage(stocks1M, MV11M))
        mv3stock1M2 = (movingaverage(stocks1M, MV21M))

        SP1M1 = len(time1M[MV11M-1:])
        SP1M2 = len(time1M[MV21M - 1:])
        stock1M = datas1M[:, ][:, 2]

        # 1Y plot
        datas1Y = np.genfromtxt('AllPrice/'+symbol+'1Y.txt', delimiter=',')
        #name1Y = pd.read_csv('AllPrice/'+symbol+'1Y.txt')
        stocks1Y = tuple(datas1Y[:,][:,2])
        time1Y = datas1Y[:, ][:, 1]
        time1Y = time1Y - time1Y[0]
        MV11Y = int(len(stocks1Y) * 0.01)
        MV21Y = int(len(stocks1Y) * 0.025)
        if MV11Y > 1:
            MV11Y = MV11Y
        else:
            MV11Y = 2

        if MV21Y > 1:
            MV21Y = MV21Y
        else:
            MV21Y = 4


        mv3stock1Y1 = (movingaverage(stocks1Y, MV11Y))
        mv3stock1Y2 = (movingaverage(stocks1Y, MV21Y))

        SP1Y1 = len(time1Y[MV11Y-1:])
        SP1Y2 = len(time1Y[MV21Y - 1:])
        stock1Y = datas1Y[:, ][:, 2]

        mvavgplot11D = str(MV11D) + ' MA'
        mvavgplot21D = str(MV21D) + ' MA'

        fig = plt.figure(facecolor='black')
        fig1 = fig.add_subplot(2,2,1, axisbg='black')
        fig1.plot(time1D, stock1D[:, ][:, ], 'b-')
        fig1.plot(time1D[-SP1D1:], mv3stock1D1[-SP1D1:], 'r-', label=mvavgplot11D)
        fig1.plot(time1D[-SP1D2:], mv3stock1D2[-SP1D2:], 'g-', label=mvavgplot21D)
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
        fig2.plot(time1M, stock1M[:, ][:, ], 'b-')
        fig2.plot(time1M[-SP1M1:],mv3stock1M1[-SP1M1:] , 'r-',label=mvavgplot11M)
        fig2.plot(time1M[-SP1M2:],mv3stock1M2[-SP1M2:], 'g-',label=mvavgplot21M)
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
        fig3.plot(time1Y, stock1Y[:, ][:, ], 'b-')
        fig3.plot(time1Y[-SP1Y1:],mv3stock1Y1[-SP1Y1:] , 'r-',label=mvavgplot11Y)
        fig3.plot(time1Y[-SP1Y2:], mv3stock1Y2[-SP1Y2:], 'g-',label=mvavgplot21Y)
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
