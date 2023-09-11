# PERMUTACIÓN # 4 horas
'''Crea un programa que sea capaz de generar e imprimir todas las permutaciones disponibles
formadas por las letras de una palabra.
    - Las palabras generadas no tienen por qué existir.
    - Deben usarse todas las letras en cada permutación.
    - Ejemplo: sol, slo, ols, osl, los, lso ''' 

import numpy
import random

word = input("Por favor, introduzca la palabra de la que quiere conocer las permutas ")

letters, word_lenght  = list(sorted(word)), len(word)

# Letras repetidas
repeated_letters = []
for i in letters:
    counter = letters.count(i)
    if counter > 1 and i not in repeated_letters:
        repeated_letters.append(i)

# Cálculo de posibilidades
if len(repeated_letters) == 0:
    possibilities = int(word_lenght * numpy.prod(range(1, word_lenght)))
else: # Se divide entre 2 por cada letra repetida
    possibilities = int((word_lenght * numpy.prod(range(1, word_lenght)))/(2*len(repeated_letters)))
    

# Iteración
all_words = []
possibility = 0
while possibility < possibilities:
    new_word = letters
    if "".join(new_word) not in all_words:
            all_words.append("".join(new_word))
            possibility = possibility + 1
    else:
        popped_letter = letters.pop()
        new_index = random.randrange(0, word_lenght)
        letters.insert(new_index, popped_letter)     
            
print(f"Existen {possibilities} posibilidades: {sorted(all_words)}")