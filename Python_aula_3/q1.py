lista_alunos = []

while True:
    nome = str(input("Digite um nome: "))
    if nome == "fim":
        break
    nota = float(input("Digite uma nota: "))
    lista_alunos.append([nome, nota])

maior_nota = 0
melhor_aluno = ""

for aluno in lista_alunos:
    if aluno[1] > maior_nota:
        maior_nota = aluno[1]
        melhor_aluno = aluno[0]

print(f"O melhor aluno foi {melhor_aluno} com a nota {maior_nota}")
