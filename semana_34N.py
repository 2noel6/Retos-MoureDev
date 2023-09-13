'''
Crea un programa capaz de interactuar con un fichero TXT.
+ Si no existe, debe crear un fichero llamado "text.txt".
+ Desde el programa debes ser capaz de introducir texto por consola y guardarlo en una 
nueva línea cada vez que se pulse el botón "Enter".
+ Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo a 
continuación o borrar su contenido y comenzar desde el principio.
+ Si se selecciona continuar escribiendo, se tiene que mostrar por consola el texto que
ya posee el fichero.  
'''

contents = "I love programming\n"
contents += "I love creating games\n"
contents += "I also love working with data\n"
decision = ""

#
try:
    file = open("semana_34N.txt", "x")
except FileExistsError:
    decision = input("File name already exists\nPress 's' to overwrite or 'm' to keep the text ")
    while decision != "s" and decision != "m":
        decision = input("File name already exists\nPress 's' to overwrite or 'm' to keep the text ")
        if decision != "s" and decision != "m":
            print("that is not an option")
           
while True:
    new_contents = input("Tell me something about programming (write 'q' to exit) ")
    if new_contents == "q":
        break
    else:
        contents += new_contents + "\n"

if decision == "m":
    with open("semana_34N.txt", "a") as file:
        file.write(contents)
        file.close()
else:
    with open("semana_34N.txt", "w") as file:
        file.write(contents)
        file.close()
    

