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
colors=["green","black", "blue", "orange"]
#change markersize here
mark_size=3
fontsize_axis=11
fontsize_legend=11
#change total figuresize here
a=4
fig, (PIM,ATM) = plt.subplots(1, 2,figsize=(a*1.62,a*2.28))

sizes=[4,6,8,10]

colorscheme=plt.cm.Wistia

#include 4
disorders=[0.148]
#change x range here as beta-/+ (p_plus is for lower T bound) value from the critical point
#critical point is given in beta as beta_guess
p_plus=[0.12]
p_minus=[0.1]
#shaded regime if changed here needs to be changed in the other plots and phase diagram aswell
temp_plus_shade=[1.78]
temp_minus_shade=[1.66]
beta_guess=[1./np.array((temp_plus_shade[i]+temp_minus_shade[i])/2) for i in range(len(temp_plus_shade))]


p_counter=0

for p in disorders:
    for L_counter,L in enumerate(sizes):
        k_min=2.*cmath.pi/L
        #print k_min
        prefactor=1./(2*math.sin(k_min/2.))
        alternative_prefactor=L/(2*cmath.pi)
        correl_fct_simple_boot=np.load('PIM/boots_correl_fct_overL_simple_p=%0.3f_L=%2d.npy'%(p,L))/prefactor*alternative_prefactor
        correl_fct_simple_boot_err=np.load('PIM/boots_correl_fct_overL_simple_err_p=%0.3f_L=%2d.npy'%(p,L))/prefactor*alternative_prefactor
        
        x_axis=np.load('PIM/boots_Temperature_p=%.3f_L=%2d.npy'%(p,L))
        beta=1./np.load('PIM/boots_Temperature_p=%.3f_L=%2d.npy'%(p,L))

        cross_end=np.searchsorted(1./beta,1./(beta_guess[p_counter]-p_minus[p_counter]))
        cross_start=np.searchsorted(1./beta,1./(beta_guess[p_counter]+p_plus[p_counter]))
        shade_bottom_value=correl_fct_simple_boot[cross_start]
        shade_top_value=correl_fct_simple_boot[cross_end]
        
            
        PIM.errorbar(x_axis[cross_start:cross_end],correl_fct_simple_boot[cross_start:cross_end],yerr=correl_fct_simple_boot_err[cross_start:cross_end],capsize=2,linestyle="dotted",marker=marker_list[L_counter], markersize=4,color=colors[L_counter])
        PIM.plot(x_axis[cross_start:cross_end],correl_fct_simple_boot[cross_start:cross_end], linestyle='',marker=marker_list[L_counter], markersize=4,label="%d"%L,color=colors[L_counter])
    
    
    PIM.tick_params(axis ='both', which ='both',direction='in',labelsize=fontsize_axis)
    PIM.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.1))

    PIM.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    PIM.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())


    

    #change x and y limit here manually if wished
    #plt.xlim([1.3,2.25])
    #PIM.ylim([0,correl_fct_simple_boot[cross_start]+0.2])
    PIM.set_aspect(1.0/PIM.get_data_ratio(), adjustable='box')
    #plt.annotate("PIM $p^X=%0.3f$"%p,[temp_plus_shade[p_counter]+0.01*temp_plus_shade[p_counter],correl_fct_simple_boot[cross_start]-0.2])

    PIM.text(0.74, 0.9,"RPI\n $p=%0.3f$"%p,
             horizontalalignment='left',
             verticalalignment='center',
             transform = PIM.transAxes,fontsize=fontsize_axis)


    PIM.text(0.24, 0.42,r"$L$",
               horizontalalignment='center',
               verticalalignment='center',
               transform = PIM.transAxes,fontsize=fontsize_axis)
    PIM.set_xlabel(r"$T$")
    PIM.set_ylabel(r"$\xi_L/L$")
    PIM.text(0.15, 0.95,"(a)",
         horizontalalignment='center',
         verticalalignment='center',
         transform = PIM.transAxes,fontsize=fontsize_legend)

    #shading of the p_c area
    x = np.linspace(temp_minus_shade,temp_plus_shade,10)
    y = np.linspace(PIM.get_ylim()[0],PIM.get_ylim()[1],10)
    z = [[-z] * 10 for z in range(10)]
    num_bars = 1000  # more bars = smoother gradient
    #change colormap for shaded area here as cmap=...
    PIM.contourf(x, y, z, num_bars,cmap=colorscheme)
    #change location of the legend here as loc=...
    PIM.legend(loc='lower left',frameon=False,fontsize=fontsize_legend)
    p_counter+=1

####ATM
sizes=[6,8,10,12]

disorders=[0.073]
#change x range here as beta-/+ (p_plus is for lower T bound) value from the critical point
#critical point is given in beta as beta_guess
beta_guess=[1.02]
p_plus=[0.14*3.]
p_minus=[0.1*1.8]
temp_plus_shade=[1.06]
temp_minus_shade=[0.92]

####ATM
p_counter=0
for p in disorders:
    for L_counter,L in enumerate(sizes):
        k_min=2.*cmath.pi/L
        #print k_min
        prefactor=1./(2*math.sin(k_min/2.))
        alternative_prefactor=L/(2*cmath.pi)
        correl_fct_simple_boot=np.load('ATM/boots_correl_fct_overL_simple_p=%0.3f_L=%2d.npy'%(p,L))/prefactor*alternative_prefactor
        correl_fct_simple_boot_err=np.load('ATM/boots_correl_fct_overL_simple_err_p=%0.3f_L=%2d.npy'%(p,L))/prefactor*alternative_prefactor
        
        x_axis=np.load('ATM/boots_Temperature_p=%.3f_L=%2d.npy'%(p,L))
        beta=1./np.load('ATM/boots_Temperature_p=%.3f_L=%2d.npy'%(p,L))
        
        cross_end=np.searchsorted(1./beta,1./(beta_guess[p_counter]-p_minus[p_counter]))
        cross_start=np.searchsorted(1./beta,1./(beta_guess[p_counter]+p_plus[p_counter]))
        shade_bottom_value=correl_fct_simple_boot[cross_start]
        shade_top_value=correl_fct_simple_boot[cross_end]
        
        
        
        ATM.errorbar(x_axis[cross_start:cross_end],correl_fct_simple_boot[cross_start:cross_end], yerr=correl_fct_simple_boot_err[cross_start:cross_end],capsize=2,linestyle="dotted",marker=marker_list[L_counter], markersize=4,color=colors[L_counter])
        ATM.plot(x_axis[cross_start:cross_end],correl_fct_simple_boot[cross_start:cross_end],linestyle="",marker=marker_list[L_counter], markersize=4,label="%d"%L,color=colors[L_counter])


    ATM.tick_params(axis ='both', which ='both',direction='in',labelsize=fontsize_axis)
    ATM.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.1))
    ATM.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    ATM.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(.05))
    ATM.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())



    #ATM.fill_between([temp_plus_shade[p_counter],temp_minus_shade[p_counter]],shade_bottom_value,shade_top_value,color='yellow', alpha=0.9)




    ATM.axis([0.69,1.21,0.18,0.66])
    ATM.set_aspect(1.0/ATM.get_data_ratio(), adjustable='box')
    ATM.text(0.24, 0.42,r"$L$",
         horizontalalignment='center',
         verticalalignment='center',
         transform = ATM.transAxes,fontsize=fontsize_axis)
    ATM.set_xlabel(r"$T$")
    #remove the "#" before the next line to add y label
    #ATM.set_ylabel(r"$\xi_L/L$")

    ATM.text(0.74, 0.9,"RACAT\n $p=%0.3f$"%p,
         horizontalalignment='left',
         verticalalignment='center',
         transform = ATM.transAxes,fontsize=fontsize_axis)
    ATM.text(0.15, 0.95,"(b)",
         horizontalalignment='center',
         verticalalignment='center',
         transform = ATM.transAxes,fontsize=fontsize_legend)
    #shading of the p_c area
    x = np.linspace(temp_minus_shade,temp_plus_shade,10)
    y = np.linspace(ATM.get_ylim()[0],ATM.get_ylim()[1],10)
    z = [[-z] * 10 for z in range(10)]
    num_bars = 1000  # more bars = smoother gradient
    #change colormap for shaded area here
    ATM.contourf(x, y, z, num_bars,cmap=colorscheme)
    #change location of the legend here as loc=...
    ATM.legend(loc='lower left',frameon=False,fontsize=fontsize_legend)
                         
plt.tight_layout()

fig.savefig("xi_combined.pdf",format='pdf',bbox_inches='tight', dpi=300)
