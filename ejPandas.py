import pandas as pd
import matplotlib.pyplot as plt

ventas_mensuales = [
{"mes": "Enero", "total_ventas": 15000, "año": 2023},
{"mes": "Febrero", "total_ventas": 18000, "año": 2023},
{"mes": "Marzo", "total_ventas": 22000, "año": 2023},
{"mes": "Abril", "total_ventas": 19000, "año": 2023},
{"mes": "Mayo", "total_ventas": 25000, "año": 2023},
{"mes": "Junio", "total_ventas": 28000, "año": 2023},
{"mes": "Julio", "total_ventas": 32000, "año": 2023},
{"mes": "Agosto", "total_ventas": 30000, "año": 2023},
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
{"mes": "Octubre", "total_ventas": 31000, "año": 2023},
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
{"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
{"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
{"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
{"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]

mes_trimestre = {"Enero": 1, "Febrero": 1, "Marzo": 1,
    "Abril": 2, "Mayo": 2, "Junio": 2,
    "Julio": 3, "Agosto": 3, "Septiembre": 3,
    "Octubre": 4, "Noviembre": 4, "Diciembre": 4,
    "Enero 2": 5, "Febrero 2": 5, "Marzo 2": 5,
    "Abril 2": 6, "Mayo 2": 6, "Junio 2": 6,
    "Julio 2": 7, "Agosto 2": 7, "Septiembre 2": 7,
    "Octubre 2": 8, "Noviembre 2": 8, "Diciembre 2": 8

}

#Agrupa los datos por trimestre y calcula el total de ventas para cada trimestre.
df = pd.DataFrame(ventas_mensuales)

df["trimestre"] = df["mes"].map(mes_trimestre)
trimestral = df.groupby("trimestre")["total_ventas"].sum()

#Filtrar y mostrar solo los meses donde las ventas superen 20000.
ventas = df[df["total_ventas"] > 20000]

#Encontrar el mes con el mayor volumen de ventas y mostrar esta información.
mayor_mes_ventas = df["mes"][df["total_ventas"].idxmax()]

#Calcular el promedio de ventas mensuales y mostrar esta información.
promedio_ventas = df['total_ventas'].mean()


print("\nTotal ventas trimestral:\n", trimestral)
print("\nMeses en que las ventas superan 20000:\n", ventas)
print("\nMes con mayor volumen de ventas:\n", mayor_mes_ventas)
print("\nPromedio ventas mensuales:\n", promedio_ventas)
#Crea un DataFrame que incluya dos columnas una para los meses y otra para el total de ventas de cada mes.
print("\nDataFrame con los meses y el total de ventas:\n", df[['mes', 'total_ventas']])


plt.plot(df["trimestre"], df["total_ventas"])
plt.title("Tendencia de ventas")
plt.show()