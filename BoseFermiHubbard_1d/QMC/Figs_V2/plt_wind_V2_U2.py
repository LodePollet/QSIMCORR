import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt("wind_V2_U2.txt")
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
plt.errorbar(1./np.log(data[:,3]), data[:,6], yerr=data[:,7],  fmt="bo-", label=r"$<W^2_{\uparrow}>$")
plt.errorbar(1./np.log(data[:,3]), data[:,12], yerr=data[:,13], fmt="rx-", label=r"$<(W_\uparrow + W_{\downarrow})^2>$")
plt.errorbar(1./np.log(data[:,3]), data[:,10], yerr=data[:,11], fmt="gs-", label=r"$<(W_\uparrow - W_{\downarrow})^2>$")
#plt.xlabel(r"$1/L$", fontdict=font1)
#plt.xlim([0, 0.3])
#plt.ylim([0, 1.1])
plt.xlabel(r"$1/{\rm ln} L$", fontdict=font1)
plt.ylabel(r"$<W^2_{\uparrow}>, <(W_\uparrow \pm W_{\downarrow})^2>$", fontdict=font1)
plt.legend(loc="best", fontsize=14)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_wind_V2_U2.pdf", format="pdf", bbox_inches="tight")
