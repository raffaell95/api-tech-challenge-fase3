from typing import List
from sqlalchemy.orm import Session
from infra.models.models import UData, UItem
from schemas.schemas import UDataSchema, UItemSchema


class RepositoryUData:

    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self):
        udata = self.db.query(UData).all()
        return udata

    def save(self, udata_list: List[UDataSchema]):
        db_udatas = []
        for udata in udata_list:
            db_udata = UData(
                user_id=udata.user_id,
                item_id=udata.item_id,
                rating=udata.rating,
                timestamp=udata.timestamp
            )
            db_udatas.append(db_udata)

        self.db.add_all(db_udatas)
        self.db.commit()

        for db_udata in db_udatas:
            self.db.refresh(db_udata)
        
        return db_udatas
    

class RepositoryUItem:

    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self):
        uitem = self.db.query(UItem).all()
        return uitem

    def save(self, uitem_list: List[UItemSchema]):
        db_utems = []
        for uitem in uitem_list:
            db_item = UItem(
                movie_id = uitem.movie_id,
                movie_title = uitem.movie_title,
                release_date = uitem.release_date,
                video_release_date = uitem.video_release_date,
                imdb_url = uitem.imdb_url,
                unknown = uitem.unknown,
                action = uitem.action,
                adventure = uitem.adventure,
                animation= uitem.animation,
                childrens = uitem.childrens,
                comedy = uitem.comedy,
                crime = uitem.crime,
                documentary = uitem.documentary,
                drama = uitem.drama,
                fantasy = uitem.fantasy,
                film_noir = uitem.film_noir,
                horror = uitem.horror,
                musical = uitem.musical,
                mystery = uitem.mystery,
                romance = uitem.romance,
                sci_fi = uitem.sci_fi,
                thriller = uitem.thriller,
                war = uitem.war,
                western = uitem.western
            )
            db_utems.append(db_item)

        self.db.add_all(db_utems)
        self.db.commit()

        for db_item in db_utems:
            self.db.refresh(db_item)
        
        return db_utems