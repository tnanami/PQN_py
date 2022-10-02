# PQN_py

**Piecewise Quadratic Neuron (PQN) model** is a spiking neuron model designed to faithfully reproduce a variety of neuronal activities with limited computational cost.
PQN_py provides a simple python implementation of the PQN model. You can choose from the following 8 mode. Each mode is fitted to reproduce the corresponding ionic-conductance model.

|        |Mode                            |Target ionic-conductance model|Comment                    |
|:-------|:------------------------------:|:---------------------------:|:-------------------------:|
| RSexci |Regular Spiking                 |[1]                          |Fitted to a excitatory cell|
| RSinhi |Regular Spiking                 |[1]                          |Fitted to an inhibitory cell|
| FS     |Fast Spiking                    |[1]|
| LTS    |Low-threshold Spiking           |[1]|
| IB     |Intrinsically Bursting          |[2]|
| EB     |Elliptic Bursting               |[3]|
| PB     |Parablic Bursting               |[4]|
| Class2 |Class2 of Hodgkin Classification||

---

![demo](https://user-images.githubusercontent.com/108346049/191765808-160a4049-e4a5-4b7a-a9ed-0b254782c24e.png)

    git clone git@github.com:tnanami/PQN_py.git
    cd PQN_py
    python demo.py
