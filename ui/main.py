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

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sincronia Status", pos = wx.DefaultPosition, size = wx.Size( 722,442 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.datalist = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.datalist, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.lbl_delay_count = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Atualizando em : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_delay_count.Wrap( -1 )

		bSizer4.Add( self.lbl_delay_count, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl_delay = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Delay ( em segundos ) *Min : 5 seg", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_delay.Wrap( -1 )

		bSizer7.Add( self.lbl_delay, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt_delay = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.txt_delay, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer5 )
		self.m_panel1.Layout()
		bSizer5.Fit( self.m_panel1 )
		bSizer3.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.btn_stop_check = wx.Button( self, wx.ID_ANY, u"Parar checagem", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btn_stop_check, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( bSizer3, 0, wx.EXPAND, 5 )


		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.menu_item_config = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Configurações", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menu_item_config )

		self.m_menubar1.Append( self.m_menu2, u"Opções" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.btn_stop_check.Bind( wx.EVT_BUTTON, self.stop_thread )
		self.Bind( wx.EVT_MENU, self.open_config, id = self.menu_item_config.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()

	def stop_thread( self, event ):
		event.Skip()

	def open_config( self, event ):
		event.Skip()


