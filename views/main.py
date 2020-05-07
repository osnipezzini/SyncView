import sys
import threading
import time
from datetime import datetime

import wx
from wx.dataview import DATAVIEW_CELL_INERT, DATAVIEW_COL_REORDERABLE, DATAVIEW_COL_RESIZABLE

from ui.main import frmMain
from controllers.sync import SyncController
from views.config import ConfigWindow


class MainView(frmMain):
    def __init__(self, app, parent=None):
        frmMain.__init__(self, parent)
        self.thread_stopped = True
        self.app = app
        self.controller = SyncController(app)
        self.thread = None
        self.fill_table()

    def on_close(self, event):
        self.thread_stopped = True
        sys.exit()

    def fill_table(self):
        self.fill_cols()
        self.thread = threading.Thread(target=self.fill_rows, args=(10,), daemon=True)
        self.thread_stopped = False
        self.thread.start()

    def stop_thread(self, event):
        if self.thread_stopped:
            self.thread_stopped = False
            self.btn_stop_check.SetLabelText('Parar checagem')
        else:
            self.thread_stopped = True
            self.btn_stop_check.SetLabelText('Iniciar checagem')

    def open_config(self, event):
        now = datetime.now()
        senha = now.year - now.month - now.day - now.hour
        dlg = wx.TextEntryDialog(self, 'Digite a senha de acesso as configurações !', 'Senha de configuração', '',
                                 wx.CENTRE | wx.OK | wx.TE_PASSWORD)

        if dlg.ShowModal() == wx.ID_OK:
            senha_cap = dlg.GetValue()
            if senha_cap == str(senha):
                view = ConfigWindow(self, icon=self.GetIcon())
                if view.ShowModal() == wx.OK:
                    self.fill_data()
            else:
                wx.MessageBox('Senha inválida !', 'Erro', wx.OK | wx.CENTRE | wx.ICON_ERROR)
                dlg.Close(True)

    def fill_cols(self):
        self.datalist.AppendBitmapColumn("Status", 0, width=50)
        self.datalist.AppendTextColumn('Nome', width=220, mode=DATAVIEW_CELL_INERT, align=wx.ALIGN_LEFT,
                                       flags=DATAVIEW_COL_REORDERABLE | DATAVIEW_COL_RESIZABLE)
        self.datalist.AppendTextColumn('Ultima atualização', mode=DATAVIEW_CELL_INERT, width=120, align=wx.ALIGN_LEFT,
                                       flags=DATAVIEW_COL_RESIZABLE | DATAVIEW_COL_REORDERABLE)
        self.datalist.AppendTextColumn('Atraso', mode=DATAVIEW_CELL_INERT, width=wx.COL_WIDTH_AUTOSIZE,
                                       align=wx.ALIGN_LEFT,
                                       flags=DATAVIEW_COL_RESIZABLE | DATAVIEW_COL_REORDERABLE)
        self.datalist.AppendTextColumn('Conexão', mode=DATAVIEW_CELL_INERT, width=wx.COL_WIDTH_AUTOSIZE,
                                       align=wx.ALIGN_LEFT,
                                       flags=DATAVIEW_COL_RESIZABLE | DATAVIEW_COL_REORDERABLE)


    def fill_data(self):
        self.datalist.DeleteAllItems()
        for nickname, atrasos in self.controller.get_data():
            try:
                for atraso in atrasos:
                    ts = str(atraso.ts)
                    if atraso.atraso >= 500000:
                        img_name = 'as-ic-delet.png'
                    elif atraso.atraso >= 50000:
                        img_name = 'ind_vermelho_20.png'
                    elif atraso.atraso >= 10000:
                        img_name = 'ind_amarelo_20.png'
                    elif atraso.atraso >= 5000:
                        img_name = 'ind_azul_20.png'
                    else:
                        img_name = 'ind_verde_20.png'
                    img = wx.Bitmap(self.app.get_resource(['img', img_name]))
                    hora = datetime.fromisoformat(ts)
                    self.datalist.AppendItem(
                        [img, str(atraso.nome), hora.strftime('%d/%m/%Y %H:%M'), str(atraso.atraso), nickname])
            except Exception as e:
                pass

    def fill_rows(self, delay=10):
        while True:
            delay_txt = self.txt_delay.GetValue()
            if delay_txt != '' and delay_txt.isdigit() and int(delay_txt) >= 5:
                delay = int(delay_txt)
            while not self.thread_stopped:
                self.fill_data()
                for i in reversed(range(0, delay)):
                    if self.thread_stopped:
                        self.lbl_delay_count.SetLabelText('Desligado')
                        break
                    sec = 'segundos'
                    if i == 1:
                        sec = 'segundo'
                    lbl_delay = "Atualizando em : {} {} .".format(str(i), sec)
                    if i == 0:
                        lbl_delay = "Atualizando ..."
                    self.lbl_delay_count.SetLabelText(lbl_delay)
                    time.sleep(1)
