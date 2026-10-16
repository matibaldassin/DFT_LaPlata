import re
import numpy as np
import matplotlib.pyplot as plt

# Salida de ev.x: columnas Lat.Par (Ang), E_calc (Ry), E_fit (Ry), ...
datos = np.loadtxt("curvaA.out", comments="#")
a, e_calc, e_fit = datos[:, 0], datos[:, 1], datos[:, 2]

# Parametros del ajuste desde el encabezado
with open("curvaA.out") as f:
    encabezado = f.read()
a0 = float(re.search(r"a0 =\s*([\d.]+) Ang", encabezado).group(1))
k0 = float(re.search(r"k0 =\s*([\d.]+) GPa", encabezado).group(1))
emin = float(re.search(r"emin =\s*(-?[\d.]+)", encabezado).group(1))

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(a, e_fit, "-", color="#2a6fdb", lw=2, label="Ajuste Birch-Murnaghan")
ax.plot(a, e_calc, "o", color="#d9534f", ms=6, label="Calculada (pw.x)")
ax.axvline(a0, ls=":", color="gray")
ax.annotate(f"$a_0$ = {a0:.4f} Å\n$B_0$ = {k0:.1f} GPa\n$E_{{min}}$ = {emin:.5f} Ry",
            xy=(a0, emin), xytext=(0.5, 0.75), textcoords="axes fraction",
            ha="right", fontsize=10,
            bbox=dict(boxstyle="round", fc="white", ec="lightgray"))

ax.set_xlabel("Parámetro de red a (Å)")
ax.set_ylabel("Energía total (Ry)")
ax.set_title("Si: energía total vs parámetro de red")
ax.ticklabel_format(axis="y", useOffset=False)
ax.grid(alpha=0.3)
ax.legend(loc="lower left")

fig.tight_layout()
fig.savefig("curvaA.png", dpi=150)
plt.show()
