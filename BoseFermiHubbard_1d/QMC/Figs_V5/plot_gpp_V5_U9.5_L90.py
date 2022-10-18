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

#data = np.loadtxt("stat_dens.out")
#xpp = data[:,0]
#gpp = data[:,15]
#gpp_err = data[:,16]
#gph = data[:,13]
#gph_err = data[:,14]


cdw_data = np.loadtxt("stat_cdwsdw_V5_U9,5_L90.out")
xcdw = cdw_data[:,0]
L = xcdw.size
print(L)
cdw = cdw_data[:,1]
cdw_err = cdw_data[:,2]/L


def g(x,K,c):
  return (c * np.power(np.sin(np.pi*x/L), -K))



def f(x, K, A):
  #return ( -K/np.pi/np.pi/x/x + A*np.cos(np.pi*x)*np.power(np.sin(np.pi*x/L), -K))
  return ( -K/L/L/np.sin(np.pi*x/L)/np.sin(np.pi*x/L) + A*np.cos(np.pi*x)*np.power(np.sin(np.pi*x/L), -K))

def fconst(x, K, A, B):
  #return ( -K/np.pi/np.pi/x/x + A*np.cos(np.pi*x)*np.power(np.sin(np.pi*x/L), -K))
  return ( B*np.cos(np.pi*x) -K/L/L/np.sin(np.pi*x/L)/np.sin(np.pi*x/L) + A*np.cos(np.pi*x)*np.power(np.sin(np.pi*x/L), -K))

print(cdw)


#popt_pp, pcov_pp = curve_fit( g, xdata=xpp[5:L-5], ydata=gpp[5:L-5], sigma=gpp_err[5:L-5]) 
#print ("K_pp : ", popt_pp[0], pcov_pp[0,0])
#print(popt_pp)
#print(pcov_pp)

popt_cdw, pcov_cdw = curve_fit( f, xdata=xcdw[3:L//2], ydata=cdw[3:L//2], sigma = cdw_err[3:L//2])
print ("K_cdw : ", popt_cdw[0], pcov_cdw[0,0])
popt_const_cdw, pcov_const_cdw = curve_fit( fconst, xdata=xcdw[3:L//2], ydata=cdw[3:L//2], sigma = cdw_err[3:L//2])
print ("const : ", popt_const_cdw[2], pcov_const_cdw[2,2])
print(popt_const_cdw)
print(pcov_const_cdw)

#plt.figure()
#plt.errorbar(np.log(xpp[1:L]), np.log(np.abs(gpp[1:L])), yerr = gpp_err[1:L] / gpp[1:L] * np.abs(np.log(gpp_err[1:L] + 1e-12)), fmt = "bo", label=r"$\mathcal{G}^{pp}$")
#plt.errorbar(np.log(xpp[1:L]), np.log(np.abs(gph[1:L])), yerr = gph_err[1:L] / gph[1:L] * np.abs(np.log(gph_err[1:L] + 1e-12)), fmt = "gx", label=r"$\mathcal{G}^{ph}$")
#plt.plot(np.log(xpp[5:L//2]), np.log(np.abs(g(xpp[5:L//2], *popt_pp))), "r-", label=r"$fit, K_{pp} \approx %2.2f$"  %(popt_pp[0])) 
#plt.legend(loc="best")
#plt.xlabel(r"$\ln x$", fontdict=font1)
#plt.ylabel(r"$\ln \mathcal{G}^{pp}(x), \mathcal{G}^{ph}(x)$", fontdict=font1)
#plt.savefig("fig_pp_V5_U9,5_L90.pdf", format="pdf")

xcdw_fit = np.linspace(0.5,L/2,num=(L//2-1)*21)

plt.figure()
plt.errorbar(xcdw, cdw, yerr = cdw_err, fmt = 'b.')
plt.plot(xcdw_fit, f(xcdw_fit, *popt_cdw), "r--", label = r"$fit, {\eta}_{cdw} \approx  %2.2f$" %(popt_cdw[0]))
plt.plot(xcdw_fit, fconst(xcdw_fit, *popt_const_cdw), "b--", label = r"$fit, C \approx  %3.3f$" %(popt_const_cdw[2]))
plt.legend(loc="best", fontsize=16)
plt.xlabel(r"$x$", fontdict=font1)
#plt.ylabel(r"$<n(x)n(0)> - 1$")
plt.ylabel(r"$C^{\rm CDW}(x)$", fontdict=font1)
plt.savefig("fig_cdw_V5_U9,5_L90.pdf", format="pdf", bbox_inches="tight")



