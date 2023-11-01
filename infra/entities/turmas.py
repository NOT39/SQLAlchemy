from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from infra.configs.base import Base
from infra.entities.turmas_professor import turmas_professor

class Turmas(Base):
  __tablename__ = "turmas"

  id: int = Column(Integer, primary_key=True, autoincrement=True)
  curso: str = Column(String(255), nullable=False)
  alunos = relationship("Alunos", backref="alunos")
  professores = relationship("Professores", secondary=turmas_professor, back_populates="turmas")

  def __repr__(self):
    return f"Turma: [id={self.id}, curso={self.curso}]"