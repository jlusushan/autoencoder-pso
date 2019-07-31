import math
import numpy as np
from random_initial import random_int_list
# sphere function
def func1(x):
    total = 0
    for i in range(0, len(x)):
        total += x[i] ** 2
    #print(x[i])
    return total

# Quardirc function
def func2(x):
    total = 0
    for i in range(0, len(x)):
        for j in range(0, i+1):
            total += x[j]**2
    return total

# Rosenbrock function
def func3(x):
    total = 0
    for i in range(0, len(x)-1):
        total += (x[i+1] - (x[i]**2))**2 + (x[i] - 1)**2
    return total

# Schwefel function
def func4(x):
    total = 0
    for i in range(0, len(x)):
        total += 418.9829 -x[i] * math.sin(math.sqrt(abs(x[i])))
    return total
#420.9687

# Step function
def func5(x):
    total = 0
    for i in range(0, len(x)):
            total += int(x[i] -0.5) ** 2
    return total

# Dminima function
def func6(x):
    total_1 = 0
    for i in range(0, len(x)):
        total_1 += (x[i] ** 4 - 16 * (x[i] ** 2) + 5 * x[i])  /len(x)
    total = 78.332331408 + total_1
    return total

#High conditioned Elliptic function
def func7(x):
    total = 0
    for i in range(0, len(x)):
        total += ((10 ** 6) ** ((i-1) / (len(x)-1))) * (x[i] ** 2)
    return total

#Diffpower function
def func8(x):
    total = 0
    for i in range(1, len(x)):
        a = 10 ** ((i-1)/(len(x)-1))
        total += x[i] ** (2 + a)
    return  total

def func9(x):
    a = x[1:] - (x[:-1] ** 2)  # [:-1]->todos exceto os 2 últimos
    b = x[:1] - 1  # [:1]->do começo ao fim-1
    y = 100 * (a ** 2) + (b ** 2)
    return y.sum()

def func10(x):
    total = 0
    for i in range(1,len(x)):
        total += x[i]**2 - 10*math.cos(2*(math.pi)*x[i])+10
    return total

def func11(x):
    total = 0
    total_1 = 0
    a = 0
    b = 1
    for i in range(1,len(x)+1):
        a += x[i-1] ** 2
        b *= math.cos(x[i-1]/math.sqrt(i))
    total = a/4000 - b + 1

    return total

def func12(x):
    total_1 = 0
    total_2 = 0
    for i in range(0,len(x)):
        total_1 += x[i] ** 2
        total_2 +=(1/len(x))* math.cos(2*math.pi* x[i])
    #a = -20*math.exp(-0.2 * math.sqrt((1/len(x))* total_1))
    #b = -math.exp((1/len(x)* total_2))
    total = -20*math.exp(-0.2 * math.sqrt((1/len(x))* total_1)) + -math.exp(total_2) + 20 + math.e
    return total

def func13(x):
    a = 0.5
    b= 3
    k_max = 20
    total = 0
    total_1 = 0
    total_2 = 0
    for i in range(0, len(x)):
        for k in range(0, k_max):
            total_1 += (a ** k) * math.cos(2*math.pi * (b**k) * (x[i]+0.5))
    for k in range(0, k_max):
        total_2 += (a ** k) * math.cos(2 * math.pi * (b ** k) * 0.5)
    total = total_1 - total_2 * len(x)
    return total

def func14(x):
    total = 0
    for i in range(2,len(x )):
        total += x[i] ** 2
    return (1000* x[1])**2 + total

def func15(x):
    total = 0
    for i in range(1,len(x )):
        #print(x[i])
        total += x[i] ** 2
    return  x[0]**2 + total*(10 ** 6)

#Generalized penalized function1
def func16(x):
    total_1 = 0
    total_2 = 0
    y = []
    a = 0.5
    k =20
    m =3
    for i in range(1, len(x)-1):
        y[i] = 1 + 0.25*(x[i] + 1)
        total_1 += ((y[i] - 1)**2)*(1+(10*(math.sin(math.pi*y[i+1])**2)))
    for i in range(1, len(x)-1):
        if x[i] > a:
            total_2 += k*((x[i] - a)**m)
        elif x[i]< -a:
            total_2 += k*((-x[i] - a)**m)
        else:
            total_2 += 0
    return (math.pi/len(x))*(10*(math.sin(math.pi*y[1])**2)+total_1 + (y[len(x)]-1)**2) +total_2



#func1, func2, func7  func8正常
#func3, func5全0
#func4 趋近于834  func6趋近于78