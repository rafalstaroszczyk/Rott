import numpy as np

def separate():
    data = np.loadtxt('plot_data.txt')
    filelen = data.shape[0]
    padlen = len(str(filelen))
    for i in range(filelen):
        np.savetxt("data/" + str(i).zfill(padlen) + ".txt", data[i,:])


if __name__ == '__main__':
    separate()

