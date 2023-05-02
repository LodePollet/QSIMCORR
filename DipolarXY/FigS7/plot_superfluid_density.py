import numpy as np
import matplotlib.pylab as plt

data9 = np.loadtxt("../Fig1/Delta0/out_L9")
data17 = np.loadtxt("../Fig1/Delta0/out_L17")
data33 = np.loadtxt("../Fig1/Delta0/out_L33")
data49 = np.loadtxt("../Fig1/Delta0/out_L49")
data65 = np.loadtxt("../Fig1/Delta0/out_L65")
data97 = np.loadtxt("../Fig1/Delta0/out_L97")
data127 = np.loadtxt("../Fig1/Delta0/out_L127")
data257 = np.loadtxt("../Fig1/Delta0/out_L257")

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

plt.figure()
plt.errorbar(data9[:,0], data9[:,-2], yerr = data9[:,-1],    fmt = "k.-", label = r"$L=9$")
plt.errorbar(data17[:,0], data17[:,-2], yerr = data17[:,-1], fmt = "g.-", label = r"$L=17$")
plt.errorbar(data33[:,0], data33[:,-2], yerr = data33[:,-1], fmt = "m,-", label = r"$L=33$")
plt.errorbar(data49[:,0], data49[:,-2], yerr = data49[:,-1], fmt = "c.-", label = r"$L=49$")
plt.errorbar(data65[:,0], data65[:,-2], yerr = data65[:,-1], fmt = "y.-", label = r"$L=65$")
plt.errorbar(data97[:,0], data97[:,-2], yerr = data97[:,-1], fmt = "r.-", label = r"$L=97$")
plt.errorbar(data127[:,0], data127[:,-2], yerr = data127[:,-1], fmt = "b.-", label = r"$L=127$")
plt.errorbar(data257[:,0], data257[:,-2], yerr = data257[:,-1], fmt = "g.-", label = r"$L=257$")
#plt.xlim([0.4,0.6])
plt.xlim([0.518,0.522])
#plt.ylim([0,0.4])
plt.ylim([0.05,0.2])
plt.xlabel(r"$\beta J$", fontdict=font1)
#plt.ylabel(r"$\rho_{\rm sf}$", fontdict=font1)
plt.ylabel(r"$\chi_{\rm s}$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
#plt.savefig("fig_rho_sf.pdf", format="pdf")
plt.savefig("fig_rho_sf_zoom.pdf", format="pdf", bbox_inches="tight")
plt.show()


beta_crit = 0.5198
eta = 1.0
f9 =  np.power(9., eta)
f17 = np.power(17., eta)
f33 = np.power(33, eta)
f49 = np.power(49, eta)
f65 = np.power(65, eta)
f97 = np.power(97, eta)
f127 = np.power(127, eta)
f257 = np.power(257, eta)
nu = 1.0
f9x =  np.power(9., nu)
f17x = np.power(17., nu)
f33x = np.power(33, nu)
f49x = np.power(49, nu)
f65x = np.power(65, nu)
f97x = np.power(97, nu)
f127x = np.power(127, nu)
f257x = np.power(257, nu)

plt.figure()
plt.errorbar( (data9[:,0] - beta_crit)*f9x, data9[:,-2], yerr = data9[:,-1],    fmt = "k.", label = r"$L=9$")
plt.errorbar( (data17[:,0] - beta_crit)*f17x, data17[:,-2], yerr = data17[:,-1], fmt = "g.", label = r"$L=17$")
plt.errorbar( (data33[:,0] - beta_crit)*f33x, data33[:,-2], yerr = data33[:,-1], fmt = "m.", label = r"$L=33$")
plt.errorbar( (data49[:,0] - beta_crit)*f49x, data49[:,-2], yerr = data49[:,-1], fmt = "c.", label = r"$L=49$")
plt.errorbar( (data65[:,0] - beta_crit)*f65x, data65[:,-2], yerr = data65[:,-1], fmt = "r.", label = r"$L=65$")
plt.errorbar( (data97[:,0] - beta_crit)*f97x, data97[:,-2], yerr = data97[:,-1], fmt = "b.", label = r"$L=97$")
plt.errorbar( (data127[:,0] - beta_crit)*f127x, data127[:,-2], yerr = data127[:,-1], fmt = "g.", label = r"$L=127$")
plt.errorbar( (data257[:,0] - beta_crit)*f257x, data257[:,-2], yerr = data257[:,-1], fmt = "c.-", label = r"$L=257$")
plt.xlim([-2,2])
plt.ylim([0,1])
plt.xlabel(r"$(\beta - \beta_c) J L^{1/\nu}$", fontdict=font1)
#plt.ylabel(r"$\rho_{\rm sf}$")
plt.ylabel(r"$\chi_{\rm s}$", fontdict=font1)
#plt.title(r"$\nu = 0.8$")
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_rho_sf_collapse.pdf", format="pdf", bbox_inches="tight")


# -------------------------------
# two panel figure with collapse
# -------------------------------

fig = plt.figure()
gs = fig.add_gridspec(2, 1)
# spans two rows:
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])

#ax1.errorbar( (data9[:,0] - beta_crit)*f9x, data9[:,-2], yerr = data9[:,-1],    fmt = "k.", label = r"$L=9$")
ax1.errorbar( (data17[:,0] - beta_crit)*f17x, data17[:,-2], yerr = data17[:,-1], fmt = "b.", label = r"$L=17$")
ax1.errorbar( (data33[:,0] - beta_crit)*f33x, data33[:,-2], yerr = data33[:,-1], fmt = "m.", label = r"$L=33$")
#ax1.errorbar( (data49[:,0] - beta_crit)*f49x, data49[:,-2], yerr = data49[:,-1], fmt = "c.", label = r"$L=49$")
ax1.errorbar( (data65[:,0] - beta_crit)*f65x, data65[:,-2], yerr = data65[:,-1], fmt = "r.", label = r"$L=65$")
#ax1.errorbar( (data97[:,0] - beta_crit)*f97x, data97[:,-2], yerr = data97[:,-1], fmt = "b.", label = r"$L=97$")
ax1.errorbar( (data127[:,0] - beta_crit)*f127x, data127[:,-2], yerr = data127[:,-1], fmt = "g.", label = r"$L=127$")
ax1.errorbar( (data257[:,0] - beta_crit)*f257x, data257[:,-2], yerr = data257[:,-1], fmt = "c.-", label = r"$L=257$")
ax1.set_xlim([-2,2])
ax1.set_ylim([0,1])
#ax1.set_xlabel(r"$(\beta - \beta_c) J L^{1/\nu}$", fontdict=font1)
ax1.set_ylabel(r"$\chi_{\rm s}$", fontdict=font1)
ax1.legend(loc="best", fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.tick_params(axis='both', which='minor', labelsize=10)


#ax2.errorbar( (data9[:,0]  - beta_crit)*f9x,  data9[:,1]*f9, yerr = data9[:,2]*f9,    fmt = "k.", label = r"$L=9$")
ax2.errorbar( (data17[:,0] - beta_crit)*f17x, data17[:,1]*f17, yerr = data17[:,2]*f17, fmt = "b.", label = r"$L=17$")
ax2.errorbar( (data33[:,0] - beta_crit)*f33x, data33[:,1]*f33, yerr = data33[:,2]*f33, fmt = "m.", label = r"$L=33$")
#ax2.errorbar( (data49[:,0] - beta_crit)*f49x, data49[:,1]*f49, yerr = data49[:,2]*f49, fmt = "c.", label = r"$L=49$")
ax2.errorbar( (data65[:,0] - beta_crit)*f65x, data65[:,1]*f65, yerr = data65[:,2]*f65, fmt = "r.", label = r"$L=65$")
#ax2.errorbar( (data97[:,0] - beta_crit)*f97x, data97[:,1]*f97, yerr = data97[:,2]*f97, fmt = "b.", label = r"$L=97$")
ax2.errorbar( (data127[:,0] - beta_crit)*f127x, data127[:,1]*f127, yerr = data127[:,2]*f127, fmt = "g.", label = r"$L=127$")
ax2.errorbar( (data257[:,0] - beta_crit)*f257x, data257[:,1]*f257, yerr = data257[:,2]*f257, fmt = "c.-", label = r"$L=257$")
ax2.set_xlim([-2,2])
ax2.set_ylim([0,5])
ax2.set_xlabel(r"$(\beta -\beta_c)J L^{1/\nu}$", fontdict =font1)
#plt.ylabel(r"$L^{\eta}n_0$", fontdict = font1)
ax2.set_ylabel(r"$L^{\eta}m_{\perp}^2$", fontdict = font1)
ax2.legend(loc="best", fontsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='minor', labelsize=10)
#ax2.yaxis.set_label_position("right")
#ax2.yaxis.tick_right()
plt.savefig("fig_QMC_delta0_collapse_combined.pdf", format="pdf", bbox_inches="tight")




