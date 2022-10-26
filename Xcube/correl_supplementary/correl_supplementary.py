# -*- coding: utf-8 -*-
from decimal import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import math
import cmath
from scipy.signal import argrelextrema
from scipy.optimize import curve_fit
#change font here
plt.rcParams.update({
                    "text.usetex": True,
                    "font.family": "sans-serif",
                    "font.sans-serif": ["Helvetica"]})

#change markers here: first is smallest lattice size
marker_list=["^",'o',"s","v"]
#change colors here: first is smallest lattice size
colors=["firebrick", "darkorange", "limegreen", "mediumslateblue"]
#change markersize here
mark_size=3
#fontsizes
fontsize_legend=7
fontsize_axis=8

fig, ax = plt.subplots(2, 3)
sizes=[6,8,10,12]

annotations=["d","e","f", "a","b","c"]

#disorder values
p_values=[0.073,0.075,0.078]

#change x range here as beta-/+ (p_plus is for lower T bound) value from the critical point
#critical point is given in beta as beta_guess
beta_guess=[1,1,1]
p_plus=[0.3,0.3,0.3]
p_minus=[0.2,0.2,0.2]
#change shaded regime, if changed here we need to change it in the phase diagram!
#temp_plus_shade=[1.02,0.98,0.98]
#temp_minus_shade=[0.9,0.78,0.98]

spacing_x_major=[0.1,0.1,0.1]
spacing_y_major=[0.1,0.1,0.1]

#lower row(Binder)
savename="Binder/p=%0.3f/L%03d_p%2.3f_%s.npy"

for p_num,p in enumerate(p_values):
    #legend top row
    #ax[1,p_num].plot(beta_guess[p_num],[0.4],color="w",label="$L$",linestyle='')
    for L_counter,L in enumerate(sizes):
        k_min=2.*cmath.pi/L
        #print k_min
        prefactor=1./(2*math.sin(k_min/2.))
        alternative_prefactor=L/(2*cmath.pi)
        
        correl_fct_simple_boot=np.load('data_atm/boots_correl_fct_overL_simple_p=%0.3f_L=%2d.npy'%(p,L))/prefactor*alternative_prefactor
        correl_fct_simple_boot_err=np.load('data_atm/boots_correl_fct_overL_simple_err_p=%0.3f_L=%2d.npy'%(p,L))/prefactor*alternative_prefactor
        
        x_axis=np.load('data_atm/boots_Temperature_p=%.3f_L=%2d.npy'%(p,L))
        beta=1./np.load('data_atm/boots_Temperature_p=%.3f_L=%2d.npy'%(p,L))
        
        cross_end=np.searchsorted(1./beta,1./(beta_guess[p_num]-p_minus[p_num]))
        cross_start=np.searchsorted(1./beta,1./(beta_guess[p_num]+p_plus[p_num]))
        shade_bottom_value=correl_fct_simple_boot[cross_start]
        shade_top_value=correl_fct_simple_boot[cross_end]
        
        
        ax[1,p_num].errorbar(x_axis[cross_start:cross_end],correl_fct_simple_boot[cross_start:cross_end], yerr=correl_fct_simple_boot_err[cross_start:cross_end],capsize=2,color=colors[L_counter],marker=marker_list[L_counter], markersize=mark_size)
        ax[1,p_num].plot(x_axis[cross_start:cross_end],correl_fct_simple_boot[cross_start:cross_end] ,linestyle='',color=colors[L_counter],marker=marker_list[L_counter], markersize=mark_size,label="$L=%2d$"%L)
    

    #change y range here
    bottom, top = ax[1,p_num].get_ylim()
    #ax[1,p_num].set_ylim([bottom,top+(top-bottom)/8.])
    ax[1,p_num].set_ylim([0.15,0.68])
    #boxformat
    ax[1,p_num].set_aspect(1.0/ax[1,p_num].get_data_ratio(), adjustable='box')
    #change here if you want the shaded regime remove """ on top and bottom
    """#shaded regime
    if temp_plus_shade[p_num]-temp_minus_shade[p_num]!=0:
        #shading of the p_c area
        x = np.linspace(temp_minus_shade[p_num],temp_plus_shade[p_num],10)
        y = np.linspace(ax[1,p_num].get_ylim()[0],ax[1,p_num].get_ylim()[1],10)
        z = [[-z] * 10 for z in range(10)]
        num_bars = 1000  # more bars = smoother gradient
        ax[1,p_num].contourf(x, y, z, num_bars,cmap=plt.cm.Wistia)
    """
    ax[1,p_num].tick_params(axis ='both', which ='both',direction='in',labelsize=fontsize_axis)
    ax[1,p_num].xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(spacing_x_major[p_num]))
    ax[1,p_num].xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    ax[1,p_num].yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(spacing_y_major[p_num]))
    ax[1,p_num].yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    
    
    ax[1,p_num].text(0.68, 0.9,"RACAT\n$p=%0.3f$"%p,
                     horizontalalignment='left',
                     verticalalignment='center',
                     transform = ax[1,p_num].transAxes,fontsize=fontsize_axis)

    if p_num==0:
        ax[1,p_num].set_ylabel(r"$\xi_L/L$",fontsize=fontsize_axis)
    ax[1,p_num].set_xlabel(r"$T$",fontsize=fontsize_axis)

    ax[1,p_num].text(0.1, 0.93,r"(%s)"%annotations[p_num],
                     horizontalalignment='center',
                     verticalalignment='center',
                     transform = ax[1,p_num].transAxes,fontsize=fontsize_axis)
    #change location of the L above the legend here
    """
    ax[1,p_num].text(0.18, 0.42,r"$L$",
                 horizontalalignment='center',
                 verticalalignment='center',
                 transform = ax[1,p_num].transAxes)"""
    #change location of the legend here as bbox_to_anchor=...
    ax[1,p_num].legend(bbox_to_anchor=(-0, -0.,0.1,0.5),loc="lower left",frameon=False,handletextpad=0,labelspacing=0.1,fontsize=fontsize_legend)

### RPI
sizes=[4,6,8,10]

spacing_x_major=[0.2,0.2,0.4]
spacing_y_major=[0.4,0.4,0.4]

#disorder values
p_values=[0.148,0.152,0.156]
#change x range here as beta-/+ (p_plus is for lower T bound) value from the critical point
#critical point is given in beta as beta_guess
p_plus=[0.29,0.4,0.7]#do 0.8 instead of 0.4 for low T in p=0.156
p_minus=[0.1,0.08,0.1]
#change shaded regime, if changed here we need to change it in the phase diagram!
#temp_plus_shade=[1.87,1.78,1.5]
#temp_minus_shade=[1.73,1.66,1.5]
#beta_guess=[1./np.array((temp_plus_shade[i]+temp_minus_shade[i])/2) for i in range(len(temp_plus_shade))]
beta_guess=[0.55,0.55,0.55]
#change y axis here first entry is smallest p value
bottom_y=[0.2,0.2,0.2]
top_y=[2.45,2.05,1.85]

#upper row
savename="Binder/p=%0.3f/L%03d_p%2.3f_%s.npy"

for p_num,p in enumerate(p_values):
    #legend top row
    #ax[0,p_num].plot(1./beta_guess[p_num],[1.],color="w",label="$L$",linestyle='')
    for L_counter,L in enumerate(sizes):
        k_min=2.*cmath.pi/L
        #print k_min
        prefactor=1./(2*math.sin(k_min/2.))
        alternative_prefactor=L/(2*cmath.pi)
        
        correl_fct_simple_boot=np.load('data_pim/boots_correl_fct_overL_simple_p=%0.3f_L=%2d.npy'%(p,L))/prefactor*alternative_prefactor
        correl_fct_simple_boot_err=np.load('data_pim/boots_correl_fct_overL_simple_err_p=%0.3f_L=%2d.npy'%(p,L))/prefactor*alternative_prefactor
        
        x_axis=np.load('data_pim/boots_Temperature_p=%.3f_L=%2d.npy'%(p,L))
        beta=1./np.load('data_pim/boots_Temperature_p=%.3f_L=%2d.npy'%(p,L))
        
        cross_end=np.searchsorted(1./beta,1./(beta_guess[p_num]-p_minus[p_num]))
        cross_start=np.searchsorted(1./beta,1./(beta_guess[p_num]+p_plus[p_num]))
        shade_bottom_value=correl_fct_simple_boot[cross_start]
        shade_top_value=correl_fct_simple_boot[cross_end]
        
        
        ax[0,p_num].errorbar(x_axis[cross_start:cross_end],correl_fct_simple_boot[cross_start:cross_end], yerr=correl_fct_simple_boot_err[cross_start:cross_end],capsize=2,color=colors[L_counter],marker=marker_list[L_counter], markersize=mark_size)
        ax[0,p_num].plot(x_axis[cross_start:cross_end],correl_fct_simple_boot[cross_start:cross_end] ,linestyle='',color=colors[L_counter],marker=marker_list[L_counter], markersize=mark_size,label="$L=%2d$"%L)


    #change y range here
    bottom, top = ax[0,p_num].get_ylim()
    #ax[0,p_num].set_ylim([bottom,top+(top-bottom)/8.])
    #old version
    #ax[0,p_num].set_ylim([0.2,2.45])
    ax[0,p_num].set_ylim([bottom_y[p_num],top_y[p_num]])
    #boxformat
    ax[0,p_num].set_aspect(1.0/ax[0,p_num].get_data_ratio(), adjustable='box')
    #change here if you want the shaded regime remove """ on top and bottom
    """
        if temp_plus_shade[p_num]-temp_minus_shade[p_num]!=0:
        #shading of the p_c area
        x = np.linspace(temp_minus_shade[p_num],temp_plus_shade[p_num],10)
        y = np.linspace(ax[0,p_num].get_ylim()[0],ax[0,p_num].get_ylim()[1],10)
        z = [[-z] * 10 for z in range(10)]
        num_bars = 1000  # more bars = smoother gradient
        ax[0,p_num].contourf(x, y, z, num_bars,cmap=plt.cm.Wistia)
        """
    ax[0,p_num].tick_params(axis ='both', which ='both',direction='in',labelsize=fontsize_axis)
    ax[0,p_num].xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(spacing_x_major[p_num]))
    ax[0,p_num].xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    ax[0,p_num].yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(spacing_y_major[p_num]))
    ax[0,p_num].yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

    ax[0,p_num].text(0.68, 0.9,"RPI\n $p=%0.3f$"%p,
                   horizontalalignment='left',
                   verticalalignment='center',
                   transform = ax[0,p_num].transAxes,fontsize=fontsize_axis)
    
    if p_num==0:
        ax[0,p_num].set_ylabel(r"$\xi_L/L$",fontsize=fontsize_axis)
    ax[0,p_num].set_xlabel(r"$T$")

    ax[0,p_num].text(0.1, 0.93,r"(%s)"%annotations[3+p_num],
               horizontalalignment='center',
               verticalalignment='center',
               transform = ax[0,p_num].transAxes,fontsize=fontsize_axis)
    #change location of the L above the legend here
    """
    ax[0,p_num].text(0.18, 0.42,r"$L$",
               horizontalalignment='center',
               verticalalignment='center',
               transform = ax[0,p_num].transAxes)"""
    #change location of the legend here as bbox_to_anchor=...
    ax[0,p_num].legend(bbox_to_anchor=(-0, -0.0,0.1,0.5),loc="lower left",frameon=False,handletextpad=-0.,labelspacing=0.1,fontsize=fontsize_legend)



fig.tight_layout(h_pad=-1.1)

fig.savefig("fig_xi_all.pdf",format='pdf',bbox_inches='tight', dpi=300)
