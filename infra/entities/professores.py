from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from infra.configs.base import Base
from infra.entities.turmas_professor import turmas_professor


class Professores(Base):
  __tablename__ = "professores"

  id: int = Column(Integer, primary_key=True, autoincrement=True)
  nome: str = Column(String(255), nullable=False)
  especialidade: str = Column(String(255), nullable=False)
  turmas = relationship("Turmas", secondary=turmas_professor, back_populates="professores")

  def __repr__(self):
    return f"Professor: [id={self.id}, nome={self.nome}, especialidade={self.especialidade}]"