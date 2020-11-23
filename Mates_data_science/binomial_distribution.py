#EXERCISE TO PRACTICE BINOMIAL DISTRIBUTION 

import numpy as np 
from numpy.random import binomial
from scipy.stats import binom 
from math import factorial
import matplotlib.pyplot as plt 

#function that implements binomial distribution 
def my_binomial(k,n,p):
    return factorial(n)/factorial(k)*factorial(n-k)*pow(p,k)*pow(1-p,n-k)

#Example with scipy library Probability density
dist= binom(3,0.5).pmf(2)

#Accumulated Probability density/ second example
dist_2=binom(3,0.5).cdf(2) 

#Simulation with 100 launches of an equilibrated coin
p=0.5
n=3

def plot_graph(num_trials):
    values=[0,1,2,3]
    arr=[]
    for _ in range(100):
        arr.append(binomial(n,p))
    sim= np.unique(arr,return_counts=True)[1]/len(arr)
    teoric=[binom(3,0.5).pmf(k) for k in values]
    plt.bar(values,sim, color= 'red')
    plt.bar(values,teoric , alpha=0.5, color= 'blue')
    plt.title(f'Experiments {num_trials}')
    plt.savefig('barras.png')
    plt.show


if __name__ == "__main__":
    example= my_binomial(2,3,0.5)
    print(f'Example 1 {example}')
    print(f'Example 2 {dist}')
    print(f'Example 3 {dist_2}')
    plot_graph(2000)
    



