alunos_turma = int(input("alunos_turma: "))
alunos_presentes = int(input("alunos presentes: "))
turma = str(input("turma: "))

alunos_ausentes =  alunos_turma-alunos_presentes

porcentagem_ausentes = (alunos_presentes/alunos_turma)*100

print("porcentagem de alunos ausentes: ", porcentagem_ausentes, "da turma: ", turma.upper())

quantidade = 14

while quantidade > 0:
    id = input("Identificação da turma: ")
    n_mat = int(input("Número de alunos: "))
    lista = []
    cont = 0
    total_alunos = n_mat
    while n_mat > 0:
        matricula = input("Matricula do aluno: ")
        chamada = input("A ou P: ")
        lista.append([n_mat, chamada])
        n_mat = n_mat -1

    for i in range (len(lista)):
        if lista[i][1] == "A":
            cont = cont + 1
    quantidade = quantidade -1
    ausencia = cont / total_alunos
    print("A porcentagem de ausentes é: ", ausencia)