import sys

import psycopg2
import wx

from core.config import Config
from ui.config_ui import ConfigUI


class ConfigWindow(ConfigUI):

    def __init__(self, parent, icon=None):
        super(ConfigWindow, self).__init__(parent)
        self.parent = parent
        self.config = dict()
        self.app = wx.GetApp()
        self.SetIcon(icon)
        cfg = Config()
        self.exit = True
        if cfg.is_config('db'):
            self.config = cfg.get('db')
            self.dict2field(self.config)

    def accept(self, event):
        cfg = self.field2dict()
        self.config['db'] = cfg
        self.save()

    def save(self):
        cfg = Config()
        try:
            conn = psycopg2.connect(**self.config['db'])
            conn.set_client_encoding('latin1')
            if cfg.set(self.config):
                msg = wx.MessageBox(
                    "As configurações foram salvas em : " + cfg.cfg_file,
                    caption="Sucesso", style=wx.OK | wx.CENTRE | wx.ICON_INFORMATION, parent=None,
                )
                if msg == wx.OK:
                    self.EndModal(wx.OK)
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
        self.textHost.setText(cfg["host"])
        self.textPort.setText(cfg["port"])
        self.textUser.setText(cfg["user"])
        self.textPassword.setText(cfg["password"])
        self.textName.setText(cfg["dbname"])

    def validate_fields(self):
        self.textHost.SetValue("localhost" if self.textHost.GetValue() == "" else self.textHost.GetValue())
        self.textPort.SetValue("5432" if self.textPort.GetValue() == "" else self.textPort.GetValue())
        self.textName.SetValue("autosystem" if self.textName.GetValue() == "" else self.textName.GetValue())
        self.textUser.SetValue("postgres" if self.textUser.GetValue() == "" else self.textUser.GetValue())

    def field2dict(self):
        self.validate_fields()
        cfg = dict()
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

    def cancel(self, event):
        sys.exit()
