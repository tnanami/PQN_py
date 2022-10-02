from src import PQNModel
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

if __name__ == "__main__":

    # set a PQN cell
    # you can use RSexci, RSinhi, FS, LTS, IB, EB, PB, or Class2 mode
    cell0=PQNModel(mode='RSexci')

    # length of simulation  0.1ms
    tmax=20000

    # set step input
    I=np.zeros(tmax)
    I[int(tmax/4):int(tmax/4*3)] = 0.09

    # run simulatiion
    v0=[]
    for i in range(tmax):
        cell0.update(I[i])
        v0.append(cell0.get_membrane_potential())

    # plot simulation results
    fig = plt.figure(figsize=(8,4))
    spec = gridspec.GridSpec(ncols=1, nrows=2, figure=fig, hspace=0.1, height_ratios=[4, 1])
    ax0 = fig.add_subplot(spec[0])
    ax1 = fig.add_subplot(spec[1])
    ax0.plot([i*cell0.PARAM['dt'] for i in range(0, tmax)], v0)
    ax0.set_xlim(0, tmax*cell0.PARAM['dt'])
    ax0.set_ylabel("v")
    ax0.set_xticks([])
    ax1.plot([i*cell0.PARAM['dt'] for i in range(0, tmax)], I, color="black")
    ax1.set_xlim(0, tmax*cell0.PARAM['dt'])
    ax1.set_xlabel("[s]")
    ax1.set_ylabel("I")
    plt.savefig("demo.png")
    plt.show()
