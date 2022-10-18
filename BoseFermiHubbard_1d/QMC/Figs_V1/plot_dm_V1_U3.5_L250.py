import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

#####################################################

L = 250


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

def f(x,a, K):
  return a - np.log(np.sin(np.pi * x / L))/2. / K

data_dens = np.loadtxt("stat_dens_V1_U3.5_L250.out")
xdata = data_dens[:,0]
ydata = np.log(data_dens[:,7])
ystd = np.abs((data_dens[:,8] / data_dens[:,7]) * np.log(data_dens[:,7]))


popt, pcov = curve_fit(f, xdata[5:L-5], ydata[5:L-5], sigma=ystd[5:L-5])
print (popt, pcov)

plt.figure()
plt.errorbar(np.log(xdata[1:L//2:2]) , ydata[1:L//2:2], yerr= ystd[1:L//2:2], fmt="bo",  label=r"$\mathcal{G}^{b}$")
#plt.plot(np.log(xdata[3:L//2]), np.log(np.abs(f(xdata[3:L//2], *popt))), "r--", label=r"$fit, \eta_{b} = %2.2f(2)$"  %(popt[0])) 
plt.plot(np.log(xdata[1:L//2]), f(xdata[1:L//2], *popt), 'r--', label=r"$fit, \eta_{b} = %2.2f(2)$"  %(popt[1]))
plt.xlabel(r"${\rm ln} \,\, x$", fontdict=font1)
plt.ylabel(r"$\rm{ln} \, \mathcal{G}^B(x), {\rm fit}$", fontdict=font1  )
plt.legend(loc="best", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.savefig("fig_dm_boson_V1_U3,5_L250.pdf", format="pdf", bbox_inches="tight")



