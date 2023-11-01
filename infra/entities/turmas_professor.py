from sqlalchemy import Table, Column, ForeignKey

from infra.configs.base import Base

turmas_professor = Table("turmas_professor",
                          Base.metadata,
                          Column("turma_id", ForeignKey("turmas.id"), primary_key=True),
                          Column("professor_id", ForeignKey("professores.id"), primary_key=True)
                        )