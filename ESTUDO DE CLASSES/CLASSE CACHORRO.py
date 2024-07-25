class Coleira:
    #método construtor
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
    
    def mostrar_marca(self):
        print(self.marca)
        
    def mostrar_cor(self):
        print(self.cor)


class Cachorro:
    #método construtor
    def __init__(self, cor, raca, tamanho, sexo, coleira) :
        self.cor = cor
        self.raca = raca
        self.tamanho = tamanho
        self.sexo = sexo
        self.coleira = coleira

    def mostrar_cor(self):
        print(self.cor)
    
    def mostrar_raca(self):
        print(self.raca)

    def mostrar_tamanho(self):
        print(self.tamanho)

    def mostrar_sexo(self):
        print(self.sexo)

    def alterar_cor(self, nova_cor):
        self.cor = nova_cor

    def alterar_raca(self, nova_raca):
        self.raca = nova_raca

    def alterar_tamanho(self, novo_tamanho):
        self.raca = novo_tamanho
    
    def alterar_sexo(self, novo_sexo):
        self.raca = novo_sexo
    
obj_coleira = Coleira('nikedog', 'azul')

obj_pinsher = Cachorro('preta', 'pinsher', 10, 'femino', obj_coleira)
obj_dalmata = Cachorro('Branco com machas pretas', 'Dalmata', 100, 'macho', None)



obj_pinsher.mostrar_raca()
obj_pinsher.mostrar_cor()
obj_pinsher.mostrar_tamanho()
obj_pinsher.mostrar_sexo()
obj_pinsher.coleira.mostrar_marca()
obj_pinsher.coleira.mostrar_cor()

obj_dalmata.mostrar_raca()
obj_dalmata.mostrar_cor()
obj_dalmata.mostrar_tamanho()
obj_dalmata.mostrar_sexo()
