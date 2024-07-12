# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import read
import UI
import ListView
import pyttsx3

import gettext
_ = gettext.gettext

###########################################################################
## Class LernEnglish
###########################################################################

class LernLanuage ( wx.Frame ):
   
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = 'Lerning Language', pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        vMain = wx.BoxSizer( wx.VERTICAL )

        hTitle = wx.BoxSizer( wx.HORIZONTAL )
        value = read.readRandomDict(0)
        
        keys = list(value.keys())
        values = list(value.values())
         
        current = value['current']
        size = value['size']

        cbDaysChoices = value['sheets_no']
        self.cbDays = wx.ComboBox( self, wx.ID_ANY, _(u"Day1"), wx.DefaultPosition, wx.DefaultSize, cbDaysChoices, 0 )
        hTitle.Add( self.cbDays, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.labSize = wx.StaticText( self, wx.ID_ANY, _(current + "/" + size), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.labSize.Wrap( -1 )

        hTitle.Add( self.labSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        vMain.Add( hTitle, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        hText = wx.BoxSizer( wx.HORIZONTAL )

        self.labText = wx.StaticText( self, wx.ID_ANY, _(keys[0]), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.labText.Wrap( -1 )

        self.labText.SetFont( wx.Font( 26, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Palatino Linotype" ) )

        hText.Add( self.labText, 0, wx.ALL, 5 )

        vMain.Add( hText, 0, wx.EXPAND, 5 )

        hContainer = wx.BoxSizer( wx.HORIZONTAL )

        self.btnHide = wx.Button( self, wx.ID_ANY, _(u"HIDE"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hContainer.Add( self.btnHide, 0, wx.ALL, 5 )

        self.btnSpeak = wx.Button( self, wx.ID_ANY, _(u"SPEAK"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hContainer.Add( self.btnSpeak, 0, wx.ALL, 5 )

        self.btnNext = wx.Button( self, wx.ID_ANY, _(u"RANDOM"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hContainer.Add( self.btnNext, 0, wx.ALL, 5 )

        self.btnListView = wx.Button( self, wx.ID_ANY, _(u"ListView"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hContainer.Add( self.btnListView, 0, wx.ALL, 5 )

        vMain.Add( hContainer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        hTranslate = wx.BoxSizer( wx.HORIZONTAL )

        self.labTranslate = wx.StaticText( self, wx.ID_ANY, _(values[0] + ' '), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.labTranslate.Wrap( -1 )

        self.labTranslate.SetFont( wx.Font( 22, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "標楷體" ) )

        hTranslate.Add( self.labTranslate, 0, wx.ALL, 5 )

        vMain.Add( hTranslate, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.SetSizer( vMain )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.cbDays.Bind( wx.EVT_COMBOBOX, self.onCbDayClicked )
        self.btnHide.Bind( wx.EVT_BUTTON, self.onBtnHideClicked )
        self.btnSpeak.Bind( wx.EVT_BUTTON, self.onBtnSpeakClicked )
        self.btnNext.Bind( wx.EVT_BUTTON, self.onBtnNextClicked )
        self.btnListView.Bind( wx.EVT_BUTTON, self.onBtnListViewClicked )

    def __del__( self ):
        pass

    def onCbDayClicked( self, event ):
        day = str(self.cbDays.Value)[3:]
        day = int(day) - 1
        value = read.readRandomDict(day)
        
        keys = list(value.keys())
        values = list(value.values())
         
        current = value['current']
        size = value['size']

        self.labText.SetLabelText(keys[0])
        self.labTranslate.SetLabelText(values[0] + ' ')
        self.labSize.SetLabelText(current + "/" + size)
        
    # Virtual event handlers, override them in your derived class
    def onBtnHideClicked( self, event ):
       if self.labTranslate.IsShown():
            self.labTranslate.Hide()
            self.btnHide.SetLabel("SHOW")
       else:
            self.labTranslate.Show()
            self.btnHide.SetLabel("HIDE")

    def onBtnSpeakClicked( self, event ):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Fred')
        engine.setProperty('rate', 200)
        engine.say(self.labText.LabelText)
        engine.runAndWait()

        # engine.say(self.labTranslate.LabelText)
        # engine.runAndWait()

    def onBtnNextClicked( self, event ):
        day = str(self.cbDays.Value)[3:]
        day = int(day) - 1
        value = read.readRandomDict(day)
        
        keys = list(value.keys())
        values = list(value.values())
        
        current = value['current']
        size = value['size']
        
        self.labText.SetLabelText(keys[0])
        self.labTranslate.SetLabelText(values[0] + ' ')
        self.labSize.SetLabelText(current + "/" + size)

    def onBtnListViewClicked( self, event ):
        day = str(self.cbDays.Value)[3:]
        day = int(day) - 1
        dialog = ListView.ListView(None, day)
        dialog.ShowModal()


