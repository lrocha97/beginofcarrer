class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def Saudacao(self):
        print(f'Seja bem vindo {self.nome}')

    def Deposito(self):
        dep = int(input('Digite o valor que deseja depositar em sua conta: '))
        self.saldo = dep + self.saldo

    def Saque(self):
        if self.saldo <= 0:
            print('Não é possível realizar o saque pois a conta está com saldo NEGATIVO!')

        else:
            saque = int(input('Digite a o valor em reais que deseja sacar: R$ '))
            if saque > self.saldo:
                print(f'Não é possível realizar o saque pois seu saldo é de R$ : {self.saldo}')
            else:
                self.saldo = self.saldo - saque
            
        
    def Saldo(self):
        print(f'Seu saldo é de R$: {self.saldo}')

conta1 = Conta('Lucas', 10321, 3215, 1500 )

while True:
    conta1.Saudacao()
    print("Opções do Banco Quebrado")
    print("Opção 1: Depositar")
    print("Opção 2: Sacar")
    print("Opção 3: Verificar Saldo")
    print("Opção 4: SAIR")
    
    o=int(input("Digite uma opção acima: "))

    if o == 1:
        conta1.Deposito()

    elif o == 2:
        conta1.Saque()

    elif o == 3:
        conta1.Saldo()

    else:
        print('Obrigado por utlizar nosso aplicativo!')
        break

    