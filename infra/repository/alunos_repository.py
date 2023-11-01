from infra.configs.connection import DBConnectionHandler
from infra.entities.alunos import Alunos
from infra.entities.turmas import Turmas

class AlunosRepository():

  def select(self):
    with DBConnectionHandler() as db:
      data = db.session.query(Alunos, Turmas).join(Turmas, Alunos.turma_id == Turmas.id).with_entities(Alunos.id, Alunos.cpf, Alunos.nome, Turmas.curso).all()
      return data
    
  def insert(self, nome: str, cpf: str, turma_id: int):
    with DBConnectionHandler() as db:
      insert_data = Alunos(nome=nome, cpf=cpf, turma_id=turma_id)

      db.session.add(insert_data)
      db.session.commit()
  
  def update(self, id: int, novo_aluno: dict):
    with DBConnectionHandler() as db:
      db.session.query(Alunos).filter(Alunos.id == id).update(novo_aluno)

      db.session.commit()
    
  def delete(self, id: int):
    with DBConnectionHandler() as db:
      db.session.query(Alunos).filter(Alunos.id == id).delete()

      db.session.commit()