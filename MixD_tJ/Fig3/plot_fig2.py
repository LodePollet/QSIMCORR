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
        'color':  'darkgreen',
        'weight': 'normal',
        'size': 16,
        }

def gs_latt_rho(x1, x2, N, L):
    k = np.arange(-N//2+1, N//2+1) * 2*np.pi/L
    return (np.sum(np.exp(1j*(x1-x2)*k)))/L


def gs_latt_dd(N,L):
    n = N/L
    x = np.arange(L)
    prop = np.array([gs_latt_rho(xx,0,N,L)*gs_latt_rho(0,xx,N,L) for xx in x])
    y = np.array([ -y + n**2 for i, y in enumerate(prop)])
    return x, y


system_size_x=30
data_fig_2=np.loadtxt("figure_2_data.txt", comments='#')
temperatures_fig_2=["0.2", "0.5", "1.0"]
nh_fig_2=["3", "4", "5", "6", "7", "8"]

fig, ax =plt.subplots(2,3, figsize=(15,10))
j=0 #stride for indexing the right data
for i in range(0,3):
  ax[0][0].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
#ax[0][0].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[0])
#ax[0][0].set_xlabel(r"$r$", fontdict=font1)
ax[0][0].set_ylabel(r"$\rho_{hh}(r)$", fontdict=font1)
ax[0][0].set_title(r"$N_{h}$="+nh_fig_2[0])
x,y=gs_latt_dd(int(nh_fig_2[0]), system_size_x)
ax[0][0].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
ax[0][0].legend(loc="best", fontsize=14, frameon=False)

j=9
for i in range(0,3):
  ax[0][1].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
#ax[0][1].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[1])
#ax[0][1].set_xlabel(r"$r$", fontdict=font1)
#ax[0][1].set_ylabel(r"$\rho_{hh}(r)$", fontdict=font1)
x,y=gs_latt_dd(int(nh_fig_2[1]), system_size_x)
ax[0][1].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
ax[0][1].set_title(r"$N_{h}$="+nh_fig_2[1])
#ax[0][1].legend(loc="best", fontsize=16)

j=18
for i in range(0,3):
  ax[0][2].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
#ax[0][2].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[2])
#ax[0][2].set_xlabel(r"$r$", fontdict=font1)
#ax[0][2].set_ylabel(r"$\rho_{hh}(r)$", fontdict=font1)
x,y=gs_latt_dd(int(nh_fig_2[2]), system_size_x)
ax[0][2].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
#ax[0][2].legend(loc="best", fontsize=16)
ax[0][2].set_title(r"$N_{h}$="+nh_fig_2[2])
ax[0][2].set_ylim([0.015, 0.03])

j=27
for i in range(0,3):
  ax[1][0].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
#ax[1][0].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[3])
ax[1][0].set_xlabel(r"$r$", fontdict=font1)
ax[1][0].set_ylabel(r"$\rho_{hh}(r)$", fontdict=font1)
x,y=gs_latt_dd(int(nh_fig_2[3]), system_size_x)
ax[1][0].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
#ax[1][0].legend(loc="best", fontsize=16)
ax[1][0].set_title(r"$N_{h}$="+nh_fig_2[3])
ax[1][0].set_ylim([0.0275, 0.0425])

j=36
for i in range(0,3):
  ax[1][1].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
#ax[1][1].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[4])
ax[1][1].set_xlabel(r"$r$", fontdict=font1)
#ax[1][1].set_ylabel(r"$\rho_{hh}(r)$", fontdict=font1)
x,y=gs_latt_dd(int(nh_fig_2[4]), system_size_x)
ax[1][1].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
#ax[1][1].legend(loc="best", fontsize=16)
ax[1][1].set_title(r"$N_{h}$="+nh_fig_2[4])
ax[1][1].set_ylim([0.04, 0.0575])

j=45
for i in range(0,3):
  ax[1][2].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
#ax[1][2].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[5])
ax[1][2].set_xlabel(r"$r$", fontdict=font1)
#ax[1][2].set_ylabel(r"$\rho_{hh}(r)$", fontdict=font1)
x,y=gs_latt_dd(int(nh_fig_2[5]), system_size_x)
ax[1][2].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
#ax[1][2].legend(loc="best", fontsize=16)
ax[1][2].set_ylim([0.062, 0.073])
ax[1][2].set_title(r"$N_{h}$="+nh_fig_2[5])

plt.savefig("fig2.pdf", format="pdf", bbox_inches="tight")
plt.show()
