P = float((input("Quantos pães foram vendidos?: ")))
B = float((input("Quantas broas foram vendidas?: ")))
soma = (P*0.12)+(B*1.5)
poupança = (soma/100)*10
print ("Foi vendido o valor total de: R$" , soma, "e tem que que guardar: R$", poupança)