from os import listdir
from fnmatch import fnmatch
import helmholtz_firedrake.utils as utils
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

this_directory = './'

csv_list = []
for filename in listdir():
    print(filename)
    if fnmatch(filename,'*csv'):
        csv_list.append(this_directory + filename)

info_data = utils.read_repeats_from_csv(this_directory+csv_list[0])

k_list = [10.0,20.0,30.0,40.0,50.0,60.0]

betas = [0.99,1.0,1.01]

df = pd.DataFrame(index=k_list,columns=betas)

for file in csv_list:

    data = utils.read_repeats_from_csv(this_directory+file)

    k = data[0]['k']

    beta = np.log(1.0/data[0]['scale'])/np.log(k)

    # A bit of a hack
    for new_beta in betas:
        if np.isclose(beta,new_beta):
            beta = new_beta

    df.loc[k,beta] = data[1][:,1]

for beta in betas:

    plt.figure()

    for k in k_list:

        data = df.loc[k,beta]

        plt.plot(k*np.ones((len(data))),data,'.')

    print(beta)
        
    plt.show()
