# script to generate figures for the paper
# each figure has its own function, function calls are at the end of the script

import matplotlib
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


#figure 1
#requires "figure_1_top_data.txt" and "figure_1_bottom_data.txt" as data sources
#the strucutre for "figure_1_top_data.txt" is:
#each T/J has a section of 3 properties/arrays: r, C_perp, C_perp error
#the strucutre for "figure_1_bottom_data.txt" is:
#3 arrays: T/J, C_perp, C_perp error
def plot_fig_1():
    data_fig_1_top=np.loadtxt("figure_1_top_data.txt", comments='#')
    temperatures_fig_1_top=["0.075", "0.1", "0.2", "0.5", "1.0"]

    data_fig_1_bottom=np.loadtxt("figure_1_bottom_data.txt")

    fig, ax =plt.subplots(2,1)
    for i in range (len(temperatures_fig_1_top)):
        ax[0].errorbar(data_fig_1_top[3*i], data_fig_1_top[3*i+1],yerr=data_fig_1_top[3*i+2], marker='s', label='$T/J$= '+temperatures_fig_1_top[i])
    ax[0].set_yscale('log')
    ax[0].set(xlabel=r"$\boldsymbol{r}_x$", ylabel=r"$C_{\perp}(\boldsymbol{r}_{x}) = \langle \hat{S}^{+}_{\boldsymbol{r}_{x}} \hat{S}^{-}_{0} + h.c.\rangle$")
    ax[0].legend()

    ax[1].errorbar(data_fig_1_bottom[0],data_fig_1_bottom[1], yerr=data_fig_1_bottom[2], marker="s")
    ax[1].set(xlabel=r"$T/J$", ylabel=r"$C_{\perp}(\boldsymbol{r}_{1}-\boldsymbol{r}_{2} = \frac{L_{x}}{2})$")
    #plt.savefig("fig1.pdf",format="pdf", bbox_inches="tight")
    plt.show()


#figure 2
#requires "figure_2_data.txt" as data source
#the strucutre for "figure_2_data.txt" is:
#section of n_h and T/J combinations (n_h outer loop, T/J inner loop)
#each section has 3 arrays: r, rho, rho error
def gs_latt_rho(x1, x2, N, L):
    k = np.arange(-N//2+1, N//2+1) * 2*np.pi/L
    return (np.sum(np.exp(1j*(x1-x2)*k)))/L


def gs_latt_dd(N,L):
    n = N/L
    x = np.arange(L)
    prop = np.array([gs_latt_rho(xx,0,N,L)*gs_latt_rho(0,xx,N,L) for xx in x])
    y = np.array([ -y + n**2 for i, y in enumerate(prop)])
    return x, y


def plot_fig_2():
    system_size_x=30
    data_fig_2=np.loadtxt("figure_2_data.txt", comments='#')
    temperatures_fig_2=["0.2", "0.5", "1.0"]
    nh_fig_2=["3", "4", "5", "6", "7", "8"]

    fig, ax =plt.subplots(2,3)
    j=0 #stride for indexing the right data
    for i in range(0,3):
        ax[0][0].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
    ax[0][0].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[0])
    x,y=gs_latt_dd(int(nh_fig_2[0]), system_size_x)
    ax[0][0].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
    ax[0][0].legend()

    j=9
    for i in range(0,3):
        ax[0][1].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
    ax[0][1].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[1])
    x,y=gs_latt_dd(int(nh_fig_2[1]), system_size_x)
    ax[0][1].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
    ax[0][1].legend()

    j=18
    for i in range(0,3):
        ax[0][2].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
    ax[0][2].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[2])
    x,y=gs_latt_dd(int(nh_fig_2[2]), system_size_x)
    ax[0][2].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
    ax[0][2].legend()
    ax[0][2].set_ylim([0.015, 0.03])

    j=27
    for i in range(0,3):
        ax[1][0].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
    ax[1][0].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[3])
    x,y=gs_latt_dd(int(nh_fig_2[3]), system_size_x)
    ax[1][0].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
    ax[1][0].legend()
    ax[1][0].set_ylim([0.0275, 0.0425])

    j=36
    for i in range(0,3):
        ax[1][1].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
    ax[1][1].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[4])
    x,y=gs_latt_dd(int(nh_fig_2[4]), system_size_x)
    ax[1][1].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
    ax[1][1].legend()
    ax[1][1].set_ylim([0.04, 0.0575])

    j=45
    for i in range(0,3):
        ax[1][2].errorbar(data_fig_2[j+0+3*i], data_fig_2[j+1+3*i],yerr=data_fig_2[j+2+3*i], marker='s', label='$T/J$= '+temperatures_fig_2[i])
    ax[1][2].set(xlabel=r"$r$", ylabel=r"$\rho_{hh}(r)$", title=r"$N_{h}$="+nh_fig_2[5])
    x,y=gs_latt_dd(int(nh_fig_2[5]), system_size_x)
    ax[1][2].plot(x,y.real, label='T=0, finite box', color='black', linestyle='dashed')
    ax[1][2].legend()
    ax[1][2].set_ylim([0.062, 0.073])

    plt.show()



#figure 3
#requires "figure_3_data.txt" and "figure_3_fit.txt" as data sources
#the strucutre for "figure_3_data.txt" is:
#sections of n_h
#each section has 3 arrays: beta, E, E error
#the strucutre for "figure_3_fit.txt" is:
#sections of n_h
#each section has 2 arrays: fit parameters, fit parameters error
#with the fit parameters in the order of a,b,c for a*np.exp(-b*x) + c
def exp_func(x,a,b,c):
    return a*np.exp(-b*x) + c

def plot_fig_3():
    system_size_x=30
    system_size_y=30
    nh_max=8
    data_fig_3_top=[]
    for i in range(0,nh_max+1):
        data_fig_3_top.append(np.loadtxt("figure_3_data.txt", comments='#', skiprows=5*i, max_rows=3))

    data_fig_3_bottom=np.loadtxt("figure_3_fit.txt", comments='#')
    
    colors=["tab:blue","tab:orange","tab:red","tab:purple","tab:green","tab:pink","tab:gray","tab:olive","tab:cyan"]
    fig, ax =plt.subplots(2,1)
    for i in range(0,nh_max+1):
        ax[0].errorbar(data_fig_3_top[i][0],data_fig_3_top[i][1],yerr=data_fig_3_top[i][2],fmt="s",label=f'$n_h={i}$', color=colors[i])
        param_fit1, param_fit2 = optimize.curve_fit(exp_func,data_fig_3_top[i][0],data_fig_3_top[i][1],sigma=data_fig_3_top[i][2], absolute_sigma=True, p0=[250,0.3,data_fig_3_top[i][1][-1]])
        p_err=np.sqrt(np.diag(param_fit2))
        ax[0].plot(data_fig_3_top[i][0],exp_func(data_fig_3_top[i][0],param_fit1[0],param_fit1[1],param_fit1[2]), color=colors[i])
    ax[0].legend(loc='best',ncol=2)
    ax[0].set(xlabel=r"$\beta$", ylabel=r"$E$")
    
    density_holes=np.arange(1,nh_max+1)/system_size_x
    e_h=[]
    e_h_error=[]
    for i in range (1, nh_max+1):
        e_h.append((data_fig_3_bottom[2*i][2]-data_fig_3_bottom[0][2])/(i*system_size_y))
        e_h_error.append(np.sqrt((data_fig_3_bottom[1][2])**2+(data_fig_3_bottom[2*i+1][2])**2)/(i*system_size_y))
    ax[1].errorbar(density_holes,e_h, yerr=e_h_error,marker="s",label=r"$\beta \rightarrow \infty$")
    ax[1].set(xlabel=r"$n_h$", ylabel=r"$\epsilon (h)$")
    ax[1].legend()

    plt.show()


plot_fig_1()
plot_fig_2()
plot_fig_3()
