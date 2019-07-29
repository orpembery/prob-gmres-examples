import numpy as np
from scipy.optimize import bisect
from matplotlib import pyplot as plt
from scipy.stats import expon

def G(diff,eps,C,k,N):
    """Defines the probabalistic GMRES bound function.

    diff - L^\infty norm of n^(1) - n^(2)

    eps - in (0,1), the tolerance

    C - C_2 in the GMRES result

    k - the wavenumber

    N - the number of dofs

    Returns the bound. Uses natural logs
    """
    
    alpha = C * k * diff

    if alpha >= 1.0:
        val = N

    if alpha == 0.0:
        val = 1

    else:
    
        complicated = np.log(eps) / np.log( (2.0*alpha**0.5) / ((1.0+alpha)**2.0) )

        val = min([N,complicated+1.0])

    return val

def calc_prob(R,eps,C,k,N,scale):
    """Calculates the probability that GMRES converges in fewer than R
    iterations when the L^\infty norm of the difference is
    exp(scale)"""
    
    if R >= N:
        total_prob = 1.0
    else:

        def G_single(x):
            return G(x,eps,C,k,N)

        def G_single_R(y):
            return G_single(y) - R

        # Find the point at which we revert to the worst-case GMRES estimate
        endpoint = 1.0/(C*k)

        # Find the point at which the gradient is zero
        # One can calculate this by hand
        gradpoint = 1.0/(3.0*C*k)

        total_prob = 0.0
        
        if G_single(gradpoint) < R:
            # integrate [0,end]
            total_prob += expon.cdf(endpoint,scale=scale)

        elif int(G_single(gradpoint)) == int(R):
            total_prob = 1.0

        else:

            if G_single(0.0) < R:
                lower_point = bisect(G_single_R,0.0,gradpoint)
                lower_point = inch_forward(G_single_R,lower_point)
                # integrate [0,lower_point]
                total_prob += expon.cdf(lower_point,scale=scale)

            nearly_end = endpoint - 10.0**-10.0

            if G_single(nearly_end) < R:
                higher_point = bisect(G_single_R,gradpoint,nearly_end)
                higher_point = inch_backward(G_single_R,higher_point)
                # integrate [higher_point,end]
                total_prob += (expon.cdf(endpoint,scale=scale)-expon.cdf(higher_point,scale=scale))

    return total_prob

def inch_forward(fn,x):

    shift = 0.001
    
    while fn(x) == 0:
        x += shift
    return x-shift

def inch_backward(fn,x):

    shift = 0.001
    
    while fn(x) == 0:
        x -= shift
    return x+shift

if __name__ == "__main__":
    # This was a test. It worked
    #print(G(0.0,1.0,1.0,1.0,1000.0))

    # This was also a test. It also worked
    #print(G(10.0,1.0,1.0,1.0,1000.0))

    eps = 10.0**-6.0

    probs = []

    k_range = np.linspace(10.0,200.0,1001)


    for k in k_range:
    
        d = 2.0

        N = np.ceil(k**(d*1.5))

        C = 0.1 # Would need to estimate this?

        x = np.linspace(0.01,0.99,10000)

        y = np.array([G(xi,eps,C,k,N) for xi in x])
        
        #plt.figure()
        
        #plt.step(x,y,where="mid")

        scale = 1.0/k

        def next(Ri):
            return calc_prob(float(Ri),eps,C,k,N,scale)

        R_prob = [next(1.0)]

        Ri = 1.0

        while R_prob[-1] != 1.0:
            Ri += 1.0
            R_prob.append(next(Ri))
            
        R_prob = np.array(R_prob[:-1])

        R = np.arange(1,N+1)

        R = R[:len(R_prob)]

        #print(R_prob)

        #plt.figure()

        #plt.semilogy(R,R_prob,'.')

        #plt.show()

        probs.append(calc_prob(float(20),eps,C,k,N,scale))

        print(k)

    plt.plot(k_range,probs,'.')
    
    plt.show()
