from elibs import Base

from core.db import DB


class Model(Base):
    def __init__(self, app):
        Base.__init__(self, app)
        self.db = DB(app)

