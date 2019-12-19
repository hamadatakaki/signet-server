from . import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import URLType
from furl import furl


class Signet(Base):
    __tablename__ = 'regesterd_signet'

    signet_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    url = Column(URLType)
    position = Column(Integer)

    def __repl__(self):
        return f'id: {self.signet_id}, url: {self.url.url}'

    __str__ = __repl__

    def serialize(self):
        return {
            'signet_id': self.signet_id,
            'url': self.url.url,
            'position': self.position,
        }
