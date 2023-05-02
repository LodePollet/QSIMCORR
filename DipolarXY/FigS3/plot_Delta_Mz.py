import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit
font1 = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }

font2 = {'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 20,
        }

font3 = {'family': 'serif',
        'color':  'darkgreen',
        'weight': 'normal',
        'size': 20,
        }


data = np.loadtxt("mz_L33.dat")
datad2 = np.loadtxt("mz_L33_d2.dat")
L = 33
Lsq = L * L
norm = Lsq/4.

data_obc = np.loadtxt("../FigS1/L10_OBC/en_L10.dat")
norm_obc = 25



T_AFM = [0.500000, 0.600000, 0.700000, 0.800000, 0.900000, 1.000000, 1.100000, 1.200000, 1.300000, 1.400000, 1.500000, 1.600000, 1.700000, 1.800000, 1.900000, 2.000000, 2.500000, 3.000000, 3.500000, 4.000000, 4.500000, 5.000000, 5.500000, 6.000000, 6.500000, 7.000000, 7.500000, 8.000000, 8.500000, 9.000000, 9.500000, 10.000000]
DM_AFM = [0.691456, 0.727386, 0.761607, 0.791962, 0.818105, 0.840334, 0.859185, 0.875186, 0.888788, 0.900419, 0.910415, 0.919043, 0.926500, 0.933055, 0.938802, 0.943867, 0.961828, 0.972468, 0.979227, 0.983794, 0.987009, 0.989356, 0.991128, 0.992498, 0.993575, 0.994442, 0.995136, 0.995706, 0.996184, 0.996588, 0.996927, 0.997215]




xs = np.linspace(0, 1.8, 15)

plt.figure()
#plt.errorbar(1./data[:,0], data[:,-2]/norm, yerr = data[:,-1]/norm,    fmt = "bo", label=r"FM, L=33, $\delta=0$")
#plt.errorbar(1./datad2[:,0], datad2[:,-2]/norm, yerr = datad2[:,-1]/norm,    fmt = "cx", label=r"FM, L=33, $\delta=2$")
plt.errorbar(1./data_obc[:,0], data_obc[:,-2]/norm_obc, yerr = data_obc[:,-1]/norm_obc,    fmt = "m.", label="FM, L=10, OBC")
#plt.plot(T_AFM, DM_AFM, "rs", label="AFM")
#plt.plot(xs, xs*0.33, "c--", label = "0.33T/J")
#plt.plot(xs, xs*0.443,"b--", label = "0.443T/J")
plt.plot(xs, xs*0.6, "m--", label = "0.6T/J")
plt.xlabel(r"$T/J$", fontdict=font1)
#plt.ylabel(r"$S^+S^-(x) + h.c. - n_0(\beta)$", fontdict=font1)
plt.ylabel(r"$(\Delta M_z)^2/N$", fontdict=font1)
plt.xlim([0, 4.0])
plt.ylim([0,1])
plt.legend(loc="best", fontsize=12)
plt.savefig("fig_Delta_Mz_L33_OBC.pdf", format="pdf", bbox_inches="tight")


