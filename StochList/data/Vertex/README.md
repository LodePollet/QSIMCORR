Data for comparing the first order selfconsistent 3point-vertex diagram of the Frohlich polaron with a Monte Carlo simulation using a bare series expansion

System parameters 
-----------------
* alpha = 5  	(effective coupling strength)
* mu = -4    		(energy offset)
* P = 10^6   		(list length)


Contents
--------

* qc_green : results obtained by the stochastic list method. Columns are: (1) tau  (2) G(p=0, tau) (3) error bar
* qc_NCA   : reference data following J. Greitemann and L. Pollet, arXiv/1711.03044; columns are (1) tau (2) G(p=0, tau)
* plot_vertex.gpl : gnuplot plotting file
* fig_vertex_comparison.eps : plot of the data; this is Fig 3 in the text

Remarks
-------

the convergence in the list length is examined in the subdirectory "Convergence" in relative terms. This is not discussed in the text.
