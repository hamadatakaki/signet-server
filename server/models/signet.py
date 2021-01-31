from . import Base

import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql.functions import current_timestamp
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
    icon = Column(URLType)
    title = Column(String(30))
    comment = Column(String(140))
    position = Column(Integer)
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=current_timestamp()
    )

    @property
    def get_url(self):
        return str(self.url)

    @property
    def get_icon(self):
        return str(self.icon)

    def __repl__(self):
        return f'<id: {self.signet_id}, url: {self.get_url}>'

    __str__ = __repl__

    def serialize(self):
        created_at = self.created_at
        return {
            'signet_id': self.signet_id,
            'url': self.get_url,
            'icon': self.get_icon,
            'title': self.title,
            'comment': self.comment,
            'position': self.position,
            'created_at': datetime.datetime.strftime(created_at.astimezone(), '%Y-%m-%d %H:%M:%S.%f')
        }
