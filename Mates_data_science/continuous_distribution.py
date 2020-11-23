#EXERCISE TO PRACTICE CONTINUOUS DISTRIBUTION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Transforming continuous distribution formula, into code (density dist)

def gaussian(x,mu,sigma):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*pow((x-mu)/sigma,2))

#Using scipy Acumulated distribution 

dist= norm(0,1)
x_1=np.arange(-4,4,0.1)
y_1=[dist.cdf(value) for value in x_1]



if __name__ == "__main__":
    x= np.arange(-4,4,0.1)
    y= gaussian(x,0.0,1.0)
    plt.plot(x,y)
    plt.savefig('barras_cont.png')
    plt.show

    plt.plot(x_1,y_1)
    plt.savefig('barras_cont_2.png')
    plt.show







