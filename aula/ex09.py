distancia = float(input("Digite a distância: "))
pedagio = float(input("Digite quantos pedágios tem: "))

CP = pedagio*8
GG = (distancia/15)*5.30
GV = CP+GG

print("Será gasto na viagem: R$ ", GV)