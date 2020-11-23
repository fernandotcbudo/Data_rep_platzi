#EXERCISE TO PRACTICE CONTINUOUS DISTRIBUTION - WINGS SIZE OF FLIES 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

df= pd.read_excel('s057.xls')
arr= df['Normally Distributed Housefly Wing Lengths'].values[3:]
values,dist= np.unique(arr,return_counts=True)


if __name__ == "__main__":
    plt.bar(values,dist)
    plt.savefig('flies.png')
    plt.show
