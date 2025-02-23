import numpy as np

def main():
    header = "a, b, c, mc, mt, ic, it, g, beta0"
    dane = np.array([1,         # a
                     1,         # b
                     1,         # c
                     1,         # mc
                     1,         # mt
                     2,         # ic
                     2,         # it
                     1,         # g
                     np.pi/2,   # beta0
                     0,         # t0
                     np.pi,     # alpha0
                     1,         # alpha_der0
                     0,         # gamma0
                     0,         # gamma_der0
                     0.00001,   # step_size
                     1000000,   # steps
                     4,         # ilosc_rown
                     960        # anim_freq
                     ])
    np.savetxt('parametry.txt', dane, header=header)



if __name__ == '__main__':
    main()

