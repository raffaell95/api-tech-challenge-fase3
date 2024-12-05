from sqlalchemy import Column, Integer, String
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
    movie_id = Column(String)
    movie_title = Column(String)
    release_date = Column(String)
    video_release_date = Column(String)
    imdb_url = Column(String)
    unknown = Column(String)
    action = Column(String)
    adventure = Column(String)
    animation= Column(String)
    childrens = Column(String)
    comedy = Column(String)
    crime = Column(String)
    documentary = Column(String)
    drama = Column(String)
    fantasy = Column(String)
    film_noir = Column(String)
    horror = Column(String)
    musical = Column(String)
    mystery = Column(String)
    romance = Column(String)
    sci_fi = Column(String)
    thriller = Column(String)
    war = Column(String)
    western = Column(String)