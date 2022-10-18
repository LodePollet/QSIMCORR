import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

data = np.loadtxt("strf_V8_U13.out")

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




x = data[:,0]


def linear(x,a,b):
  return a + b*x

def constant(x,a):
  return a 

popt_ch, pcov_ch = curve_fit( linear, xdata=x[1:-1], ydata=data[1:-1,2], sigma = data[1:-1,3])
popt_sp, pcov_sp = curve_fit( constant, xdata=x[1:-1], ydata=data[1:-1,4], sigma = data[1:-1,5])
popt_b,  pcov_b  = curve_fit( linear, xdata=x[:-1], ydata=data[:-1,6], sigma = data[:-1,7])

print(popt_ch)
print(popt_sp)
print(popt_b)

plt.figure()
plt.errorbar(x, data[:,2], yerr=data[:,3], fmt="bo", label=r"$S^{\rm CDW}(\pi)$")
plt.errorbar(x, data[:,4], yerr=data[:,5], fmt="gs", label=r"$S^{\rm SDW}(\pi)$")
plt.errorbar(x, data[:,6], yerr=data[:,7], fmt="rx", label=r"$S^{\rm bb}(\pi)$")
#plt.plot(x, linear(x, *popt_ch),   "b--", label=r"linear fit,\\ slope $\approx %3.3f$" %(popt_ch[1]) )  
#plt.plot(x, popt_sp[0]*np.ones_like(x), "g--", label=r"constant fit") 
#plt.plot(x, linear(x, *popt_b ),   "r--", label=r"linear fit, slope $\approx %3.3f$" %(popt_b[1]) ) 
plt.plot(x, linear(x, *popt_ch),   "b:", label=r"linear fit, slope $\approx %3.2f(2)$" %(popt_ch[1]) )  
#plt.plot(x, linear(x, *popt_ch),   "b--")  
plt.plot(x, popt_sp[0]*np.ones_like(x), "g--") 
plt.plot(x, linear(x, *popt_b ),   "r--" ) 
plt.xlim([0, 75])
plt.legend(loc="best", fontsize=16, frameon=False)
plt.xlabel(r"$L$", fontdict=font1)
plt.ylabel(r"$S(\pi)$", fontdict=font1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_strf_V8_U13.pdf", format="pdf", bbox_inches="tight")
