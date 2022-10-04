import numpy as np
import matplotlib.pylab as plt

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



sf60 = np.loadtxt("sf_L60.dat")
sfh60 = np.loadtxt("sfh_L60.dat")
sf120 = np.loadtxt("sf_L120.dat")
sfh120 = np.loadtxt("sfh_L120.dat")


plt.errorbar(sf60[:,0], sf60[:,9], yerr=sf60[:,10], fmt="bs-", label=r"$O_{\rm AFM}^2, L_x = 60$")
plt.errorbar(sfh60[:,0], sfh60[:,1], yerr=sfh60[:,2], fmt="rd-", label=r"$O_{h}, L_x = 60$")
plt.errorbar(sf120[:,0], sf120[:,9], yerr=sf120[:,10], fmt="cs-", label=r"$O_{\rm AFM}^2, L_x = 120$")
plt.errorbar(sfh120[:,0], sfh120[:,1], yerr=sfh120[:,2], fmt="mo-", label=r"$O_{h}, L_x = 120$")
plt.xlabel(r"$\beta$", fontdict=font1)
plt.ylabel(r"$O_{\rm AFM}^2, O_h$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_stripes_nh_33_percent.pdf", format="pdf", bbox_inches="tight")

