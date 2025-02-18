import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def plot():
    data = np.loadtxt('plot_data.txt')
    x = data[:,0]
    y = data[:,1:5]
    plt.plot(x, y[:,0], label='alpha')
    plt.plot(x, y[:,1], label='alpha_der')
    plt.plot(x, y[:,2], label='gamma')
    plt.plot(x, y[:,3], label='gamma_der')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    plot()

