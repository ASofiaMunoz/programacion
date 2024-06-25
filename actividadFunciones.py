#Solicitar ingreso de numeros y convertirlos en lista
def Lista_num():
    Lista_numIngre=input("Ingrese numeros separados: ").split(" ") #el split los convierte en lista
    print(Lista_numIngre)
    return Lista_numIngre



#Validar que sean numeros enteros part1
def validarLista_num(Lista_numIngre):
    listaNueva=[]
    try:
        for num in Lista_numIngre:
            listaNueva.append(int(num))
    except ValueError:
        print("Error en ingreso de los datos, estos deben ser enteros")
        return False
    return listaNueva





#validar que sean numeros enteros part2
#def validar_listaNum(numIngre):
#    if type(numIngre)== int:
#        return True
#    else:
#        return False
    
def par_impar(Lista_numIngre):
    pares=[] #lista vacia de los numeros par
    impar=[] #lista vacia de los numeros impar
    for num in Lista_numIngre: #se usa el for para iterar a traves de cada numero de la lista
        if num % 2 ==0:
            pares.append(num)
        else:
            impar.append(num)
    return pares, impar



def mostrar_resultados(pares, impar):
    print(f"Los numeros par son: {pares}")
    print(f"Los numeros {impar}")


    
