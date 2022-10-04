import matplotlib.pylab as plt
import numpy as np
from scipy import optimize


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



#figure 1
#requires "figure_1_top_data.txt" and "figure_1_bottom_data.txt" as data sources
#the strucutre for "figure_1_top_data.txt" is:
#each T/J has a section of 3 properties/arrays: r, C_perp, C_perp error
#the strucutre for "figure_1_bottom_data.txt" is:
#3 arrays: T/J, C_perp, C_perp error
#def plot_fig_1():

data_fig_1_top=np.loadtxt("figure_1_top_data.txt", comments='#')
temperatures_fig_1_top=["0.075", "0.1", "0.2", "0.5", "1.0"]

data_fig_1_bottom=np.loadtxt("figure_1_bottom_data.txt")

fig = plt.figure()
for i in range (len(temperatures_fig_1_top)):
  plt.errorbar(data_fig_1_top[3*i], data_fig_1_top[3*i+1],yerr=data_fig_1_top[3*i+2], marker='s', label='$T/J$= '+temperatures_fig_1_top[i])
plt.yscale('log')
plt.xlabel(r"$\mathbf{r}_x$", fontdict=font1)
plt.ylabel(r"$C_{\perp}(0,\mathbf{r}_{x})$", fontdict=font1)
plt.legend(loc="best", fontsize=14, frameon=False)
plt.savefig("fig1a.pdf",format="pdf", bbox_inches="tight")

fig = plt.figure()
plt.errorbar(data_fig_1_bottom[0],data_fig_1_bottom[1], yerr=data_fig_1_bottom[2], marker="s")
plt.xlabel(r"$T/J$", fontdict=font1)
plt.ylabel(r"$C_{\perp}(0,\frac{L_{x}}{2})$", fontdict=font1)
plt.savefig("fig1b.pdf",format="pdf", bbox_inches="tight")


#fig, ax =plt.subplots(2,1)
#for i in range (2,len(temperatures_fig_1_top)):
#  ax[0].errorbar(data_fig_1_top[3*i], data_fig_1_top[3*i+1],yerr=data_fig_1_top[3*i+2], marker='s', label='$T/J$= '+temperatures_fig_1_top[i])
#ax[0].set_yscale('log')
##ax[0].set(xlabel=r"$\mathbf{r}_x$", ylabel=r"$C_{\perp}(\mathbf{r}_{x}) = \langle \hat{S}^{+}_{\mathbf{r}_{x}} \hat{S}^{-}_{0} + h.c.\rangle$", fontdict = font1)
#ax[0].set_xlabel(r"$\mathbf{r}_x$", fontdict=font1) 
##ax[0].set_ylabel(r"$C_{\perp}(\mathbf{r}_{x}) = \langle \hat{S}^{+}_{\mathbf{r}_{x}} \hat{S}^{-}_{0} + h.c.\rangle$", fontdict=font1)
#ax[0].set_ylabel(r"$C_{\perp}(0,\mathbf{r}_{x})$", fontdict=font1)
#ax[0].legend(loc="best", fontsize=14, frameon=False)

#ax[1].errorbar(data_fig_1_bottom[0],data_fig_1_bottom[1], yerr=data_fig_1_bottom[2], marker="s")
#ax[1].set_xlabel(r"$T/J$", fontdict=font1)
##ax[1].set_ylabel(r"$C_{\perp}(\mathbf{r}_{1}-\mathbf{r}_{2} = \frac{L_{x}}{2})$", fontdict=font1)
#ax[1].set_ylabel(r"$C_{\perp}(0,\frac{L_{x}}{2})$", fontdict=font1)
##ax[1].legend(loc="best", fontsize=16)
#plt.savefig("fig1.pdf",format="pdf", bbox_inches="tight")
#plt.show()
