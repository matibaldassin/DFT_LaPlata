import numpy as np
import matplotlib.pyplot as plt

# Leer solo las filas con 2 columnas (Ecut, Energia)
datos = []
with open("curvaEcut.dat") as f:
    for linea in f:
        campos = linea.split()
        if len(campos) == 2:
            datos.append([float(c) for c in campos])
datos = np.array(datos)
ecut, energia = datos[:, 0], datos[:, 1]

# Diferencia respecto del valor mas convergido (Ecut maximo)
dE = np.abs(energia - energia[-1])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

ax1.plot(ecut, energia, "o-", color="#2a6fdb")
ax1.set_xlabel("Ecut (Ry)")
ax1.set_ylabel("Energía total (Ry)")
ax1.set_title("Convergencia de la energía con Ecut")
ax1.grid(alpha=0.3)

ax2.semilogy(ecut[:-1], dE[:-1], "o-", color="#d9534f")
ax2.axhline(1e-3, ls="--", color="gray", label="1 mRy")
ax2.set_xlabel("Ecut (Ry)")
ax2.set_ylabel(r"$|E - E_{70}|$ (Ry)")
ax2.set_title("Error respecto de Ecut = 70 Ry")
ax2.grid(alpha=0.3, which="both")
ax2.legend()

fig.tight_layout()
fig.savefig("curvaEcut.png", dpi=150)
plt.show()
