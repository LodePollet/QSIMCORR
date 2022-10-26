# -*- coding: utf-8 -*-
"""
Created on Dez 09:53:00 2016
Prints the values of the connectec correlationfunction and the squared winding numbers for a set of L and U_bf
@author: Janik
"""


from decimal import *
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import math
from scipy.optimize import curve_fit

from matplotlib.patches import PathPatch
from matplotlib.path import Path

plt.rcParams.update({
                    "text.usetex": True,
                    "font.family": "sans-serif",
                    "font.sans-serif": ["Helvetica"]})
a=3
fig, (PIM,ATM) = plt.subplots(1, 2)
aspect=0.717

######################################
#PIM PLOT
######################################

fontsize_legend=6
fontsize_axis=6
linewidths=1.
markersizes=5.
capsizes=2.

#set limits and subticks
PIM.axis([0, 0.2,0.,4])
PIM.set_aspect(aspect/PIM.get_data_ratio(), adjustable='box')
PIM.tick_params(axis ='both', which ='both',direction='in',labelsize=fontsize_axis)
PIM.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.02))

PIM.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
PIM.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

#mean field line not shown as not discussed in the maintext
#p_theory=[0,      0.03, 0.05, 0.08, 0.1,  0.12, 0.13,   0.14,   0.15,   0.16,   0.16945]
#t_c_theory=[3.62784808749,3.325,3.117,2.791,2.559,2.309,2.174,  2.027,  1.862,  1.661,  1.258]
#PIM.plot(p_theory,t_c_theory,label="theory(mean field)",color="black")

#Nishimori Line
x=np.linspace(0.0001,0.3,50)
y=2/np.log((1-x)/x)
PIM.plot(x,y,label="Nishimori line",linestyle='dotted',color="deepskyblue",linewidth=linewidths)
#show T_c of observables P(E),c_V,chi,Binder
#1 yes 0 no
plot_obs=[0,1,1,0]
discard_P_E_PIM=-3
#Energy Histogram
p_hist=[0.,0.05,0.1,0.146,0.148,0.15]
t_c_hist=[3.612672656179627,3.077274536964732,2.5180077566860817,1.873887295330505,1.8230656031331254,1.9254305080659981]
t_c_hist_err=[0.010385579255035757,0.010351459198518948,0.010115246785463985,0.010725278175924394,0.010398852048785205,0.010497451664797713]
if plot_obs[0]==1:
    PIM.errorbar(p_hist[:discard_P_E_PIM],t_c_hist[:discard_P_E_PIM],yerr=t_c_hist_err[:discard_P_E_PIM], marker='.',markersize=markersizes,color='purple',capsize=capsizes,linestyle='',label=r"$T_c^{P(E)}$")

#Values of quadratic fits to other Order parameters for the regime of first order transition
#c_v
p_load=np.load("PIM/disordersc_v_mean.npy")
t_c_load=np.load("PIM/t_inf_array_3c_v_mean.npy")
t_c_err_load=np.load("PIM/t_inf_array_3_errorc_v_mean.npy")
if plot_obs[1]==1:
    PIM.errorbar(p_load,t_c_load,yerr=t_c_err_load, marker='.',markersize=markersizes,color='red',capsize=capsizes,linestyle='',label=r"$T_c^{c_V}$")

#chi
p_load_chi=np.load("PIM/disorderschi.npy")
t_c_load_chi=np.load("PIM/t_inf_array_3chi.npy")
t_c_err_load_chi=np.load("PIM/t_inf_array_3_errorchi.npy")
if plot_obs[2]==1:
    PIM.errorbar(p_load_chi,t_c_load_chi,yerr=t_c_err_load_chi, marker='.',markersize=markersizes,color='blue',capsize=capsizes,linestyle='',label=r"$T_c^{\chi}$")

#p=0 values
#value from C_V
if plot_obs[1]==1:
    PIM.errorbar(0,3.629369137919435,yerr=0.011314529416324375,capsize=capsizes, marker='.',markersize=markersizes,color="red")
#value from Chi
if plot_obs[2]==1:
    PIM.errorbar(0,3.6293715117326464,yerr=0.011332206256818378,capsize=capsizes, marker='.',markersize=markersizes,color="blue")
#value from Binder
if plot_obs[3]==1:
    PIM.errorbar(0,3.6128493151581758,yerr=0.009732528548131787,capsize=capsizes, marker='.',markersize=markersizes,color="green")




#p=0 value from chi
p_inf=[0]
t_c_inf_binder_square=[3.6294471931219463]
t_c_inf_binder_square_err=[0.011209813477447953]
#p=0 value taken from Janke's paper
#p_inf=[0]
#t_c_inf_binder_square=[3.62784808749]
#t_c_inf_binder_square_err=[0.01042588624675441]
# load T_c obtained by quadratic Binder dip fits for different p values (first order PT regime)
if plot_obs[3]==1:
    p_load=np.load("PIM/disorders.npy")
    t_c_load=np.load("PIM/t_inf_array_3.npy")
    t_c_err_load=np.load("PIM/t_inf_array_3_error.npy")
    PIM.errorbar(p_load[:],t_c_load[:],yerr=t_c_err_load[:], marker='.',markersize=markersizes,color='green',capsize=capsizes,linestyle='',label=r"$T_c^B$")

#now use chi
p_inf=np.append(p_inf,p_load_chi)
t_c_inf_binder_square=np.append(t_c_inf_binder_square,t_c_load_chi)
t_c_inf_binder_square_err=np.append(t_c_inf_binder_square_err,t_c_err_load_chi)
#7. value is p=0.142, stop here as Binder dips start to be constant/shrink no longer first order
#p_inf=p_inf[:7]
#t_c_inf_binder_square=t_c_inf_binder_square[:7]
#t_c_inf_binder_square_err=t_c_inf_binder_square_err[:7]

#8. value is p=0.142, stop here as Binder dips start to be constant/shrink no longer first order
#p_inf=p_inf[:8]
#t_c_inf_binder_square=t_c_inf_binder_square[:8]
#t_c_inf_binder_square_err=t_c_inf_binder_square_err[:8]

#PIM.errorbar(p_inf,t_c_inf_binder_square,yerr=t_c_inf_binder_square_err, marker='.',markersize=markersizes,color='blue',capsize=capsizes,linestyle='')


"""
#values obtained by the correlation lenght/L plot as shown in Figure 4
p_correl=[0.142,0.144,0.146,0.148]
t_c_correl_global_fit=[1.845,1.84,1.80, 1.72]
t_c_correl_global_fit_err=[0.095,0.08,0.07 ,0.06]
#start with correl lenght values at 0.146
p_correl=p_correl[1:]
t_c_correl_global_fit=t_c_correl_global_fit[1:]
t_c_correl_global_fit_err=t_c_correl_global_fit_err[1:]

PIM.errorbar(p_correl,t_c_correl_global_fit,yerr=t_c_correl_global_fit_err,capsize=capsizes, marker='.',markersize=markersizes,linestyle='',color='blue')
PIM.errorbar(1000,1000,yerr=0.1,marker='.',markersize=markersizes,color='blue',capsize=capsizes,linestyle='--',label="RPI")
"""





# second part of the PB 0.142<p<0.148
#p_boundary=np.append(p_inf,p_correl)
p_boundary=p_inf
#t_c_boundary= np.append(t_c_inf_binder_square,t_c_correl_global_fit)
t_c_boundary= t_c_inf_binder_square
#t_c_boundary_err=1./np.append(t_c_inf_binder_square_err,t_c_correl_global_fit_err)
t_c_boundary_err=1./t_c_inf_binder_square_err
z=np.polyfit(p_boundary, t_c_boundary,3,w=t_c_boundary_err)
p = np.poly1d(z)
xp = np.linspace(0, 0.142, 100)
#with downward line
#x_values=np.append(xp,0.148)
#y_values=np.append(p(xp),0.0)
#PIM.plot(x_values,y_values,color='blue',linestyle='--')

#no downward line
PIM.plot(xp,p(xp),color='blue',linestyle='--',linewidth=linewidths)
#store values of PB for shaded region
store_boundary_x=xp
store_boundary_y=p(xp)
"""
#gradient shading of ordered Phase
xx=np.append(store_boundary_x,[0.148,0.148,0])
yy=np.append(store_boundary_y,[p(0.148),0,0])

path2 = Path(np.array([xx,yy]).transpose())
patch2 = PathPatch(path2, facecolor='none',linewidth=0)
PIM.add_patch(patch2)
#change colormap of shading area of ordered phase here as cmap=...
im=PIM.imshow(xx.reshape(yy.size,1),  cmap=plt.cm.Wistia,interpolation="bicubic",
              origin='lower',extent=[0,0.15,0.0,3.6],aspect="auto", clip_path=patch2,alpha=0.4, clip_on=True )

#shading of the p_c area
x = np.linspace(0.144,0.152,10)
y = np.linspace(0.,2.2,10)
z = [[-z] * 10 for z in range(10)]
num_bars = 1000  # more bars = smoother gradient
#change colormap of shading area of p_c here as cmap=...
PIM.contourf(x, y, z, num_bars,cmap=plt.cm.Reds)
"""




#Annotations and arrows for the plot
PIM.text(0.05, 0.95,"(a) RPI",
     horizontalalignment='left',
     verticalalignment='center',
     transform = PIM.transAxes,fontsize=fontsize_axis)
#PIM.annotate(" Stable ordered Phase\n(error correction feasible)",[0.025,2.])
#PIM.annotate(" $p^X_c \simeq 0.148(4)$",[0.1,1.5])
"""
#change arrows here if the p_c regime changes
PIM.annotate("",
             xy=(0.1455,1.4), xycoords='data',
             xytext=(0.1359,1.4), textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )
PIM.annotate("",
             xy=(0.1505,1.4), xycoords='data',
             xytext=(0.1601,1.4), textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )
             """
#change x and y label here
PIM.set_xlabel("Bit-flip error rate "+r"$p$",fontsize=fontsize_axis)
PIM.set_ylabel("Temperature "+r"$T$",fontsize=fontsize_axis)
#change location of the legend here as bbox_to_anchor=... or loc=... if desired
PIM.legend(frameon=False,loc="upper right",fontsize=fontsize_legend)


######################################
#ATM PLOT
######################################
#set limits and subticks
ATM.axis([0, 0.10,0.,1.8])
ATM.set_aspect(aspect/ATM.get_data_ratio(), adjustable='box')

ATM.tick_params(axis ='both', which ='both',direction='in',labelsize=fontsize_axis)
ATM.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.01))

ATM.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
ATM.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

#mean field line not shown as not discussed in the maintext
#p_theory=[0,      0.03, 0.05, 0.08, 0.1,  0.12, 0.13,   0.14,   0.15,   0.16,   0.16945]
#t_c_theory=[3.62784808749,3.325,3.117,2.791,2.559,2.309,2.174,  2.027,  1.862,  1.661,  1.258]
#PIM.plot(p_theory,t_c_theory,label="theory(mean field)",color="black")

#Nishimori Line
x=np.linspace(0.0001,0.3,50)
y=2/np.log((1-x)/x)
ATM.plot(x,y,label="Nishimori line",linestyle='dotted',color="deepskyblue",linewidth=linewidths)
x=0.158


discard_P_E_ATM=-3
#Energy Histogram
p_hist=[0.04,0.06,0.074,0.075,0.076]
t_c_hist=[1.3264998149935914,1.207766795381014,1.1242865134975097,1.1155606336867627,1.1016226851836075]
t_c_hist_err=[0.013909493876626782,0.013684548564919796,0.013624626503725904,0.013781644058508317,0.0140390370451765]
if plot_obs[0]==1:
    ATM.errorbar(p_hist[:discard_P_E_ATM],t_c_hist[:discard_P_E_ATM],yerr=t_c_hist_err[:discard_P_E_ATM], marker='.',markersize=markersizes,color='purple',capsize=capsizes,linestyle='',label=r"$T_c^{P(E)}$")

#Values of quadratic fits to other Order parameters for the regime of first order transition

#c_v
p_load=np.load("ATM/disordersc_v_mean.npy")
t_c_load=np.load("ATM/t_inf_array_3c_v_mean.npy")
t_c_err_load=np.load("ATM/t_inf_array_3_errorc_v_mean.npy")
if plot_obs[1]==1:
    ATM.errorbar(p_load,t_c_load,yerr=t_c_err_load, marker='.',markersize=markersizes,color='red',capsize=capsizes,linestyle='',label=r"$T_c^{c_V}$")

#chi
p_load_chi=np.load("ATM/disorderschi.npy")
t_c_load_chi=np.load("ATM/t_inf_array_3chi.npy")
t_c_err_load_chi=np.load("ATM/t_inf_array_3_errorchi.npy")
if plot_obs[2]==1:
    ATM.errorbar(p_load_chi,t_c_load_chi,yerr=t_c_err_load_chi, marker='.',markersize=markersizes,color='blue',capsize=capsizes,linestyle='',label=r"$T_c^{\chi}$")


#p=0 values
#value from C_V
if plot_obs[1]==1:
    ATM.errorbar(0,1.5221620489273304,yerr=0.0034060109500150754,capsize=capsizes, marker='.',markersize=markersizes,color="red")
#value from Chi
if plot_obs[2]==1:
    ATM.errorbar(0,1.522109041845764,yerr=0.0033725960984438926,capsize=capsizes, marker='.',markersize=markersizes,color="blue")
#value from Binder
if plot_obs[3]==1:
    ATM.errorbar(0,1.5273178464881678,yerr=0.0030189382041256973,capsize=capsizes, marker='.',markersize=markersizes,color="green")


#p=0 value taken from duality to PIM with chi value
p_inf=[0]
t_c_inf_binder_square=[1.522109041845764]
t_c_inf_binder_square_err=[0.0033725960984438926]
#Janke_values
#t_c_inf_binder_square=[2./1.31329]
#t_c_inf_binder_square_err=[0.00012/1.31329*2./1.31329]
if plot_obs[2]==1:
    ATM.errorbar(p_inf,t_c_inf_binder_square,yerr=t_c_inf_binder_square_err, marker='.',markersize=markersizes,color='blue',capsize=capsizes,linestyle='')

# load T_c obtained by quadratic Binder dip fits for different p values (first order PT regime)
if plot_obs[3]==1:
    p_load=np.load("ATM/disorders.npy")
    t_c_load=np.load("ATM/t_inf_array_3.npy")
    t_c_err_load=np.load("ATM/t_inf_array_3_error.npy")
    ATM.errorbar(p_load[:],t_c_load[:],yerr=t_c_err_load[:], marker='.',markersize=markersizes,color='green',capsize=capsizes,linestyle='',label=r"$T_c^{B}$")



p_inf=np.append(p_inf,p_load_chi)
t_c_inf_binder_square=np.append(t_c_inf_binder_square,t_c_load_chi)
t_c_inf_binder_square_err=np.append(t_c_inf_binder_square_err,t_c_err_load_chi)



#ATM.errorbar(p_inf,t_c_inf_binder_square,yerr=t_c_inf_binder_square_err, marker='.',markersize=markersizes,color='blue',capsize=2,linestyle='')
ATM.errorbar(1000,1000,yerr=0.1,marker='.',markersize=markersizes,color='blue',capsize=capsizes,linestyle='--',linewidth=linewidths)
#values obtained by the correlation lenght/L plot as shown in Figure 4
p_correl=[0.074,0.075,0.076]
t_c_inf_correl=[0.96,0.94, 0.88]
t_c_inf_correl_err=[0.06,0.08,0.1]


#ATM.errorbar(p_correl,t_c_inf_correl,yerr=t_c_inf_correl_err, marker='.',color='blue',capsize=2,linestyle='')








#p_boundary=np.append(p_inf,np.array(p_correl))
p_boundary=p_inf
#t_c_boundary= np.append(t_c_inf_binder_square,np.array(t_c_inf_correl))
t_c_boundary= t_c_inf_binder_square
#t_c_boundary_err=1./np.append( t_c_inf_binder_square_err,np.array(t_c_inf_correl_err))
t_c_boundary_err=1./t_c_inf_binder_square_err

z=np.polyfit(p_boundary, t_c_boundary,3,w=t_c_boundary_err)
p = np.poly1d(z)
xp = np.linspace(0., 0.073, 100)
#with downward line
#x_values=np.append(xp,0.075)
#y_values=np.append(p(xp),0.0)
#ATM.plot(x_values,y_values,color='blue',linestyle='--')
#no downward line
ATM.plot(xp,p(xp),color='blue',linestyle='--',linewidth=linewidths)

#store values of PB for shaded region
store_boundary_x=xp
store_boundary_y=p(xp)

#gradient shading of ordered Phase
xx=np.append(store_boundary_x,[0.076,0.076,0])
yy=np.append(store_boundary_y,[p(0.076),0,0])
"""
path2 = Path(np.array([xx,yy]).transpose())
patch2 = PathPatch(path2, facecolor='none',linewidth=0)
ATM.add_patch(patch2)
#change colormap of shading area of ordered phase here as cmap=...
im=ATM.imshow(xx.reshape(yy.size,1),  cmap=plt.cm.Wistia,interpolation="bicubic",
              origin='lower',extent=[0,0.08,-0.0,1.60],aspect="auto", clip_path=patch2,alpha=0.4, clip_on=True)

#shading of the p_c area
x = np.linspace(0.074,0.078,10)
y = np.linspace(0.,1.3,10)
z = [[-z] * 10 for z in range(10)]
num_bars = 1000  # more bars = smoother gradient
#change colormap of shading area of p_c here as cmap=...
ATM.contourf(x, y, z, num_bars,cmap=plt.cm.Reds)
"""
#Annotations and arrows for the plot
ATM.text(0.05, 0.95,"(b) RACAT",
         horizontalalignment='left',
         verticalalignment='center',
         transform = ATM.transAxes,fontsize=fontsize_axis)
#ATM.annotate(" Stable ordered Phase\n(error correction feasible)",[0.01,0.8])
#ATM.annotate(" $p^Z_c \simeq 0.076(2)$",[0.052,0.58])
#change arrows here if the p_c regime changes
"""
ATM.annotate("",
             xy=(0.0748,0.7), xycoords='data',
             xytext=(0.070,0.7), textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )
ATM.annotate("",
             xy=(0.0772,0.7), xycoords='data',
             xytext=(0.082,0.7), textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )
"""

#change x and y label here
ATM.set_xlabel("Phase-flip error rate "+r"$p$",fontsize=fontsize_axis)
ATM.set_ylabel("Temperature "+r"$T$",fontsize=fontsize_axis)
#change location of the legend here as bbox_to_anchor=... or loc=... if desired
ATM.legend(frameon=False,loc="upper right",fontsize=fontsize_legend)

plt.tight_layout()
fig.savefig('Phase_Diagram_observable_comparison.pdf',format='pdf',bbox_inches='tight', dpi=300)
