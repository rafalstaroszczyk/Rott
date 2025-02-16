import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def runge_kutta(x_start, y_start, x_end, h, no_of_steps, f):
    x = np.zeros((2, no_of_steps))
    x[:,0] = x_start
    y[:,0] = y_start
    
    for i in range(no_of_steps):
        f0 = f(x[i]      , y[i]           )
        f1 = f(x[i] + h/2, y[i] + h/2 * f0)
        f2 = f(x[i] + h/2, y[i] + h/2 * f1)
        f2 = f(x[i] + h  , y[i] + h   * f2)

        x[i+1] = x[i] + h
        y[i+1] = y[i] + h/6 * (f0 + 2*f1 + 2*f2 + f3)

    return x, y

def rott():
    a = 1
    b = 1
    c = 1
    mt = 1
    mc = 1

    beta0 = np.pi/2




def main():
    rott()

if __name__ == '__main__':
    main()

