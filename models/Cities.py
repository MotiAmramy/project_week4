from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from config.base import Base


class cities(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)

    country = relationship('countries', back_populates='cities')
    targets = relationship('targets', back_populates='city')

    def __repr__(self):
        return f"<City(id={self.city_id}, name='{self.city_name}', country_id={self.country_id})>"
