'''Simulación de un diccionario funcional'''

def crearDiccionario():
    diccionario = {}
    print("Introduce 5 parejas de palabras (español-inglés).")
    for i in range(5):
        palabra_ing = input(f"Ingrese la palabra {i+1} en inglés: ")
        palabra_esp = input(f"Introduzca la palabra {i+1} en español: ")
        diccionario[palabra_ing] = palabra_esp
    return diccionario
    

def traducir():
    print("==MODO DE TRADUCCIÓN==")
    print("Ingrese la palabra 'salir' si desea terminar.")
    



def main():
    diccionario = crearDiccionario()
    traducir(diccionario)