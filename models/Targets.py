from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from config.base import Base


class targets(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)

    city = relationship('cities', back_populates='targets')
    target_type = relationship('targettypes', back_populates='targets')

    def __repr__(self):
        return (f"<Target(id={self.target_id}, industry='{self.target_industry}', "
                f"city_id={self.city_id}, target_type_id={self.target_type_id}, "
                f"priority={self.target_priority})>")
