def lerTempo(mensagem):
    
    hora = 90
    minuto = 90
    while not(hora <=24 and hora>=0):
        hora = int(input("Hora {}: ".format(mensagem)))

    while not (minuto <=60 and minuto>=0):
        minuto = int(input("Minuto {}: ".format(mensagem)))
    tempo = (hora,minuto)
    return tempo


horaInicial,minutoInicial = lerTempo("Inicial")
horaFinal,minutoFinal = lerTempo("Final")

horaConvertida = (horaFinal - horaInicial) * 60
diferecaMinutos = minutoFinal-minutoInicial
somaMinutos = diferecaMinutos + horaConvertida

horas = somaMinutos//60
minutos = diferecaMinutos %60

if(horas < 0 ):
    horas = 24 + horas

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas,minutos) )
