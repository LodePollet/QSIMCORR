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


data = np.loadtxt("stat_structfact_V6_U12_L70.out")
xsf_cdw = data[:,0]

L = xsf_cdw.size
print(L)

sf_cdw = data[:,1]
sf_cdw_err = data[:,2]
ysf_cdw = sf_cdw[1:L] / xsf_cdw[1:L] * np.pi
ysf_cdw_err = sf_cdw_err[1:L] / xsf_cdw[1:L] * np.pi

xsf_sdw = data[:,0]
sf_sdw = data[:,3]
sf_sdw_err = data[:,4]
ysf_sdw = sf_sdw[1:L] / xsf_sdw[1:L] * np.pi
ysf_sdw_err = sf_sdw_err[1:L] / xsf_sdw[1:L] * np.pi


def linear(x,c,m):
  return c + m*x

def const(x, c):
  return c

#popt_sf_cdw, pcov_sf_cdw = curve_fit( const, xdata=xsf_cdw[0:4], ydata=ysf_cdw[0:4], sigma = ysf_cdw_err[0:4])
popt_sf_cdw, pcov_sf_cdw = curve_fit( linear, xdata=xsf_cdw[1:6], ydata=ysf_cdw[0:5], sigma = ysf_cdw_err[0:5])
print ("eta_cdw : ", popt_sf_cdw[0], pcov_sf_cdw[0])
print(popt_sf_cdw)

popt_sf_sdw, pcov_sf_sdw = curve_fit( linear, xdata=xsf_sdw[1:4], ydata=ysf_sdw[0:3], sigma = ysf_sdw_err[0:3])
print ("eta_sdw : ", popt_sf_sdw[0], pcov_sf_sdw[0])
print(popt_sf_sdw)

xfit = np.linspace(0, 1.5, num=51)

plt.figure()
plt.errorbar(xsf_cdw[1:L], ysf_cdw, yerr = ysf_cdw_err , fmt = "bo", label=r"$\frac{ \pi S^{\rm CDW}(k) }{k} $")
plt.errorbar(xsf_cdw[1:L], ysf_sdw, yerr = ysf_sdw_err , fmt = "mo", label=r"$\frac{ \pi S^{\rm SDW}(k) }{k} $")
plt.plot(xfit, linear(xfit,*popt_sf_cdw), "r--", label = r"$fit, \eta_{\rm CDW} \approx %2.2f$" %(popt_sf_cdw[0]))
plt.plot(xfit, linear(xfit,*popt_sf_sdw), "c--", label = r"$fit, \eta_{\rm SDW} \approx %2.2f$" %(popt_sf_sdw[0]))
plt.legend(loc="best", fontsize=14)
plt.xlabel(r"$k$", fontdict=font1)
plt.xlim([0, np.pi * 2])
plt.ylabel(r"$ \frac{ \pi S^{\rm CDW/SDW}(k) }{k} $", fontdict=font1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_sf_cdw_scaled_V6_U12_L70.pdf", format="pdf", bbox_inches="tight")




