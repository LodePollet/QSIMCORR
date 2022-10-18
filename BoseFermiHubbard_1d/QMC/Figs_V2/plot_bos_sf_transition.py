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


data_U4_L70 = np.loadtxt("./U4/stat_structfact_V2_U4_L70.out")
data_U4_L110 = np.loadtxt("./U4/stat_structfact_V2_U4_L110.out")
data_U4_L150 = np.loadtxt("./U4/stat_structfact_V2_U4_L150.out")
data_U45_L70 = np.loadtxt("./U4.5/stat_structfact_V2_U4,5_L70.out")
data_U45_L110 = np.loadtxt("./U4.5/stat_structfact_V2_U4,5_L110.out")
data_U45_L150 = np.loadtxt("./U4.5/stat_structfact_V2_U4,5_L150.out")

fig, ax = plt.subplots()

plt.errorbar(data_U4_L70[1:,0]/np.pi , data_U4_L70[1:,5]/ data_U4_L70[1:,0] * 2 * np.pi, yerr = data_U4_L70[1:,6]/ data_U4_L70[1:,0] * 2 * np.pi, fmt = "r.", label = r"$U=4.0, L=70 $")
plt.errorbar(data_U4_L110[1:,0]/np.pi , data_U4_L110[1:,5]/ data_U4_L110[1:,0] * 2 * np.pi, yerr = data_U4_L110[1:,6]/ data_U4_L110[1:,0] * 2 * np.pi, fmt = "b.", label = r"$U=4.0, L=110$")
plt.errorbar(data_U4_L150[1:,0]/np.pi , data_U4_L150[1:,5]/ data_U4_L150[1:,0] * 2 * np.pi, yerr = data_U4_L150[1:,6]/ data_U4_L150[1:,0] * 2 * np.pi, fmt = "g.-", label = r"$U=4.0, L=150$")
plt.errorbar(data_U45_L70[1:,0]/np.pi , data_U45_L70[1:,5]/ data_U45_L70[1:,0] * 2 * np.pi, yerr = data_U45_L70[1:,6]/ data_U45_L70[1:,0] * 2 * np.pi, fmt = "y.", label = r"$U=4.5, L=70 $")
plt.errorbar(data_U45_L110[1:,0]/np.pi , data_U45_L110[1:,5]/ data_U45_L110[1:,0] * 2 * np.pi, yerr = data_U45_L110[1:,6]/ data_U45_L110[1:,0] * 2 * np.pi, fmt = "m.", label = r"$U=4.5, L=110$")
plt.errorbar(data_U45_L150[1:,0]/np.pi , data_U45_L150[1:,5]/ data_U45_L150[1:,0] * 2 * np.pi, yerr = data_U45_L150[1:,6]/ data_U45_L150[1:,0] * 2 * np.pi, fmt = "c.-", label = r"$U=4.5, L=150$")
plt.xlim( [0, 1.01])
plt.legend(loc="lower right", fontsize=14)
plt.xlabel(r"$k/\pi$", fontdict=font1)
plt.ylabel(r"$ \frac{2 \pi S^{\rm bb}(k)}{k}$", fontdict=font1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

axins = ax.inset_axes([0.05, 0.25, 0.2, 0.2])
x1, x2, y1, y2 = 0.0, 0.08, 1.7, 1.9
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.set_xticklabels([])
axins.set_yticklabels([])
axins.errorbar(data_U45_L70[1:,0]/np.pi , data_U45_L70[1:,5]/ data_U45_L70[1:,0] * 2 * np.pi, yerr = data_U45_L70[1:,6]/ data_U45_L70[1:,0] * 2 * np.pi, fmt = "y.", label = r"$U=4.5, L=70 $")
axins.errorbar(data_U45_L110[1:,0]/np.pi , data_U45_L110[1:,5]/ data_U45_L110[1:,0] * 2 * np.pi, yerr = data_U45_L110[1:,6]/ data_U45_L110[1:,0] * 2 * np.pi, fmt = "m.", label = r"$U=4.5, L=110$")
axins.errorbar(data_U45_L150[1:,0]/np.pi , data_U45_L150[1:,5]/ data_U45_L150[1:,0] * 2 * np.pi, yerr = data_U45_L150[1:,6]/ data_U45_L150[1:,0] * 2 * np.pi, fmt = "c.", label = r"$U=4.5, L=150$")

ax.indicate_inset_zoom(axins, edgecolor="black")


plt.savefig("fig_bos_sf_transition_V2.pdf", format="pdf", bbox_inches="tight")
