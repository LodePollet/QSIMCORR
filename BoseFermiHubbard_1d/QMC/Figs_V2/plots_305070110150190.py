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
data_110 = np.loadtxt("jump_L110")

plt.figure()
#plt.plot(data_30[:,1], data_30[:,-1], 'rs-', label="L=30")
#plt.plot(data_50[:,1], data_50[:,-1], 'bo-', label="L=50")
#plt.plot(data_70[:,1], data_70[:,-1], 'mx-', label="L=70")
#plt.plot(data_110[:,1], data_110[:,-1], 'kx-', label="L=110")
#plt.plot(data_150[:,1], data_150[:,-1], 'yx-', label="L=150")
plt.errorbar(data_30[:,1], data_30[:,-1], yerr=0.002, fmt= 'rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,-1], yerr=0.002, fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,-1], yerr=0.003, fmt='mx-', label="L=70")
plt.errorbar(data_110[:,1], data_110[:,-1], yerr=0.005, fmt='kx-', label="L=110")
plt.errorbar(data_150[:,1], data_150[:,-1], yerr=0.01, fmt='yx-', label="L=150")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$n(k_f^-) - n(k_f^+)$", fontdict=font1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(loc="best", fontsize=16)


plt.savefig("fig_jump.pdf", format="pdf", bbox_inches="tight")


##############################################################


data_30 = np.loadtxt("winding_L30")
data_50 = np.loadtxt("winding_L50")
data_70 = np.loadtxt("winding_L70")
data_150 = np.loadtxt("winding_L150")
data_110 = np.loadtxt("winding_L110")
data_190 = np.loadtxt("winding_L190")

plt.figure()
plt.errorbar(data_30[:,1], data_30[:,4], yerr=data_30[:,5], fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,4], yerr=data_50[:,5], fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,4], yerr=data_70[:,5], fmt='mx-', label="L=70")
plt.errorbar(data_110[:,1], data_110[:,4], yerr=data_110[:,5], fmt='kx-', label="L=110")
plt.errorbar(data_150[:,1], data_150[:,4], yerr=data_150[:,5], fmt='yx-', label="L=150")
plt.errorbar(data_190[:,1], data_190[:,4], yerr=data_190[:,5], fmt='go--', label="L=190")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< W^2_b \right>$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_bosonic_winding.pdf", format="pdf", bbox_inches="tight")


plt.figure()
plt.errorbar(data_30[:,1], data_30[:,6], yerr=data_30[:,7], fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,6], yerr=data_50[:,7], fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,6], yerr=data_70[:,7], fmt='mx-', label="L=70")
plt.errorbar(data_110[:,1], data_110[:,6], yerr=data_110[:,7], fmt='kx-', label="L=110")
plt.errorbar(data_150[:,1], data_150[:,6], yerr=data_150[:,7], fmt='yx-', label="L=150")
plt.errorbar(data_190[:,1], data_190[:,6], yerr=data_190[:,7], fmt='go--', label="L=190")
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
plt.errorbar(data_110[:,1], data_110[:,8], yerr=data_110[:,9], fmt='kx-', label="L=110")
plt.errorbar(data_150[:,1], data_150[:,8], yerr=data_150[:,9], fmt='yx-', label="L=150")
plt.errorbar(data_190[:,1], data_190[:,8], yerr=data_190[:,9], fmt='go--', label="L=190")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< W^2_{\downarrow} \right>$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_down_winding.pdf", format="pdf", bbox_inches="tight")

plt.figure()
plt.errorbar(data_30[:,1], data_30[:,10], yerr=data_30[:,11], fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,10], yerr=data_50[:,11], fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,10], yerr=data_70[:,11], fmt='mx-', label="L=70")
plt.errorbar(data_110[:,1], data_110[:,10], yerr=data_110[:,11], fmt='kx-', label="L=110")
plt.errorbar(data_150[:,1], data_150[:,10], yerr=data_150[:,11], fmt='yx-', label="L=150")
plt.errorbar(data_190[:,1], data_190[:,10], yerr=data_190[:,11], fmt='go--', label="L=190")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< (W_{\uparrow} - W_{\downarrow})^2 \right>$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_pair_winding.pdf", format="pdf", bbox_inches="tight")

plt.figure()
plt.errorbar(data_30[:,1], data_30[:,12], yerr=data_30[:,13], fmt='rs-', label="L=30")
plt.errorbar(data_50[:,1], data_50[:,12], yerr=data_50[:,13], fmt='bo-', label="L=50")
plt.errorbar(data_70[:,1], data_70[:,12], yerr=data_70[:,13], fmt='mx-', label="L=70")
plt.errorbar(data_110[:,1], data_110[:,12], yerr=data_110[:,13], fmt='kx-', label="L=110")
plt.errorbar(data_150[:,1], data_150[:,12], yerr=data_150[:,13], fmt='yx-', label="L=150")
plt.errorbar(data_190[:,1], data_190[:,12], yerr=data_190[:,13], fmt='go--', label="L=190")
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
plt.errorbar(data_110[:,1], (data_110[:,10] - data_110[:,12])/4., yerr=data_110[:,13], fmt='kx-', label="L=110")
plt.errorbar(data_150[:,1], (data_150[:,10] - data_150[:,12])/4., yerr=data_150[:,13], fmt='yx-', label="L=150")
plt.errorbar(data_190[:,1], (data_190[:,10] - data_190[:,12])/4., yerr=data_190[:,13], fmt='go--', label="L=190")
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\left< (W_{\uparrow} W_{\downarrow}) \right>$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_diff_winding.pdf", format="pdf", bbox_inches="tight")


##############################################################


data_30 = np.loadtxt("powerlaw_L30")
data_50 = np.loadtxt("powerlaw_L50")
data_70 = np.loadtxt("powerlaw_L70")
data_150 = np.loadtxt("powerlaw_L150")
data_110 = np.loadtxt("powerlaw_L110")

plt.figure()
#plt.plot(data_30[:,1], data_30[:,4], 'rs-', label="L=30, boson")
#plt.plot(data_30[:,1], data_30[:,5], 'bo-', label=r"$L=30, \eta_{\rm CDW}$")
#plt.plot(data_30[:,1], data_30[:,6], 'mx-', label=r"$L=30, \eta_{\rm SDW}$")
#plt.errorbar(data_30[:,1], data_30[:,5], yerr = np.ones_like(data_30[:,1])*0.02 fmt='bo-', label=r"$L=30, \eta_{\rm CDW}$")
#plt.errorbar(data_30[:,1], data_30[:,6], yerr = np.ones_like(data_30[:,1])*0.02, fmt='mx-', label=r"$L=30, \eta_{\rm SDW}$")
plt.errorbar(data_30[:,1], data_30[:,5], yerr = np.ones_like(data_30[:,1])*0.02, fmt='bo-', label=r"$\eta_{\rm CDW}$")
plt.errorbar(data_30[:,1], data_30[:,6], yerr = np.ones_like(data_30[:,1])*0.02, fmt='mx-', label=r"$\eta_{\rm SDW}$")
#plt.plot(data_50[:,1], data_50[:,4], 'rs--', label="L=50, boson")
#plt.plot(data_50[:,1], data_50[:,5], 'bo--', label=r"$L=50, \eta_{\rm CDW}$")
#plt.plot(data_50[:,1], data_50[:,6], 'mx--', label=r"$L=50, \eta_{\rm SDW}$")
#plt.errorbar(data_50[:,1], data_50[:,5], yerr = np.ones_like(data_50[:,1])*0.03, fmt='bo--', label=r"$L=50, \eta_{\rm CDW}$")
#plt.errorbar(data_50[:,1], data_50[:,6], yerr = np.ones_like(data_50[:,1])*0.03, fmt='mx--', label=r"$L=50, \eta_{\rm SDW}$")
plt.errorbar(data_50[:,1], data_50[:,5], yerr = np.ones_like(data_50[:,1])*0.03, fmt='bo--')
plt.errorbar(data_50[:,1], data_50[:,6], yerr = np.ones_like(data_50[:,1])*0.03, fmt='mx--')
#plt.plot(data_70[:,1], data_70[:,4], 'rs-.', label=r"$L=70, boson$")
#plt.plot(data_70[:,1], data_70[:,5], 'bo-.', label=r"$L=70, \eta_{\rm CDW}$")
#plt.plot(data_70[:,1], data_70[:,6], 'mx-.', label=r"$L=70, \eta_{\rm SDW}$")
#plt.errorbar(data_70[:,1], data_70[:,5],yerr = np.ones_like(data_70[:,1])*0.05, fmt='bo-.', label=r"$L=70, \eta_{\rm CDW}$")
#plt.errorbar(data_70[:,1], data_70[:,6],yerr = np.ones_like(data_70[:,1])*0.05, fmt='mx-.', label=r"$L=70, \eta_{\rm SDW}$")
plt.errorbar(data_70[:,1], data_70[:,5],yerr = np.ones_like(data_70[:,1])*0.05, fmt='bo-.')
plt.errorbar(data_70[:,1], data_70[:,6],yerr = np.ones_like(data_70[:,1])*0.05, fmt='mx-.')
#plt.plot(data_90[:,1], data_90[:,4], 'rs:', label="L=90, boson")
#plt.plot(data_90[:,1], data_90[:,5], 'bo:', label=r"$L=90, \eta_{\rm CDW}$")
#plt.plot(data_90[:,1], data_90[:,6], 'mx:', label=r"$L=90, \eta_{\rm SDW}$")
#plt.plot(data_150[:,1], data_150[:,4], 'rs-', label="L=150, boson")
#plt.plot(data_150[:,1], data_150[:,5], 'bo-', label=r"$L=150, \eta_{\rm CDW}$")
#plt.plot(data_150[:,1], data_150[:,6], 'mx-', label=r"$L=150, \eta_{\rm SDW}$")
#plt.errorbar(data_30[:,1], data_30[:,4], yerr = np.ones_like(data_30[:,1])*0.02, fmt='cs-', label=r"$L=30, \eta_{\rm bb}$")
#plt.errorbar(data_50[:,1], data_50[:,4], yerr = np.ones_like(data_50[:,1])*0.03, fmt='cs--', label=r"$L=50, \eta_{\rm bb}$")
#plt.errorbar(data_70[:,1], data_70[:,4],yerr = np.ones_like(data_70[:,1])*0.04, fmt='cs-.', label=r"$L=70, \eta_{\rm bb}$")
#plt.errorbar(data_30[0:,1], data_30[0:,4], yerr = np.ones_like(data_30[0:,1])*0.04, fmt='cs-', label=r"$\eta_{\rm bb}$")
#plt.errorbar(data_50[0:,1], data_50[0:,4], yerr = np.ones_like(data_50[0:,1])*0.06, fmt='cs--')
#plt.errorbar(data_70[0:,1], data_70[0:,4],yerr = np.ones_like(data_70[0:,1])*0.08, fmt='cs-.')
plt.plot(data_30[:,1], np.ones_like(data_30[:,1]), 'b:')
#plt.plot(data_30[:,1], np.ones_like(data_30[:,1])*2, 'c:')
plt.xlabel("U", fontdict=font1)
#plt.ylabel("power law exponents", fontdict=font1)
#plt.ylabel(r"$\eta_{\rm CDW}, \eta_{\rm SDW}, \eta_{\rm bb}$", fontdict=font1)
plt.ylabel(r"$\eta_{\rm CDW}, \eta_{\rm SDW}$", fontdict=font1)
plt.legend(loc="best", fontsize=14)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
#plt.savefig("fig_powerlaw_densmat.pdf", format="pdf")
plt.savefig("fig_Luttinger_cdw_sdw.pdf", format="pdf", bbox_inches="tight")
plt.figure()
plt.errorbar(data_30[0:,1], data_30[0:,4], yerr = np.ones_like(data_30[0:,1])*0.04, fmt='cs-', label=r"$\eta_{\rm bb}$")
plt.errorbar(data_50[0:,1], data_50[0:,4], yerr = np.ones_like(data_50[0:,1])*0.06, fmt='cs--')
plt.errorbar(data_70[0:,1], data_70[0:,4],yerr = np.ones_like(data_70[0:,1])*0.08, fmt='cs-.')
plt.plot(data_30[:,1], np.ones_like(data_30[:,1])*2, 'c:')
plt.xlabel("U", fontdict=font1)
plt.ylabel(r"$\eta_{\rm bb}$", fontdict=font1)
plt.legend(loc="best", fontsize=14)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig("fig_Luttinger_bb.pdf", format="pdf", bbox_inches="tight")


