class Escola:
    def __init__(self):
        self.turmas = []

    def AdicionarTurma(self):
        pass


class Aluno:
    def __init__(self, nome, turma, notas:list):
        self.nome = nome
        self.turma = turma
        self.notas = notas

    def AtualizarAluno(self):

        pass


class Turmas:
    def __init__(self):
        self.turmas = []

    def CadastrarAluno(self):
        notas = []
        nome = input('Digite o nome do Aluno: ')
        turma = input(f'Digite a turma do Aluno {nome}: ')
        while len(notas) < 4:
            nota = float(input(f'Digite uma nota para o Aluno {nome}: '))
            notas.append(nota)  
        aluno = Aluno(nome,turma,notas)
        self.turmas.append(aluno)
    
    def ShowTurmas(self):
        for i in self.turmas:
            print(f'{i.nome}')
            print(f'{i.turma}')

    def AtualizarNomeAluno(self):
        for i in self.turmas:
            nome = input('Digite o nome do Aluno: ')
            if i.nome == nome:
                novonome = input(f'Corrija o nome do Aluno {i.nome}')
                i.nome = novonome

    def AtualizarNotaAluno(self): 
        nome = input("Digite o nome do Aluno: ")
        for i in self.turmas:
            if i.nome == nome:
                indice = 1
                for j in range(len(i.notas)):
                    print(f"As notas do ALUNO: {nome} são: {indice} - {i.notas[j]}")
                    indice += 1
                alterarnota = int(input('Digite a nota que deseja ALTERAR: ')) - 1
                novanota = float(input(f'Digite a NOVA NOTA do ALUNO {nome}'))
                i.notas[alterarnota] = novanota
                print(i.notas)

    def RemoverTurma(self):
        nome = input('Digite o nome do ALUNO: ')
        turma = input(f'Digite a TURMA do ALUNO: {nome} ')
        for i in self.turmas:
            if i.nome == nome and i.turma == turma:
                decisao = str(input(f'Deseja retirar o ALUNO: {i.nome} da sua TURMA: {i.turma}?. Responda com SIM ou NÃO. ')).upper() 
                if decisao == 'SIM':
                    i.turma == None
                    print(f'O ALUNO não pertence mais a uma TURMA!')
                else:
                    print(f'O ALUNO: {nome}, PERMANECEU na mesma TURMA: {i.turma}!')
    


aluno = Turmas()

aluno.CadastrarAluno()
aluno.RemoverTurma()
aluno.ShowTurmas