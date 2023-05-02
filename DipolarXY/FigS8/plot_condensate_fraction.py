import numpy as np
import matplotlib.pylab as plt

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


nu = 1
eta = 1
z = 0.5

data9 = np.loadtxt("../Fig1/Groundstate/z_one_half/out_L9")
data17 = np.loadtxt("../Fig1/Groundstate/z_one_half/out_L17")
data33 = np.loadtxt("../Fig1/Groundstate/z_one_half/out_L33")
#data49 = np.loadtxt("../Fig1/Groundstate/z_one_half/out_L49")
data65 = np.loadtxt("../Fig1/Groundstate/z_one_half/out_L65")
#data97 = np.loadtxt("../Fig1/Groundstate/z_one_half/out_L97")
data129= np.loadtxt("../Fig1/Groundstate/z_one_half/out_L129")
data257= np.loadtxt("../Fig1/Groundstate/z_one_half/out_L257")

#f9 = 9
#f17 = 17
#f33 = 33
#f49 = 49
#f65 = 65
#f97 = 97
#f129 = 129

f9 = 8 * np.power(9., eta)
f17 = 11.3137085 * np.power(17., eta)
f33 = 16 * np.power(33., eta)
f65 = 22.627416998 * np.power(65., eta)
f129 = 32 * np.power(129., eta)
f257 = 45.254834 * np.power(257., eta)

plt.figure()
plt.errorbar(data9[:,0], data9[:,1]*f9, yerr = data9[:,2] * f9,    fmt = "ko-", label = r"$L=9$")
plt.errorbar(data17[:,0], data17[:,1]*f17, yerr = data17[:,2] * f17, fmt = "gs-", label = r"$L=17$")
plt.errorbar(data33[:,0], data33[:,1]*f33, yerr = data33[:,2]* f33, fmt = "md-", label = r"$L=33$")
#plt.errorbar(data49[:,0], data49[:,1]*f49, yerr = data49[:,2] * f49, fmt = "c.-", label = r"$L=49$")
plt.errorbar(data65[:,0], data65[:,1]*f65, yerr = data65[:,2] * f65, fmt = "ro-", label = r"$L=65$")
#plt.errorbar(data97[:,0], data97[:,1]*f97, yerr = data97[:,2] * f97, fmt = "bd-", label = r"$L=97$")
plt.errorbar(data129[:,0], data129[:,1]*f129, yerr = data129[:,2] * f129, fmt = "bd-", label = r"$L=129$")
plt.errorbar(data257[:,0], data257[:,1]*f257, yerr = data257[:,2] * f257, fmt = "c.-", label = r"$L=257$")
plt.xlim([3.9,4.5])
plt.ylim([0,10])
#plt.title(r"$\beta \sim \sqrt{L}$")
plt.xlabel(r"$\delta / J$", fontdict = font1)
#plt.ylabel(r"$n_0 \beta L^{\eta}$", fontdict=font1)
plt.ylabel(r"$m_{\perp}^2 \beta L^{\eta}$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_n0_gs_rescaled.pdf", format="pdf", bbox_inches="tight")
plt.show()


plt.figure()
delta_crit = 4.029
f9x =  np.power(9., 1./(nu)) / delta_crit
f17x = np.power(17., 1./(nu)) / delta_crit
f33x = np.power(33, 1./(nu )) / delta_crit
#f49x = np.power(49, 1./(nu)) / delta_crit
f65x = np.power(65, 1./(nu )) / delta_crit
#f97x = np.power(97, 1./(nu)) / delta_crit
f129x = np.power(129, 1./(nu)) / delta_crit
f257x = np.power(257, 1./nu) / delta_crit
print(f9x, f17x, f33x, f65x, f129x)
plt.errorbar( (data9[:,0] - delta_crit)*f9x, data9[:,1]*f9, yerr = data9[:,2]*f9,    fmt = "ko", label = r"$L=9$")
plt.errorbar( (data17[:,0] - delta_crit)*f17x, data17[:,1]*f17, yerr = data17[:,2]*f17, fmt = "gs", label = r"$L=17$")
plt.errorbar( (data33[:,0] - delta_crit)*f33x, data33[:,1]*f33, yerr = data33[:,2]*f33, fmt = "md", label = r"$L=33$")
#plt.errorbar( (data49[:,0] - delta_crit)*f49x, data49[:,1]*f49, yerr = data49[:,2]*f49, fmt = "c.", label = r"$L=49$")
plt.errorbar( (data65[:,0] - delta_crit)*f65x, data65[:,1]*f65, yerr = data65[:,2]*f65, fmt = "ro", label = r"$L=65$")
#plt.errorbar( (data97[:,0] - delta_crit)*f97x, data97[:,1]*f97, yerr = data97[:,2]*f97, fmt = "bd", label = r"$L=97$")
plt.errorbar( (data129[:,0] - delta_crit)*f129x, data129[:,1]*f129, yerr = data129[:,2]*f129, fmt = "bd", label = r"$L=129$")
plt.errorbar( (data257[:,0] - delta_crit)*f257x, data257[:,1]*f257, yerr = data257[:,2]*f257, fmt = "c.-", label = r"$L=257$")
plt.xlim([-1.5,2])
plt.ylim([0,10])
plt.xlabel(r"$(\delta - \delta_c) L^{1/\nu}$", fontdict=font1)
#plt.ylabel(r"$n_0 \beta L^{\eta}$", fontdict=font1)
plt.ylabel(r"$m_{\perp}^2 \beta L^{\eta}$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_n0_gs_collapse.pdf", format="pdf", bbox_inches="tight")

# -------------------------------
# two panel figure with collapse
# -------------------------------

fig = plt.figure()
gs = fig.add_gridspec(2, 1)
# spans two rows:
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])


f9 = 8
f17 = 11.3137085
f33 = 16
f65 = 22.627416998
f129 = 32
f257 = 45.254834


#ax1.errorbar( (data9[:,0] - delta_crit)*f9x, data9[:,-2]*f9, yerr = data9[:,-1]*f9,    fmt = "ko", label = r"$L=9$")
ax1.errorbar( (data17[:,0] - delta_crit)*f17x, data17[:,-2]*f17, yerr = data17[:,-1]*f17, fmt = "b.", label = r"$L=17$")
ax1.errorbar( (data33[:,0] - delta_crit)*f33x, data33[:,-2]*f33, yerr = data33[:,-1]*f33, fmt = "m.", label = r"$L=33$")
#plt.errorbar( (data49[:,0] - delta_crit)*f49x, data49[:,-2]*f49, yerr = data49[:,-1]*f49, fmt = "c.", label = r"$L=49$")
ax1.errorbar( (data65[:,0] - delta_crit)*f65x, data65[:,-2]*f65, yerr = data65[:,-1]*f65, fmt = "r.", label = r"$L=65$")
#plt.errorbar( (data97[:,0] - delta_crit)*f97x, data97[:,-2]*f97, yerr = data97[:,-1]*f97, fmt = "bd", label = r"$L=97$")
ax1.errorbar( (data129[:,0] - delta_crit)*f129x, data129[:,-2]*f129, yerr = data129[:,-1]*f129, fmt = "g.", label = r"$L=129$")
ax1.errorbar( (data257[:,0] - delta_crit)*f257x, data257[:,-2]*f257, yerr = data257[:,-1]*f257, fmt = "c.-", label = r"$L=257$")
ax1.set_xlim([-1.5,2])
ax1.set_ylim([0,10])
#ax1.set_xlabel(r"$(\delta - \delta_c) L^{1/\nu}$", fontdict=font1)
#plt.ylabel(r"$\rho_{\rm sf} \beta$")
ax1.set_ylabel(r"$\chi_{\rm s} \beta$", fontdict=font1)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.tick_params(axis='both', which='minor', labelsize=10)
ax1.legend(loc="best", fontsize=12)

f9 = 8 * np.power(9., eta)
f17 = 11.3137085 * np.power(17., eta)
f33 = 16 * np.power(33., eta)
f65 = 22.627416998 * np.power(65., eta)
f129 = 32 * np.power(129., eta)
f257 = 45.254834 * np.power(257., eta)
#ax2.errorbar( (data9[:,0] - delta_crit)*f9x, data9[:,1]*f9, yerr = data9[:,2]*f9,    fmt = "ko", label = r"$L=9$")
ax2.errorbar( (data17[:,0] - delta_crit)*f17x, data17[:,1]*f17, yerr = data17[:,2]*f17, fmt = "b.", label = r"$L=17$")
ax2.errorbar( (data33[:,0] - delta_crit)*f33x, data33[:,1]*f33, yerr = data33[:,2]*f33, fmt = "m.", label = r"$L=33$")
#ax1.errorbar( (data49[:,0] - delta_crit)*f49x, data49[:,1]*f49, yerr = data49[:,2]*f49, fmt = "c.", label = r"$L=49$")
ax2.errorbar( (data65[:,0] - delta_crit)*f65x, data65[:,1]*f65, yerr = data65[:,2]*f65, fmt = "r.", label = r"$L=65$")
#ax2.errorbar( (data97[:,0] - delta_crit)*f97x, data97[:,1]*f97, yerr = data97[:,2]*f97, fmt = "b.", label = r"$L=97$")
ax2.errorbar( (data129[:,0] - delta_crit)*f129x, data129[:,1]*f129, yerr = data129[:,2]*f129, fmt = "g.", label = r"$L=129$")
ax2.errorbar( (data257[:,0] - delta_crit)*f257x, data257[:,1]*f257, yerr = data257[:,2]*f257, fmt = "c.-", label = r"$L=257$")
ax2.set_xlim([-1.5,2])
ax2.set_ylim([0,10])
ax2.set_xlabel(r"$(\delta - \delta_c) L^{1/\nu}$", fontdict=font1)
ax2.set_ylabel(r"$m_{\perp}^2 \beta L^{\eta}$", fontdict=font1)
ax2.legend(loc="best", fontsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='minor', labelsize=10)
#ax2.yaxis.set_label_position("right")
#ax2.yaxis.tick_right()
plt.savefig("fig_QMC_gs_collapse_combined.pdf", format="pdf", bbox_inches="tight")





