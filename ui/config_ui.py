# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Apr 16 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext

###########################################################################
## Class ConfigUI
###########################################################################

class ConfigUI ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Configurações do banco de dados"), pos = wx.DefaultPosition, size = wx.Size( 422,200 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.list_config = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.col_name = self.list_config.AppendTextColumn( _(u"Apelido"), wx.DATAVIEW_CELL_INERT, -1, wx.ALIGN_CENTER_HORIZONTAL, wx.DATAVIEW_COL_RESIZABLE|wx.DATAVIEW_COL_SORTABLE )
		self.col_host = self.list_config.AppendTextColumn( _(u"Host"), wx.DATAVIEW_CELL_INERT, -1, wx.ALIGN_CENTER_HORIZONTAL, wx.DATAVIEW_COL_RESIZABLE )
		bSizer7.Add( self.list_config, 1, wx.ALL|wx.EXPAND, 5 )

		self.pnl_config = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnl_config.Hide()

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self.pnl_config, wx.ID_ANY, _(u"Host     "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textHost = wx.TextCtrl( self.pnl_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.textHost, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self.pnl_config, wx.ID_ANY, _(u"Porta"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textPort = wx.TextCtrl( self.pnl_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.textPort, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer41.Add( fgSizer2, 0, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self.pnl_config, wx.ID_ANY, _(u"Usuário"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textUser = wx.TextCtrl( self.pnl_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.textUser, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self.pnl_config, wx.ID_ANY, _(u"Senha"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer4.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textPassword = wx.TextCtrl( self.pnl_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer4.Add( self.textPassword, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self.pnl_config, wx.ID_ANY, _(u"Nome"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer4.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.textName = wx.TextCtrl( self.pnl_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.textName, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer41.Add( fgSizer4, 1, wx.EXPAND, 5 )

		buttonBox = wx.StdDialogButtonSizer()
		self.buttonBoxSave = wx.Button( self.pnl_config, wx.ID_SAVE )
		buttonBox.AddButton( self.buttonBoxSave )
		self.buttonBoxCancel = wx.Button( self.pnl_config, wx.ID_CANCEL )
		buttonBox.AddButton( self.buttonBoxCancel )
		buttonBox.Realize();

		bSizer41.Add( buttonBox, 0, wx.EXPAND, 5 )


		self.pnl_config.SetSizer( bSizer41 )
		self.pnl_config.Layout()
		bSizer41.Fit( self.pnl_config )
		bSizer7.Add( self.pnl_config, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )

		self.pnl_button = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.btn_add = wx.BitmapButton( self.pnl_button, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_add.SetBitmap( wx.Bitmap( u"C:\\Projetos\\Python\\SyncView\\resources\\img\\icons-add.png", wx.BITMAP_TYPE_ANY ) )
		self.btn_add.SetBitmapPosition( wx.TOP )
		bSizer6.Add( self.btn_add, 0, wx.ALL, 5 )

		self.btn_edit = wx.BitmapButton( self.pnl_button, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_edit.SetBitmap( wx.Bitmap( u"C:\\Projetos\\Python\\SyncView\\resources\\img\\icons-edit.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.btn_edit, 0, wx.ALL, 5 )

		self.btn_delete = wx.BitmapButton( self.pnl_button, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_delete.SetBitmap( wx.Bitmap( u"C:\\Projetos\\Python\\SyncView\\resources\\img\\icons-delete.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.btn_delete, 0, wx.ALL, 5 )


		self.pnl_button.SetSizer( bSizer6 )
		self.pnl_button.Layout()
		bSizer6.Fit( self.pnl_button )
		bSizer5.Add( self.pnl_button, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonBoxCancel.Bind( wx.EVT_BUTTON, self.cancel )
		self.buttonBoxSave.Bind( wx.EVT_BUTTON, self.accept )
		self.btn_add.Bind( wx.EVT_BUTTON, self.add_config )
		self.btn_edit.Bind( wx.EVT_BUTTON, self.edit_config )
		self.btn_delete.Bind( wx.EVT_BUTTON, self.delete_config )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cancel( self, event ):
		event.Skip()

	def accept( self, event ):
		event.Skip()

	def add_config( self, event ):
		event.Skip()

	def edit_config( self, event ):
		event.Skip()

	def delete_config( self, event ):
		event.Skip()


