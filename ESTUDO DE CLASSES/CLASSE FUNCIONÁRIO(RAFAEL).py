class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhads = horas_trabalhadas
        self.valor_hora = valor_hora
        
        #NomeCompleto OKAY
    def NomeCompleto(self):
        print(f'O nome do funcionário é: {self.nome} {self.sobrenome}')

    def CalcularSalario(self):
        salario = self.horas_trabalhads * self.valor_hora
        print(f'O salário do funcionário {self.nome} {self.sobrenome} é de R$: {salario}')

    def IncrementarHoras(self, nova_hora):
        self.valor_hora = nova_hora
        salario = salario = self.horas_trabalhads * self.valor_hora
        print(f'O novo salário do funcionário {self.nome} {self.sobrenome} é de R$: {salario}')

f1 = Funcionario('Lucas', 'Rocha', 220, 6.42)

f1.NomeCompleto()
f1.CalcularSalario()
f1.IncrementarHoras(10)

