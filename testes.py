# [{"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},{"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},] -> Caso "Normal"
# [{"notas": [8.5, 9.0, 7.5], "curso": "Matemática"}]
# [{"nome": "Alice", "curso": "Matemática"}]
# [{"nome": "Alice", "notas": [8.5, 9.0, 7.5]}]
# [{"nome": 123, "notas": [8.5, 9.0, 7.5], "curso": "Matemática"}]
# [{"nome": 123, "notas": [8.5, 9.0, 7.5], "curso": "Matemática"}]
# Caso com nenhum argumento
# Caso aluno aprovado
# Caso aluno reprovado
# Caso números negativos
# Caso lista em ordem não decrescente
def media(notas):
    return sum(notas) / len(notas)

def aluno_aprovado(aluno, nota_minima=7.0):
    return media(aluno['notas']) >= nota_minima
    
alunos = [
    {"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
    {"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},
    {"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}
]

alunos_aprovados = list(filter(aluno_aprovado, alunos))
            
print(alunos_aprovados)

