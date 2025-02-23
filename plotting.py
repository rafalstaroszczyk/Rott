import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def plot():
    data = np.loadtxt('plot_data.txt')
    x = data[:,0]
    y = data[:,1:5]
    plt.rcParams.update({
        #"text.usetex": True,
        "font.family": "sans-serif"
    })
    plt.rc('text', usetex=True)
    plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
    plt.plot(x, y[:,0], label=r'$\alpha$')
    plt.plot(x, y[:,1], label=r'$\dot{\alpha}$')
    plt.plot(x, y[:,2], label=r'$\gamma$')
    plt.plot(x, y[:,3], label=r'$\dot{\gamma}$')
    plt.xlabel(r'$t$')
    plt.legend()
    plt.savefig("wykres.png")
    #plt.show()


if __name__ == '__main__':
    plot()

