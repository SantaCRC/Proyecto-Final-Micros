
def guardar_linea(linea):
    f = open ('holamundo.txt','a')
    f.write(str(linea.get())+"\n")
    f.close()