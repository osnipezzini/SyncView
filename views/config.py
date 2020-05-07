import sys

import psycopg2
import wx

from core.config import Config
from ui.config_ui import ConfigUI


class ConfigWindow(ConfigUI):

    def __init__(self, parent, icon=None):
        super(ConfigWindow, self).__init__(parent)
        self.parent = parent
        self.config = None
        self.app = wx.GetApp()
        self.index = -1
        self.SetIcon(icon)
        self.set_glyphs()
        cfg = Config()
        self.exit = True
        if cfg.is_config('db'):
            self.config = cfg.get('db')
            self.dict2list()

    def set_glyphs(self):
        self.btn_add.Bitmap = wx.Bitmap(self.app.get_resource(['img', 'icons-add.png']))
        self.btn_edit.Bitmap = wx.Bitmap(self.app.get_resource(['img', 'icons-edit.png']))
        self.btn_delete.Bitmap = wx.Bitmap(self.app.get_resource(['img', 'icons-delete.png']))

    def show_pnl(self):
        self.pnl_config.Show()
        self.list_config.Hide()
        self.btn_add.Disable()
        self.btn_delete.Disable()
        self.btn_edit.Disable()

    def hide_pnl(self):
        self.pnl_config.Hide()
        self.list_config.Show()
        self.btn_add.Enable()
        self.btn_delete.Enable()
        self.btn_edit.Enable()

    def add_config(self, event):
        self.reset()
        self.show_pnl()

    def delete_config(self, event):
        cfg = Config()
        row = self.list_config.GetSelectedRow()
        if row is not wx.NOT_FOUND:
            idx = int(self.list_config.GetTextValue(row, 0))
            conf = self.config
            self.config = {'db': conf}
            del self.config['db'][idx]
            cfg.set(self.config)
        cfg = Config()
        self.config = cfg.get('db')
        self.dict2list()

    def edit_config(self, event):
        row = self.list_config.GetSelectedRow()
        if row is not wx.NOT_FOUND:
            idx = int(self.list_config.GetTextValue(row, 0))
            cfg = self.config[idx]
            self.dict2field(cfg)
            self.index = idx
            self.show_pnl()
        cfg = Config()
        self.config = cfg.get('db')
        self.dict2list()

    def accept(self, event):
        config = self.field2dict()
        self.save(config)
        cfg = Config()
        self.config = cfg.get('db')
        self.dict2list()

    def save(self, config: dict):
        cfg = Config()
        if not cfg.is_config('db'):
            self.config = {'db': []} if self.config is None else self.config
            self.config['db'] = []
            self.config['db'].append(config)
        elif self.index >= 0:
            conf = self.config
            self.config = {'db': conf}
            del self.config['db'][self.index]
            self.config['db'].append(config)
        else:
            conf = self.config
            self.config = {'db': conf}
            self.config['db'].append(config)

        try:
            conn = psycopg2.connect(
                host=config['host'], port=config['port'],
                dbname=config['dbname'], user=config['user'],
                password=config['password']
            )
            conn.set_client_encoding('latin1')
            if cfg.set(self.config):
                self.hide_pnl()
                self.config = self.config['db']
                self.dict2list()
            else:
                wx.MessageBox(
                    "Ocorreu um erro ao salvar as configurações , verificar se o arquivo " +
                    cfg.cfg_file + " não está sendo usado e se você tem permissão de escrita !",
                    caption="Erro", style=wx.OK | wx.CENTRE | wx.ICON_ERROR, parent=None,
                )
        except Exception as e:
            wx.MessageBox(
                "Ocorreu um erro ao conectar ao banco de dados, verifique os dados informados e tente novamente !",
                caption="Erro", style=wx.OK | wx.CENTRE | wx.ICON_WARNING, parent=None,
            )
            self.app.logger.critical(e)
            return False

    def dict2field(self, cfg):
        self.textHost.SetValue(cfg["host"])
        self.textPort.SetValue(cfg["port"])
        self.textUser.SetValue(cfg["user"])
        self.textPassword.SetValue(cfg["password"])
        self.textName.SetValue(cfg["dbname"])
        self.text_nickname.SetValue(cfg["nickname"])

    def validate_fields(self):
        if self.text_nickname.GetValue() == '':
            wx.MessageBox("Apelido não pode ficar em branco ", 'Erro na validação de dados ', wx.ICON_WARNING)
            self.text_nickname.SetFocus()
        else:
            self.textHost.SetValue("localhost" if self.textHost.GetValue() == "" else self.textHost.GetValue())
            self.textPort.SetValue("5432" if self.textPort.GetValue() == "" else self.textPort.GetValue())
            self.textName.SetValue("autosystem" if self.textName.GetValue() == "" else self.textName.GetValue())
            self.textUser.SetValue("postgres" if self.textUser.GetValue() == "" else self.textUser.GetValue())

    def field2dict(self):
        self.validate_fields()
        cfg = dict()
        cfg['nickname'] = self.text_nickname.GetValue()
        cfg["host"] = self.textHost.GetValue()
        cfg["port"] = self.textPort.GetValue()
        cfg["dbname"] = self.textName.GetValue()
        cfg["user"] = self.textUser.GetValue()
        cfg["password"] = self.textPassword.GetValue()
        return cfg

    def reset(self):
        self.textHost.SetValue("")
        self.textPort.SetValue("")
        self.textUser.SetValue("")
        self.textPassword.SetValue("")
        self.textName.SetValue("")
        self.text_nickname.SetValue("")

    def cancel(self, event):
        self.hide_pnl()

    def exit(self, event):
        self.EndModal(wx.OK)

    def dict2list(self):
        self.list_config.DeleteAllItems()
        cnt = 0
        for cfg in self.config:
            self.list_config.AppendItem([str(cnt), cfg['nickname'], cfg['host']])
            cnt += 1
