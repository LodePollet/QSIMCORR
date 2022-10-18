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


data = np.loadtxt("stat_dens_V4_U6_L150.out")
xp = data[:,0]
gp = data[:,7]
gp_err = data[:,8]

L = xp.size
print(L)


def g(x,K,c):
  return (c * np.power(np.sin(np.pi*x/L), -(0.5/K)))



popt_dm, pcov_dm = curve_fit( g, xdata=xp[5:L-5], ydata=gp[5:L-5], sigma=gp_err[5:L-5]) 
print ("K_b : ", popt_dm[0], pcov_dm[0,0])
print(popt_dm)
print(pcov_dm)

plt.figure()
plt.errorbar(np.log(xp[1:L//2]), np.log(np.abs(gp[1:L//2])), yerr = gp_err[1:L//2] / gp[1:L//2] * np.abs(np.log(gp_err[1:L//2] + 1e-12)), fmt = "bo", label=r"$\mathcal{G}^{b}$")
plt.plot(np.log(xp[3:L//2]), np.log(np.abs(g(xp[3:L//2], *popt_dm))), "r-", label=r"$fit, \eta_{b} = %2.2f(2)$"  %(popt_dm[0])) 
plt.plot(np.log(xp[3:L//2]), np.log(np.abs(g(xp[3:L//2], 2.,popt_dm[1]))), "r--", label=r"$\eta_{b} = 2$" ) 
plt.legend(loc="best", fontsize=16)
plt.xlabel(r"$\ln x$", fontdict=font1)
plt.ylabel(r"$\ln \mathcal{G}^{b}(x)$", fontdict=font1)
plt.savefig("fig_dm_V4_U6_L150.pdf", format="pdf")




