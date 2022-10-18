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

cdw_data30 = np.loadtxt("stat_cdwsdw_V5_U9,5_L30.out")
cdw_data50 = np.loadtxt("stat_cdwsdw_V5_U9,5_L50.out")
cdw_data70 = np.loadtxt("stat_cdwsdw_V5_U9,5_L70.out")
cdw_data90 = np.loadtxt("stat_cdwsdw_V5_U9,5_L90.out")
cdw_data110 = np.loadtxt("stat_cdwsdw_V5_U9,5_L110.out")
cdw_data130 = np.loadtxt("stat_cdwsdw_V5_U9,5_L130.out")
cdw_data150 = np.loadtxt("stat_cdwsdw_V5_U9,5_L150.out")
xcdw30 = cdw_data30[:,0]
L30 = xcdw30.size
cdw30 = cdw_data30[:,1]
cdw30_err = cdw_data30[:,2]/L30
xcdw50 = cdw_data50[:,0]
L50 = xcdw50.size
cdw50 = cdw_data50[:,1]
cdw50_err = cdw_data50[:,2]/L50
xcdw70 = cdw_data70[:,0]
L70 = xcdw70.size
cdw70 = cdw_data70[:,1]
cdw70_err = cdw_data70[:,2]/L70
xcdw90 = cdw_data90[:,0]
L90 = xcdw90.size
cdw90 = cdw_data90[:,1]
cdw90_err = cdw_data90[:,2]/L90
xcdw110 = cdw_data110[:,0]
L110 = xcdw110.size
cdw110 = cdw_data110[:,1]
cdw110_err = cdw_data110[:,2]/L110
xcdw130 = cdw_data130[:,0]
L130 = xcdw130.size
cdw130 = cdw_data130[:,1]
cdw130_err = cdw_data130[:,2]/L30
xcdw150 = cdw_data150[:,0]
L150 = xcdw150.size
cdw150 = cdw_data150[:,1]
cdw150_err = cdw_data150[:,2]/L150




plt.figure()
plt.errorbar(xcdw30[0:L30//2], cdw30[0:L30//2], yerr = cdw30_err[0:L30//2], fmt = 'yo-', label="$L=30$")
plt.errorbar(xcdw50[0:L50//2], cdw50[0:L50//2], yerr = cdw50_err[0:L50//2], fmt = 'kx-', label="$L=50$")
plt.errorbar(xcdw70[0:L70//2], cdw70[0:L70//2], yerr = cdw70_err[0:L70//2], fmt = 'cx--', label="$L=70$")
plt.errorbar(xcdw90[0:L90//2], cdw90[0:L90//2], yerr = cdw90_err[0:L90//2], fmt = 'm.--', label="$L=90$")
plt.errorbar(xcdw110[0:L110//2], cdw110[0:L110//2], yerr = cdw110_err[0:L110//2], fmt = 'g.--', label="$L=110$")
#plt.errorbar(xcdw130[0:L130//2], cdw130[0:L130//2], yerr = cdw130_err[0:L130//2], fmt = 'r.--', label="$L=130$")
#plt.errorbar(xcdw150[0:L150//2], cdw150[0:L150//2], yerr = cdw150_err[0:L150//2], fmt = 'b.--', label="$L=150$")
plt.ylim([-0.15,0.15])
plt.legend(loc="best", fontsize=14)
plt.xlabel(r"$x$", fontdict=font1)
plt.ylabel(r"$C^{\rm CDW}(x)$", fontdict=font1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_cdw_V5_U9,5_FSS.pdf", format="pdf", bbox_inches="tight")



