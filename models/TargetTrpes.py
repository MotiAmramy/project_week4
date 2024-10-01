from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.base import Base


class targettypes(Base):
    __tablename__ = 'targettypes'

    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String(255), unique=True, nullable=False)

    targets = relationship('targets', back_populates='target_type')

    def __repr__(self):
        return f"<TargetType(id={self.target_type_id}, name='{self.target_type_name}')>"

