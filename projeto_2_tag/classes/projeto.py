class Projeto:
    def __init__(self, id, vagas, nota_min, alunos = None) -> None:
        self.id = id
        self.vagas = vagas
        self.nota_min = nota_min
        self.alunos = [] if alunos == None else alunos

    def is_full(self):
        return len(self.alunos) == self.vagas
    
    def add_aluno(self, id_aluno: str):
        if not self.is_full():
            self.alunos.append(id_aluno)

    def rmv_aluno(self, id_aluno: str):
        self.alunos.remove(id_aluno)
