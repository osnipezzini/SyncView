import wx

from core.app import App
from core.config import Config
from ui.main import VersionDialog, SyncSelectDialogBase


class VersionDialogView(VersionDialog):
    def __init__(self):
        VersionDialog.__init__(self, None)

    def ok_modal(self, event):
        self.EndModal(wx.OK)


class SyncSelectDialog(SyncSelectDialogBase):
    selected_config = None

    def __init__(self, parent, app: App):
        SyncSelectDialogBase.__init__(self, parent)
        self.app = app
        self.configs = Config().get('db')
        self.fill_combo()

    def fill_combo(self):
        options = []
        for config in self.configs:
            options.append(config['nickname'])
        self.combo_configs.SetItems(options)

    def choosed_sync(self, event):
        selected_word = self.combo_configs.GetStringSelection()
        self.selected_config = [sub['nickname'] for sub in self.configs if sub['nickname'] == selected_word][0]
        self.EndModal(wx.OK)
