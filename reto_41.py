# LA CASA ENCANTADA
"""
    Te encuentras explorando una mansión abandonada llena de habitaciones. 
    - En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
    - Tu misión es encontrar la habitación de los dulces.
    - Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
(Tienes total libertad para ser creativo con los textos).
    - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4 que deberás modelar. 
    Las habitaciones de puerta y dulces no tienen enigma. (16 habitaciones, siendo una de entrada 
    y otra donde están los dulces). Esta podría ser una representación:
            🚪⬜️⬜️⬜️
            ⬜️👻⬜️⬜️
            ⬜️⬜️⬜️👻
            ⬜️⬜️🍭⬜️
    - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
    - Si no lo aciertas no podrás desplazarte.
    - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
    (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
    - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
    - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y 
    tengas que responder dos preguntas para salir de ella.
 """

from enum import Enum
import keyboard
import random
import os


# Función para imprimir la casa junta
def print_house(house: list, text: str):
    print(f"\n{text}\n")
    for row in house:
        print("".join(map(str, row)))


# SOLUCIÓN
the_haunted_house = [["🧐", "⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️", "⬜️"]]
the_haunted_house[random.randrange(0, 3)][random.randrange(0, 3)] = "👻"
the_haunted_house[random.randrange(0, 3)][random.randrange(0, 3)] = "👻"
the_haunted_house[random.randrange(1, 3)][random.randrange(0, 3)] = "🍭"
the_haunted_house[0][0] = "🧐"
print_house(the_haunted_house, "THE HAUNTED HOUSE")

# DECLARACIÓN DE VARIABLES
candies = False
ghost = False
no_move = False

class Movement(Enum): # Clase para el movimiento
    UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4

def haunted_house(): #FUNCIÓN PRINCIPAL
    
    house = [["🧐", "⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛", "⬛"],]
    print_house(house, "LA CASA ENCANTADA")

    while True:
        
        event = keyboard.read_event()

        if event.name == "esc":
            break

        elif event.event_type == keyboard.KEY_DOWN:
            if event.name == "up":
                (house, candy) = move_piece(house, Movement.UP)
            elif event.name == "down":
                (house, candy)  = move_piece(house, Movement.DOWN)
            elif event.name == "right":
                (house, candy)  = move_piece(house, Movement.RIGHT)  
            elif event.name == "left":
                (house, candy)  = move_piece(house, Movement.LEFT)
        
        if candy == True:
            break
    return


def move_piece(house: list, movement: Movement) -> (list, bool):
    
    os.system("clear")
    candy = False
    no_move = False

    # CONOCER LA CASA TRAS EL MOVIMIENTO
    new_house = [["⬛"] * 4 for _ in range(4)]
    for row_index, row in enumerate(house):
        for column_index, item in enumerate(row):
            if item == "⬜️":
                new_house[row_index][column_index] = "⬜️"
            if item == "🧐":
                new_house[row_index][column_index] = "⬜️"
                new_row_index = 0
                new_column_index = 0
                
                match movement:
                    case Movement.UP:
                        new_row_index = row_index - 1
                        new_column_index = column_index
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                # Movimiento fuera de la casa        
                if (new_row_index > 3 or new_row_index < 0 or new_column_index > 3 or new_column_index < 0):
                    os.system("clear")
                    print_house(house, "LA CASA ENCANTADA")
                    print("\nNo se puede realizar el movimiento\nPulse otra flecha para continuar\n")
                    no_move = True
                    return (house, candy)
                else:
                    new_house[new_row_index][new_column_index] = "🧐"

    print_house(new_house, "LA CASA ENCANTADA")

    candy = situation(new_house, no_move)
    
    return (new_house, candy)


# Función que analiza la habitación
def situation(new_house: list, no_move: bool) -> bool:

    candy = False
    if no_move == True:
        return
    else:
        for row_index, row in enumerate(new_house):
            for column_index, item in enumerate(row):
                if item == "🧐":
                    if the_haunted_house[row_index][column_index] == "🍭":
                        riddle()
                        os.system("clear")
                        candy = True
                        print(f"\n¡Enhorabuena! Has encontrado los dulces 🍭\n")
                        print_house(the_haunted_house, "SOLUCIÓN")
                        return candy
                    if the_haunted_house[row_index][column_index] == "👻":
                        print("\n¡Oh! Hay un fantasma en esta habitación. Tendrás que acertar dos preguntas para avanzar:\n")
                        riddle()
                        print("\n¡Es correcto! Vamos con la segunda pregunta:\n")
        riddle()
        print("Es correcto! puedes acceder a la siguiente habitación")
    return candy

# Función acertijo(s)
def riddle():
    halloween_questions = {
        "¿Cuál es el color tradicional de Halloween?": "naranja",
        "¿Cuál es la fecha de Halloween?": "31 de octubre",
        "¿Cuál es el personaje más popular de Halloween?": "vampiro",
        "¿Cuál es el dulce tradicional de Halloween?": "caramelos",
        "¿Cuál es el juego tradicional de Halloween?": "truco o trato"}
    
    question = list(halloween_questions.keys())[random.randrange(0, len(halloween_questions))]
    print(question + "\n")

    while True:
        
        answer = input()
        the_answer = halloween_questions[question]

        if answer.lower() == the_answer.lower():
            break
        else:
            print("No es correcto. Vuelve a intentarlo\n")
            continue
    return 


haunted_house()
