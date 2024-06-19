def menu():
    print("Bienvenido")
    print("1) Verificar si un número es primo")
    print("2)Verificar si un número es par o impar")
    print("3)Calcular la suma de los números primos ingresados")
    print("4)Salir")
    op = int(input("Ingrese la opción "))
    return op

numeros_primos = []

def num_primos ():
    with open("text.txt", "w") as archivo:
        for primo in num_primos:
            archivo.write(f"{primo} \n")
    print("Números primos guardados en 'text.txt'")

suma_par = []

def opcion_escogida(x):
    if x ==1:
        try:
            n = (int(input("Ingrese el número que desea verificar: ")))

            if n <= 1:
                print(f"El número {n} no es un número primo")
                return
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    print(f"El número {n} no es un número primo")
                    break
                print(f"El número {n} es un número primo")
                numeros_primos.append(n)
                num_primos()
                
        except ValueError:
            print("Ingrese un valor numérico")
    elif x == 2:
            try:
                parimp = int(input("Ingrese el numero que desea verficiar: "))
                if parimp%2 == 0:
                    print(f"El número {parimp} es un número par")
                    suma_par.append(parimp)
                elif parimp%2==1:
                    print(f"El número {parimp} no es un número par")
            except:
                print("Ingrese por favor un valor númerico")
    elif x == 3:
        print(f"La suma de todos los pares ingresados es:{sum(suma_par)}")
    elif x == 4:
        print("Salio del menú")    
    else:
        print("Ingrese una de las opciones del menú")
        print("tao pai pai")
