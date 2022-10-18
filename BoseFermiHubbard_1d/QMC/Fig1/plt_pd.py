import numpy as np
import matplotlib.pylab as plt
from scipy import interpolate


#SS : V=3, U = 4.2 and 4.5; nothing for larger V; V= 2 : unclear, try to get good results for U2 and U=2.5

#bos_sf = np.array([ [0,0,0], [1, 0.5, 0.25], [2, 1.5, 0.25], [3, 3.0, 0.25],  [4,6,0.25], [4,6.5,0.25], [3.,5, 0.25], [2,4.2,0.2], [1, 3.60, 0.02], [0, 3.25, 0.05] ])
bos_sf = np.array([ [0,0,0], [1, 0.5, 0.25], [2, 1.5, 0.25], [3, 3.0, 0.25],  [4, 5.5,0.5], [5, 7.75, 0.25], [6, 10, 0.5], [5, 8.75, 0.25], [4,6.75,0.25], [3.,5.25, 0.25], [2,4.2,0.2], [1, 3.60, 0.02], [0, 3.25, 0.05] ])
phase_sep = np.array([ [0,0,0], [1, 0.3, 0.2], [2, 1.0, 0.25], [3, 2.5, 0.25] ])
phase_sep2 = np.array( [ [3,3], [4,5.3], [5,7.5], [6, 9.5], [8,12] ] )

#bos_sf_plot = np.array([ [0,0,0], [1, 0.5, 0.25], [2, 1.5, 0.25], [3, 3.1, 0.25], [3.5, 4.25, 0.25], [3.75, 5.0,0.25 ], [3.85, 5.33,0.2], [4,5.9,0.25], [4.1, 6.3,0.25], [4,6.5,0.25], [3.75, 6.2, 0.25], [3.5, 5.75,0.25], [3.,5, 0.25], [2,4.2,0.2], [1, 3.60, 0.02], [0, 3.25, 0.05] ])
bos_sf_plot = bos_sf
tck, u = interpolate.splprep([bos_sf_plot[:,0], bos_sf_plot[:,1]], s=0)
unew = np.arange(0, 13.01, 0.01)
out_bos_sf = interpolate.splev(unew, tck)

#bos_meso_channel = np.array([ [3,5], [4,6.25], [5,8], [6,10], [8,14] ] )
bos_meso_channel_dn = np.array([ [4,5.5], [5,7.5], [6,9.8], [8,14] ] )
bos_meso_channel_up = np.array([ [4,7], [5,8.75], [6,10.2], [8,14] ] )

#cdw = np.array( [ [4.05,6.0,0.5], [5, 7.5, 0.5], [6,9, 0.5], [8,12, 1], [8,16,1], [6,12.2,0.5], [5,10.2,0.5], [4,8.0,0.5], [4.05,6.0,0.5] ])
#ss_down = np.array( [ [3, 4.2], [5,8.5], [6, 10.5], [8,16] ] )
#ss_up = np.array( [ [3, 4.5], [5,10], [6, 12], [8,16] ] )

#sc = np.array( [ [2, 1.5, 0.5], [3, 4.2, 0.2], [4, 7., 0.5], [5, 9.5, 0.5], [6, 12, 0.3], [8, 16, 0.2] ])
sc = np.array( [ [3, 3.0, 0.25], [4, 6.25, 0.25], [5, 9.0, 0.25], [6, 11, 0.25], [8, 16, 0.25] ])
#ss_up = np.array ( [ [0.001, 5.25,0.5], [1, 5.6, 0.5], [2, 6.2, 0.5], [3, 7.5 , 1],  [4,9.2, 0.5],   [5, 12, 0.5], [6, 14, 0.5], [8, 18, 0.5] ])


eta_rho = np.array( [ [0,3.5,0.5], [1,4, 0.5], [2,4.5, 0.4], [3, 5.5, 0.5], [4, 7.0, 0.5], [5, 8.75, 0.5], [6, 10.25, 0.5], [8,13, 1.0] ] )  


free_crossover = np.array( [ [0, 5.25], [1, 5.60], [2, 6.25], [3, 7.6], [4, 9.5], [5, 12], [6, 14], [8, 18] ] )

#tck2, u2 = interpolate.splprep([cdw[:,0], cdw[:,1]], s=0)
#unew2 = np.arange(0, 9.1, 0.1)
#out_cdw = interpolate.splev(unew2, tck2)




#ps2 = phase_sep + [4., 4./0.717, 0.25]
#print(ps2)
phase_sep_x = np.arange(0, 4.1, 0.1)

V_low_asymp = np.arange(4.,10.5,.5)
U_low_asymp  = V_low_asymp / 0.717
V_high_asymp = np.arange(4.,10.5,.5)
U_high_asymp = V_high_asymp * 2

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

font4 = {'family': 'serif',
        'color':  'blue',
        'weight': 'normal',
        'size': 11,
        }

plt.figure()
plt.errorbar(phase_sep[:,0], phase_sep[:,1], phase_sep[:,2], fmt="k_")
plt.plot(phase_sep2[:,0], phase_sep2[:,1], "c:")
plt.errorbar(phase_sep_x, phase_sep_x * phase_sep_x / np.pi, fmt="k:")
plt.errorbar(bos_sf[:,0], bos_sf[:,1], bos_sf[:,2], fmt="r_")
#plt.errorbar(bos_meso_channel[:,0], bos_meso_channel[:,1], yerr = 0.5, fmt="r:")
#plt.plot(bos_meso_channel_dn[:,0], bos_meso_channel_dn[:,1], "r:")
#plt.plot(bos_meso_channel_up[:,0], bos_meso_channel_up[:,1], "r:")
#plt.errorbar(cdw[:4,0], cdw[:4,1], yerr = cdw[:4,2], fmt="g_-")
#plt.plot(ss_down[:,0], ss_down[:,1], "b:" )
#plt.plot(ss_up[:,0], ss_up[:,1], "b:" )
plt.errorbar(sc[:,0], sc[:,1], yerr = sc[:,2]*2, fmt="go-")
plt.errorbar(eta_rho[:,0], eta_rho[:,1], yerr = eta_rho[:,2], fmt="b--")
#plt.errorbar(ss_up[:,0], ss_up[:,1], yerr = ss_up[:,2], fmt="bx--")

#plt.errorbar(4.5,9.0,xerr=0.3, fmt="g_-")
#plt.plot(out_cdw[0], out_cdw[1], "g--")
plt.errorbar(bos_sf[:,0], bos_sf[:,1], yerr=bos_sf[:,2], fmt= "r-")
#plt.plot(out_bos_sf[0], out_bos_sf[1], "r-")
plt.plot(V_low_asymp, U_low_asymp, "k--",)
plt.plot(V_high_asymp, U_high_asymp, "k--")
plt.plot(free_crossover[:,0], free_crossover[:,1], "g.:")
plt.text(4, 2.5, "phase separation", fontdict=font1)
plt.text(0.2, 14.5, "bosonic Mott + free fermions", fontdict=font1)
plt.text(0.2, 1.5, "SF",  fontdict=font2)
plt.text(6.9, 12.8 , r"$\eta_{\rm CDW}=1$", fontdict=font4)
plt.text(7, 15 , "SC", fontdict=font3)
plt.xlim((0,8.04))
plt.xlim((0,8.04))
plt.ylim((0,20))

plt.xlabel(r"$V$", fontdict=font1)
plt.ylabel(r"$U$", fontdict=font1)

plt.savefig("fig_pd.pdf", format="pdf")
