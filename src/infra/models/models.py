from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from infra.config.database import Base

class UData(Base):
    __tablename__ = 'u_data'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    item_id = Column(String)
    rating = Column(String)
    timestamp = Column(String)


class UItem(Base):
    __tablename__ = 'u_item'
    id = Column(Integer, primary_key=True, index=True)
    