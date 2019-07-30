from helmholtz_nearby_preconditioning.experiments import nearby_preconditioning_experiment_exponential as experiment
import numpy as np

k_range = [10.0,20.0,30.0,40.0,50.0,60.0]

num_repeats = 100

for k in k_range:

    for scale_exponent in [0.0,0.5,1.0]:
        print(k,scale_exponent)

        scale = 1.0/k**scale_exponent    

        np.random.seed(12)
        
        experiment([k],scale,num_repeats)

