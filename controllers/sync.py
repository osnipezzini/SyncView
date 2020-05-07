from controllers import Controller
from models.sync import Sync


class SyncController(Controller):
    def __init__(self, app):
        Controller.__init__(self, app)
        self.model = Sync(app)

    def get_data(self):
        return self.model.get_data()
