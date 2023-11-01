from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Alunos(Base):
  __tablename__ = "alunos"

  id: int = Column(Integer, primary_key=True, autoincrement=True)
  nome: str = Column(String(255), nullable=False)
  cpf: str = Column(String(11), nullable=False, unique=True)
  turma_id: int = Column(Integer, ForeignKey("turmas.id"))

  def __repr__(self):
    return f"Aluno [id: {self.id}, nome={self.nome}, cpf={self.cpf}, turma={self.turma_id}"