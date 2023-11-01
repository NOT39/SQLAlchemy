from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infra.configs.base import Base

class DBConnectionHandler:
  def __init__(self):
    self.__connection_string = 'sqlite:///infra/db/teste.sqlite'
    self.__engine = self.__create_database_engine()
    self.session = None

  def __create_database_engine(self):
    return create_engine(self.__connection_string)
  
  def get_engine(self):
    return self.__engine
  
  def __enter__(self):
    Base.metadata.create_all(bind=self.__engine)
    
    session_make = sessionmaker(bind=self.__engine)
    self.session = session_make()
    return self
  
  def __exit__(self, exc_type, exc_value, exc_tb):
    self.session.close()