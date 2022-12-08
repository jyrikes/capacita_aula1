def calculaSalario(salarioBruto):
    #Basta multiplicar ((100-11)/100) *((100-15)/100) -> fator de conversão para salário líquido
    salarioLiquido = salarioBruto * 0.7565
    return salarioLiquido

#teste da função 
salarioBruto = float(input("Digite o seu salário Bruto :"))
print("O seu salário líquido é : R$ {:.2f}".format(calculaSalario(salarioBruto)))

