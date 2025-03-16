numeros = input("ingrese los numeros ").split()
cadena = " "
for i in numeros:
    if int(i) % 3 ==0:
        continue
    else:   
        cadena += str(i) + "-"
print(cadena)