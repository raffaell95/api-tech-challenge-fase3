from pydantic import BaseModel
from typing import Optional


class UDataSchema(BaseModel):
    id: Optional[int] = None
    user_id: str
    item_id: str
    rating: str
    timestamp: str

    class Config:
        orm_mode = True

class UItemSchema(BaseModel):
    id: Optional[int] = None
    movie_id: str
    movie_title: str
    release_date: str
    video_release_date: str
    imdb_url: str
    unknown: str
    action: str
    adventure: str
    animation: str
    childrens: str
    comedy: str
    crime: str
    documentary: str
    drama: str
    fantasy: str
    film_noir: str
    horror: str
    musical: str
    mystery: str
    romance: str
    sci_fi: str
    thriller: str
    war: str
    western: str

    class Config:
        orm_mode = True