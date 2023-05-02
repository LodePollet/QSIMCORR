import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

data1 = np.loadtxt("FM_100_corr_t_1000.0000_ns.txt")
data2 = np.loadtxt("FM_100_corr_t_2000.0000_ns.txt")
data4 = np.loadtxt("FM_100_corr_t_4000.0000_ns.txt")
data8 = np.loadtxt("FM_100_corr_t_8000.0000_ns.txt")

b110 = np.loadtxt("dm_b11_L10.dat")
b100 = np.loadtxt("dm_b1_L10.dat")
b09  = np.loadtxt("dm_b09_L10.dat")
b085 = np.loadtxt("dm_b085_L10.dat")
b082 = np.loadtxt("dm_b082_L10.dat")
b075 = np.loadtxt("dm_b075_L10.dat")
b072 = np.loadtxt("dm_b072_L10.dat")
b07  = np.loadtxt("dm_b07_L10.dat")
b065 = np.loadtxt("dm_b065_L10.dat")

L = 10 
Lh = 5
fac = 1.208





plt.figure()
plt.errorbar(data1[:,0], data1[:,1]*fac, yerr = data1[:,3]*fac, fmt = "go", label = r"$t = 1 \mu s (\times 1.208)$") 
plt.errorbar(data2[:,0], data2[:,1]*fac, yerr = data2[:,3]*fac, fmt = "bo", label = r"$t = 2 \mu s (\times 1.208)$") 
#plt.errorbar(data4[:,0], data4[:,1]*fac, yerr = data4[:,3]*fac, fmt = "ro", label = r"$t = 4 \mu s (\times 1.208)$") 
plt.errorbar(data8[:,0], data8[:,1]*fac, yerr = data8[:,3]*fac, fmt = "mo", label = r"$t = 8 \mu s (\times 1.208)$") 
plt.errorbar(b065[:,0], b065[:,1], yerr=b065[:,2], fmt ="y--", label = r"$\beta = 0.65 (S/N \approx 0.54)$")
plt.errorbar(b072[:,0], b072[:,1], yerr=b072[:,2], fmt ="m--", label = r"$\beta = 0.72 (S/N \approx 0.5)$")
#plt.errorbar(b075[:,0], b075[:,1], yerr=b075[:,2], fmt ="m--", label = r"$\beta = 0.75$")
#plt.errorbar(b085[:,0], b085[:,1], yerr=b085[:,2], fmt ="r--", label = r"$\beta = 0.85$")
plt.errorbar(b082[:,0], b082[:,1], yerr=b082[:,2], fmt ="b--", label = r"$\beta = 0.82 (S/N \approx 0.41)$")
#plt.errorbar(b110[:,0], b110[:,1], yerr=b110[:,2], fmt ="c--", label = r"$\beta = 1.1$")
#plt.errorbar(b100[:,0], b100[:,1], yerr=b100[:,2], fmt ="c--", label = r"$\beta = 1.0$")
#plt.errorbar(b09[:,0], b09[:,1], yerr=b09[:,2], fmt ="c--", label = r"$\beta = 0.9$")
plt.errorbar(b09[:,0], 0.5*(b09[:,1] + b100[:,1]), yerr = 0.5*(b100[:,1] - b09[:,1]), fmt ="c--", label = r"$\beta = 0.9 - 1 (S/N \approx 0.27-0.33)$")
plt.xlabel(r"$x$")
plt.xlim([1,11])
plt.ylabel(r"$S^+S^-(x) + h.c.$")
plt.legend(loc="best", fontsize=10)
plt.ylim([0, 0.5])
plt.savefig("fig_corrfun_expt.pdf", format="pdf", bbox_inches="tight")
