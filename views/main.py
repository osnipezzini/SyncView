from datetime import datetime

import wx
from wx.dataview import DATAVIEW_CELL_INERT, DATAVIEW_COL_REORDERABLE, DATAVIEW_COL_RESIZABLE

from ui.main import frmMain
from controllers.sync import SyncController


class MainView(frmMain):
    def __init__(self, app, parent=None):
        frmMain.__init__(self, parent)
        self.app = app
        self.controller = SyncController(app)
        self.fill_table()

    def fill_table(self):
        self.fill_cols()
        self.fill_rows()

    def fill_cols(self):
        self.datalist.AppendBitmapColumn("Status", 0, width=50)
        self.datalist.AppendTextColumn('Nome', width=220, mode=DATAVIEW_CELL_INERT, align=wx.ALIGN_LEFT,
                                       flags=DATAVIEW_COL_REORDERABLE | DATAVIEW_COL_REORDERABLE)
        self.datalist.AppendTextColumn('Ultima atualização', mode=DATAVIEW_CELL_INERT, width=120, align=wx.ALIGN_LEFT,
                                       flags=DATAVIEW_COL_RESIZABLE | DATAVIEW_COL_REORDERABLE)
        self.datalist.AppendTextColumn('Atraso', mode=DATAVIEW_CELL_INERT, width=wx.COL_WIDTH_AUTOSIZE,
                                       align=wx.ALIGN_LEFT,
                                       flags=DATAVIEW_COL_RESIZABLE | DATAVIEW_COL_REORDERABLE)

    def fill_rows(self):
        self.datalist.DeleteAllItems()
        atrasos = self.controller.get_data()
        for atraso in atrasos:
            ts = str(atraso.ts)
            img = wx.Bitmap(self.app.get_resource(['img', 'ind_verde_20.png']))
            if atraso.atraso >= 5000:
                img = wx.Bitmap(self.app.get_resource(['img', 'ind_vermelho_20.png']))
            elif atraso.atraso >= 1000:
                img = wx.Bitmap(self.app.get_resource(['img', 'ind_amarelo_20.png']))
            hora = datetime.fromisoformat(ts)
            self.datalist.AppendItem([img, str(atraso.nome), hora.strftime('%d/%m/%Y %H:%M'), str(atraso.atraso)])
