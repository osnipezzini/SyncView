import wx

from ui.main import VersionDialog


class VersionDialogView(VersionDialog):
    def __init__(self):
        VersionDialog.__init__(self, None)

    def ok_modal(self, event):
        self.EndModal(wx.OK)
