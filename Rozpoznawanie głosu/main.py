import soundfile
import sys
from os import listdir
from os.path import isfile, join

import numpy as np
from numpy import argmax
from scipy.fftpack import fft, fftfreq
from scipy.signal import decimate

PATH = "train/"
male = (80, 175)
female = (175, 300)
positive = 0
kk = 0
mm = 0
km = 0
mk = 0
negative = 0
all = 0


def check_file(file_name, flag=0):
    global positive, negative, all, kk, km, mk, mm
    if file_name == "empty":
        file_name = PATH + sys.argv[1]
    else:
        file_name = PATH + file_name
    data, samplerate = soundfile.read(file_name, always_2d=True)
    data = data[:, 0]
    datax = fftfreq(len(data), 1 / samplerate)

    data = data * np.kaiser(len(data), 20)
    data = abs(fft(data))
    data_cpy = data.copy()
    temp = 0
    for i in range(2, 5):
        temp = decimate(data, i)
        data_cpy[:len(temp)] += temp
    data_masked = []
    datax_masked = []
    for i in range(len(datax)):
        if (male[0] <= datax[i]) & (datax[i] <= female[1]):
            data_masked.append(data_cpy[i])
            datax_masked.append(datax[i])
    # print(argmax(data_cpy[mask]))
    # print(*data[:100])
    # print(*mask[:100])
    freq = datax_masked[argmax(data_masked)]

    # print(freq)
    if male[0] <= freq < male[1] and not flag:
        print("M")

    if female[0] <= freq < female[1] and not flag:
        print("K")

    if male[0] <= freq < male[1] and flag:
        if "M" in file_name:
            print("M " + file_name + " True")
            positive += 1
            mm += 1
        else:
            print("M " + file_name + " False")
            negative += 1
            print(freq)
            mk += 1
    if female[0] <= freq < female[1] and flag:
        if "K" in file_name:
            print("K " + file_name + " True")
            positive += 1
            kk += 1
        else:
            print("K " + file_name + " False")
            negative += 1
            km += 1
            print(freq)
    all += 1
    # print(data.shape)


def check_folder():
    files = [f for f in listdir(PATH) if isfile(join(PATH, f))]
    print(files)
    for file in files:
        check_file(file, 1)


def main():
    if len(sys.argv) == 2:
        check_file("empty")
    else:
        check_folder()
        print("Testów posytywnych ", round(positive / all *100, 2) , "%")
        print("Testów negatywnych ", round(negative / all *100, 2) , "%")

        print("Kobieta rozpoznana jako Kobieta = " + str(kk))
        print("Kobieta rozpoznana jako Mężczyzna = " + str(km))
        print("Mężczyzna rozpoznany jako Mężczyzna = " + str(mm))
        print("Mężczyzna rozpoznany jako Kobieta = " + str(mk))


if __name__ == "__main__":
    main()