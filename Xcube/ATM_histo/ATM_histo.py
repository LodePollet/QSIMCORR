# -*- coding: utf-8 -*-
from decimal import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import glob
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#change font here
plt.rcParams.update({
                    "text.usetex": True,
                    "font.family": "sans-serif",
                    "font.sans-serif": ["Helvetica"]})

#change markers here: first is smallest lattice size
marker_list=['o',"s","v","^"]
#change colors here: first is smallest lattice size
colors=["tomato", "limegreen", "royalblue"]
#change markersize here
mark_size=3
#fontsizes
fontsize_legend=7
fontsize_axis=8

a=5
fig, ax = plt.subplots(1, 3)
sizes=[8,10,12]

annotations=["a","b","c","d","e","f"]

#disorder values
p_values=[0.040,0.06,0.075]
#reweighting parameters
indices_list=[[28,33,27],[30,30,30],[31,29,32]]
delta_k_list=[[0.005,0.003,0.003],[-0.002,0.004,0.00],[-0.028,-0.002,-0.004]]



#histogram specific observables
hist_obs_name=['Histo_E']
binsizes=[69,69,69]
binlenght=1./np.array(binsizes)
x_axis_size_dependend=[np.linspace(0.,1.,binnum) for binnum in binsizes]

#Upper row(Histograms)
for p_num,p in enumerate(p_values):
    indices=indices_list[p_num]
    p=p_values[p_num]
    delta_k=delta_k_list[p_num]
    #legend top row
    ax[p_num].plot([0],[0],color="w",label="$L$ \t ($T$)",linestyle='')
    for L_counter,L in enumerate(sizes):
        

        index=indices[L_counter]
        
        temp_axis=np.load("ATM/p=%0.03f/L%03d/Temperature_axis.npy"%(p,L))
        x_axis=np.load('ATM/p=%0.03f/one_pure_L%03d_%s_%s_hdf5.npy'%(p,L,hist_obs_name[0],index))
        y_values=np.load('ATM/p=%0.03f/two_pure_L%03d_%s_%s_hdf5.npy'%(p,L,hist_obs_name[0],index))

        
        y_values_old=y_values
        y_values_new=np.zeros(binsizes[L_counter])
        counter_overhead=0
        for i in np.arange(1,binsizes[L_counter]):
            counter_bin=0
            value_added=0
            while x_axis[counter_overhead+counter_bin]< x_axis_size_dependend[L_counter][i]:
                value_added+=y_values_old[counter_overhead+counter_bin]
                counter_bin+=1
            if i==binsizes[L_counter]-1:
                value_added+=y_values_old[counter_overhead+counter_bin]
                counter_bin+=1
            y_values_new[i]=value_added/counter_bin
            counter_overhead+=counter_bin
        
      
        
        
        norm2=np.sum(binlenght[L_counter]*y_values_new * np.exp(delta_k[L_counter]*(-3*L**2)* x_axis_size_dependend[L_counter]))
        
        
        ax[p_num].plot(x_axis_size_dependend[L_counter], y_values_new/norm2 * np.exp(delta_k[L_counter]*(-3*L**2)* x_axis_size_dependend[L_counter]) , linestyle="",marker=marker_list[L_counter],markersize=mark_size, label="$%2d$ ($%0.3f$)"%(L,temp_axis[index]+delta_k[L_counter]),color=colors[L_counter])
        
        
        
        y=y_values_new/norm2 * np.exp(delta_k[L_counter]*(-3*L**2)* x_axis_size_dependend[L_counter])
        x=x_axis_size_dependend[L_counter]
        #get the interpolation between points
        from scipy.interpolate import make_interp_spline, BSpline
        
        xnew = np.linspace(x_axis_size_dependend[L_counter].min(), x_axis_size_dependend[L_counter].max(), 300)
        spl = make_interp_spline(x_axis_size_dependend[L_counter], y_values_new/norm2 * np.exp(delta_k[L_counter]*(-3*L**2)* x_axis_size_dependend[L_counter]), k=3)
        power_smooth = spl(xnew)
        ax[p_num].plot(xnew, power_smooth,color=colors[L_counter])
    


    

    #change x and y range here
    ax[p_num].axis([-0.05,1.,0.,12.])
    ax[p_num].set_aspect(1.0/ax[p_num].get_data_ratio(), adjustable='box')

    ax[p_num].tick_params(axis ='both', which ='both',direction='in',labelsize=fontsize_axis)
    ax[p_num].xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.2))
    ax[p_num].xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    ax[p_num].yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(2.))
    ax[p_num].yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

    ax[p_num].text(0.78, 0.93,"$p=%0.3f$"%p,
         horizontalalignment='center',
         verticalalignment='center',
         transform = ax[p_num].transAxes,fontsize=fontsize_axis)

    if p_num==0:
        ax[p_num].set_ylabel(r"$P(E)$",fontsize=fontsize_axis)
    ax[p_num].set_xlabel(r"$-E$",fontsize=fontsize_axis)

    ax[p_num].text(0.1, 0.93,r"(%s)"%annotations[p_num],
         horizontalalignment='center',
         verticalalignment='center',
         transform = ax[p_num].transAxes,fontsize=fontsize_axis)
    #change location of the L above the legend here
    #ax[p_num].text(0.24, 0.315,r"$T$", horizontalalignment='center', verticalalignment='center', transform = ax[p_num].transAxes,fontsize=fontsize_legend)
    #change location of the legend here as bbox_to_anchor=...

    ax[p_num].legend(bbox_to_anchor=(-0.05,0.,0.1,0.5),loc="lower left",frameon=False,handletextpad=-0.4,labelspacing=0.1,fontsize=fontsize_legend)







fig.tight_layout(h_pad=-1.1)

fig.savefig("fig_P_B_ATM.pdf",format='pdf',bbox_inches='tight', dpi=300)
