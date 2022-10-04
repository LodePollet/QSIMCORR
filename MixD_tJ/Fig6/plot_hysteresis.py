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
fw120 = np.loadtxt("FW_L120.dat")
bw120 = np.loadtxt("BW_L120.dat")

V1 = 1800
V2 = 7200

plt.errorbar(fw60[:,0], fw60[:,1]/V1, yerr=fw60[:,2]/V1, fmt="bs-", label=r"$L_x = 60$")
plt.errorbar(bw60[:,0], bw60[:,1]/V1, yerr=bw60[:,2]/V1, fmt="ro-", label=r"$L_x = 60$")
plt.errorbar(fw120[:,0], fw120[:,1]/V2, yerr=fw120[:,2]/V2, fmt="cx-", label=r"$L_x = 120$")
plt.errorbar(bw120[:,0], bw120[:,1]/V2, yerr=bw120[:,2]/V2, fmt="m.-", label=r"$L_x = 120$")
plt.xlabel(r"$\mu$", fontdict=font1)
plt.ylabel("n", fontdict=font1)
plt.annotate("", xy=(0.85, 0.78), xytext=(0.8, 0.76), arrowprops=dict(edgecolor="blue",arrowstyle="->", connectionstyle="arc3"))
plt.annotate("", xy=(0.92, 0.81), xytext=(0.86, 0.785), arrowprops=dict(edgecolor="cyan",arrowstyle="->", connectionstyle="arc3"))
plt.annotate("", xy=(0.8, 0.8), xytext=(0.85, 0.82), arrowprops=dict(edgecolor="red",arrowstyle="->", connectionstyle="arc3"))
plt.annotate("", xy=(0.72, 0.77), xytext=(0.76, 0.785), arrowprops=dict(edgecolor="magenta",arrowstyle="->", connectionstyle="arc3"))
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_hysteresis.pdf", format="pdf")

