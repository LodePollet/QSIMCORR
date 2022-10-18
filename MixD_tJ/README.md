Phase Diagram of Mixed-Dimensional Anisotropic t-J-Models
=========================================================

Open access data to supplement our preprint J.Dicke et al, arXiv:2210.07300
Please refer to this main text for an in-depth discussion.
THIS README provides information on how the data, which is made available in this repo, is structured

Authors
-------
* Julius Dicke, LMU Munich, Germany
* Lukas Rammelmueller, LMU Munich
* Fabian Grusdt, LMU Munich, Germany
* Lode Pollet, LMU Munich, Germany

Structure
---------

Data for all Figures of the main text are made available in the subdirectories with the same name.
For units and conventions we refer to the main text.

### Figure 1

Only a pdf file

### Figures 2-5

See the python scripts to read and plot the data

### Figure 6

See the python scripts to read and plot the data. Note the additional directory for beta=10, showing the absence of hysteresis as claimed but not shown in the text

### Figures 7-9

See the python scripts to read and plot the data. The textfiles contain data for 
- the structure factor (sfh_L60.dat and sfh_L120.dat : the length of the system along the x-direction is mentioned in the file name; the files contain three columns : beta, value and error).
- the antiferromagnetic order parameters (sfh_L60.dat and sfh_L120.dat : the length of the system along the x-direction is mentioned in the file name; the files contain 11 columns: (1) beta, (2) measure for the hole-hole order parameter and not used, (3) error bar, (4) AFM order parameter without squeeze, (5) error bar, (6) squared AFM order parameter without squeeze, (7) error bar, (8) AFM order parameter in squeezed space, (9) error bar, (10) squared AFM order parameter in squeezed space, (11) error bar)


Requirements
------------

Only a text viewer is needed to read the data. 
Python3 with numpy and matplotlib are needed to generate the plots. Python3 with scipy is needed for fitting.  


License
-------

Copyright © 2020  Lode Pollet

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
