# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 May  7 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import wx.adv

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sincronia Status", pos = wx.DefaultPosition, size = wx.Size( 722,359 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.datalist = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.datalist, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl_delay = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Delay ( em segundos ) *Min : 5 seg", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_delay.Wrap( -1 )

		bSizer7.Add( self.lbl_delay, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt_delay = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.txt_delay, 0, wx.ALL, 5 )

		self.btn_stop_check = wx.Button( self.m_panel1, wx.ID_ANY, u"Parar checagem", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.btn_stop_check, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer5 )
		self.m_panel1.Layout()
		bSizer5.Fit( self.m_panel1 )
		bSizer3.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer6.Add( bSizer3, 0, wx.EXPAND, 5 )


		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.menubar = wx.MenuBar( 0 )
		self.menu_options = wx.Menu()
		self.menu_item_config = wx.MenuItem( self.menu_options, wx.ID_ANY, u"Configurações", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_options.Append( self.menu_item_config )

		self.menubar.Append( self.menu_options, u"Opções" )

		self.menu_sync = wx.Menu()
		self.menu_item_run_all_sync = wx.MenuItem( self.menu_sync, wx.ID_ANY, u"Rodar em todas as configurações", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_sync.Append( self.menu_item_run_all_sync )

		self.menu_item_run_selected_sync = wx.MenuItem( self.menu_sync, wx.ID_ANY, u"Rodar a configuração selecionada", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_sync.Append( self.menu_item_run_selected_sync )

		self.menubar.Append( self.menu_sync, u"Rodar sincronia" )

		self.SetMenuBar( self.menubar )

		self.statusbar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.btn_stop_check.Bind( wx.EVT_BUTTON, self.stop_thread )
		self.Bind( wx.EVT_MENU, self.open_config, id = self.menu_item_config.GetId() )
		self.Bind( wx.EVT_MENU, self.run_all_sync, id = self.menu_item_run_all_sync.GetId() )
		self.Bind( wx.EVT_MENU, self.run_selected_sync, id = self.menu_item_run_selected_sync.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()

	def stop_thread( self, event ):
		event.Skip()

	def open_config( self, event ):
		event.Skip()

	def run_all_sync( self, event ):
		event.Skip()

	def run_selected_sync( self, event ):
		event.Skip()


###########################################################################
## Class VersionDialog
###########################################################################

class VersionDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nova versão encontrada", pos = wx.DefaultPosition, size = wx.Size( 431,217 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.img_information = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.img_information, 0, wx.ALL, 5 )


		bSizer12.Add( bSizer13, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer10.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Há uma nova versão disponível do programa .", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer10.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Para fazer o download acesse : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer11.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.link_download = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		bSizer11.Add( self.link_download, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer9.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer9, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.btn_end_modal = wx.ToggleButton( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btn_end_modal, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer7.Add( bSizer8, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_end_modal.Bind( wx.EVT_TOGGLEBUTTON, self.ok_modal )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ok_modal( self, event ):
		event.Skip()


###########################################################################
## Class SyncSelectDialogBase
###########################################################################

class SyncSelectDialogBase ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Seleçao de sincronia", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Seleciona a configuração a ser executada : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer14.Add( self.m_staticText6, 0, wx.ALL, 5 )

		combo_configsChoices = [ u"Meta", u"Juninho", u"Menegatti", u"Central" ]
		self.combo_configs = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, combo_configsChoices, 0 )
		self.combo_configs.SetSelection( 0 )
		bSizer14.Add( self.combo_configs, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer15.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()
		bSizer15.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.combo_configs.Bind( wx.EVT_CHOICE, self.choosed_sync )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()

	def choosed_sync( self, event ):
		event.Skip()


