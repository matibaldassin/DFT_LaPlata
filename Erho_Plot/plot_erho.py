import numpy as np
import matplotlib.pyplot as plt

ECUTWFC = 40  # Ry, valor fijo usado en loopErho.sh

# Columnas: multiplicador, ecutrho (Ry), energia total (Ry)
datos = []
with open("curvaErho.dat") as f:
    for linea in f:
        campos = linea.split()
        if len(campos) == 3:
            datos.append([float(c) for c in campos])
datos = np.array(datos)
erho, energia = datos[:, 1], datos[:, 2]

# Diferencia respecto del valor mas convergido (ecutrho maximo)
dE = np.abs(energia - energia[-1])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

ax1.plot(erho, energia, "o-", color="#2a6fdb")
ax1.axvline(4 * ECUTWFC, ls=":", color="gray", label=r"$4\times$ecutwfc")
ax1.set_xlabel("ecutrho (Ry)")
ax1.set_ylabel("Energía total (Ry)")
ax1.set_title(f"Convergencia con ecutrho (ecutwfc = {ECUTWFC} Ry)")
ax1.ticklabel_format(axis="y", useOffset=False)
ax1.grid(alpha=0.3)
ax1.legend()

ax2.semilogy(erho[:-1], dE[:-1], "o-", color="#d9534f")
ax2.axhline(1e-3, ls="--", color="gray", label="1 mRy")
ax2.set_xlabel("ecutrho (Ry)")
ax2.set_ylabel(rf"$|E - E_{{{erho[-1]:.0f}}}|$ (Ry)")
ax2.set_title(f"Error respecto de ecutrho = {erho[-1]:.0f} Ry")
ax2.grid(alpha=0.3, which="both")
ax2.legend()

# Eje superior con la relacion ecutrho/ecutwfc
for ax in (ax1, ax2):
    sec = ax.secondary_xaxis("top", functions=(lambda x: x / ECUTWFC,
                                               lambda r: r * ECUTWFC))
    sec.set_xlabel("ecutrho / ecutwfc")

fig.tight_layout()
fig.savefig("curvaErho.png", dpi=150)
plt.show()
