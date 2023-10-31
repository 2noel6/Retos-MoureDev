# SIMULADOR DE CLIMA
'''Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
de un lugar ficticio al pasar un número concreto de días según estas reglas:
 · La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 · Cada día que pasa:
    + 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
    + Si la temperatura supera los 25 grados, la probabilidad de lluvia al día siguiente aumenta en un 20%.
    + Si la temperatura baja de 5 grados, la probabilidad de lluvia al día siguiente disminuya en un 20%.
    + Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
    + La función recibe el número de días de la predicción y muestra la temperatura y si llueve durante todos esos días.
    + También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.'''

import random

def clima(T0: int, rain: float, days: int):
    
    days_temperature = [T0]
    is_raining = []
    
    # First day
    T = T0
    if random.random() <= rain:
        is_raining.append("🌧️")
    else:
        is_raining.append("🌞")

    for day in range(1, days):

        # next day
        if T > 25:
            rain = rain + 0.2
        elif T < 5:
            rain = rain - 0.2
        if rain == 1:
            T = T - 1       

        # Temperature
        if random.random() <= 0.10:
            T = T + random.choice([+2, -2])
        days_temperature.append(T)

        # Rain
        if random.random() <= rain:
            is_raining.append("🌧️")
        else:
            is_raining.append("🌞")
        
    for day in range(1, days + 1):
        print(f"\nDay {day}:\n{is_raining[day-1]} {days_temperature[day-1]}°C")
    days_raining = is_raining.count("🌧️")
    print(f"\nEn este periodo:\n- La temperatura máxima y mínima ha sido de {max(days_temperature)} y {min(days_temperature)} °C, respectivamente.\n- Ha llovido durante {days_raining} días.")
    return 

clima(20, 0.5, 5)