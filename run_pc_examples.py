from helmholtz_nearby_preconditioning.experiments import nearby_preconditioning_experiment_exponential as experiment

k_range = [10.0,20.0,30.0,40.0,50.0,60.0]

num_repeats = 100

for k in k_range:

    for scale_exponent in [0.99,1.0,1.01]:
        print(k,scale_exponent)

        scale = 1.0/k**scale_exponent    

        experiment([k],scale,num_repeats)

