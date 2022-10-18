import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit


font1 = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

font2 = {'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 16,
        }

font3 = {'family': 'serif',
        'color':  'darkgreen',
        'weight': 'normal',
        'size': 16,
        }

K4 = np.loadtxt("./U4/Kbos.dat")
K45 = np.loadtxt("./U4.5/Kbos.dat")
plt.errorbar((1/np.log(K4[:,0])), K4[:,1], yerr=K4[:,2], fmt="r.-", label = r"$U=4.0$")
plt.errorbar((1/np.log(K45[:,0])), K45[:,1], yerr=K45[:,2], fmt="b.-", label = r"$U=4.5$")
plt.legend(loc="best", fontsize=16)
plt.xlabel(r"$1/{\rm ln} \, L$", fontdict=font1)
plt.ylabel(r"$\eta_{\rm b}$", fontdict=font1)
plt.savefig("fig_bos_K_transition_V2.pdf", format="pdf", bbox_inches="tight")
