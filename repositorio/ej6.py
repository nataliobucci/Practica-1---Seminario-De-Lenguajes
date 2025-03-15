numeros = input("ingrese los numeros separados por coma: ").split(",")

pares=[]
impares=[]    

for i in numeros:
    if int(i) < 0:
        break
    if int(i)%2==0:
        pares.append(i)
    else:
        impares.append(i)
print("pares: ", pares)
print("impares: ", impares)

