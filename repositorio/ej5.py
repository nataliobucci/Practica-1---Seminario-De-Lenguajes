numeros = input("ingrese los numeros separados por coma: ").split(",")
for i in numeros:
    if int(i) < 0:
        break
    else:
        print(i)