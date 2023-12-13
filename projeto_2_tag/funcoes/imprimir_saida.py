from classes import projeto as pjt
from classes import aluno as aln

def imprimir_saida(emparelhamento : list[pjt.Projeto], logs : list[str]):
    pares = 0
    for projeto in emparelhamento:
        pares += len(projeto.alunos)

    with open("saidaProj2Tag.txt", 'w') as saida:
        saida.write("Log de iterações:\n")
        for log in logs:
            saida.write(f"\t{log}\n")

        saida.write('\n')

        saida.write(f"Emparelhamento máximo e estável com {pares} pares Projetos x Alunos:\n")
        for projeto in emparelhamento:
            for aluno in projeto.alunos:
                saida.write(f"\t{projeto.id, aluno}\n")

        saida.close()