from infra.entities.professores import Professores
from infra.configs.connection import DBConnectionHandler

class ProfessoresRepository:
  def select(self):
    with DBConnectionHandler() as db:
      return db.session.query(Professores).all()