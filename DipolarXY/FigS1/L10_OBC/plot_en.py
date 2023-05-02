import numpy as np
import matplotlib.pylab as plt
from scipy.interpolate import CubicSpline

L = 10
Lsq = L*L
Np = (L * L )//2
Sinf = 0
for i in np.arange(Np+1,Lsq+1):
  Sinf += np.log(i*1.)
for i in np.arange(1,Lsq - Np+1):
  Sinf -= np.log(i*1.)
#Sinf = np.log(2.) *Lsq
print("# Sinf : ", Sinf, Sinf/Lsq)



data = np.loadtxt("en_L10.dat" )
beta = data[:,0]
en = data[:,5] / Lsq
enerr = data[:,6] / Lsq

def lattsum(L):
  s = 0
  for i1 in np.arange(0,L):
    for j1 in np.arange(0,L):
      for i2 in np.arange(0,L):
        for j2 in np.arange(0,L):
          x = i1 - i2
          y = j1 - j2
          if (x*x + y*y > 0):
            s += np.power(x*x + y*y, -3.0)
  return (s/L/L)

def lattsum_triple(L):
  s = 0
  for i1 in np.arange(0,L):
    for j1 in np.arange(0,L):
      for i2 in np.arange(0,L):
        for j2 in np.arange(0,L):
          for i3 in np.arange(0,L):
            for j3 in np.arange(0,L):
              dx1 = i2 - i1
              dy1 = j2 - j1
              dx2 = i3 - i2
              dy2 = j3 - j2
              dx3 = i1 - i3
              dy3 = j1 - j3
              if ((dx1*dx1 + dy1*dy1) > 0 and (dx2*dx2 + dy2 * dy2 > 0) and (dx3*dx3 + dy3*dy3 > 0)):
                s += np.power(dx1*dx1 +dy1*dy1, -1.5)*np.power(dx2*dx2+dy2*dy2, -1.5) * np.power(dx3*dx3 + dy3*dy3, -1.5)
  return (s/L/L)


#print(lattsum(10), 4.6589, lattsum_triple(L), 13.6527)

temperature = 1/beta
temp_low_to_high = np.copy(np.flip(temperature))
en_low_to_high = np.copy(np.flip(en))
enerr_low_to_high = np.copy(np.flip(enerr))


T_low = 0.4
indx_low = np.where(temp_low_to_high == T_low)[0][0]
#gamma = 0.865253 
#E0 = -0.810657 
gamma = 0.442679
E0 = -0.848487
dE_low = gamma * np.power(T_low, 5.) 
S_low = 5 * gamma / 4. * np.power(T_low, 4.) 
I_low = gamma/4. * np.power(T_low, 4.) 
print("# T_low, indx_low, gamma, dE_low, S_low : " , T_low, indx_low,temp_low_to_high[indx_low],  gamma, dE_low, S_low)


# E = - alpha * beta = -alpha/T  (includes Lsq)
# C_v = alpha/ T^2
# S = S(inf) - \int_T^{\inf} alpha / T^3 = S(inf) - alpha/2 T^{-2}
# I = \int_T^{infty} -alpha/(T'^3) dT' = alpha/2 T^{-2}
#alpha = 0.303
T_up = 5
indx_up = np.where(temp_low_to_high == T_up)[0][0]
phi2_pbc = 4.6589 / 16.
phi3_pbc = 13.6527 / 64
# from lattsum:
# -0.2575237568293452*x -10.549744784793207/64.*x*x
phi2 = 0.2575237568293452
phi3 = 10.549744784793207/64.
print("# phi2: " , phi2, phi2_pbc)
print("# phi3: " , phi3, phi3_pbc)
E_up = -phi2/T_up - phi3/ T_up / T_up
I_up = 0.5 * phi2 / T_up / T_up + phi3 / T_up / T_up /T_up / 3.
S_up = Sinf/Lsq - I_up
print("# T_up, indx_up, alpha, E_up, I_up, S_up : " , T_up, indx_up,temp_low_to_high[indx_up], phi2, E_up, I_up, S_up)

#alpha = 0.322
#T_up = 10
#indx_up = np.where(temp_low_to_high == T_up)[0][0]
#E_up = -alpha / T_up
#I_up = 0.5 * alpha / T_up / T_up
#S_up = Sinf/Lsq  - I_up
#print("# T_up, indx_up, alpha, E_up, I_up, S_up : " , T_up, indx_up,temp_low_to_high[indx_up], alpha, E_up, I_up, S_up)


eb_low_to_high = (en_low_to_high[:] - en_low_to_high[indx_low]*np.ones_like(en)) / temp_low_to_high
eberr_low_to_high = enerr_low_to_high / temp_low_to_high
ebb_low_to_high = eb_low_to_high / temp_low_to_high
ebberr_low_to_high = eberr_low_to_high /temp_low_to_high


cs  = CubicSpline(temp_low_to_high,en_low_to_high - en_low_to_high[indx_low] )
cs1 = CubicSpline(temp_low_to_high,(en_low_to_high - en_low_to_high[indx_low])/temp_low_to_high)
cs2 = CubicSpline(temp_low_to_high,(en_low_to_high - en_low_to_high[indx_low])/temp_low_to_high/temp_low_to_high)

#T_low = min(temperature)
T_crit = 1.924

x1 = []
s1 = []

print("# Low temperature:")
for t in np.linspace(T_low, T_crit, 200):
    x1.append(t)
    s1.append(S_low + cs1(t) + cs2.integrate(T_low, t))
    print(t, S_low + cs1(t) + cs2.integrate(T_low, t))


cs  = CubicSpline(temp_low_to_high,-en_low_to_high + en_low_to_high[indx_up] )
cs1 = CubicSpline(temp_low_to_high,(-en_low_to_high + en_low_to_high[indx_up])/temp_low_to_high)
cs2 = CubicSpline(temp_low_to_high,(-en_low_to_high + en_low_to_high[indx_up])/temp_low_to_high/temp_low_to_high)

x2 = []
s2 = []

print("# High temperature:")
for t in np.linspace(T_crit, T_up, 200):
    x2.append(t)
    s2.append(S_up - cs1(t) + cs2.integrate(t, T_up))
    print(t, S_up - cs1(t) + cs2.integrate(t, T_up))


#cs = CubicSpline(beta,en)
#cs2 = CubicSpline(temp_low_to_high[indx_low:indx_up+1],ebb_low_to_high[indx_low:indx_up+1] )
#FI = cs2.integrate(temp_low_to_high[indx_low],temp_low_to_high[indx_up])
#print("full integral : ", FI, FI+S_low +S_up, np.log(2.))

#intg = np.zeros_like(temp_low_to_high)
#entropy = np.zeros_like(temp_low_to_high)

#print("# Forward integration:")
#for i in np.arange(0,len(temp_low_to_high)-1):
#  if (temp_low_to_high[i] > T_low and temp_low_to_high[i]  < T_crit*1.05):
#    #intg[i] = intg[i-1] - (temp_low_to_high[i] - temp_low_to_high[i-1]) * (ebb_low_to_high[i-1] + ebb_low_to_high[i])/2.
#    intg[i] = intg[i-1] + cs2.integrate(temp_low_to_high[i-1],temp_low_to_high[i])
#    entropy[i] = intg[i] + eb_low_to_high[i] + S_low
#    print(temp_low_to_high[i],en_low_to_high[i], eb_low_to_high[i], intg[i], entropy[i] )
#  else:
#    intg[i] = I_low
#    #print(temp_low_to_high[i],en_low_to_high[i], eb_low_to_high[i], intg[i], S_low )


#print("# Backward integration:")
#intg = np.zeros_like(temp_low_to_high)
#entropy = np.zeros_like(temp_low_to_high)


#eb_low_to_high = (-en_low_to_high[:] + en_low_to_high[indx_up]*np.ones_like(en)) / temp_low_to_high
#eberr_low_to_high = enerr_low_to_high / temp_low_to_high
#ebb_low_to_high = eb_low_to_high / temp_low_to_high
#ebberr_low_to_high = eberr_low_to_high /temp_low_to_high


#for i in np.arange(len(temp_low_to_high)-1, 0, -1):
#  if (temp_low_to_high[i] <= T_up and temp_low_to_high[i] >= T_crit*0.95 ):
#    #intg[i] = intg[i+1] - (temp_low_to_high[i+1] - temp_low_to_high[i]) * (ebb_low_to_high[i] + ebb_low_to_high[i+1])/2.
#    intg[i] = intg[i+1] - cs2.integrate(temp_low_to_high[i],temp_low_to_high[i+1] )
#    entropy[i] = intg[i] + eb_low_to_high[i] + S_up
#    print (temp_low_to_high[i], en_low_to_high[i], eb_low_to_high[i], intg[i], entropy[i] )
#  else:
#    intg[i] = I_up
    

xs = np.linspace(0, beta[-1], 200)
xs2 = np.linspace(T_low, T_up, 2000)




plt.figure()
#plt.errorbar(temp_low_to_high, entropy, fmt="bo-", label=r"$S/L^2$")
plt.plot(x1,s1, "b.-", label=r"$S_{\rm low T}/L^2$")
plt.plot(x2,s2, "r.-", label=r"$S_{\rm high T}/L^2$")
plt.xlabel(r"$T$")
plt.ylabel(r"$S/L^2$")
plt.xlim([T_low,T_up])
plt.ylim([0,0.7])
plt.savefig("fig_entropy.pdf", format="pdf")


#xs = np.linspace(0, np.max(temperature), 200)



#intg = np.zeros_like(temperature)
#entropy = np.zeros_like(temperature)
#T1 = T_up
#E1 = E_up
#for i in np.arange(intg.size):
#  if (temperature[i] < T_up):
#    v = (T1 - temperature[i]) * (
#  intg[i] = cs2.integrate(0, temperature[i])
#  entropy[i] = S0/Lsq + en[i]/temperature[i] + intg[i]
#  print(i, intg[i], beta[i]*en[i], entropy[i])


#cs = CubicSpline(beta,en)
#xs = np.linspace(0, beta[-1], 200)

#intg = np.zeros_like(beta)
#entropy = np.zeros_like(beta)
#for i in np.arange(intg.size):
#  intg[i] = cs.integrate(0, beta[i])
#  entropy[i] = S0/Lsq + (intg[i] + beta[i] * en[i])
#  print(i, intg[i], beta[i]*en[i], entropy[i])



#plt.figure()
#plt.errorbar(beta, en, yerr=enerr, fmt="bo", label=r"$E/L^2$")
#plt.plot(xs,cs(xs), "r--", label="cubic spline") 
#plt.xlabel(r"$\beta$")
#plt.ylabel(r"$E/L^2$")
#plt.savefig("fig_energy.pdf", format="pdf")

