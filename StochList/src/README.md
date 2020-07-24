Program
-------
Implementation of the stochastic list for the 2D Heisenberg model using protocol 3 (see text).


General Usage
-------------

### compilation
g++ -std=c++11 -O3 -o xstochlist.x mc.cpp

### Running a simulation from a parameter file
./xstochlist.x

edit the params file to fix the parameters


### output (all text files) ###
* qc_params       : listing the system and simulation variables
* qc_conf         : checkpointing
* qc_updates      : statistics of the Monte Carlo updates
* qc_convergence  : monitoring the convergence as a function on Monte Carlo time
  
