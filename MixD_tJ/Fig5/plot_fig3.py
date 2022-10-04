import numpy as np
import matplotlib.pylab as plt
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
    #fig, ax =plt.subplots(2,1)
    fig = plt.figure()
    for i in range(0,nh_max+1):
        #ax[0].errorbar(data_fig_3_top[i][0],data_fig_3_top[i][1],yerr=data_fig_3_top[i][2],fmt="s",label=f'$n_h={i}$', color=colors[i])
        plt.errorbar(data_fig_3_top[i][0],data_fig_3_top[i][1],yerr=data_fig_3_top[i][2],fmt="s",label=f'$n_h={i}$', color=colors[i])
        param_fit1, param_fit2 = optimize.curve_fit(exp_func,data_fig_3_top[i][0],data_fig_3_top[i][1],sigma=data_fig_3_top[i][2], absolute_sigma=True, p0=[250,0.3,data_fig_3_top[i][1][-1]])
        p_err=np.sqrt(np.diag(param_fit2))
        #ax[0].plot(data_fig_3_top[i][0],exp_func(data_fig_3_top[i][0],param_fit1[0],param_fit1[1],param_fit1[2]), color=colors[i])
        plt.plot(data_fig_3_top[i][0],exp_func(data_fig_3_top[i][0],param_fit1[0],param_fit1[1],param_fit1[2]), color=colors[i])
    #ax[0].legend(loc='best',ncol=2, fontsize=16)
    #ax[0].set_xlabel(r"$\beta$", fontdict=font1)
    plt.xlabel(r"$\beta t$", fontdict=font1)
    #ax[0].set_ylabel(r"$E$", fontdict=font1)
    plt.ylabel(r"$E/t$", fontdict=font1)
    plt.savefig("fig3a.pdf", format="pdf", bbox_inches="tight")
   
    fig = plt.figure() 
    density_holes=np.arange(1,nh_max+1)/system_size_x
    e_h=[]
    e_h_error=[]
    for i in range (1, nh_max+1):
        e_h.append((data_fig_3_bottom[2*i][2]-data_fig_3_bottom[0][2])/(i*system_size_y))
        e_h_error.append(np.sqrt((data_fig_3_bottom[1][2])**2+(data_fig_3_bottom[2*i+1][2])**2)/(i*system_size_y))
    #ax[1].errorbar(density_holes,e_h, yerr=e_h_error,marker="s",label=r"$\beta \rightarrow \infty$")
    #plt.errorbar(density_holes,e_h, yerr=e_h_error,marker="s",label=r"$\beta \rightarrow \infty$")
    plt.errorbar(density_holes[::2],e_h[::2], yerr=e_h_error[1::2],  marker="s",label="odd hole number")
    plt.errorbar(density_holes[1::2],e_h[1::2], yerr=e_h_error[1::2],marker="s",label="even hole number")
    xmin = np.linspace(0.12, 0.15, 6)
    plt.plot(xmin ,-0.9786073879166669 * np.ones_like(xmin), 'k--')
    print(density_holes, e_h)
    #ax[1].set_xlabel(r"$n_h$", fontdict=font1)
    plt.xlabel(r"$n_h$", fontdict=font1)
    #ax[1].set_ylabel(r"$\epsilon (h)$", fontdict=font1)
    plt.ylabel(r"$\epsilon (h)$/t", fontdict=font1)
    #ax[1].legend(loc="best", fontsize=16)
    plt.legend(loc="best", fontsize=16)
    plt.savefig("fig3b.pdf", format="pdf")
    #plt.show()


plot_fig_3()
