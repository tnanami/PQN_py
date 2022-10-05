# PQN_py

**Piecewise Quadratic Neuron (PQN) model** is a spiking neuron model designed to faithfully reproduce a variety of neuronal activities with limited computational cost.
The PQN_py provides a simple python implementation of the PQN model. You can choose from the following 8 mode. Each mode is fitted to reproduce the corresponding ionic-conductance model.
VHDL version of the PQN model is available from [PQN_vhdl](https://github.com/tnanami/PQN_vhdl "PQN_vhdl").

|        |Mode                            |Target ionic-conductance model|Comment                    |
|:-------|:------------------------------:|:---------------------------:|:-------------------------:|
| RSexci |Regular Spiking                 |[1]                          |Fitted to a excitatory cell|
| RSinhi |Regular Spiking                 |[1]                          |Fitted to an inhibitory cell|
| FS     |Fast Spiking                    |[1]|
| LTS    |Low-threshold Spiking           |[1]|
| IB     |Intrinsically Bursting          |[1]|
| EB     |Elliptic Bursting               |[2]|
| PB     |Parablic Bursting               |[3]|
| Class2 |Class2 of Hodgkin Classification||

[1] M. Pospischil et al., “Minimal hodgkin-huxley type models for different classes of cortical and thalamic neurons.” Biological Cybernetics, vol. 99, no. 4-5, pp. 427–441, 2008.  
[2] X. J. Wang, “Ionic basis for intrinsic 40 hz neuronal oscillations,” NeuroReport, vol. 5, pp. 221–224, 1993  
[3] R. E. Plant, “Bifurcation and resonance in a model for bursting nerve cells,” Journal of Mathematical Biology, vol. 67, pp. 15–32, 1981.

# Usage
![demo](https://user-images.githubusercontent.com/108346049/191765808-160a4049-e4a5-4b7a-a9ed-0b254782c24e.png)

    git clone git@github.com:tnanami/PQN_py.git
    cd PQN_py

    # run simulation (RSexci mode) and plot result
    python demo.py

# demo.py
    # set a PQN cell
    # you can use RSexci, RSinhi, FS, LTS, IB, EB, PB, or Class2 mode
    cell0 = PQNModel(mode='RSexci')

    # length of simulation [s]
    tmax = 2

    # set the number of iterations
    number_of_iterations = int(tmax/cell0.PARAM['dt'])

    # set step input
    I = np.zeros(number_of_iterations)
    I[int(number_of_iterations/4):int(number_of_iterations/4*3)] = 0.09

    # run simulatiion
    v0 = []
    for i in range(number_of_iterations):
      cell0.update(I[i])
      v0.append(cell0.get_membrane_potential())

    # plot simulation result
    fig = plt.figure(figsize=(8,4))
    spec = gridspec.GridSpec(ncols=1, nrows=2, figure=fig, hspace=0.1, height_ratios=[4, 1])
    ax0 = fig.add_subplot(spec[0])
    ax1 = fig.add_subplot(spec[1])
    ax0.plot([i*cell0.PARAM['dt'] for i in range(0, number_of_iterations)], v0)
    ax0.set_xlim(0, tmax)
    ax0.set_ylabel("v")
    ax0.set_xticks([])
    ax1.plot([i*cell0.PARAM['dt'] for i in range(0, number_of_iterations)], I, color="black")
    ax1.set_xlim(0, tmax)
    ax1.set_xlabel("[s]")
    ax1.set_ylabel("I")
    plt.savefig("demo.png")
    plt.show()

## Example
![all](https://user-images.githubusercontent.com/108346049/194097484-b11a4031-efba-43f9-9c8b-e6649d6cb27f.png)
