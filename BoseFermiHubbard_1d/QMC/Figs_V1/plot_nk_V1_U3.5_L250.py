import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

#####################################################

L = 250
data_nk = np.loadtxt("qc_nk_V1_U3.5_L250")


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

plt.figure()
plt.errorbar(data_nk[:,1][1:L//2]/np.pi, data_nk[:,2][1:L//2], yerr=np.ones_like( data_nk[:,2][1:L//2]) * 0.01, fmt='bs-')
plt.xlabel(r"$k/{\pi}$", fontdict = font1)
plt.ylabel(r"$n(k)$", fontdict = font1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.savefig("fig_nk_V1_U3,5_L250.pdf", format="pdf", bbox_inches="tight")

