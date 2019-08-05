from helmholtz_nearby_preconditioning.experiments import nearby_preconditioning_experiment_exponential as experiment
import numpy as np

k_range = [15.0,25.0,35.0]#,40.0,50.0,60.0]

num_repeats = 1000

scale_exponents = [0.0,1.0,2.0]

for k in k_range:

    for scale_exponent in scale_exponents:
        print(k,scale_exponent)

        scale = 1.0/k**scale_exponent    

        np.random.seed(12)
        
        experiment([k],scale,num_repeats)

