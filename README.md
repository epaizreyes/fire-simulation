# Fire Simulator

This program simulates the spread of fire fire in a forest represented by a grid of dimensions w x h.

## Description

The simulation is carried out as follows:
* In the initial state, one or more squares are on fire.
* If a node of the forest grid is on fire at step t, then at step t+1 the fire will go out and this node will be filled with ash and can no longer burn. There is a probability p that the fire will spread to each of the 4 adjacent nodes.
* The simulation stops when there are no more nodes on fire.

## Input

The dimensions of the grid, the position of the nodes initially on fire, as well as the probability of propagation, are program parameters stored in a configuration file (either `.txt` or `.json`). The input parameters are case sensitive, please follow the corresponding sintaxis:

Example of a `.txt`:
```bash
widthGrid=3
heightGrid=3
burningProbability=0.5
initFire=[[1,1]]
```

Example of a `.json`:
```bash
{
    "widthGrid": 9,
    "heightGrid": 7, 
    "burningProbability": 0.7,
    "initFire": [[1,8], [4, 4]]
}
```

## Run

Python3 is used to run your simulation, for example as:

```bash
python3 src/main.py params.txt
```