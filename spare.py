
if __name__ == "__main__":
    # This was a test. It worked
    #print(G(0.0,1.0,1.0,1.0,1000.0))

    # This was also a test. It also worked
    #print(G(10.0,1.0,1.0,1.0,1000.0))

    plot_k(10000)

    
# To keep

 #                x = np.linspace(0.01,0.99,10000)

#             y = np.array([G(xi,eps,C,k,N) for xi in x])

#             #plt.figure()

#             #plt.step(x,y,where="mid")



# def next(Ri):
        #     return calc_prob(float(Ri),eps,C,k,N,scale)

# for k in k_range:
        
        # R_prob = [next(1.0)]

        # Ri = 1.0

        # while R_prob[-1] != 1.0:
        #     Ri += 1.0
        #     R_prob.append(next(Ri))

        # R_prob = np.array(R_prob)

        # to_use.append(R_prob)

        # R = np.arange(1,len(R_prob)+1)

        # print(R_prob)

        # plt.figure()

        # plt.semilogy(R,R_prob,'.')

        # plt.show()
