import numpy as np

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

    else:
    
        complicated = np.log(eps) / np.log(2.0*alpha**0.5 / (1.0+alpha)**2.0 )

        val = min([N,complicated+1.0])

    return val

if __name__ == "__main__":
    # This was a test. It worked
    #print(G(0.0,1.0,1.0,1.0,1000.0))

    # This was also a test. It also worked
    #print(G(10.0,1.0,1.0,1.0,1000.0))

    
