from classes import aluno as aln
from classes import projeto as pjt

def tira_espacos(x: str):
    return x.strip()

def ler_entrada(arquivo):
    projetos, alunos = {}, {}
    with open(arquivo, 'r') as entrada:
        for linha in entrada:
            if "/" in linha: continue
            linha = linha.strip('\n')

            if linha == '': continue
            linha = linha.replace('(','')
            linha = linha.replace(')','')

            if len(projetos) < 50:
                id,vagas,nota_min = map(tira_espacos, linha.split(','))
                pi = pjt.Projeto(id, int(vagas), int(nota_min))
                projetos[id] = pi
                continue

            id, dados = linha.split(':')
            pjt_aluno, nota = [x.strip() for x in dados[:len(dados)-1].split(',')], int(dados[-1])
            ai = aln.Aluno(id,pjt_aluno,nota)
            alunos[id] = ai

        entrada.close()

        return [projetos, alunos]
        