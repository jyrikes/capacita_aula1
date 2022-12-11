class Ponto():

    def __init__(self) :
        self.x = float(input("Digite o valor x do  ponto "))
        self.y = float(input("Digite o valor y do  ponto "))
       
    def distancia(self,ponto):
        x2 = ponto.x
        y2 = ponto.y
        x1 = self.x
        y1 = self.y
        deltax = x2 - x1
        deltay = y2 - y1
        dis = ((deltax**2)+(deltay**2))**1/2
        return dis
    
        
if __name__ == '__main__':
    
    p1 = Ponto()
    pontos = []
    for i in range(5):
        print("Digite mais um ponto\n")
        pontos.append(Ponto())

        print("A distância do ponto 1 para o ponto ", i+2 , " é " , p1.distancia(pontos[i]))

   