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

V = 12 


d4 = np.loadtxt("./L4/V12/stat.txt")
d6 = np.loadtxt("./L6/V12/stat.txt")
d8 = np.loadtxt("./L8/V12/stat.txt")

x4 = d4[:,0]
x6 = d6[:,0]
x8 = d8[:,0]

ps4 = d4[:,-1]
ps6 = d6[:,-1]
ps8 = d8[:,-1]


cdw4 = d4[:,1]
cdw6 = d6[:,1]
cdw8 = d8[:,1]


filter4 = x4 <= 18
filter6 = x6 <= 18
filter8 = x8 <= 18

v1 = V / 0.717 
v2 = V * 2


plt.plot(x4[filter4], ps4[filter4], "go--")
plt.plot(x6[filter6], ps6[filter6], "rs--")
plt.plot(x8[filter8], ps8[filter8], "bd--")


filter4 = x4 >= 16
filter6 = x6 >= 16
filter8 = x8 >= 16


plt.plot(x4[filter4], cdw4[filter4], "go-", label="L=4")
plt.plot(x6[filter6], cdw6[filter6], "rs-", label="L=6")
plt.plot(x8[filter8], cdw8[filter8], "bd-", label="L=8")
plt.vlines(v1, 0 ,1,colors='k', linestyles='dotted', linewidths=[3])
plt.vlines(v2, 0 ,1,colors='k', linestyles='dotted', linewidths=[3])
plt.legend(loc="best", fontsize=16)
plt.xlabel(r"$U$", fontdict=font1)
plt.ylabel(r"$O^{\rm PS}, O^{\rm CDW}$", fontdict=font1)
plt.savefig("fig_Lanczos_V12.pdf", format="pdf", bbox_inches="tight")

