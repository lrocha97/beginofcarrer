class Barbearia:
    def __init__(self):
        self.agendamentos = []

    def Agendar(self):
        cliente = input('Olá seja bem vindo ao nosso AGENDAMENTO ONLINE, qual o seu NOME? ')
        data = input('Qual o dia da semana gostaria de marcar seu(s) serviço(s)? ')
        hora = input(f'Qual HORA do dia escolhido,{data}, gostaria de marcar seu(s) serviço(s)? ')
        agenda = Agendamento(cliente, data, hora)
        agenda.SaberServico()
        print(f'CLIENTE {cliente} FOI AGENDADO COM SUSCESSO!')
        self.agendamentos.append(agenda)

    def VisuAgenda(self):
        if len(self.agendamentos) <1:
            print('NÃO HÁ CLIENTES AGENDADOS!!!')
        else:
            for i in self.agendamentos:
                print("CLIENTE: ", i.cliente)
                print("DATA: ", i.data)
                print("HORA: ", i.hora)
                print("SERVIÇO: ", i.servico)

    def CancelarAgenda(self):
        nome = input('Digite o nome do CLIENTE que deseja CANCELAR o AGENDAMENTO: ')
        variavel = True
        for i in self.agendamentos:
            if i.cliente == nome:
                self.agendamentos.remove(i)
                print(f'CLIENTE {nome} TEVE SEU AGENDAMENTO CANCELADO!')
                variavel = False
        if variavel == True:
            print('CLIENTE NÃO ENCONTRADO!!')
        
class Agendamento:  
    def __init__(self,cliente, data, hora):
        self.cliente = cliente
        self.data = data
        self.hora = hora
        self.lsita_servico = ["1 - CORTAR CABELO.","2 - FAZER A BARBA.","3 - CORTAR CABELO E FAZER A BARBA.", "4 - SAIR"]
        self.servico = []

    def SaberServico(self):
        
        for i in self.lsita_servico:
            print(i)
        op = int(input('Quais dos serviços deseja? 1, 2, 3 ou 4?? '))
        if op == 1:
            self.servico.append('CORTAR CABELO')
        elif op == 2:
            self.servico.append('FAZER A BARBA')
        elif op == 3:
            self.servico.append('CORTAR CABELO E FAZER A BARBA')
        elif op == 4:
            print('OBRIGADO POR USAR NOSSO SISTEMA. VOLTE SEMPRE!!!')

cliente = Barbearia()

print('SEJA BEM VINDO A BARBEARIA NOVA IMAGEM')
while True:

    print('1 - DESEJA REALIZAR UM AGENDAMENTO?')
    print('2 - DESEJA VISUALIZAR A AGENDA?')
    print('3 - DESEJA CANCELAR UM AGENDAMENTO?')
    print('4 - SAIR?')
    op = int(input('Digite uma das opções: '))

    if op == 1:
        cliente.Agendar()
    elif op == 2:
        cliente.VisuAgenda()
    elif op == 3:
        cliente.CancelarAgenda()
    elif op == 4:
        print('OBRIGADO POR USAR NOSSO SISTEMA!!!')
        break