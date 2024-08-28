alunos = [
    {"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
    {"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},
    {"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}
]


def media(aluno):
    aluno['media'] = round(sum(aluno['notas']) / len(aluno['notas']), 2)
    return aluno

def is_aprovado(aluno):
    return aluno['media'] >= 7
       

def extrair_media(aluno):
    return aluno['media']


aprovados = []
for aluno in filter(is_aprovado, list(map(media, alunos))):
    aprovados.append(aluno)

print(sorted(aprovados, key=extrair_media, reverse=True))



