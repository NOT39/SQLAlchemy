from infra.repository.alunos_repository import AlunosRepository
from infra.repository.professores_repository import ProfessoresRepository
from infra.repository.turmas_repository import TurmasRepository

alunos_repo = AlunosRepository()
professores_repo = ProfessoresRepository()
turmas_repo = TurmasRepository()

# turmas_repo.insert("DEV FS")

# alunos_repo.insert(cpf="11111111111", nome="Cleber", turma_id=1)
# alunos_repo.insert(cpf="22222222222", nome="Roberto", turma_id=1)

# alunos_repo.update(id=1, novo_aluno={"nome": "Robinho"})

# alunos_repo.delete(2)


data = alunos_repo.select()
# data = professores_repo.select()
# data = turmas_repo.select()
print(data)