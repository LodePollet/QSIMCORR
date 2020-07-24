Data for the ground state energy per spin in the 2D Heisenberg model using the stochastic list method 
compared to the value obtained by A. Sandvik using the Stochastic Series Expansion method, Ref: A. W. Sandvik, Phys. Rev. B 56, 11678 (1997).
No trial wave function has been used.

System parameters 	
-----------------
* J = 1			(spin exchange amplitude)
* L = 10			(linear system size)


Contents
--------

* hetherington.dat : diffusion Monte Carlo results using Hetherington's scheme, see J. H. Hetherington, Phys. Rev. A 30, 2713 (1984)
* protocol1.dat : data obtained using protocol1 (see text; ie, the length of the list is kept fixed; a measuring list is sequentially filled and replaces the existing list when full)
* protocol2.dat : data obtained using protocol2 (see text; ie, the length of the list is kept fixed but a new measurement replaces an existing list entry at random)
* protocol3.dat : data obtained using protocol3 (see text; ie, the length of the list is given P = sqrt{MC_{time} / kappa} with kappa = 1.35 and MC_{time} the total number of Monte Carlo steps. 
* plot_comp_log.gpl : gnuplot plotting file
* comp_log.eps : plot of the data; this is Fig 4 in the text


Remarks
-------

For the Hetherington, protocol1 and protocol2 schemes the error has been estimated from the stochastic fluctuations within the same calculation.
For protocol3.dat the error bar is the maximum spread between 5-10 independent runs. In all cases the systematic error largely dominates over the stochastic one,
so we saw no reason to improve on the stochastic one.

