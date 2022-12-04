numerosPares= 0
numerosImpares = 0
for i in range (5):
    numero = int(input("Digite um número :"))
    if numero%2 ==0:
        numerosPares = numerosPares + 1
    else:
        numerosImpares = numerosImpares+1
print("Pares: ",numerosPares)
print("Impares",numerosImpares)