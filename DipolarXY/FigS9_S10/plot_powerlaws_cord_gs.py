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

def cord(x,L):
  return np.sin(x * np.pi / L) * L / np.pi

data1 = np.loadtxt("dm_b1_L33.dat")
data2 = np.loadtxt("dm_b2_L33.dat")
data5 = np.loadtxt("dm_b5_L33.dat")
data10 = np.loadtxt("dm_b10_L33.dat")

L = 33 
Lh = 17


def pwlaw10(x,a):
  #return a * np.power(np.sin(np.pi * x / L), -1.)
  return a * np.power( x, -1.)

def pwlaw15(x,a):
  #return a * np.power(np.sin(np.pi * x / L), -1.5)
  return a * np.power(x, -1.5)

def pwlaw30(x,a):
  #return a * np.power(np.sin(np.pi * x / L), -3.)
  return a * np.power(x, -3.)

def pwlaw_free(x,a,b):
  #return a * np.power(np.sin(np.pi * x / L), -b)
  return a * np.power( x, -b)

def pwlaw_free_n0(x,a,b,n0):
  return n0 + a*np.power(x,-b)


popt_1, pcov_1 = curve_fit( pwlaw_free_n0, xdata=cord(data1[1:Lh,0], L), ydata=data1[1:Lh,1], sigma=data1[1:Lh,2]) 
print(popt_1, pcov_1)
popt_2, pcov_2 = curve_fit( pwlaw_free_n0, xdata=cord(data2[1:Lh,0], L), ydata=data2[1:Lh,1], sigma=data2[1:Lh,2]) 
print(popt_2, pcov_2)
popt_5, pcov_5 = curve_fit( pwlaw_free_n0, xdata=cord(data5[1:Lh,0], L), ydata=data5[1:Lh,1], sigma=data5[1:Lh,2]) 
print(popt_5, pcov_5)
popt_10, pcov_10 = curve_fit( pwlaw_free_n0, xdata=cord(data10[1:Lh,0], L), ydata=data10[1:Lh,1], sigma=data10[1:Lh,2]) 
print(popt_10, pcov_10)

plt.figure()
plt.errorbar(cord(data1[1:Lh,0],L), data1[1:Lh,1], yerr = data1[1:Lh,2],    fmt = "cx",  label = r"$\beta=1$")
plt.plot(cord(data1[1:Lh,0],L), pwlaw_free_n0(cord(data1[1:Lh,0],L), *popt_1),      "c--", label =r"$n_0 = %1.3f$" % (popt_1[2])) 
plt.errorbar(cord(data2[1:Lh,0],L), data2[1:Lh,1], yerr = data2[1:Lh,2],    fmt = "bo",  label = r"$\beta=2$")
plt.plot(cord(data2[1:Lh,0],L), pwlaw_free_n0(cord(data2[1:Lh,0],L), *popt_2),      "b--", label =r"$n_0 = %1.3f$" % (popt_2[2])) 
plt.errorbar(cord(data5[1:Lh,0],L), data5[1:Lh,1], yerr = data5[1:Lh,2],    fmt = "rs",  label = r"$\beta=5$")
plt.plot(cord(data5[1:Lh,0],L), pwlaw_free_n0(cord(data5[1:Lh,0],L), *popt_5),      "r--", label =r"$n_0 = %1.3f$" % (popt_5[2])) 
plt.errorbar(cord(data10[1:Lh,0],L), data10[1:Lh,1], yerr = data10[1:Lh,2],    fmt = "gd",  label = r"$\beta=10$")
plt.plot(cord(data10[1:Lh,0],L), pwlaw_free_n0(cord(data10[1:Lh,0],L), *popt_10),      "g--", label =r"$n_0 = %1.3f$" % (popt_10[2])) 
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel(r"$\frac{L}{\pi} \sin(\frac{ \pi x}{L})$", fontdict=font1)
#plt.ylabel(r"$S^+S^-(x) + h.c. - n_0(\beta)$", fontdict=font1)
plt.ylabel(r"$S^+S^-(x) + {\rm h.c.}$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_pwlaw_spsm_cord_gs.pdf", format="pdf", bbox_inches="tight")
plt.show()


plt.figure()
plt.errorbar(cord(data1[1:Lh,0],L), data1[1:Lh,1] - popt_1[2], yerr = data1[1:Lh,2],    fmt = "cx",  label = r"$\beta=1$")
plt.plot(cord(data1[1:Lh,0],L), pwlaw_free_n0(cord(data1[1:Lh,0],L), *popt_1)- popt_1[2],      "c--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (popt_1[1], np.sqrt(pcov_1[1,1])))
plt.errorbar(cord(data2[1:Lh,0],L), data2[1:Lh,1] - popt_2[2], yerr = data2[1:Lh,2],    fmt = "bo",  label = r"$\beta=2$")
plt.plot(cord(data2[1:Lh,0],L), pwlaw_free_n0(cord(data2[1:Lh,0],L), *popt_2)- popt_2[2],      "b--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (popt_2[1], np.sqrt(pcov_2[1,1])))
plt.errorbar(cord(data5[1:Lh,0],L), data5[1:Lh,1] - popt_5[2], yerr = data5[1:Lh,2],    fmt = "rs",  label = r"$\beta=5$")
plt.plot(cord(data5[1:Lh,0],L), pwlaw_free_n0(cord(data5[1:Lh,0],L), *popt_5) - popt_5[2],      "r--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (popt_5[1], np.sqrt(pcov_5[1,1])))
plt.errorbar(cord(data10[1:Lh,0],L), data10[1:Lh,1] - popt_10[2], yerr = data10[1:Lh,2],    fmt = "gd",  label = r"$\beta=10$")
plt.plot(cord(data10[1:Lh,0],L), pwlaw_free_n0(cord(data10[1:Lh,0],L), *popt_10) - popt_10[2],      "g--", label = r"$\sim x^{-%1.2f(%1.2f)}$" % (popt_10[1], np.sqrt(pcov_10[1,1]))) 
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r"$\frac{L}{\pi} \sin(\frac{ \pi x}{L})$", fontdict=font1)
#plt.ylabel(r"$S^+S^-(x) + h.c. - n_0(\beta)$", fontdict=font1)
plt.ylabel(r"$S^+S^-(x) + {\rm h.c.} - m_{\perp}^2$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_pwlaw_spsm_cord_gs_log.pdf", format="pdf", bbox_inches="tight")
plt.show()

qopt_1, qcov_1 = curve_fit( pwlaw_free, xdata=cord(data1[1:Lh,0], L), ydata=np.abs(data1[1:Lh,3]), sigma=data1[1:Lh,4])
print(qopt_1, qcov_1)
qopt_2, qcov_2 = curve_fit( pwlaw_free, xdata=cord(data2[1:Lh,0], L), ydata=np.abs(data2[1:Lh,3]), sigma=data2[1:Lh,4])
print(qopt_2, qcov_2)
qopt_5, qcov_5 = curve_fit( pwlaw_free, xdata=cord(data5[1:Lh,0], L), ydata=np.abs(data5[1:Lh,3]), sigma=data5[1:Lh,4])
print(qopt_5, qcov_5)
qopt_10, qcov_10 = curve_fit( pwlaw_free, xdata=cord(data10[1:Lh,0], L), ydata=np.abs(data10[1:Lh,3]), sigma=data10[1:Lh,4])
print(qopt_10, qcov_10)

plt.figure()
plt.errorbar(cord(data1[1:Lh,0],L), np.abs(data1[1:Lh,3]), yerr = data1[1:Lh,4],    fmt = "cx",  label = r"$\beta=1$")
plt.plot(cord(data1[1:Lh,0],L), pwlaw_free(cord(data1[1:Lh,0],L), *qopt_1),      "c--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (qopt_1[1], np.sqrt(qcov_1[1,1])))
plt.errorbar(cord(data2[1:Lh,0],L), np.abs(data2[1:Lh,3]), yerr = data2[1:Lh,4],    fmt = "bo",  label = r"$\beta=2$")
plt.plot(cord(data2[1:Lh,0],L), pwlaw_free(cord(data2[1:Lh,0],L), *qopt_2),      "b--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (qopt_2[1], np.sqrt(qcov_2[1,1])))
plt.errorbar(cord(data5[1:Lh,0],L), np.abs(data5[1:Lh,3]), yerr = data5[1:Lh,4],    fmt = "rs",  label = r"$\beta=5$")
plt.plot(cord(data5[1:Lh,0],L), pwlaw_free(cord(data5[1:Lh,0],L), *qopt_5),      "r--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (qopt_5[1], np.sqrt(qcov_5[1,1])))
plt.errorbar(cord(data10[1:Lh,0],L), np.abs(data10[1:Lh,3]), yerr = data10[1:Lh,4],    fmt = "gd",  label = r"$\beta=10$")
plt.plot(cord(data10[1:Lh,0],L), pwlaw_free(cord(data10[1:Lh,0],L), *qopt_10),      "g--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (qopt_10[1], np.sqrt(qcov_10[1,1])))
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r"$\frac{L}{\pi} \sin(\frac{ \pi x}{L})$", fontdict=font1)
plt.ylabel(r"$\vert S^zS^z(x) \vert$", fontdict=font1)
plt.legend(loc="best", fontsize=16)
plt.savefig("fig_pwlaw_szsz_cord_gs_log.pdf", format="pdf", bbox_inches="tight")
plt.show()



# -----------------------------------------------
# SAME BUT THE LOG FIGURES COMBINED IN TWO PANELS
# -----------------------------------------------


fig = plt.figure()
gs = fig.add_gridspec(2, 1)
# spans two rows:
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])


ax1.errorbar(cord(data1[1:Lh,0],L), data1[1:Lh,1] - popt_1[2], yerr = data1[1:Lh,2],    fmt = "cx",  label = r"$\beta=1, p={%1.2f(%1.2f)}$"% (popt_1[1], np.sqrt(pcov_1[1,1])))
#ax1.plot(cord(data1[1:Lh,0],L), pwlaw_free_n0(cord(data1[1:Lh,0],L), *popt_1)- popt_1[2],      "c--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (popt_1[1], np.sqrt(pcov_1[1,1])))
ax1.plot(cord(data1[1:Lh,0],L), pwlaw_free_n0(cord(data1[1:Lh,0],L), *popt_1)- popt_1[2],      "c--")
ax1.errorbar(cord(data2[1:Lh,0],L), data2[1:Lh,1] - popt_2[2], yerr = data2[1:Lh,2],    fmt = "bo",  label = r"$\beta=2, p={%1.2f(%1.2f)}$"% (popt_2[1], np.sqrt(pcov_2[1,1])))
#ax1.plot(cord(data2[1:Lh,0],L), pwlaw_free_n0(cord(data2[1:Lh,0],L), *popt_2)- popt_2[2],      "b--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (popt_2[1], np.sqrt(pcov_2[1,1])))
ax1.plot(cord(data2[1:Lh,0],L), pwlaw_free_n0(cord(data2[1:Lh,0],L), *popt_2)- popt_2[2],      "b--")
ax1.errorbar(cord(data5[1:Lh,0],L), data5[1:Lh,1] - popt_5[2], yerr = data5[1:Lh,2],    fmt = "rs",  label = r"$\beta=5, p={%1.2f(%1.2f)}$"% (popt_5[1], np.sqrt(pcov_5[1,1])))
#ax1.plot(cord(data5[1:Lh,0],L), pwlaw_free_n0(cord(data5[1:Lh,0],L), *popt_5) - popt_5[2],      "r--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (popt_5[1], np.sqrt(pcov_5[1,1])))
ax1.plot(cord(data5[1:Lh,0],L), pwlaw_free_n0(cord(data5[1:Lh,0],L), *popt_5)- popt_5[2],      "r--")
ax1.set_xscale('log')
ax1.set_yscale('log')
#ax1.set_xlabel(r"$\frac{L}{\pi} \sin(\frac{ \pi x}{L})$", fontdict=font1)
#ax1.set_ylabel(r"$S^+S^-(x) + {\rm h.c.} - m_{\perp}^2$", fontdict=font1)
ax1.set_ylabel(r"$C^{+-}(x) - \left< m_{\perp}^2 \right>$", fontdict=font1)
ax1.legend(loc="best", fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.tick_params(axis='both', which='minor', labelsize=10)


ax2.errorbar(cord(data1[1:Lh,0],L), np.abs(data1[1:Lh,3]), yerr = data1[1:Lh,4],    fmt = "cx",  label = r"$\beta=1, q={%1.2f(%1.2f)}$"% (qopt_1[1], np.sqrt(qcov_1[1,1])))
#ax2.plot(cord(data1[1:Lh,0],L), pwlaw_free(cord(data1[1:Lh,0],L), *qopt_1),      "c--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (qopt_1[1], np.sqrt(qcov_1[1,1])))
ax2.plot(cord(data1[1:Lh,0],L), pwlaw_free(cord(data1[1:Lh,0],L), *qopt_1),      "c--")
ax2.errorbar(cord(data2[1:Lh,0],L), np.abs(data2[1:Lh,3]), yerr = data2[1:Lh,4],    fmt = "bo",  label = r"$\beta=2, q={%1.2f(%1.2f)}$"% (qopt_2[1], np.sqrt(qcov_2[1,1])))
#ax2.plot(cord(data2[1:Lh,0],L), pwlaw_free(cord(data2[1:Lh,0],L), *qopt_2),      "b--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (qopt_2[1], np.sqrt(qcov_2[1,1])))
ax2.plot(cord(data2[1:Lh,0],L), pwlaw_free(cord(data2[1:Lh,0],L), *qopt_2),      "b--")
ax2.errorbar(cord(data5[1:Lh,0],L), np.abs(data5[1:Lh,3]), yerr = data5[1:Lh,4],    fmt = "rs",  label = r"$\beta=5, q={%1.2f(%1.2f)}$"% (qopt_5[1], np.sqrt(qcov_5[1,1])))
#ax2.plot(cord(data5[1:Lh,0],L), pwlaw_free(cord(data5[1:Lh,0],L), *qopt_5),      "r--", label =r"$\sim x^{-%1.2f(%1.2f)}$" % (qopt_5[1], np.sqrt(qcov_5[1,1])))
ax2.plot(cord(data5[1:Lh,0],L), pwlaw_free(cord(data5[1:Lh,0],L), *qopt_5),      "r--")
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel(r"$\frac{L}{\pi} \sin(\frac{ \pi x}{L})$", fontdict=font1)
ax2.set_ylabel(r"$\vert C^{zz}(x) \vert$", fontdict=font1)
ax2.legend(loc="best", fontsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='minor', labelsize=10)
ax2.set_ylim([1e-5, 0.25])
#ax2.yaxis.set_label_position("right")
#ax2.yaxis.tick_right()
plt.savefig("fig_pwlaw_gs_combined_log.pdf", format="pdf", bbox_inches="tight")
plt.show()











