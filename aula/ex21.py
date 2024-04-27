caractere = input("Digite um caractere: ")

vogal = ["A","a","E","e","I","i","O","o","U","u"]
numero = ["0","1","2","3","4","5","6","7","8","9"]
consoante = ["B","b","C","c","D","d","F","f","G","g","H","h","J","j","K","k","L","l","M","m","N","n","P","p","Q","q","R","r","S","s","T","t","V","v","X","x","Y","y","Z","z"]
controle = False

for i in range(len(vogal)):
    if caractere == vogal[i]:
        print("O caractere é uma vogal")

for i in range(len(numero)):
    if caractere == numero[i]:
        print("O caractere é um número")

for i in range(len(consoante)):
    if caractere == consoante[i]:
        print("O caractere é uma consoante")
        controle = True

if controle == False:
    print("O caracter é um caracter especial")