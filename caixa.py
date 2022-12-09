import time

log = open("teste.txt", "r+")
totalPago = 0
numeroPrestacoes = 0


def valorPagamento(prestacao,diasAtrasados):
    if diasAtrasados >=0:

        if diasAtrasados == 0 :
            return prestacao
        else:
            multa = prestacao * 0.03
            prestacao = prestacao *((1+0.001)**diasAtrasados)
            prestacao = prestacao + multa
            return prestacao
    else:
        return None
#--------------------------------------------------------------------------------------------------------------
print("Caixa de prestações \n \n          OPERAÇÕES INICIADAS\n")

prestacao = -1
while(prestacao != 0):
   
    prestacao = float(input("Digite o valor da prestação : "))

    if(prestacao ==0):
        break
    numeroPrestacoes = numeroPrestacoes + 1
    diasAtrasados = int(input("Digite a quantidade de dias atrasados : "))
    
    prestacao = valorPagamento(prestacao,diasAtrasados)
    prestacao = round(prestacao,2)
    
    while(prestacao == None):
        print("Digite uma quantidade válida de prestações")
        diasAtrasados = int(input("Digite a quantidade de dias atrasados : "))
        prestacao = valorPagamento(prestacao,diasAtrasados)
    totalPago = totalPago + prestacao
    
    log.writelines("Prestação : "+str(prestacao)
    +"|  "+"Valor Acumulado : "
    +str(totalPago)+"|  "+"Nº : "
    +str(numeroPrestacoes)+"\n")
    time.sleep(0.1)

    print("\n O cliente pagará R$ {}\n".format(prestacao))

print("\nRelatório da execução:\n"
"       Valor total das prestações : R$ {}\n"
"       Número total de parcelas    :    {}\n "
"\nPara o relatório de todas execuções digite 1".format(totalPago,numeroPrestacoes))
ques = int(input())
if ques == 1 :

    print("\n")
    for linha in log:
        print(linha)
    print("\n")

else:
    print("Obrigado por usar nosso serviço :)")

log.close()