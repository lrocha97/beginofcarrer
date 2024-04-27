metros = float(input("Quantidade metros da área: "))

litros = metros/6
print("Quantidade de litros necessários: ", litros)

#Calculando a quantidade de latas para pintar a área desejada ( só estou pegando a parte inteira da divisão )
qtdLatas = litros // 18
if litros % 18 !=0:
qtdLatas = qtdLatas + 1

print("Quantidade de latas de 18 litros: ", qtdLatas)
preco_latas = qtdLatas*80.00
print("valor da compra das latas R$: ", preco_latas)


qtdGaloes = litros // 3.6
if litros % 3.6 !=0:
qtdGaloes = qtdGaloes + 1

print("Quantidade de galões de 3.6 litros: ", qtdGaloes)
preco_galoes = qtdGaloes*25.00
print("valor da compra das latas R$: ", preco_galoes)

#cobertura de area da lata de 18 L
cobertura_latas = 18 * 6
cobertura_galao = 3.6 * 6


qtd_latas_mistura = int(metros/cobertura_latas)

#tamanho da area contemplada com as latas
area_comtemp = qtd_latas_mistura * cobertura_latas

#tamanho da area que falta
area_falta = metros - area_comtemp

litros_galao_mistura = area_falta / 6

qtd_galao_mistura = int(litros_galao_mistura/3.6)
if litros_galao_mistura % 3.6 !=0:
qtd_galao_mistura = qtd_galao_mistura + 1

print("Quantidade de galoes de mistura: ", qtd_galao_mistura)

print("PREÇO: ", ((qtd_latas_mistura*80.00) + (qtd_galao_mistura * 25.00)))