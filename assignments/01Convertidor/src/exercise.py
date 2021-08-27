
    # Escribe tu código abajo de esta línea
def pies_cm(pies):
    total_cm =  pies*30.48
    return total_cm
def pulgadas_cm(pul):
    total_cm =  pul*2.54
    return total_cm
def yar_cm(yar):
    total_cm =  yar*91.44
    return total_cm
def main():
    print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')
    op = int(input('Introduce una opcion: '))
    cant= int(input('Introduce la cantidad: '))
    if op ==1:
        cm= pies_cm(cant)
        print(cm)
    elif op ==2:
        cm= pulgadas_cm(cant)
        print(cm)
    elif op == 3:
        cm = yardas_cm(cant)
        print(cm)
    else:
        print('Error')

            
if __name__ == '__main__':
    main()
