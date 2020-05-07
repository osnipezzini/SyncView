from datetime import datetime

import wx
from elibs import Base, dict_to_prop
import psycopg2
from psycopg2.extras import RealDictCursor

from core.config import Config


class DB(Base):
    def __init__(self, app, *args, **kwargs):
        self.app = wx.GetApp()
        self.cfg = Config()
        Base.__init__(self, self.app, cfg=Config, **kwargs)
        self.model = None

    def fill_response(self, response):
        self.status_code = response.status_code
        self.encoding = response.encoding
        self.text = response.text
        self.json = response.json()
        self.content = response.content

    @property
    def conn(self):
        try:
            conn = psycopg2.connect(
                host=self.model.host, port=self.model.port, dbname=self.model.dbname, user=self.model.user,
                password=self.model.password
            )
            conn.set_client_encoding('latin1')
            return conn
        except Exception as e:
            self.log(e, 'critical')
            return False

    @property
    def cur(self):
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        return cursor

    def delete(self, id, safe_delete=False):
        try:
            if safe_delete:
                query = "UPDATE {} SET delete_on={} WHERE id={}".format(
                    self.model.lower(), datetime.now(), id
                )
            else:
                query = "DELETE FROM {} WHERE id={}".format(
                    self.model.lower(), datetime.now()
                )
            if self.conn:
                self.cur.execute(query)
                self.log(query, 'debug')
                return True
        except Exception as e:
            self.log('Error when delete', 'critical')
            return False

    def update(self, data):
        try:
            query = "UPDATE {} SET delete_on={} WHERE id={}".format(
                self.model.lower(), datetime.now(), id
            )
            if self.conn:
                self.cur.execute(query)
                self.log(query, 'debug')
                return True
        except Exception as e:
            self.log('Error when update', 'critical')

    def create(self, data):
        try:
            query = "UPDATE {} SET delete_on={} WHERE id={}".format(
                self.model.lower(), datetime.now(), id
            )
            if self.conn:
                self.cur.execute(query)
                self.log(query, 'debug')
                return True
        except Exception as e:
            self.log('Error when creating', 'critical')

    def get(self, query):
        try:
            config = self.cfg.get('db')
            for conf in config:
                self.model = dict_to_prop(conf)
                if self.conn:
                    cur = self.cur
                    cur.execute(query)
                    self.log(query, 'debug')
                    result = cur.fetchall()
                    self.log(result, 'debug')
                    yield self.model.nickname, dict_to_prop(result)
        except Exception as e:
            self.log('Error when getting data', 'critical')
            return False
