from infra.entities.turmas import Turmas
from infra.configs.connection import DBConnectionHandler

class TurmasRepository:
  def select(self):
    with DBConnectionHandler() as db:
      return db.session.query(Turmas).all()
    
  def insert(self, curso):
    with DBConnectionHandler() as db:
      insert_data = Turmas(curso=curso)

      db.session.add(insert_data)
      db.session.commit()