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
plt.errorbar(data9[:,0], data9[:,1]/0.5, yerr = data9[:,2]/0.5,    fmt = "ko-", label = r"$L=9$")
plt.errorbar(data17[:,0], data17[:,1]/0.5, yerr = data17[:,2]/0.5, fmt = "ys-", label = r"$L=17$")
plt.errorbar(data33[:,0], data33[:,1]/0.5, yerr = data33[:,2]/0.5, fmt = "md-", label = r"$L=33$")
plt.errorbar(data49[:,0], data49[:,1]/0.5, yerr = data49[:,2]/0.5, fmt = "c.-", label = r"$L=49$")
plt.errorbar(data65[:,0], data65[:,1]/0.5, yerr = data65[:,2]/0.5, fmt = "ro-", label = r"$L=65$")
plt.errorbar(data127[:,0], data127[:,1]/0.5, yerr = data127[:,2]/0.5, fmt = "bd-", label = r"$L=127$")
plt.errorbar(data257[:,0], data257[:,1]/0.5, yerr = data257[:,2]/0.5, fmt = "go-", label = r"$L=257$")
plt.xlim([0.5,0.6])
plt.ylim([0,0.4])
plt.xlabel(r"$\beta J$")
plt.ylabel(r"$n_0$")
plt.legend(loc="best", fontsize=17)
#plt.savefig("fig_delta0_n0.pdf", format="pdf")
plt.savefig("fig_delta0_n0_zoom.pdf", format="pdf")


plt.figure()
eta = 1.0
f9 =  2. * np.power(9., eta) 
f17 = 2. * np.power(17., eta) 
f33 = 2. * np.power(33, eta)
f49 = 2. * np.power(49, eta)
f65 = 2. * np.power(65, eta)
f97 = 2. * np.power(97, eta)
f127 = 2. * np.power(127, eta)
f257 = 2. * np.power(257, eta)
#plt.errorbar(data9[:,0],  data9[:,1]*f9, yerr = data9[:,2]*f9,    fmt = "k.-", label = r"$L=9$")
plt.errorbar(data17[:,0], data17[:,1]*f17, yerr = data17[:,2]*f17, fmt = "k.-", label = r"$L=17$")
plt.errorbar(data33[:,0], data33[:,1]*f33, yerr = data33[:,2]*f33, fmt = "m.-", label = r"$L=33$")
#plt.errorbar(data49[:,0], data49[:,1]*f49, yerr = data49[:,2]*f49, fmt = "c.-", label = r"$L=49$")
plt.errorbar(data65[:,0], data65[:,1]*f65, yerr = data65[:,2]*f65, fmt = "r.-", label = r"$L=65$")
#plt.errorbar(data97[:,0], data97[:,1]*f97, yerr = data97[:,2]*f97, fmt = "r.-", label = r"$L=97$")
plt.errorbar(data127[:,0], data127[:,1]*f127, yerr = data127[:,2]*f127, fmt = "b.-", label = r"$L=127$")
plt.errorbar(data257[:,0], data257[:,1]*f257, yerr = data257[:,2]*f257, fmt = "g.-", label = r"$L=257$")
#plt.xlim([0.47,0.53])
plt.xlim([0.516,0.522])
plt.ylim([1,1.5])
#plt.ylim([0,5])
plt.xlabel(r"$\beta J$", fontdict=font1)
#plt.ylabel(r"$L^{\eta}n_0$", fontdict=font1)
plt.ylabel(r"$L^{\eta}m_{\perp}^2$", fontdict=font1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(loc="best", fontsize=20)
plt.savefig("fig_delta0_n0_rescaled.pdf", format="pdf", bbox_inches="tight")
plt.show()


plt.figure()
f9 =  2. * np.power(9., eta)
f17 = 2. * np.power(17., eta)
f33 = 2. * np.power(33, eta)
f49 = 2. * np.power(49, eta)
f65 = 2. * np.power(65, eta)
f97 = 2. * np.power(97, eta)
f127 = 2. * np.power(127, eta)
beta_crit = 0.51985
nu = 1.0
f9x =  np.power(9., nu)
f17x = np.power(17., nu)
f33x = np.power(33, nu)
f49x = np.power(49, nu)
f65x = np.power(65, nu)
f97x = np.power(97, nu)
f127x = np.power(127, nu)
f257x = np.power(257, nu)
plt.errorbar( (data9[:,0]  - beta_crit)*f9x,  data9[:,1]*f9, yerr = data9[:,2]*f9,    fmt = "b.", label = r"$L=9$")
#plt.errorbar( (data17[:,0] - beta_crit)*f17x, data17[:,1]*f17, yerr = data17[:,2]*f17, fmt = "ys-", label = r"$L=17$")
plt.errorbar( (data33[:,0] - beta_crit)*f33x, data33[:,1]*f33, yerr = data33[:,2]*f33, fmt = "k.", label = r"$L=33$")
plt.errorbar( (data49[:,0] - beta_crit)*f49x, data49[:,1]*f49, yerr = data49[:,2]*f49, fmt = "c.", label = r"$L=49$")
plt.errorbar( (data65[:,0] - beta_crit)*f65x, data65[:,1]*f65, yerr = data65[:,2]*f65, fmt = "y.", label = r"$L=65$")
#plt.errorbar( (data97[:,0] - beta_crit)*f97x, data97[:,1]*f97, yerr = data97[:,2]*f97, fmt = "b.", label = r"$L=97$")
plt.errorbar( (data127[:,0] - beta_crit)*f127x, data127[:,1]*f127, yerr = data127[:,2]*f127, fmt = "g.", label = r"$L=127$")
plt.errorbar( (data257[:,0] - beta_crit)*f257x, data257[:,1]*f257, yerr = data257[:,2]*f257, fmt = "r.-", label = r"$L=257$")
plt.xlim([-2,2])
plt.ylim([0,9])
plt.xlabel(r"$(\beta -\beta_c)J L^{1/\nu}$", fontdict =font1)
#plt.ylabel(r"$L^{\eta}n_0$", fontdict = font1)
plt.ylabel(r"$L^{\eta}m_{\perp}^2$", fontdict = font1)
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_QMC_delta0_n0_collapse.pdf", format="pdf", bbox_inches="tight")

