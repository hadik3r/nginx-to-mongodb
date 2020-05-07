import logging
import os
from datetime import datetime
from mongoengine import Document, connect, StringField, DateTimeField, BooleanField, signals

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("nginx-to-monogdb:model")
LOG.setLevel(logging.INFO)

class log_record(Document):
    """
    We use mongoengine as ORM to interact with MongoDB.
    """
    rec_id = StringField(primary_key=True, required=True)
    rec_date = StringField(required=True, unique=True)
    user_agent = StringField(required=True, unique=False)
    response_code = StringField(required=False)

    def __repr__(self):
        return "Record(rec_id=%r, rec_date=%r, user_agent=%r, response_code=%r)" % (self.rec_id, self.rec_date, self.user_agent, self.response_code)

    def __str__(self):
        return self.__repr__()

    def save(self, **kwargs):
        super().save(**kwargs)
        LOG.debug("Saved: %s" % self)

    def to_dict(self):
        """
        Convert to dict.
        :return:
        """
        res = dict()
        res["rec_id"] = self.rec_id
        res["rec_date"] = self.rec_date
        res["user_agent"] = self.user_agent
        res["response_code"] = self.response_code
        return res

def initialize(db="nginx-logs",
               host=os.environ.get("mongo_host", "mongo"),
               port=int(os.environ.get("mongo_port", 27017)),
               clear_db=True):
    db_conn = connect(db, host=host, port=port)
    LOG.info("Connected to MongoDB %r@%s:%d" % (db, host, port))
    if clear_db:
        # remove all old data from DB
        LOG.info("Clearing  MongoDB")
        db_conn.drop_database(db)
        LOG.info("Cleared DB %r" % db)