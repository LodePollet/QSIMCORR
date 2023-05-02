import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit
font1 = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }

font2 = {'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 20,
        }

font3 = {'family': 'serif',
        'color':  'darkgreen',
        'weight': 'normal',
        'size': 20,
        }


datah = np.loadtxt("dm_b02.dat")
datac = np.loadtxt("dm_b052.dat")
datal = np.loadtxt("dm_b1.dat")

L = 129
Lh = 65
n0 = 0.4397

#datal[:,1] = np.abs(datal[:,1] - n0)
datal[:,1] = datal[:,1] 

def pwlaw10(x,a):
  return a * np.power(np.sin(np.pi * x / L), -1.)
def pwlaw15(x,a):
  return a * np.power(np.sin(np.pi * x / L), -1.5)
def pwlaw30(x,a):
  return a * np.power(np.sin(np.pi * x / L), -3.)

def pwlaw_free(x,a,b):
  return a * np.power(np.sin(np.pi * x / L), -b)

print(datac[5:Lh-15,0])
print(datac[5:Lh-15,1])
print(datac[5:Lh-15,2])

popt_h, pcov_h = curve_fit( pwlaw30, xdata=datah[5:Lh-15,0], ydata=datah[5:Lh-15,1], sigma=datah[5:Lh-15,2]) 
print(popt_h, pcov_h)
popt_c, pcov_c = curve_fit( pwlaw10, xdata=datac[5:Lh,0], ydata=datac[5:Lh,1], sigma=datac[5:Lh,2]) 
print(popt_c, pcov_c)
#popt_l, pcov_l = curve_fit( pwlaw15, xdata=datal[5:Lh,0], ydata=datal[5:Lh,1], sigma=datal[5:Lh,2]) 
#popt, pcov = curve_fit( pwlaw_free, xdata=datal[5:Lh,0], ydata=datal[5:Lh,1], sigma=datal[5:Lh,2]) 
#print(popt, pcov)


plt.figure()
plt.errorbar(datah[1:Lh,0], datah[1:Lh,1], yerr = datah[1:Lh,2],    fmt = "bo",  label = r"$\beta=0.2$")
plt.plot(datah[5:Lh,0], pwlaw30(datah[5:Lh,0], *popt_h),      "b--", label =r"$\sim x^{-3}$") 
plt.errorbar(datac[1:Lh,0], datac[1:Lh,1], yerr = datac[1:Lh,2],    fmt = "rx", label = r"$\beta=0.52$")
plt.plot(datac[5:Lh,0], pwlaw10(datac[5:Lh,0], *popt_c),      "r--", label =r"$\sim x^{-1}$") 
plt.errorbar(datal[1:Lh,0], datal[1:Lh,1], yerr = datal[1:Lh,2],    fmt = "ms", label = r"$\beta=1$")
#plt.plot(datal[5:Lh,0], np.abs(pwlaw15(datal[5:Lh,0], *popt_l)),      "m--", label =r"$\sim x^{-1.5}$") 
#plt.plot(datal[5:Lh,0], np.abs(pwlaw_free(datal[5:Lh,0], *popt)),      "y--", label =r"$\sim x^{-%2.2f}$" % popt[1]) 
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r"$x$", fontdict=font1)
#plt.ylabel(r"$S^+S^-(x) + h.c. - n_0(\beta)$", fontdict=font1)
plt.ylabel(r"$S^+S^-(x) + {\rm h.c.}$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_pwlaw_spsm.pdf", format="pdf", bbox_inches="tight")


plt.figure()
plt.errorbar(datah[1:Lh,0], datah[1:Lh,3], yerr = datah[1:Lh,4],    fmt = "bo",  label = r"$\beta=0.2$")
plt.errorbar(datac[1:Lh,0], datac[1:Lh,3], yerr = datac[1:Lh,4],    fmt = "rx", label = r"$\beta=0.52$")
plt.errorbar(datal[1:Lh,0], datal[1:Lh,3], yerr = datal[1:Lh,4],    fmt = "ms", label = r"$\beta=1$")
plt.xlabel(r"$x$")
plt.ylabel(r"$S^zS^z(x)$")
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_szsz.pdf", format="pdf")




