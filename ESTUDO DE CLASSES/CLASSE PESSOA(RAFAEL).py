class Pessoa():
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def MostrarNome(self):
        print(f"O nome é: {self.nome}")

    def MostrarIdade(self,):
        print(f'A sua idade é: {self.idade}')

    def AlterarIdade(self):
        NovaIdade = input("Digite sua nova idade: ")
        self.idade = NovaIdade

    def MostrarEndereco(self):
        print(f"Seu endereço é: {self.endereco}")

pessoa1 = Pessoa('Lucas', 27, 'Av. Souza Lima')

while True:
    print('Olá')
    a = input('Deseja trocar sua idade? ')

    if a == 'Sim' or a == 'sim':
        pessoa1.AlterarIdade()

    else:
        pessoa1.MostrarNome()
        pessoa1.MostrarIdade()
        pessoa1.MostrarEndereco()
        break