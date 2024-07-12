import wx
import wx.xrc
import wx.dataview
import read

import gettext
_ = gettext.gettext

###########################################################################
## Class ListView
###########################################################################

class ListView ( wx.Dialog ):

    def __init__( self, parent, day ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = 'Language List', pos = wx.DefaultPosition, size = wx.Size( 500, 500 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.listCtrl = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_ROW_LINES )
        self.listCtrl.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "新細明體" ) )

        self.colText = self.listCtrl.AppendTextColumn( _(u"Text"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.colTranslate = self.listCtrl.AppendTextColumn( _(u"Translate"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        bSizer11.Add( self.listCtrl, 1, wx.ALL|wx.EXPAND, 5 )

        filename = 'vocabulary.ods'
        result_dict = read.ods_to_dict(filename, day)
        del result_dict["sheets_no"]

        for key in result_dict.keys():
            value = result_dict[key]
            self.listCtrl.AppendItem([key, value])
       
        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


