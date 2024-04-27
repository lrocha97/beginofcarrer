salario = float(input("digite um salario: "))

valor_para_desconto =  (salario*11) /100

if(valor_para_desconto>332.29):
    valor_para_desconto = 332.29
salario_desconto = salario- valor_para_desconto
print("salario com desconto: ", salario_desconto)