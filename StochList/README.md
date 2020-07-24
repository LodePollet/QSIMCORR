Stochastic lists: Sampling multi-variable functions with population methods
=================================================

Open access data to supplement our preprint []()
Please refer to this main text for an in-depth discussion.
THIS README provides information on how the data, which is made available in this repo, is structured

Authors
-------
* Lode Pollet, LMU Munich
* Nikolay Prokof'ev, University of Massachusetts
* Boris Svistunov, University of Massachusetts


Project Structure
-----------------

We provide open data as well as an open source implementation to reproduce Figure 5.
This is an implementation of stochastic lists for the Heisenberg model on the square lattice with J=1
using protocol 3 (ie, the length of the list is proportional to the square root of the Monte Carlo simulation time)
and implementing a Gutzwiller trial wave function (see text). 

Data for the figures can be found in the data folder; the source files for the code in the src folder.


Requirements
------------

The code requires only a C++-11 compliant compiler. It runs in serial.
Postprocessing including error evaluation is left for the user.
  

General Usage
-------------

### compilation
g++ -std=c++11 -O3 -o xstochlist.x mc.cpp

### Running a simulation from a parameter file
./xstochlist.x

edit the params file to fix the parameters


License
-------

Copyright © 2018  Lode Pollet, Nikolay Prokof'ev and Boris Svistunov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

A copy of the GNU General Public License is available in the
file [LICENSE.txt](LICENSE.txt).

