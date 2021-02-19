import numpy as np
from geneticalgorithm import geneticalgorithm as ga

"""
Rasperi Pi 50$   300g
Arduno     5$    200g
Asus Com.  400$   4000g
Sensors     20$    150g

"""

def f(X):
    pen=0
    pen2=0
    if 300*X[0]+200*X[1]+4000*X[2]+150*X[3]<10000:
        pen=(10000-(300*X[0]+200*X[1]+4000*X[2]+150*X[3]))*100
    if 300*X[0]+200*X[1]+4000*X[2]+150*X[3]>11000:
        pen=((300*X[0]+200*X[1]+4000*X[2]+150*X[3])-11000)*100

    if 50*X[0]+5*X[1]+400*X[2]+20*X[3]<1100:
        pen2=(1100-(50*X[0]+5*X[1]+400*X[2]+20*X[3]))*100
    if 50*X[0]+5*X[1]+400*X[2]+20*X[3]>1200:
        pen2=((50*X[0]+5*X[1]+400*X[2]+20*X[3])-1200)*100
    print(X)
    print("prince :")
    print(50 * X[0] + 5 * X[1] + 400 * X[2] + 20 * X[3])
    print("Weight :")
    print(300*X[0]+200*X[1]+4000*X[2]+150*X[3])
    print()
    return np.sum(-1*(X[0]+X[1]+X[2]+X[3]))+pen+pen2

varbound=np.array([[1,100]]*4)
model=ga(function=f,dimension=4,variable_type='int',variable_boundaries=varbound)
model.run()

"""
The best solution found :
X=[ 1.  7.  1. 35.]
#this means the following:
X=[1, 7, 1,35]
print(50*X[0]+5*X[1]+400*X[2]+20*X[3])  
print(300*X[0]+200*X[1]+4000*X[2]+150*X[3])
# It means the price =1185 and the weight=10950  

"""