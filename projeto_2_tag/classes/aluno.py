class Aluno:
    def __init__(self, id, projetos, nota) -> None:
        self.id = id
        self.projetos_desejados = projetos
        self.nota = nota
    
    def __str__(self) -> str:
        return f"Aluno {self.id}"