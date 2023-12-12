from classes import projeto as pjt

def imprimir_saida(emparelhamento : list[pjt.Projeto], logs : list[str]):
    alunos_emparelhados = 0
    for projeto in emparelhamento:
        alunos_emparelhados += len(projeto.alunos)

    with open("saidaProj2Tag.txt", 'w') as saida:
        saida.write("Log de iterações:\n")
        for log in logs:
            saida.write(f"\t{log}\n")

        saida.write('\n')

        saida.write(f"Emparelhamento máximo e estável com {alunos_emparelhados} pares Projetos x Alunos:\n")
        for projeto in emparelhamento:
            saida.write(f"\t{projeto.id} : {projeto.alunos if projeto.alunos else 'vazio'}\n")

        saida.close()