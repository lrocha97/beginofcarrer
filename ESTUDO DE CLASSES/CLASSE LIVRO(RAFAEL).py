class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def NomeLivro(self):
        nomelivro = input("Digite o NOME do Livro")
        self.nome = nomelivro

    def MostrarNomeLivro(self):
        print(f'O nome do LIVRO é: {self.nome}')

    def NomeAutor(self):
        nomeautor = input('Digite o AUTOR do Livro: ')
        self.autor = nomeautor

    def MostrarNomeAutor(self):
        print(f'O nome do AUTOR é: {self.autor}')
        
    def NomeEditora(self):
        nomeeditora = input('Digite a EDITORA do Livro: ')
        self.editora = nomeeditora

    def NovaEditora(self):
        novaeditora = input('Digite o nome da NOVA EDITORA: ')
        self.editora = novaeditora

    def MostrarEditora(self):
        print(f'O nome da EDITORA é: {self.editora}')


    def QtdPaginas(self):
        qtdpaginas = input('Digite a Quantidade de PÁGINAS do Livro: ')
        self.paginas = qtdpaginas

    def MostrarQtdPaginas(self):
        print(f'A quantidade de PÁGINAS é: {self.paginas}')


livro1 = Livro('O Pequeno Príncipe', 'BIENAL', 'RIO DE JANEIRO', 50560)

while True:
    print('Olá')
    a = input('Deseja trocar sua EDITORA? ')

    if a == 'Sim' or a == 'sim':
        livro1.NovaEditora
    else:
        livro1.MostrarNomeLivro()
        livro1.MostrarNomeAutor()
        livro1.MostrarEditora()
        livro1.MostrarQtdPaginas()
        break
