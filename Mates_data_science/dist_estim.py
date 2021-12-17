#EXERCISE TO PRACTICE DISTRIBUTION ESTIMATION 

import numpy as np
from matplotlib import pyplot 
from numpy.random import normal
from scipy.stats import norm

sample= normal(size= 10000)

#Parametric estimation 

sample = normal(loc=50, scale=5, size=1000) # mu = 50, sigma = 5
mu = sample.mean()
sigma = sample.std()
dist = norm(mu, sigma)
values = [value for value in range(30, 70)]
probabilities = [dist.pdf(value) for value in values]



if __name__ == "__main__":
    pyplot.hist(sample, bins=30, density=True)
    pyplot.plot(values, probabilities)
    pyplot.savefig('hist_2.png')
    pyplot.show()

    pyplot.hist(sample,bins=30)
    pyplot.show






