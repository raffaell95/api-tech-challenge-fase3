from typing import List
from sqlalchemy.orm import Session
from infra.models.models import UData, UItem
from schemas.schemas import UDataSchema


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