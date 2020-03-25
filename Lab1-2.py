from random import random
from math import sin
from time import perf_counter
import matplotlib.pyplot as plt

class Function():

    def __init__(self, A, f, w, numbers_points = 64, accuracy = 0.1):
        self.A = A
        self.f = f
        self.w = w
        self.n_p = numbers_points
        self.accuracy = accuracy

    def func_sin(self):
        result = []
        for i in range(self.n_p):
            result.append([i * self.accuracy, self.A * sin(self.w * i * self.accuracy + self.f)])
        return result

class RandomSignal(Function):

    def __init__(self,n,w,n_p = 256):
        self.pointslist = []
        self.w = w
        self.n = n
        self.n_p = n_p
    def generete_signal(self):
        A = random()
        f = random()
        W = self.w / self.n
        result_new = []
        for i in range(self.n):
            new_w = self.w - W * i
            result = Function(A, f, new_w,self.n_p)
            result = result.func_sin()
            for j in range(len(result)):
                if len(result_new) == j:
                    result_new.append(result[j])
                else :
                    result_new[j][1] += result[j][1]
        self.pointslist = result_new
        return result_new


def Rxx(arr,t):
    listy = [x[1] for x in arr]
    N=len(arr)/2
    M=sum(listy)/len(listy)
    if t>N:
        print('т занадто велике')
        return 0
    else:
        Rxx = 0
        for j in range(int(N)):
            Rxx += (listy[j] - M) * (listy[j + t] - M) / (N-1)

        return Rxx
def Rxy(arr,arr2,t):

    listy = [x[1] for x in arr]
    listy2 = [x[1] for x in arr2]
    N=len(arr)/2

    M=sum(listy)/len(listy)
    M1=sum(listy2)/len(listy2)
    if t>N:
        print('т занадто велике')
        return 0
    else:
        Rxy = 0
        for j in range(int(N)):
            Rxy += (listy[j] - M) * (listy2[j + t] - M1) / (N-1)

        return Rxy
class Main:
    n = 14
    wt = 2000
    N = 256
    obj = RandomSignal(n,wt,N)
    points = obj.generete_signal()
    time1S = perf_counter()
    Rxxtlist = []
    for tay in range(int(N / 2)):
        Rxxtlist.append(Rxx(points,tay))
    time1F = perf_counter()
    obj1 = RandomSignal(n, wt, N)
    points1 = obj1.generete_signal()
    time2S = perf_counter()
    Rxytlist = []
    for tay in range(int(N / 2)):
        Rxytlist.append(Rxy(points,points1,tay))
    time2F = perf_counter()
    taylist = list(range(int(N/2)))
    resultTime1 = time1F - time1S
    resultTime2 = time2F - time2S
    plt.plot(taylist,Rxxtlist,color='b')

    plt.plot(taylist,Rxytlist,color='r')
    plt.savefig('demo.png', bbox_inches='tight')

