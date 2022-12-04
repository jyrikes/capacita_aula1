horaInicial = int(input("Hora inicial: "))
minutoInicial = int(input("Minuto inical")) 
while not(horaInicial <=24 and horaInicial>=0):
    horaInicial = int(input("Hora inicial: "))

while not (minutoInicial <=60 and minutoInicial>=0):
    minutoInicial = int(input("Minuto inical"))

horaFinal = int(input("Hora Final: "))
minutoFinal = int(input("Minuto Final")) 

while not(horaFinal <=24 and horaFinal>=0):
    horaFinal = int(input("Hora Final: "))

while not (minutoInicial <=60 and minutoInicial>=0):
    minutoFinal = int(input("Minuto Final"))

horaConvertida = (horaFinal - horaInicial) * 60
diferecaMinutos = minutoFinal-minutoInicial

somaMinutos = diferecaMinutos + horaConvertida

horas = int(somaMinutos/60)
minutos = diferecaMinutos %60



print(horas)


print(minutos)
