# PQN_py

**Piecewise Quadratic Neuron (PQN) model** is a spiking neuron model designed to faithfully reproduce a variety of neuronal activities with limited computational cost.
PQN_py provides a simple python implementation of the PQN model. You can choose from the following 8 modes:


|  TH  |  TH  |
| ---- | ---- |
|  TD  |  TD  |
|  TD  |  TD  |

|        |Mode                            |Comment       |
|:-------|:------------------------------:|:------------:|
| RSexci |Regular Spiking                 |     This     |
| RSinhi |Regular Spiking                 |    column    |
| FS     |Fast Spiking                    |     will     |
| LTS    |Low-threshold Spiking           |      be      |
| IB     |Intrinsically Bursting          |    center    |
| EB     |Elliptic Bursting               |   aligned    |
| PB     |Parablic Bursting               |   aligned    |
| Class2 |Class2 of Hodgkin Classification|   aligned    |



---

![demo](https://user-images.githubusercontent.com/108346049/191765808-160a4049-e4a5-4b7a-a9ed-0b254782c24e.png)

    git clone git@github.com:tnanami/PQN_py.git
    cd PQN_py
    python demo.py
