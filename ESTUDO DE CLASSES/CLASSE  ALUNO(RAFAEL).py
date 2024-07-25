class Aluno:
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra
        self.notas = []

    def GerarNomeAluno(self):
        nomealuno = input("Digite o nome do Aluno")
        self.nome = nomealuno

    def GerarRaAluno(self):
        ra = input('Digite o RA do Aluno: ')
        self.ra = ra

    def GerarListaNotas(self):
        while len(self.notas) < 4:
            nota = int(input('Digite uma nota: '))
            self.notas.append(nota)
    
    def Media(self):
        media = sum(self.notas)/len(self.notas)
        
        if media >= 7:
            print(f'O Aluno: {self.nome}, com média: {media}, foi APROVADO!\nPARABÉNS!!!')

        if media == 5 or media <=6.9:
            print(f'O Aluno: {self.nome},com média: {media}, está de EXAME.\nVamos nos empenhar um pouco mais!!!')
        
        if media < 5:
            print(f'O Aluno: {self.nome}, com média {media}, infelizmente não passou!')



aluno1 = Aluno('Lucas', 252525)

aluno1.GerarListaNotas()
aluno1.Media()