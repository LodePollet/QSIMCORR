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


##############################################################


data_30 = np.loadtxt("jump_L30")
data_50 = np.loadtxt("jump_L50")
data_70 = np.loadtxt("jump_L70")
data_150 = np.loadtxt("jump_L150")
#data_250 = np.loadtxt("jump_L250")

plt.figure()
#plt.plot(data_30[:,1], data_30[:,-1], 'rs-', label="L=30")
#plt.plot(data_50[:,1], data_50[:,-1], 'bo-', label="L=50")
#plt.plot(data_70[:,1], data_70[:,-1], 'mx-', label="L=70")
plt.errorbar(data_30[:,1], data_30[:,-1], yerr = 0.002, fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,-1], yerr = 0.002, fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,-1], yerr = 0.005, fmt='mx-', label="L=70")
#plt.plot(data_150[:,1], data_150[:,-1], 'yx-', label="L=150")
#plt.plot(data_250[:,1], data_250[:,-1], 'kx-', label="L=250")
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$n(k_f^-) - n(k_f^+)$", fontdict=font1)
plt.legend(loc="best", fontsize=16)


plt.savefig("fig_jump.pdf", format="pdf", bbox_inches="tight")


##############################################################


data_30 = np.loadtxt("winding_L30")
data_50 = np.loadtxt("winding_L50")
data_70 = np.loadtxt("winding_L70")
data_150 = np.loadtxt("winding_L150")
#data_250 = np.loadtxt("winding_L250")

plt.figure()
plt.errorbar(data_30[:,1], data_30[:,4], yerr=data_30[:,5], fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,4], yerr=data_50[:,5], fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,4], yerr=data_70[:,5], fmt='mx-', label="L=70")
#plt.errorbar(data_150[:,1], data_150[:,4], yerr=data_150[:,5], fmt='yx-', label="L=150")
#plt.errorbar(data_250[:,1], data_250[:,4], yerr=data_250[:,5], fmt='kx-', label="L=250")
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< W^2_b \right>$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_bosonic_winding.pdf", format="pdf", bbox_inches="tight")


plt.figure()
plt.errorbar(data_30[:,1], data_30[:,6], yerr=data_30[:,7], fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,6], yerr=data_50[:,7], fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,6], yerr=data_70[:,7], fmt='mx-', label="L=70")
#plt.errorbar(data_150[:,1], data_150[:,6], yerr=data_150[:,7], fmt='yx-', label="L=150")
#plt.errorbar(data_250[:,1], data_250[:,6], yerr=data_250[:,7], fmt='kx-', label="L=250")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< W^2_{\uparrow} \right>$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_up_winding.pdf", format="pdf", bbox_inches="tight")

plt.figure()
plt.errorbar(data_30[:,1], data_30[:,8], yerr=data_30[:,9], fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,8], yerr=data_50[:,9], fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,8], yerr=data_70[:,9], fmt='mx-', label="L=70")
#plt.errorbar(data_150[:,1], data_150[:,8], yerr=data_150[:,9], fmt='yx-', label="L=150")
#plt.errorbar(data_250[:,1], data_250[:,8], yerr=data_250[:,9], fmt='kx-', label="L=250")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< W^2_{\downarrow} \right>$", fontdict=font1)
plt.legend(loc="lower left", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_down_winding.pdf", format="pdf", bbox_inches="tight")

plt.figure()
plt.errorbar(data_30[:,1], data_30[:,10], yerr=data_30[:,11]*2, fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,10], yerr=data_50[:,11]*2, fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,10], yerr=data_70[:,11]*2, fmt='mx-', label="L=70")
#plt.errorbar(data_150[:,1], data_150[:,10], yerr=data_150[:,11]*2, fmt='yx-', label="L=150")
#plt.errorbar(data_250[:,1], data_250[:,10], yerr=data_250[:,11]*2, fmt='kx-', label="L=250")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< (W_{\uparrow} - W_{\downarrow})^2 \right>$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_pair_winding.pdf", format="pdf", bbox_inches="tight")

plt.figure()
plt.errorbar(data_30[:,1], data_30[:,12], yerr=data_30[:,13]*2, fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,12], yerr=data_50[:,13]*2, fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,12], yerr=data_70[:,13]*2, fmt='mx-', label="L=70")
#plt.errorbar(data_150[:,1], data_150[:,12], yerr=data_150[:,13]*2, fmt='yx-', label="L=150")
#plt.errorbar(data_250[:,1], data_250[:,12], yerr=data_250[:,13]*2, fmt='kx-', label="L=250")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< (W_{\uparrow} + W_{\downarrow})^2 \right>$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_counter_winding.pdf", format="pdf", bbox_inches="tight")

plt.figure()
plt.errorbar(data_30[:,1], (data_30[:,10] - data_30[:,12])/4., yerr=data_30[:,13], fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], (data_50[:,10] - data_50[:,12])/4., yerr=data_50[:,13], fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], (data_70[:,10] - data_70[:,12])/4., yerr=data_70[:,13], fmt='mx-', label="L=70")
#plt.errorbar(data_150[:,1], (data_150[:,10] - data_150[:,12])/4., yerr=data_150[:,13], fmt='yx-', label="L=150")
#plt.errorbar(data_250[:,1], (data_250[:,10] - data_250[:,12])/4., yerr=data_250[:,13], fmt='kx-', label="L=250")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< (W_{\uparrow} W_{\downarrow}) \right>$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_diff_winding.pdf", format="pdf", bbox_inches="tight")


##############################################################




