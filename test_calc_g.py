import calc_G
import numpy as np

def test_upper_bound():
    """Tests that the upper bound of G is independent of alpha.
    """

    eps = 10.0**-5.0

    k_range = np.linspace(10.0,200.0,1001)

    max_val = []
    
    for k in k_range:

        d = 2.0

        N = np.ceil(k**(d*1.5))

        C = 0.1

        scale = 1.0

        # This should be independent of alpha if alpha < 1
        gradpoint = 1.0/(C*k*3.0)
        
        max_val.append(calc_G.G(gradpoint,eps,C,k,N))

    assert np.isclose(max_val[0],np.array(max_val)).all()

def test_default_bound():
    """Tests that when the standard GMRES estimate should kick in, it does.
    """

    eps = 10.0**-5.0

    k_range = np.linspace(10.0,200.0,1001)

    max_val = []
    
    for k in k_range:

        d = 2.0

        N = np.ceil(k**(d*1.5))

        C = 0.1

        scale = 1.0

        endpoint = 1.0/(C*k) + 1.0
        
        assert np.isclose(N,calc_G.G(endpoint,eps,C,k,N))

    
"""the probability of convergence in under R iterations is 1
(uniformly in $k$) if R is high enough."""

#probs.append(calc_G.calc_prob(float(threshold),eps,C,k,N,scale))