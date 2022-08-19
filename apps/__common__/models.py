import datetime
from db import db


class TimeStampMixin(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    deleted_at = db.Column(db.DateTime, default=None)
