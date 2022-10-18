Phase Diagram of Mixed-Dimensional Anisotropic t-J-Models
=========================================================

Open access data to supplement the preprint J.Schönmeier-Kromer and Lode Pollet, Competing Instabilities at long length scales in the one-dimensional Bose-Fermi-Hubbard model at commensurate fillings, arXiv:2210.XXXX
Please refer to this main text for an in-depth discussion.
THIS README provides information on how the data, which is made available in this repo, is structured

Authors
-------
* Janik Schönmeier-Kromer, LMU Munich, Germany
* Lode Pollet, LMU Munich, Germany

Structure
---------

Data and plotting scripts for all figures of the main text are made available in the subdirectories.
The subdirectories are grouped according to the method (Lanczos or QMC: Quantum Monte Carlo). 
Inside the QMC directory, Fig 1 contains the data for the phase diagram, Fig.5 and Fig.6 refer to the figures labelled with the corresponding number in the main text, and the directors Figs_Vn with n=1,2,3,4,5,6, and 8 group all the data for the plots for Bose-Fermi Hubbard interaction V = n.
For units and conventions we refer to the main text.


Requirements
------------

Only a text viewer is needed to read the data, and a pdf viewer to view the plots. 
Python3 with numpy and matplotlib are needed to generate the plots. Python3 with scipy is needed for fitting.  


License
-------

Copyright © 2022  Lode Pollet

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
