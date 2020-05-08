import os
import sys

import wx
from elibs import dict_to_prop
from wx import App as wxApp

from core.config import Config
from core.logger import init_logger


class App(wxApp):
    def __init__(self, name):
        self.path = self.basepath
        self.name = name
        self.logger = init_logger(self.logfile)
        wxApp.__init__(self, redirect=False, filename=self.logfile)
        self.AppName = name
        self.AppDisplayName = name
        self.icon = wx.Icon(self.get_resource('Icon.ico'))

    @property
    def version(self):
        return os.environ.get('release_version')

    def check_version(self):
        import ftplib
        filename = 'programs_release.json'
        try:
            ftp = ftplib.FTP('ftps.sistempostos.com.br')
            ftp.login('dev@sistempostos.com.br', '*1500-Blu@.')
            ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
            ftp.quit()
            with open(filename, 'r') as json_file:
                import json
                data_json = json.load(json_file)
                data = dict_to_prop(data_json)
                mensagem = f"""Há uma nova versão disponível do programa .

                                Para fazer o download acesse : {data.syncview.download_url}"""
                if data.syncview.version > self.version:
                    wx.MessageBox(mensagem, "Nova versão !", wx.ICON_INFORMATION)
        except Exception as e:
            self.logger.debug('Erro ao receber informações do ftp : \n\n' + str(e))

    @property
    def basepath(self):
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @property
    def logfile(self):
        log_path = os.path.join(self.basepath, 'log')
        try:
            os.makedirs(log_path)
        except Exception as e:
            print(e)

        log_file = os.path.join(log_path, self.name + '.log')
        return log_file

    def get_resource(self, path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(self.path)

        if isinstance(path, str):
            """ Get absolute path to resource, works for dev and for PyInstaller """
            return os.path.join(base_path, 'resources', path)
        elif isinstance(path, list):
            return os.path.join(base_path, 'resources', *path)
        else:
            raise Exception('Path must be string or a list')

    def run(self):
        self.check_version()
        cfg = Config()
        if not cfg.is_config('db'):
            msg = wx.MessageBox(
                "As configurações não foram encontradas , será aberta uma janela para configurar.",
                caption="Aviso", style=wx.OK | wx.CENTRE | wx.ICON_ERROR, parent=None,
            )
            if msg == wx.OK:
                from views.config import ConfigWindow
                cfg = ConfigWindow(None, icon=self.icon)
                cfg.SetIcon(self.icon)
                if cfg.ShowModal() == wx.OK:
                    self.run()
        else:
            cfg.config = cfg.get('db')
            from views.main import MainView
            window = MainView(self)
            window.SetIcon(self.icon)
            window.Show()
