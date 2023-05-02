import numpy as np
import matplotlib.pylab as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
from scipy import stats

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

T_AFM = np.array([0.500000, 0.600000, 0.700000, 0.800000, 0.900000, 1.000000, 1.100000, 1.200000, 1.300000, 1.400000, 1.500000, 1.600000, 1.700000, 1.800000, 1.900000, 2.000000, 2.250000, 2.500000, 2.750000, 3.000000, 3.250000, 3.500000, 3.750000, 4.000000, 4.250000, 4.500000, 4.750000, 5.000000, 5.250000, 5.500000, 5.750000, 6.000000, 6.250000, 6.500000, 6.750000, 7.000000, 7.250000, 7.500000, 7.750000, 8.000000, 8.250000, 8.500000, 8.750000, 9.000000, 9.250000, 9.500000, 9.750000, 10.000000])
s_AFM = np.array([0.531601, 0.557475, 0.580586, 0.597398, 0.610370, 0.621526, 0.630582, 0.637687, 0.643546, 0.648684, 0.653194, 0.656306, 0.659913, 0.663487, 0.665626, 0.668093, 0.672632, 0.675923, 0.678953, 0.680865, 0.682125, 0.683504, 0.684719, 0.685025, 0.686411, 0.687617, 0.687442, 0.688158, 0.688534, 0.688904, 0.689245, 0.689599, 0.689711, 0.690605, 0.690824, 0.690265, 0.691430, 0.690438, 0.689939, 0.691261, 0.691209, 0.691396, 0.691402, 0.692346, 0.692414, 0.691650, 0.691792, 0.691691])
f_AFM = np.array([-0.503576, -0.558029, -0.615002, -0.673989, -0.734385, -0.796018, -0.858638, -0.922085, -0.986144, -1.050776, -1.115865, -1.181380, -1.247139, -1.313362, -1.379800, -1.446496, -1.614129, -1.782733, -1.952075, -2.122140, -2.292466, -2.463210, -2.634208, -2.805513, -2.976788, -3.148707, -3.320510, -3.492483, -3.664568, -3.836750, -4.009018, -4.181373, -4.353802, -4.526277, -4.699062, -4.871641, -5.044303, -5.217221, -5.389553, -5.562305, -5.735097, -5.907924, -6.080784, -6.253684, -6.426902, -6.599839, -6.772784, -6.945719])
print(T_AFM.shape)
print(s_AFM.shape)
print(f_AFM.shape)
E_AFM = f_AFM + T_AFM * s_AFM


def lattsum(L):
  s = 0
  for i in np.arange(0,L):
    for j in np.arange(0,L):
      x = i
      if x > L/2.:
       x = L - i
      y = j
      if y > L/2.:
       y = L - j
      if (x*x + y*y > 0):
        s += 0.25 * np.power(x*x + y*y, -3.0)
        #print (i,j,x,y,s)
  return s

def lattsum_triple(L):
  s = 0
  for i1 in np.arange(0,L):
    for j1 in np.arange(0,L):
      dx1 = i1
      if (dx1 > L/2.):
        dx1 = L - dx1
      dy1 = j1
      if (dy1 > L/2.):
        dy1 = L - dy1
      for i2 in np.arange(0,L):
        for j2 in np.arange(0,L):
          dx2 = (i2 - i1)
          if (dx2 > L/2.):
            dx2 = L - dx2
          if (dx2 < -L/2.):
            dx2 += L
          dy2 = (j2 - j1)
          if (dy2 > L/2.):
            dy2 = L - dy2
          if (dy2 < -L/2.):
            dy2 += L
          dx3 = i2
          if (dx3 > L/2.):
            dx3 = L - dx3
          dy3 = j2
          if (dy3 > L/2.):
            dy3 = L - dy3
          if ((dx1*dx1 + dy1*dy1) > 0 and (dx2*dx2 + dy2 * dy2 > 0) and (dx3*dx3 + dy3*dy3 > 0)):
            #print(i1, j1, i2, j2, dx1, dy1, dx2, dy2, dx3, dy3,s)
            s += 0.125 * np.power(dx1*dx1 +dy1*dy1, -1.5)*np.power(dx2*dx2+dy2*dy2, -1.5) * np.power(dx3*dx3 + dy3*dy3, -1.5)
  return s

def low_energy(x,a,b):
  return (a + b*np.power(x,5.))

def high_energy(x,a):
  return (a/x)

def high_energy_beta(x,a):
  return (a*x)

def high_energy_beta_series(x,phi):
  return((-x * phi)/(1. + 0.5*x*x*phi))

L33 = 33
L33sq = L33*L33
Np33 = (L33 * L33 + 1)//2
phi33 = lattsum(L33) / 4.
print("phi33 = ", phi33)
#psi33 = lattsum_triple(33)
psi33 = 1.7065677588485995
#psi33 = 1.7
print("psi33 = ", psi33)

L65 = 65
L65sq = L65*L65
Np65 = (L65 * L65 + 1)//2
phi65 = lattsum(L65) / 4.
print("phi65 = ", phi65)

data33 = np.loadtxt("../FigS1/L33/en_L33.dat")
beta33 = data33[:,0]
en33 = data33[:,5] / L33sq
en33err = data33[:,6] / L33sq

data33E = np.loadtxt("../FigS1/L33_Ewald/en_L33.dat")
beta33E = data33E[:,0]
en33E = data33E[:,5] / L33sq
en33errE = data33E[:,6] / L33sq

data65 = np.loadtxt("../FigS1/L65/en_L65.dat")
beta65 = data65[:,0]
en65 = data65[:,5] / L65sq
en65err = data65[:,6] / L65sq

data65E = np.loadtxt("../FigS1/L65_Ewald/en_L65.dat")
beta65E = data65E[:,0]
en65E = data65E[:,5] / L65sq
en65errE = data65E[:,6] / L65sq

xmin33 = np.where(beta33 == 2)[0][0] 
xmax33 = np.where(beta33 == 10)[0][0] 
xmin33E = np.where(beta33E == 2)[0][0] 
xmax33E = np.where(beta33E == 10)[0][0] 
xmin65 = np.where(beta65 == 2)[0][0] 
xmax65 = np.where(beta65 == 10)[0][0] 
xmin65E = np.where(beta65E == 2)[0][0] 
xmax65E = np.where(beta65E == 10)[0][0] 

popt33, pcov33 = curve_fit( low_energy, xdata=1./beta33[xmin33:xmax33], ydata=en33[xmin33:xmax33], sigma = en33err[xmin33:xmax33])
print(1./beta33[xmin33:xmax33])
print(en33[xmin33:xmax33])
print(popt33)
print(pcov33)

popt33E, pcov33E = curve_fit( low_energy, xdata=1./beta33E[xmin33E:xmax33E], ydata=en33E[xmin33E:xmax33E], sigma = en33errE[xmin33E:xmax33E])
popt65, pcov65 = curve_fit( low_energy, xdata=1./beta65[xmin65:xmax65], ydata=en65[xmin65:xmax65], sigma = en65err[xmin65:xmax65])
popt65E, pcov65E = curve_fit( low_energy, xdata=1./beta65E[xmin65E:xmax65E], ydata=en65E[xmin65E:xmax65E], sigma = en65err[xmin65E:xmax65E])
print("popt65E", popt65E, pcov65E)


#xs = np.linspace(0.1, 1.25, 125)
xs = np.linspace(0.1, 1.00, 100)

plt.figure()
plt.errorbar(1/beta33, en33, yerr=en33err, fmt="r.", label=r"$L=33$, bare")
plt.plot(xs, low_energy(xs, *popt33), "r--", label=r"$E_0=%2.5f(%1.5f), \gamma=%1.3f(%1.3f) $" %(popt33[0], np.sqrt(pcov33[0][0]), popt33[1], np.sqrt(pcov33[1][1]) ))
plt.errorbar(1/beta33E, en33E, yerr=en33errE, fmt="b.", label=r"$L=33$, resummed")
plt.plot(xs, low_energy(xs, *popt33E), "b--", label=r"$E_0=%2.5f(%1.5f), \gamma=%1.3f(%1.3f) $" %(popt33E[0], np.sqrt(pcov33E[0][0]), popt33E[1], np.sqrt(pcov33E[1][1])) )
plt.errorbar(1/beta65, en65, yerr=en65err, fmt="c.", label=r"$L=65$, bare")
plt.plot(xs, low_energy(xs, *popt65), "c--", label=r"$E_0=%2.5f(%1.5f), \gamma=%1.3f(%1.3f) $" %(popt65[0], np.sqrt(pcov65[0][0]), popt65[1], np.sqrt(pcov65[1][1]) ))
plt.errorbar(1/beta65E, en65E, yerr=en65errE, fmt="m.", label=r"$L=65$, resummed")
plt.plot(xs, low_energy(xs, *popt65E), "m--", label=r"$E_0=%2.5f(%1.5f), \gamma=%1.3f(%1.3f) $" %(popt65E[0], np.sqrt(pcov65E[0][0]), popt65E[1], np.sqrt(pcov65E[1][1]) ))
plt.xlim([0.1, 1.5])
plt.ylim([-1.2, -0.8])
plt.xlabel(r"$T/J$", fontdict=font1)
plt.ylabel(r"$E/N$", fontdict=font1)
plt.legend(loc="best")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("fig_QMC_energy_lowT.pdf", format="pdf", bbox_inches="tight")
#plt.show()

plt.figure()
plt.errorbar(1/beta33, en33 - popt33[0], yerr=en33err, fmt="r.", label=r"$L=33$, bare, shifted by %2.5f(%1.5f)" %(popt33[0], np.sqrt(pcov33[0][0])) )
plt.plot(xs, popt33[1]*np.power(xs, 5.), "b--", label=r"$\gamma T^5; \gamma = %1.3f(%1.3f)$" % (popt33[1], np.sqrt(pcov33[1][1] ) ) )
plt.errorbar(1/beta65, en65 - popt65[0], yerr=en65err, fmt="c.", label=r"$L=65$, bare, shifted by %2.5f(%1.5f)" %(popt65[0], np.sqrt(pcov65[0][0])) )
plt.plot(xs, popt65[1]*np.power(xs, 5.), "m--", label=r"$\gamma T^5; \gamma = %1.3f(%1.3f)$" % (popt65[1], np.sqrt(pcov65[1][1] ) ) )
plt.xscale("log")
plt.yscale("log")
plt.xlim([0.1, 1.5])
plt.xlabel(r"$T/J$", fontdict=font1)
plt.ylabel(r"$(E-E_0)/N$", fontdict=font1)
plt.legend(loc="best")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("fig_QMC_energy_powerlaw.pdf", format="pdf", bbox_inches="tight")
#plt.show()

fig = plt.figure()
gs = fig.add_gridspec(2, 1)
# spans two rows:
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax1.errorbar(1/beta33, en33, yerr=en33err, fmt="r.", label=r"$L=33$, bare")
#ax1.plot(xs, low_energy(xs, *popt33), "r--", label=r"$E_0=%2.5f(%1.5f), \gamma=%1.3f(%1.3f) $" %(popt33[0], np.sqrt(pcov33[0][0]), popt33[1], np.sqrt(pcov33[1][1]) ))
ax1.plot(xs, low_energy(xs, *popt33), "r--" )
ax1.errorbar(1/beta33E, en33E, yerr=en33errE, fmt="b.", label=r"$L=33$, resummed")
#ax1.plot(xs, low_energy(xs, *popt33E), "b--", label=r"$E_0=%2.5f(%1.5f), \gamma=%1.3f(%1.3f) $" %(popt33E[0], np.sqrt(pcov33E[0][0]), popt33E[1], np.sqrt(pcov33E[1][1])) )
ax1.plot(xs, low_energy(xs, *popt33E), "b--")
ax1.errorbar(1/beta65, en65, yerr=en65err, fmt="c.", label=r"$L=65$, bare")
#ax1.plot(xs, low_energy(xs, *popt65), "c--", label=r"$E_0=%2.5f(%1.5f), \gamma=%1.3f(%1.3f) $" %(popt65[0], np.sqrt(pcov65[0][0]), popt65[1], np.sqrt(pcov65[1][1]) ))
ax1.plot(xs, low_energy(xs, *popt65), "c--")
ax1.errorbar(1/beta65E, en65E, yerr=en65errE, fmt="m.", label=r"$L=65$, resummed")
#ax1.plot(xs, low_energy(xs, *popt65E), "m--", label=r"$E_0=%2.5f(%1.5f), \gamma=%1.3f(%1.3f) $" %(popt65E[0], np.sqrt(pcov65E[0][0]), popt65E[1], np.sqrt(pcov65E[1][1]) ))
ax1.plot(xs, low_energy(xs, *popt65E), "m--")
ax1.set_xlim([0.1, 1.5])
ax1.set_ylim([-1.2, -0.8])
#ax1.set_xlabel(r"$T/J$", fontdict=font1)
ax1.set_ylabel(r"$E/N$", fontdict=font1)
ax1.legend(loc="best")
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.tick_params(axis='both', which='minor', labelsize=10)
#ax1.set_xticks(fontsize=14)
#ax1.set_yticks(fontsize=14)
#ax2.errorbar(1/beta33, en33 - popt33[0], yerr=en33err, fmt="r.", label=r"$L=33$, bare, shifted by %2.5f(%1.5f)" %(popt33[0], np.sqrt(pcov33[0][0])) )
ax2.errorbar(1/beta33, en33 - popt33[0], yerr=en33err, fmt="r.", label=r"$L=33$, bare")
#ax2.plot(xs, popt33[1]*np.power(xs, 5.), "b--", label=r"$\gamma T^5; \gamma = %1.3f(%1.3f)$" % (popt33[1], np.sqrt(pcov33[1][1] ) ) )
ax2.plot(xs, popt33[1]*np.power(xs, 5.), "r--", label =r"$\sim T^5$")
#ax2.errorbar(1/beta65, en65 - popt65[0], yerr=en65err, fmt="c.", label=r"$L=65$, bare, shifted by %2.5f(%1.5f)" %(popt65[0], np.sqrt(pcov65[0][0])) )
ax2.errorbar(1/beta65, en65 - popt65[0], yerr=en65err, fmt="c.", label=r"$L=65$, bare")
#ax2.plot(xs, popt65[1]*np.power(xs, 5.), "m--", label=r"$\gamma T^5; \gamma = %1.3f(%1.3f)$" % (popt65[1], np.sqrt(pcov65[1][1] ) ) )
ax2.plot(xs, popt65[1]*np.power(xs, 5.), "c--", label = r"$\sim T^5$")
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xlim([0.1, 1.5])
ax2.set_xlabel(r"$T/J$", fontdict=font1)
ax2.set_ylabel(r"$(E-E_0)/N$", fontdict=font1)
ax2.legend(loc="best")
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='minor', labelsize=10)
#ax2.yaxis.set_label_position("right")
#ax2.yaxis.tick_right()
plt.savefig("fig_QMC_energy_lowT_combined.pdf", format="pdf", bbox_inches="tight")
plt.show()



xmin33 = 0
xmax33 = np.where(beta33 == 0.2)[0][0]
xmin33E = 0
xmax33E = np.where(beta33E == 0.2)[0][0]
xmin65 = 0
xmax65 = np.where(beta65 == 0.2)[0][0]
xmin65E = 0
xmax65E = np.where(beta65E == 0.2)[0][0]

#qopt33, qcov33 = curve_fit( high_energy_beta, xdata=beta33[xmin33:xmax33], ydata=en33[xmin33:xmax33], sigma = en33err[xmin33:xmax33])
#print()
#print()
#print(xmin33, xmax33)
#print(beta33[xmin33:xmax33])
#print(en33[xmin33:xmax33])
#print(qopt33)
#print(qcov33)
#qopt33E, qcov33E = curve_fit( high_energy_beta, xdata=beta33E[xmin33E:xmax33E], ydata=en33E[xmin33E:xmax33E], sigma = en33errE[xmin33E:xmax33E])
#qopt65, qcov65 = curve_fit( high_energy_beta, xdata=beta65[xmin65:xmax65], ydata=en65[xmin65:xmax65], sigma = en65err[xmin65:xmax65])
#qopt65E, qcov65E = curve_fit( high_energy_beta, xdata=beta65E[xmin65E:xmax65E], ydata=en65E[xmin65E:xmax65E], sigma = en65err[xmin65E:xmax65E])

res33 = stats.linregress(beta33[xmin33:xmax33], en33[xmin33:xmax33])
print()
print()
print(res33.slope, res33.intercept, res33.stderr)
print()
res33E = stats.linregress(beta33E[xmin33E:xmax33E], en33E[xmin33E:xmax33E])
res65 = stats.linregress(beta65[xmin65:xmax65], en65[xmin65:xmax65])
res65E = stats.linregress(beta65E[xmin65E:xmax65E], en65E[xmin65E:xmax65E])

xs = np.linspace(0, 0.3, 30)
T_AFM_bis = np.array([1.500000, 1.600000, 1.700000, 1.800000, 1.900000, 2.000000, 2.250000, 2.500000, 2.750000, 3.000000, 3.250000, 3.500000, 3.750000, 4.000000, 4.250000, 4.500000, 4.750000, 5.000000, 5.250000, 5.500000, 5.750000, 6.000000, 6.250000, 6.500000, 6.750000, 7.000000, 7.250000, 7.500000, 7.750000, 8.000000, 8.250000, 8.500000, 8.750000, 9.000000, 9.250000, 9.500000, 9.750000, 10.000000, 12.500000, 15.000000, 17.500000, 20.000000, 25.000000, 30.000000])
E_AFM_bis = np.array([-0.134507, -0.128383, -0.122823, -0.117715, -0.113035, -0.108722, -0.099253, -0.091325, -0.084583, -0.078779, -0.073724, -0.069284, -0.065358, -0.061852, -0.058690, -0.055865, -0.053284, -0.050939, -0.048791, -0.046818, -0.045000, -0.043318, -0.041759, -0.040307, -0.038955, -0.037689, -0.036502, -0.035386, -0.034339, -0.033350, -0.032418, -0.031536, -0.030702, -0.029911, -0.029157, -0.028440, -0.027757, -0.027107, -0.021976, -0.018476, -0.015940, -0.014017, -0.011292, -0.009457])

plt.figure()
plt.errorbar(beta33, en33, yerr=en33err, fmt="r.", label=r"$L=33$, FM (QMC)")
plt.errorbar(beta65, en65, yerr=en65err, fmt="c.", label=r"$L=65$, FM (QMC)")
plt.plot(1/T_AFM_bis, E_AFM_bis, "b.", label="AFM (pm-fRG)") 
#plt.plot(xs, (-xs * phi33), "k--", label=r"$\phi = %2.3f$ (2nd order)" %(phi33)  )
plt.plot(xs, (-xs * phi33), "k--", label="2nd order")
#plt.plot(xs, (-xs * phi33-0.5*xs*xs*psi33/4.), "g--", label=r"$\psi = %2.3f$ (3rd order FM)" %(psi33)  )
#plt.plot(xs, (-xs * phi33+0.5*xs*xs*psi33/4.), "m--", label=r"$\psi = %2.3f$ (3rd order AFM)" %(psi33)  )
plt.plot(xs, (-xs * phi33-0.5*xs*xs*psi33/4.), "g--", label="3rd order FM")
plt.plot(xs, (-xs * phi33+0.5*xs*xs*psi33/4.), "m--", label="3rd order AFM")
plt.xlim([0, 0.35])
plt.ylim([-0.2, 0])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel(r"$\beta J$", fontdict=font1)
plt.ylabel(r"$E/N$", fontdict=font1)
plt.legend(loc="best", fontsize=14)
plt.savefig("fig_QMC_energy_highT.pdf", format="pdf", bbox_inches="tight")
plt.show()

