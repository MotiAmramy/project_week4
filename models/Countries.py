from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base


class countries(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(100), unique=True, nullable=False)





    cities = relationship('cities', back_populates='country')











    def __repr__(self):
        return f"<Country(id={self.country_id}, name='{self.country_name}')>"