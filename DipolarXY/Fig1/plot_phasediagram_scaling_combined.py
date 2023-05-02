import numpy as np
import matplotlib.pylab as plt


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
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }


fig = plt.figure()
#gs = fig.add_gridspec(2, 2, height_ratios = (2,1))
gs = fig.add_gridspec(2, 2)
# spans two rows:
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

# -------------------------------------------------------------------------------
# PHASE DIAGRAM
# -------------------------------------------------------------------------------


dataTc = np.loadtxt("Tc.dat")
data_gs = np.array([4.03, 0, 0.01])

ax1.errorbar(dataTc[:,0], 1./dataTc[:,1], yerr = (1./(dataTc[:,1]-dataTc[:,2]) - 1./dataTc[:,1]), fmt = "b.:")
ax1.errorbar(data_gs[0], data_gs[1]+0.01, xerr = data_gs[2], fmt = "b.-")
ax1.set_xlabel(r"$\delta/J$", fontdict=font1)
ax1.set_xlim([0,4.5])
ax1.set_ylim([0, 2])
ax1.set_ylabel(r"$T/J$", fontdict=font1)
ax1.xaxis.set_label_position('top') 
ax1.xaxis.tick_top()
ax1.text(0.02, 0.1, "(a)", transform=ax1.transAxes, fontdict=font3)
ax1.text(0.5, 0.5, "FM", transform=ax1.transAxes, fontdict=font2)
ax1.text(0.9, 0.8, "PM", transform=ax1.transAxes, fontdict=font2)
#ax1.set_xticks(fontsize=16)
#ax1.set_yticks(fontsize=16)
#plt.savefig("fig_Tc.pdf", format="pdf", bbox_inches="tight")

# -------------------------------------------------------------------------------
# THERMAL PHASE TRANSITION SCALING OF IN-PLANE MAGNETIZATION 
# -------------------------------------------------------------------------------

data9 = np.loadtxt("./Delta0/out_L9")
data17 = np.loadtxt("./Delta0/out_L17")
data33 = np.loadtxt("./Delta0/out_L33")
data49 = np.loadtxt("./Delta0/out_L49")
data65 = np.loadtxt("./Delta0/out_L65")
data97 = np.loadtxt("./Delta0/out_L97")
data127 = np.loadtxt("./Delta0/out_L127")
data257 = np.loadtxt("./Delta0/out_L257")

eta = 1.0
f9 =  2. * np.power(9., eta) 
f17 = 2. * np.power(17., eta) 
f33 = 2. * np.power(33, eta)
f49 = 2. * np.power(49, eta)
f65 = 2. * np.power(65, eta)
f97 = 2. * np.power(97, eta)
f127 = 2. * np.power(127, eta)
f257 = 2. * np.power(257, eta)

#ax2.errorbar(data9[:,0],  data9[:,1]*f9, yerr = data9[:,2]*f9,    fmt = "k.-", label = r"$L=9$")
ax2.errorbar(data17[:,0], data17[:,1]*f17, yerr = data17[:,2]*f17, fmt = "g.-", label = r"$L=17$")
ax2.errorbar(data33[:,0], data33[:,1]*f33, yerr = data33[:,2]*f33, fmt = "m.-", label = r"$L=33$")
#ax2.errorbar(data49[:,0], data49[:,1]*f49, yerr = data49[:,2]*f49, fmt = "c.-", label = r"$L=49$")
ax2.errorbar(data65[:,0], data65[:,1]*f65, yerr = data65[:,2]*f65, fmt = "r.-", label = r"$L=65$")
#ax2.errorbar(data97[:,0], data97[:,1]*f97, yerr = data97[:,2]*f97, fmt = "r.-", label = r"$L=97$")
ax2.errorbar(data127[:,0], data127[:,1]*f127, yerr = data127[:,2]*f127, fmt = "b.-", label = r"$L=127$")
ax2.errorbar(data257[:,0], data257[:,1]*f257, yerr = data257[:,2]*f257, fmt = "c.-", label = r"$L=257$")
ax2.set_xlim([0.516,0.522])
ax2.set_ylim([1,1.5])
ax2.set_xlabel(r"$\beta J$", fontdict=font1)
#ax2.set_ylabel(r"$L^{\eta}n_0$", fontdict=font1)
ax2.set_ylabel(r"$L^{\eta}m_{\perp}^2$", fontdict=font1)
ax2.text(0.02, 0.9, "(b)", transform=ax2.transAxes, fontdict=font3)



#ax2.errorbar(data17[:,0], data17[:,-2], yerr = data17[:,-1], fmt = "g.-", label = r"$L=17$")
#ax2.errorbar(data33[:,0], data33[:,-2], yerr = data33[:,-1], fmt = "m.-", label = r"$L=33$")
##ax2.errorbar(data49[:,0], data49[:,-2], yerr = data49[:,-1], fmt = "c.-", label = r"$L=49$")
#ax2.errorbar(data65[:,0], data65[:,-2], yerr = data65[:,-1], fmt = "r.-", label = r"$L=65$")
##ax2.errorbar(data97[:,0], data97[:,-2], yerr = data97[:,-1], fmt = "r.-", label = r"$L=97$")
#ax2.errorbar(data127[:,0], data127[:,-2], yerr = data127[:,-1], fmt = "b.-", label = r"$L=127$")
#ax2.errorbar(data257[:,0], data257[:,-2], yerr = data257[:,-1], fmt = "c.-", label = r"$L=257$")
##plt.xlim([0.4,0.6])
#ax2.set_xlim([0.518,0.522])
##plt.ylim([0,0.4])
#ax2.set_ylim([0.05,0.2])
#ax2.set_xlabel(r"$\beta J$", fontdict=font1)
##ax2.set_ylabel(r"$\rho_{\rm sf}$", fontdict=font1)
#ax2.set_ylabel(r"$\chi_{\rm s}$", fontdict=font1)
#ax2.text(0.02, 0.9, "(b)", transform=ax2.transAxes, fontdict=font3)
##ax2.legend(loc="best", fontsize=16)
##plt.savefig("fig_rho_sf_zoom.pdf", format="pdf", bbox_inches="tight")
##ax2.errorbar(data9[:,0], data9[:,-2], yerr = data9[:,-1],    fmt = "k.-", label = r"$L=9$")

# -------------------------------------------------------------------------------
# QUANTUM PHASE TRANSITION SCALING OF SPIN STIFFNESS
# -------------------------------------------------------------------------------

nu = 1
eta = 1
z = 0.5

f9 = 8
f17 = 11.3137085
f33 = 16
f65 = 22.627416998
f129 = 32
f257 = 64


data9 = np.loadtxt("./Groundstate/z_one_half/out_L9")
data17 = np.loadtxt("./Groundstate/z_one_half/out_L17")
data33 = np.loadtxt("./Groundstate/z_one_half/out_L33")
#data49 = np.loadtxt("./Groundstate/z_one_half/out_L49")
data65 = np.loadtxt("./Groundstate/z_one_half/out_L65")
#data97 = np.loadtxt("./Groundstate/z_one_half/out_L97")
data129= np.loadtxt("./Groundstate/z_one_half/out_L129")
data257= np.loadtxt("./Groundstate/z_one_half/out_L257")


#ax3.errorbar(data9[:,0], data9[:,-2]*f9, yerr = data9[:,-1] * f9,    fmt = "k.-", label = r"$L=9$")
ax3.errorbar(data17[:,0], data17[:,-2]*f17, yerr = data17[:,-1] * f17, fmt = "g.-", label = r"$L=17$")
ax3.errorbar(data33[:,0], data33[:,-2]*f33, yerr = data33[:,-1]* f33, fmt = "m.-", label = r"$L=33$")
#ax3.errorbar(data49[:,0], data49[:,-2]*f49, yerr = data49[:,-1] * f49, fmt = "c.-", label = r"$L=49$")
ax3.errorbar(data65[:,0], data65[:,-2]*f65, yerr = data65[:,-1] * f65, fmt = "r.-", label = r"$L=65$")
#ax3.errorbar(data97[:,0], data97[:,-2]*f97, yerr = data97[:,-1] * f97, fmt = "b.-", label = r"$L=97$")
ax3.errorbar(data129[:,0], data129[:,-2]*f129, yerr = data129[:,-1] * f129, fmt = "b.-", label = r"$L=129$")
ax3.errorbar(data257[:,0], data257[:,-2]*f257, yerr = data257[:,2]*f257, fmt = "c.-", label = r"$L=257$")
ax3.set_xlim([3.9,4.5])
ax3.set_ylim([0,6])
#ax3.title(r"$\beta \sim \sqrt{L}$")
ax3.set_xlabel(r"$\delta/ J$", fontdict=font1)
#ax3.set_ylabel(r"$\rho_{\rm sf}\beta$", fontdict=font1)
ax3.set_ylabel(r"$\chi_{\rm s} \beta$", fontdict=font1)
#ax3.xticks(fontsize=16)
#ax3.yticks(fontsize=16)
#ax3.legend(loc="best", fontsize=20)
ax3.yaxis.set_label_position("right")
ax3.yaxis.tick_right()
ax3.text(0.9, 0.9, "(c)", transform=ax3.transAxes, fontdict=font3)
ax3.text(0.5, 0.8, "QCP", transform=ax3.transAxes, fontdict=font2)




#f9 = 8  * np.power(9., eta)
#f17 = 11.3137085  * np.power(17., eta)
#f33 = 16  * np.power(33., eta)
#f49 = 19.596 * np.power(49., eta)
#f65 = 22.627416998  * np.power(65., eta)
#f97 = 27.713 * np.power(97., eta)
#f129 = 32 * np.power(129., eta)
##ax3.errorbar(data9[:,0], data9[:,1]*f9, yerr = data9[:,2] * f9,    fmt = "k.-", label = r"$L=9$")
#ax3.errorbar(data17[:,0], data17[:,1]*f17, yerr = data17[:,2] * f17, fmt = "g.-", label = r"$L=17$")
#ax3.errorbar(data33[:,0], data33[:,1]*f33, yerr = data33[:,2]* f33, fmt = "m.-", label = r"$L=33$")
##ax3.errorbar(data49[:,0], data49[:,1]*f49, yerr = data49[:,2] * f49, fmt = "c.-", label = r"$L=49$")
#ax3.errorbar(data65[:,0], data65[:,1]*f65, yerr = data65[:,2] * f65, fmt = "r.-", label = r"$L=65$")
##ax3.errorbar(data97[:,0], data97[:,1]*f97, yerr = data97[:,2] * f97, fmt = "b.-", label = r"$L=97$")
#ax3.errorbar(data129[:,0], data129[:,1]*f129, yerr = data129[:,2] * f129, fmt = "b.-", label = r"$L=129$")
#ax3.set_xlim([3.9,4.5])
#ax3.set_ylim([0,20])
#ax3.set_xlabel(r"$\delta / J$", fontdict = font1)
#ax3.set_ylabel(r"$m_{\perp}^2 \beta L^{\eta}$", fontdict=font1)
#ax3.yaxis.set_label_position("right")
#ax3.yaxis.tick_right()
#ax3.text(0.9, 0.9, "(c)", transform=ax3.transAxes, fontdict=font3)
#ax3.text(0.5, 0.8, "QCP", transform=ax3.transAxes, fontdict=font2)
##ax3.legend(loc="best", fontsize=16)
##plt.savefig("fig_n0_gs_rescaled.pdf", format="pdf", bbox_inches="tight")
##plt.show()


plt.savefig("fig_QMC_phasediagram_scaling_combined.pdf", format="pdf", bbox_inches="tight")
#plt.show()






