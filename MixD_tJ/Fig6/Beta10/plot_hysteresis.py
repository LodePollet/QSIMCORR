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



fw60 = np.loadtxt("FW_L60.dat")
bw60 = np.loadtxt("BW_L60.dat")

V1 = 1800
V2 = 7200

plt.errorbar(fw60[:,0], fw60[:,1]/V1, yerr=fw60[:,2]/V1, fmt="bs-", label=r"$L_x = 60$")
plt.errorbar(bw60[:,0], bw60[:,1]/V1, yerr=bw60[:,2]/V1, fmt="ro-", label=r"$L_x = 60$")
plt.xlabel(r"$\mu$", fontdict=font1)
plt.ylabel("n", fontdict=font1)
plt.annotate("", xy=(0.85, 0.78), xytext=(0.8, 0.76), arrowprops=dict(edgecolor="blue",arrowstyle="->", connectionstyle="arc3"))
plt.annotate("", xy=(0.8, 0.8), xytext=(0.85, 0.82), arrowprops=dict(edgecolor="red",arrowstyle="->", connectionstyle="arc3"))
#plt.arrow(0.85, 0.92, -0.05, -0.02, edgecolor="red")
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_hysteresis_beta10.pdf", format="pdf")

