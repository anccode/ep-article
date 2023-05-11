import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

print("MARZO")
muestraM = pd.read_csv(
    "marzo.csv", encoding="ISO-8859-1", sep=";"
)  # cargamos los datos de abril

muestraM.fillna(0, inplace=True)


#muestraM = datosM.sample(n=10000)  # hallamos la muestra
mediaM = muestraM["FACTURACIÓN"].mean()  # Media muestral del consumo
desv_stdM = muestraM["FACTURACIÓN"].std()  # Desviación estándar muestral del consumo

nM = len(muestraM)  # numero de la muestra

seM = desv_stdM / np.sqrt(nM)  # error estandar

zstartM = 1.96  # se usa una confianza de 95%
lcbM = mediaM - zstartM * seM
ucbM = mediaM + zstartM * seM
print(" ")
print(
    f"Intervalo de confianza para la media poblacional del facturacion: [{lcbM}, {ucbM}]"
)

# calcular la proporción muestral para cada muestra
pM = len(muestraM[muestraM["FACTURACIÓN"] > 100]) / nM
intervaloM = zstartM * np.sqrt(pM * (1 - pM) / nM)

print(
    f"Intervalo de confianza para la proporción de facturaciones mayores a 100: [{pM - intervaloM}, {pM + intervaloM}]"
)
print(" ")
print("ABRIL")

muestraA = pd.read_csv(
    "abril.csv", encoding="ISO-8859-1", sep=";"
)  # cargamos los datos de abril

muestraA.fillna(0, inplace=True)


#muestraA = datosA.sample(n=10000)  # hallamos la muestra

mediaA = muestraA["FACTURACIÓN"].mean()  # Media muestral del consumo
desv_stdA = muestraA["FACTURACIÓN"].std()  # Desviación estándar muestral del consumo

nA = len(muestraA)  # numero de la muestra

seA = desv_stdA / np.sqrt(nA)  # error estandar

zstartA = 1.96  # se usa una confianza de 95%
lcbA = mediaA - zstartA * seA
ucbA = mediaA + zstartA * seA
print(" ")
print(
    f"Intervalo de confianza para la media poblacional del facturacion: [{lcbA}, {ucbA}]"
)


# calcular la proporción muestral para cada muestra
pA = len(muestraA[muestraA["FACTURACIÓN"] > 100]) / nA
intervaloA = zstartA * np.sqrt(pA * (1 - pA) / nA)

print(
    f"Intervalo de confianza para la proporción de facturaciones mayores a 100: [{pA - intervaloA}, {pA + intervaloA}]"
)
print(" ")
print("Diferencia de medias")
d = mediaM - mediaA
sed = np.sqrt(desv_stdM**2 / nM + desv_stdA**2 / nA)
tstart = 1.96  # se usa una confianza del 95%
lcbDF = d - tstart * sed
ucbDF = d + tstart * sed

print(
    f"El intervalo de confianza para la diferencia de medias poblacionales es  [{lcbDF}, {ucbDF}] "
)


print("")
print("intervalo de confianza para la diferencia de proporciones")


# calcular la diferencia de proporciones
d_prop = pM - pA

# calcular el error estándar de la diferencia
se_prop = np.sqrt(pM * (1 - pM) / nM + pM * (1 - pA) / nA)

# calcular los límites inferior y superior del intervalo de confianza
zstart_prop = 1.96  # se usa una confianza de 95%
lcb_prop = d_prop - zstart_prop * se_prop
ucb_prop = d_prop + zstart_prop * se_prop

print(
    f"Intervalo de confianza para la diferencia de proporciones: [{lcb_prop}, {ucb_prop}]"
)


# marzo

fig, ax = plt.subplots(figsize=(8, 6))

# generar datos para curva
x = np.linspace(lcbM - 0.5 * seM, ucbM + 0.5 * seM, 100)
y = (
    np.exp(-((x - mediaM) ** 2) / (2 * seM**2))
    / (np.sqrt(2 * np.pi) * seM)
    * (ucbM - lcbM)
)

# dibujar curva
ax.plot(x, y, color="black")

# dibujar área sombreada debajo de la curva
ax.fill_between(x, y, 0, where=y > 0, color="blue", alpha=0.2)

# agregar líneas verticales para el intervalo de confianza
ax.axvline(lcbM, color="red", linestyle="--")
ax.axvline(ucbM, color="red", linestyle="--")

# agregar etiquetas y título
ax.set_xlabel("Facturación")
ax.set_ylabel("Densidad")
ax.set_title("Intervalo de confianza para la facturación de marzo")


# abril

fig, ax = plt.subplots(figsize=(8, 6))

# generar datos para curva
x = np.linspace(lcbA - 0.5 * seA, ucbA + 0.5 * seA, 100)
y = (
    np.exp(-((x - mediaA) ** 2) / (2 * seA**2))
    / (np.sqrt(2 * np.pi) * seA)
    * (ucbA - lcbA)
)

# dibujar curva
ax.plot(x, y, color="black")

# dibujar área sombreada debajo de la curva
ax.fill_between(x, y, 0, where=y > 0, color="blue", alpha=0.2)

# agregar líneas verticales para el intervalo de confianza
ax.axvline(lcbA, color="red", linestyle="--")
ax.axvline(ucbA, color="red", linestyle="--")

# agregar etiquetas y título
ax.set_xlabel("Facturación")
ax.set_ylabel("Densidad")
ax.set_title("Intervalo de confianza para la facturación de abril")

# mostrar gráfico
plt.show()
