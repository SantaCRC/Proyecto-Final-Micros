import time
import threading
import servos

def movery(instruccion):
    try:
        y = instruccion[1]
        print("y:", y)
    except Exception as e:
        print("Error: " + str(e))

def moverx(instruccion):
    try:
        x=instruccion[1]
        print("moving x to:",x)
    except Exception as e:
        print("Error: " + str(e))

def vertical(instruccion): #apunta directamente a la funcion leer_archivo
    try:
        position(0, 0)
    except:
        print("Error: no se puede apuntar a la vertical")
    

def pausa(instruccion):
    try:
        tiempo=int(instruccion[1])
        print("Inicio de pausa: " + str(tiempo))
        time.sleep(tiempo)
        print("Pausa de " + str(tiempo) + " segundos finalizada")
    except:
        print("Tiempo no especificado")

def reposo(instruccion): # se pasa el argumento de la instruccion solo por concordancia no es necesario
    position(0, 0)
    print("Estoy en reposo")


def position(x, y): #funcion de posicion absoluta
    print("Estoy en la posicion: " + str(x) + "," + str(y))

def cardinal(instruccion):
    try:
        posicion = instruccion[1]
        try:
            if posicion == "norte":
                position(0, 0)
            elif posicion == "sur":
                position(0, 200)
            elif posicion == "este":
                position(200, 0)
            elif posicion == "oeste":
                position(200, 200)    
            else:
                print("Error: " + str(posicion) + " no es una posicion valida")      
        except:
            print("No existe la posicion cardinal indicada")
    except Exception as e:
        print("Error: " + str(e))
    
    


def disparar(): #definicion de la funcion disparar
    print("Disparo")

def mover(instruccion): #definicion de la funcion mover
    try:
        x = instruccion[1] #el segundo elemento es el x
        y = instruccion[2] #el tercero es el y
        print("Muevo a la posicion: " + str(x) + "," + str(y))
        pos = [int(x),int(y)]
        threading.Thread(target=servos.main, args=(pos,)).start()
    except Exception as e:
        print("Error: " + str(e))
        

def leer_archivo(nombre_archivo): #funcion que leer el archivo con el codigo
    archivo = open(nombre_archivo, 'r')
    for instruccion in archivo: #itera para todas las intrucciones del archivo
        leer(instruccion.lower())

def leer(instruccion): #funcion que lee la instruccion
    instruccion=instruccion.split() #separa la instruccion en segmentos, 
    if instruccion[0] == 'mover': #el primer elemento define la instruccion, depende de la instruccion tendra mas argumentos
        mover(instruccion) #El comando mover tiene dos argumentos, x y y
    elif instruccion[0] == 'disparar': #disparo
        disparar()
    elif instruccion[0] == 'cardinal': #posicion cardinal
        cardinal(instruccion)
    elif instruccion[0] == 'reposo': #posicion de reposo
        reposo(instruccion)
    elif instruccion[0] == 'pausa':
        pausa(instruccion)
    elif instruccion[0] == 'vertical':
        vertical(instruccion)
    elif instruccion[0] == 'moverx':
        moverx(instruccion)
    elif instruccion[0] == 'movery':
        movery(instruccion)


if __name__ == '__main__':
    leer_archivo("instrucciones.txt")