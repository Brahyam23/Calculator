print("======================================")
print("Bienvenido a la calculadora de Brahyam")
print("====================================== \n")
repetir=1
while repetir==1:
    print("1° para suma")
    print("2° para resta")
    print("3° para multiplicación")
    print("4° para división")
    print("5° para división entera")
    print("6° para exponente")
    print("7° para módulo")

    numero=int(input("\nPor favor, inserte opción deseada: "))

    while numero<1 or numero>7:
        print("\nHa ingresado una opción que no existe.\n ")
        print("1° para suma")
        print("2° para resta")
        print("3° para multiplicación")
        print("4° para división")
        print("5° para división entera")
        print("6° para exponente")
        print("7° para módulo")
        numero=int(input("\nPor favor ingrese una opción válida:"))
    if numero==1:
        numero=float(input("\n|Ha elegido suma|\nInserte el primer valor: "))
        numero+=float(input("Inserte el segundo valor: "))
        print("\nEl resultado de la suma es: ", numero)
    elif numero==2:
        numero=float(input("\n|Ha elegido resta|\nInserte el primer valor: "))
        numero-=float(input("Inserte el segundo valor: "))
        print("\nEl resultado de la resta es: ", numero)
    elif numero==3:
        numero=float(input("\n|Ha elegido multiplicación|\nInserte el primer valor: "))
        numero*=float(input("Inserte el segundo valor: "))
        print("\nEl resultado de la multiplicación es: ", numero)
    elif numero==4:
        numero=float(input("\n|Ha elegido división|\nInserte el primer valor: "))
        numero/=float(input("Inserte el segundo valor: "))
        print("\nEl resultado de la división es: ", round(numero,2))
    elif numero==5:
        numero=float(input("\n|Ha elegido división entera|\nInserte el primer valor: "))
        numero//=float(input("Inserte el segundo valor: "))
        print("\nEl resultado de la división entera es: ", round(numero,0))
    elif numero==6:
        numero=float(input("\n|Ha elegido exponente|\nInserte el primer valor: "))
        numero**=float(input("Inserte el segundo valor: "))
        print("\nEl resultado del exponente es: ", numero)
    else:
        numero=float(input("\n|Ha elegido módulo o resto|\nInserte el primer valor: "))
        numero%=float(input("Inserte el segundo valor: "))
        print("\nEl resultado del módulo o resto es: ", numero)

    print("\nInserte 1° para continuar\nInserte 2° para finalizar")
    repetir=int(input("\n¿Desea hacer otra operación?:"))
    while repetir<1 or repetir>2:
        print("\nHa ingresado una opción que no existe, por favor ingrese una opción válida.\n")
        print("\nInserte 1° para continuar\nInserte 2° para finalizar")
        repetir=int(input("\n¿Desea hacer otra operación?: \n"))

print("Ha decidido finalizar. Hasta luego!")

