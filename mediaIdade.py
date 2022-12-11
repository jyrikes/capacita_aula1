idade = 0
somaIdade = 0
contador =0

while idade >= 0:
  #Observe que idades podem ser valores flutuantes !!
    idade = float(input("Digite a idade: "))
    idade = int(idade)
    somaIdade = somaIdade + idade
    contador = contador +1

somaIdade = somaIdade - idade
contador = contador - 1

    
print("A média das idades é {} anos ".format(somaIdade/contador))
