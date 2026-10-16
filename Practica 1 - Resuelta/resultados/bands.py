import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.pyplot as pl


Emin, Emax = 6.0010 , 6.6180

bands = np.loadtxt("si.bands.dat.gnu")
plt.plot(bands[:,0],bands[:,1]-Emin, color='k',  marker='.', markersize=3.0, label='Total',  linewidth=0.0, markerfacecolor="None")
plt.xlim(0,np.max(bands[:,0]))
plt.ylim(-12,5)

plt.axhspan(Emin-Emin,Emax-Emin, color='gold', ec='none',alpha = 1.0)
plt.xlabel('k-path',size=14)
plt.ylabel('$E-E_f$ (eV)',size=14)

plt.show()