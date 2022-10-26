Polaron mobility in the beyond quasiparticles regime
=================================================

Open access data to supplement Phys. Rev. Lett. 123, 076601 (2019), see also preprint arXiv:1812.10336 .
Please refer to the main text for an in-depth discussion.
THIS README provides information on how the data, which is made available in this repo, is structured

Authors (in alphabetical order)
------
* Abishek Kumar, University of Florida, USA
* Dmitrii L. Maslov, University of Florida, USA
* Andrey S. Mishchenko, RIKEN, Saitama, Japan
* Naoto Nagaosa, RIKEN, Saitama, Japan
* Lode Pollet, LMU Munich, Germany
* Nikolay V. Prokof'ev, University of Massachusetts, USA


Structure
---------

Data for Figs 2,3, and 4 of the main text are made available in the subdirectories with the same name.
For units and conventions we refer to the main text.

### Figure 2

The file "dc-mobility.dat" contains the result of the analytic continuation for the mobility at zero frequency, which is plotted in the paper (alpha = 2.5).
There are five columns: (i) the inverse temperature beta actually used in the simulation, (ii) the temperature T = 1/beta used for plotting, (iii) the value of the dc mobility, (iv) its lower error bar, and (v) its upper error bar.

The matsubara data for the quantity C_m (see Eq. 7 in the paper) is provided in the files named "betaxxxx.dat" where xxxx stands for the inverse temperature specified in the first column on "dc-mobility.dat". These files contain three columns: (i) the Matsubara index m, (ii) the quantity C_m, and (iii) its error bar obtained from 20-40 independent runs depending on the temperature.


### Figure 3

same as for Fig 2.

### Figure 4

Analytically continued data for the mobility as a function of frequency, mu(omega), are provided in the files named "Txxx.dat" where xxx stands for the corresponding temperature. There are 2 columns: (i) the frequency omega, and (ii) the corresponding mobility. 

The file "seeOC.gp" is optional and contains a gnuplot script to 



Requirements
------------

Only a text viewer is needed to read the data. An optional gnuplot-file is provided for Fig 4.
  

General Usage
-------------


License
-------

Copyright © 2018  Lode Pollet

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
