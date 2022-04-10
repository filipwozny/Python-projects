import matplotlib.pyplot as plt
import csv
import numpy as np

PATH = "data/"

def odczyt(name):
    with open(name, newline='') as csvfile:
        lista = csv.reader(csvfile)
        lista2 = list(lista)
    return np.array(lista2)

def konwersja(dane):
    x = np.array(dane[0:,0])
    x = x.astype(int)

    x2 = np.array(dane[0:,1])
    x2 = x2.astype(int)
    y = []

    box = np.array(dane[-1:,2:])
    box = box.astype(float)
    box = box * 100

    box = box.astype(int)

    #print(*dane[0:,2:])
    for row in dane[0:,2:]:
        z = row.astype(float)
        #np.append(y,np.mean(z))
        y.append(np.mean(z)*100)
        #print(np.mean(z))
    #print(*y)
    #print(*x)
    #print(*x2)
    return x , x2 //1000 , y , box

def main():

    plik1 = PATH + "1evolrs"
    plik2 = PATH +"1coevrs"
    plik3 = PATH +"2coevrs"
    plik4 = PATH +"1coev"
    plik5 = PATH +"2coev"

    dane1 = odczyt(plik1+".csv")
    dane2 = odczyt(plik2+".csv")
    dane3 = odczyt(plik3+".csv")
    dane4 = odczyt(plik4+".csv")
    dane5 = odczyt(plik5+".csv")
    #print(*dane1[1:,2:])
    #print(*dane1[1:,:])
    x1 , x1_2, y1 ,box1 = konwersja(dane1[1:,:])
    x2, x2_2, y2 ,box2 = konwersja(dane2[1:, :])
    x3, x3_2, y3,box3 = konwersja(dane3[1:, :])
    x4, x4_2, y4,box4 = konwersja(dane4[1:, :])
    x5, x5_2, y5,box5 = konwersja(dane5[1:, :])
    #plt.figure(figsize=(4, 4))
    #plt.figure(figsize=(4, 4))

    plt.subplot(1,2,1)
    plt.plot(x1_2, y1 ,marker ='o',markevery=25 ,color='b',linewidth=0.8,markersize=5,mec='k', label = plik1)
    plt.plot(x2_2, y2,marker ='v',markevery=25 ,color='g',linewidth=0.8,markersize=5,mec='k',label = plik2)
    plt.plot(x3_2, y3,marker ='D',markevery=25 ,color='r',linewidth=0.8,markersize=5,mec='k',label = plik3)
    plt.plot(x4_2, y4,marker ='s',markevery=25 ,color='k',linewidth=0.8,markersize=5,mec='k',label = plik4)
    plt.plot(x5_2, y5,marker ='d',markevery=25 ,color='m',linewidth=0.8,markersize=5,mec='k',label = plik5)
    plt.tick_params(axis="both" ,direction='in')
    plt.xlabel('Rozegranych gier (x 1000)')
    plt.ylabel('Odsetek wygranych gier[%]')
    plt.xlim(0,max(x1_2))
    plt.ylim(60,100)
    plt.grid(linestyle = (0, (5, 10)), linewidth = 0.7)


    plt.legend(loc=4,numpoints=2)
    axes1 = plt.gca()
    axes2 = axes1.twiny()
    axes2.set_xticks(np.arange(x1[0],x1[-1]+2,40))
    axes2.set_xlabel('Pokolenia')
    plt.tick_params(axis="both", direction='in')
    plt.subplot(1,2,2)

    box_data = np.concatenate([box1,box2,box3,box4,box5])
    box_data = box_data.T

    #box_data = np.concatenate([box1, box2, box3, box4, box5])

    plt.boxplot(box_data,vert=True,notch=True,patch_artist=True,
                sym='b+',medianprops=dict(color='red'),
                showmeans=True, meanprops={"marker":"o","markerfacecolor":"blue",
                                            "markeredgecolor":"black","markersize":"5"} ,
                boxprops=dict(facecolor='none', color='blue'),
                whiskerprops=dict(linestyle = (0, (5, 10)),color='blue' , linewidth=1.1))

    plt.xticks([1, 2, 3,4,5], [plik1,plik2 ,plik3 ,plik4,plik5] , rotation=20)
    plt.grid(linestyle = (0, (5, 10)), linewidth = 0.7)
    plt.ylim(60,100)
    plt.tick_params(axis='both', labelleft='', labelright='on',direction='in')
    plt.show()
    #plt.savefig('myplot.pdf')
    plt.close()

if __name__ == '__main__':
    main()