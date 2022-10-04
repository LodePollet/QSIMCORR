Z2 parton phases in the mixed-dimensional t-Jz model
====================================================

Open access data to supplement our F. Grusdt and L. Pollet, PRL 125, 256401 (2020).
Please refer to this main text for an in-depth discussion.
THIS README provides information on how the data, which is made available in this repo, is structured

Authors
-------
* Fabian Grusdt, LMU Munich, Germany
* Lode Pollet, LMU Munich, Germany

Structure
---------

Data for Figs 2,3, and 4 of the main text are made available in the subdirectories with the same name.
For units and conventions we refer to the main text.

### Figure 2

Contains five subdirectories corresponding to five different temperatures for the otherwise same system.

Each subdirectory contains seven files, where the affix denotes the date (July 24, 2020) when the data was taken from the cluster.

profile : col 1 : x ; col 2 : y ; col 3 average total density (<n_up(x,y)> + n_down(x,y)>) ; col 4 error bar ; col 5 average total magnetization ((<n_up(x,y)> - n_down(x,y)>)/2) ; col 6 : its error bar 

profile_rowav : same as profile, but the average over all rows is taken. Hence, only the x coordinate is shown in the first colum ranging from 0 to 29.

corrfun : this contains the hole-hole and the spin-spin correlation function; col 1 : site s1; col 2 : site s2; col 3 : <n_h(s1) n_h(s2)> col 4 : its error bar; col 5 : <S(s1) S(s2) > ; col 6 : its error bar; Sites s1 and s2 range from 0 to 899; row major ordering is used to determine this index.

gx : hole-hole correlation function with respect to the middle column; the file contains 30 rows and each row. The first entry is the row index; this is followed by 30 triplets where the first number contains the separation to the middle, the second number is the average hole-hole correlation function for these two sites and the third number is the corresponding error bar.

gy : analogous as gx but for the function gx (hole-hole correlation function with respect to the middle row -- see text)

cx : same as gx but for the spin-spin correlation function (see text) 

cy : same as gy but for the spin-spin correlation function (see text)


Simulation parameters (Chargon) : system size 30x30 (open boundary conditions, Neel background), t = 1, J = 0.333333333, 12 spin up and 12 spin down particles per row
The value of beta is mentioned in the directory name 
Error bars determined from 40 independent runs. Correlations in the error bar between the distances are neglected.

The data set (in particular corrfun) for beta = 10 was used for the structure factor in Fig 5.

### Figure 3

Contains three subdirectories Chargon, Meson, and Stripe corresponding to the three panels of Fig 3 in the paper.
Each subdirectory contains one textfile hist_240720 containing the normalized histogram of the distance distributions between the four holes, counting from left to right. The data were taken from the cluster on July 24, 2020.

The file contains thirteen columns:

col 1       : distance coordinate

col 2  + 3  : histogram between holes 1 and 2 plus the corresponding error bar

col 4  + 5  : histogram between holes 1 and 3 plus the corresponding error bar

col 6  + 7  : histogram between holes 1 and 4 plus the corresponding error bar

col 8  + 9  : histogram between holes 2 and 3 plus the corresponding error bar

col 10 + 11 : histogram between holes 2 and 4 plus the corresponding error bar

col 12 + 13 : histogram between holes 3 and 4 plus the corresponding error bar

The final line contains the value of <tau_x> + its error bar.

Simulation parameters (Chargon) : system size 80x10 (open boundary conditions, Neel background), t = 1, J = 1, 30 spin up and 30 spin down particles per row, beta = 0.1 

Simulation parameters (Meson)   : system size 80x10 (open boundary conditions, Neel background), t = 1, J = 2, 38 spin up and 38 spin down particles per row, beta = 0.5

Simulation parameters (Stripe)  : system size 80x10 (open boundary conditions, Neel background), t = 1, J = 1, 30 spin up and 30 spin down particles per row, beta = 5.0

Error bars determined from 40 independent runs. Correlations in the error bar between the distances are neglected.


### Figure 4

Same structure as for Figure 3.
Simulation parameters: system size 80x10 (open boundary conditions, Neel backgroun), t = 1, J = 1, 38 spin up and 38 spin down particles per row, beta = 1 (Meson), beta = 100 (stripe), beta = 0.05 (chargon)
For the stripe case, the combination of 4 particles with open boundary conditions led to strong boundary effects. We therefore switched to a simulation of size L = 120x60, t=J=1, periodic boundary conditions, beta = 20, and 6 holes per row. Correspondingly, the table contains 31 columns with the counting of the holes in a similar way as before. For these distance measurements the periodic boundary conditions were not taken into account.
Error bars determined from 40 independent runs. Correlations in the error bar between the distances are neglected.

Requirements
------------

Only a text viewer is needed to read the data. 
  


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
