from classes import projeto as pjt
from classes import aluno as aln
from copy import copy

def gale_shapley(projetos: dict[str, pjt.Projeto], alunos: dict[str, aln.Aluno]):
    # funcao que troca alunos de um projeto
    def troca_alunos(aluno : aln.Aluno, aluno_no_projeto : aln.Aluno, projeto : pjt.Projeto):
        projeto.rmv_aluno(aluno_no_projeto.id)
        projeto.add_aluno(aluno.id)
        aluno_no_projeto.projetos_desejados.remove(projeto.id)
        alunos_livres.append(aluno_no_projeto.id)
        projetos[projeto.id] = projeto

        log.append(f"{projeto.id} troca {aluno_no_projeto.id} pelo {aluno.id}")

    alunos_livres = [aluno for aluno in alunos.keys()]
    log = []

    while alunos_livres:
        aluno = alunos[alunos_livres[0]]
        alunos_livres.pop(0)

        for projeto in aluno.projetos_desejados:
            projeto = copy(projetos[projeto])

            # projeto nao-cheio e aluno com nota suficiente
            if not projeto.is_full() and aluno.nota >= projeto.nota_min:
                projeto.add_aluno(aluno.id)
                projetos[projeto.id] = projeto
                
                log.append(f"{projeto.id} aceita {aluno.id}")
                break
            
            # projeto cheio e aluno com nota suficiente
            elif projeto.is_full() and aluno.nota >= projeto.nota_min:
                # procura o pior aluno do projeto para troca-lo, se possivel
                for aluno_no_projeto in projeto.alunos:
                    aluno_no_projeto = alunos[aluno_no_projeto]

                    # nota melhor que a do pior aluno
                    if aluno.nota > aluno_no_projeto.nota:
                        troca_alunos(aluno, aluno_no_projeto, projeto)
                        break

                    # se possuirem ambos a mesma nota, avalia-se a preferencia dos alunos
                    elif aluno.nota == aluno_no_projeto.nota:
                        pref_aluno = aluno.projetos_desejados.index(projeto.id)
                        pref_aluno_no_projeto = aluno_no_projeto.projetos_desejados.index(projeto.id)

                        if pref_aluno < pref_aluno_no_projeto:
                            troca_alunos(aluno,aluno_no_projeto,projeto)
                            break

            # rejeitado pelo projeto
            log.append(f"{projeto.id} rejeita {aluno.id}")
    
    return (list(projetos.values()),log)

