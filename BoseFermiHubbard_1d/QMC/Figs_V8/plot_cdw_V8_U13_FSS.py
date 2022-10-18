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

cdw_data14 = np.loadtxt("stat_cdwsdw_V8_U13_L14.out")
cdw_data30 = np.loadtxt("stat_cdwsdw_V8_U13_L30.out")
cdw_data42 = np.loadtxt("stat_cdwsdw_V8_U13_L42.out")
cdw_data50 = np.loadtxt("stat_cdwsdw_V8_U13_L50.out")
cdw_data62 = np.loadtxt("stat_cdwsdw_V8_U13_L62.out")
cdw_data70 = np.loadtxt("stat_cdwsdw_V8_U13_L70.out")
cdw_data90 = np.loadtxt("stat_cdwsdw_V8_U13_L90.out")
xcdw14 = cdw_data14[:,0]
L14 = xcdw14.size
cdw14 = cdw_data14[:,1]
cdw14_err = cdw_data14[:,2]/L14

xcdw30 = cdw_data30[:,0]
L30 = xcdw30.size
cdw30 = cdw_data30[:,1]
cdw30_err = cdw_data30[:,2]/L30

xcdw42 = cdw_data42[:,0]
L42 = xcdw42.size
cdw42 = cdw_data42[:,1]
cdw42_err = cdw_data42[:,2]/L14

xcdw50 = cdw_data50[:,0]
L50 = xcdw50.size
cdw50 = cdw_data50[:,1]
cdw50_err = cdw_data50[:,2]/L50

xcdw62 = cdw_data62[:,0]
L62 = xcdw62.size
cdw62 = cdw_data62[:,1]
cdw62_err = cdw_data42[:,2]/L62

xcdw70 = cdw_data70[:,0]
L70 = xcdw70.size
cdw70 = cdw_data70[:,1]
cdw70_err = cdw_data70[:,2]/L70

xcdw90 = cdw_data90[:,0]
L90 = xcdw90.size
cdw90 = cdw_data90[:,1]
cdw90_err = cdw_data90[:,2]/L90


x = np.linspace(10, 31, 420)


plt.figure()
plt.errorbar(xcdw14[0:L14//2], cdw14[0:L14//2], yerr = cdw14_err[0:L14//2], fmt = 'y.', label="$L=14$")
plt.errorbar(xcdw30[0:L30//2], cdw30[0:L30//2], yerr = cdw30_err[0:L30//2], fmt = 'co', label="$L=30$")
plt.errorbar(xcdw42[0:L42//2], cdw42[0:L42//2], yerr = cdw42_err[0:L42//2], fmt = 'gs', label="$L=42$")
plt.errorbar(xcdw50[0:L50//2], cdw50[0:L50//2], yerr = cdw50_err[0:L50//2], fmt = 'md', label="$L=50$")
plt.errorbar(xcdw62[0:L62//2], cdw62[0:L62//2], yerr = cdw62_err[0:L62//2], fmt = 'bo', label="$L=62$")
plt.errorbar(xcdw70[0:L70//2], cdw70[0:L70//2], yerr = cdw70_err[0:L70//2], fmt = 'rx--', label="$L=70$")
#plt.plot(x, 0.097 * np.cos(np.pi * x), "r--", label = r"$0.10 \cos(\pi x)$")
#plt.errorbar(xcdw90[0:L90//2], cdw90[0:L90//2], yerr = cdw90_err[0:L90//2], fmt = 'b.--', label="$L=90$")
plt.legend(loc="best", fontsize=14)
plt.xlabel(r"$x$", fontdict=font1)
plt.ylabel(r"$C^{\rm CDW}(x)$", fontdict=font1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_cdw_V8_U13_FSS.pdf", format="pdf", bbox_inches="tight")



