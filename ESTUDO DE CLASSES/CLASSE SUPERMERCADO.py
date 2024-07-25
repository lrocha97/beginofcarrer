class Produto:
    def __init__(self, nome, quantidade):
        self.nome =  nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.estoque = []

    def AdicionarAoEstoque(self):
        nome = input('Digite o nome do PRODUTO: ')
        quantidade = int(input(f'Digite a QUANTIDADE do produto {nome}: '))
        produto = Produto(nome, quantidade)
        self.estoque.append(produto)

    def ConsultarEstoque(self):
        for i in self.estoque:
            print(f'{i.nome}: {i.quantidade}')

    def AtualizarEstoque(self):
        produto = input('Digite o PRODUTO que deseja ATUALIZAR: ')
        for i in self.estoque:
            if i.nome == produto:
                print(f'{i.nome} tem atualmente o total de: {i.quantidade}')
                novaquantidade = int(input(f'Digite a nova QUANTIDADE do {produto}: '))
                i.quantidade += novaquantidade
            else:
                print('PRODUTO NÃO CADASTRADO OU ESCRITO ERRADO!!!')

produto = Estoque()
print('Seja bem vindo ao GERENCIAMENTO DE ESTOQUE!')
while True:
    print("Opções do Estoque")
    print("Opção 1: Adicionar Produto")
    print("Opção 2: Atualizar Estoque")
    print("Opção 3: Consultar Estoque")
    print("Opção 4: SAIR")

    op = int(input('Digite uma das opções acima: '))

    if op == 1:
        produto.AdicionarAoEstoque()

    elif op == 2:
        produto.AtualizarEstoque()

    elif op == 3:
        produto.ConsultarEstoque()

    else:
        print('Obrigado por utilizar nosso sistema!!! :)')
        break