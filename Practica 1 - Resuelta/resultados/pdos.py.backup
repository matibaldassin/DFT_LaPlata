import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.pyplot as pl


dos01 = np.loadtxt("silicon.pdos_atm#1(Si)_wfc#1(s)")
# E (eV)   ldos(E)   pdos(E) 
dos02 = np.loadtxt("silicon.pdos_atm#1(Si)_wfc#2(p)")
# E (eV)   ldos(E)   pdos(E)
dos03 = np.loadtxt("si.dos.dat")
# E (eV)   dos(E)   Int dos(E)

xmin, xmax = -10 , 3  # rango de energia para la DOS

Emin, Emax = 6.0010 , 6.6180

plt.plot(dos03[:,0]-Emin,dos03[:,1], color='k',  marker='.', markersize=0, label='Total',  linewidth=1.5,markerfacecolor="None")
plt.plot(dos02[:,0]-Emin,dos02[:,2], color='blue',  marker='.', markersize=0, label='p-Si',  linewidth=1.5,markerfacecolor="None")
plt.plot(dos01[:,0]-Emin,dos01[:,2], color='red',  marker='.', markersize=0, label='s-Si',  linewidth=1.5,markerfacecolor="None")

plt.xlim(-12,5)
plt.ylim(0,1.2*np.max(dos03[:,1]))

plt.axvspan(Emin-Emin,Emax-Emin, color='gold', ec='none',alpha = 1.0)
plt.legend(loc=2,frameon=False,fontsize=14)
plt.xlabel('$E-E_f$ (eV)',size=14)
plt.ylabel('Densidad de estados',size=14)

plt.show()