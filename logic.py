import random
import os 
from words import words_list
from images import gallow, hanged

def get_word():
    return random.choice(words_list)


def play(word):
    all_letters = [] # array para guardar todas las letras que introduzca el usuario
    fails = 1 # contador de fallos que inicializo a uno (primera cadena de caracteres de hanged)
    result = [] # lista con guiones para sustituir por letras acertadas
    
    for i in range(len(word)):
        result.append("_")    
    while True:
        os.system("cls")#limpiar consola
        print("*****   JUEGO DEL AHORCADO *****")
        print("********************************")
        
        for i in range(fails): # mostramos los elementos de la lista gallow
            print(hanged[i])
        for i in range(len(gallow)-fails):
            print(gallow[i+fails])
            
        print()
        #Mostramos el resultado donde intercambiamos las letras introducidar por los guiones bajos
        print("     ", end = " ")
        for i in result:
            print(i, end=" ")
        
        print()
        print()
        #Comprobamos si se ha acertado la palabra o se han terminado los intenos
        if result == word:
            print("*****       HAS GANADO     *****")
            break
        
        if fails > 6:
            print ("La palabra era:", "".join(word))
            print("*****     HAS PERDIDO     *****")
            break

        #validar letra introducida por el usuario
        while True:
            unformatted_user_letter = input("Dime una letra: ")
            user_letter = unformatted_user_letter.upper()
            if len(user_letter) != 1:
                print("Introduce una letra")
            elif user_letter in all_letters:
                print("esa letra ya la has dicho")
            elif user_letter not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ": #el método isalpha() incluye caracteres de otros idiomas
                print("Introduce una letra")
            else:
                all_letters.append(user_letter)
                break

        #comprobramos si la letra está en la palabra si está la remplazamos por el guión bajo, en caso contrario añadimos fallo al contador
        for i in range(len(word)):
            if word[i] == user_letter:
                result[i] =  user_letter
        
        if user_letter not in word:
            fails +=1
        print()
        print()
        
        
