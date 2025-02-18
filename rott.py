import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import plotting


def runge_kutta(x_start, y_start, h, no_of_steps, size, f):
    x = np.zeros(no_of_steps)
    y = np.zeros((size, no_of_steps))
    x[0] = x_start
    y[:,0] = y_start
    
    for i in range(no_of_steps - 1):
        f0 = f(x[i]      , y[:,i]           )
        f1 = f(x[i] + h/2, y[:,i] + h/2 * f0)
        f2 = f(x[i] + h/2, y[:,i] + h/2 * f1)
        f3 = f(x[i] + h  , y[:,i] + h   * f2)

        x[i+1] = x[i] + h
        y[:,i+1] = y[:,i] + h/6 * (f0 + 2*f1 + 2*f2 + f3)

        print(i/steps)

    return x, y


def f(x, y):
    a = 1
    b = 1
    c = 1
    mc = 1
    mt = 1
    ic = 2
    it = 2
    g = 1
    beta0 = np.pi/2
    alpha = y[0]
    alpha_der = y[1]
    gamma = y[2]
    gamma_der = y[3]
    C = np.cos(beta0)*np.cos(alpha-gamma) - np.sin(beta0)*np.sin(alpha-gamma)
    S = np.sin(beta0)*np.cos(alpha-gamma) + np.cos(beta0)*np.sin(alpha-gamma)
    w = it*ic - (b*c*mc*C)**2
    w_alpha = - ic*a*mt*g*np.sin(alpha) - ic*b*c*mc*S*gamma_der**2 + b*c**2*mc**2*g*C*np.sin(gamma) - b**2*c**2*mc**2*C*S*alpha_der**2
    w_gamma = - it*c*mc*g*np.sin(gamma) + it*b*c*mc*S*alpha_der**2 + a*b*c*mt*mc*g*np.sin(alpha) + b**2*c*.2*mc**2*C*S*gamma_der**2
    alpha_dder = w_alpha/w
    gamma_dder = w_gamma/w
    return np.array([alpha_der, alpha_dder, gamma_der, gamma_dder])


def main():
    global steps
    steps = 1000 
    x, y = runge_kutta(0, (np.pi, 1, 0, 0), 0.00001, steps, 4, f)
    plt.plot(x, y[0,:])
    plt.plot(x, y[1,:])
    plt.plot(x, y[2,:])
    plt.plot(x, y[3,:])
    
    dane_do_pliku = np.concatenate((x.reshape(-1,1), np.transpose(y)), axis=1)
    np.savetxt('plot_data.txt', dane_do_pliku)
    plotting.plot()
    

if __name__ == '__main__':
    main()

