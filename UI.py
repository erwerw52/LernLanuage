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
import pyttsx3

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame2
###########################################################################

class LernEnglish ( wx.Frame ):
   
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Lern Language"), pos = wx.DefaultPosition, size = wx.Size( 300,230 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 300,230 ), wx.Size( 300,230 ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        value = read.readRandomDict(0)
        
        keys = list(value.keys())
        values = list(value.values())
        
        start = value['start']
        end = value['end']
        
        cbDaysChoices = [ _(u"Day1"), _(u"Day2"), _(u"Day3"), _(u"Day4"), _(u"Day5")]
        self.cbDays = wx.ComboBox( self, wx.ID_ANY, _(u"Day1"), wx.DefaultPosition, wx.DefaultSize, cbDaysChoices, 0 )
        self.cbDays.SetEditable(False)
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer1.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.labSize = wx.StaticText( self, wx.ID_ANY, _(start +"/" + end), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.labSize.Wrap( -1 )
        
        bSizer4.Add( self.labSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.labText = wx.StaticText( self, wx.ID_ANY, _(keys[0]), wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        self.labText.Wrap( -1 )

        self.labText.SetFont( wx.Font( 26, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "新細明體" ) )

        bSizer1.Add( self.cbDays, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        bSizer1.Add( self.labText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnHide = wx.Button( self, wx.ID_ANY, _(u"SHOW"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btnHide, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnSpeak = wx.Button( self, wx.ID_ANY, _(u"SPEAK"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btnSpeak, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnNext = wx.Button( self, wx.ID_ANY, _(u"NEXT"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btnNext, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.labTransaction = wx.StaticText( self, wx.ID_ANY, _(values[0]), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.labTransaction.Wrap( -1 )
        
        self.labTransaction.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "新細明體" ) )

        bSizer2.Add( self.labTransaction, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnHide.Bind( wx.EVT_BUTTON, self.onBtnOpenClicked )
        self.btnSpeak.Bind( wx.EVT_BUTTON, self.onBtnSpeakClicked )
        self.btnNext.Bind( wx.EVT_BUTTON, self.onBtnNextClicked )
        self.cbDays.Bind(wx.EVT_COMBOBOX, self.onSelectDay)
        self.labTransaction.Hide()

    def __del__( self ):
        pass

    def onSelectDay( self, event ):
        day = str(self.cbDays.Value)[3:]
        day = int(day) - 1
        value = read.readRandomDict(day)
        
        keys = list(value.keys())
        values = list(value.values())
        
        start = value['start']
        end = value['end']
        
        self.labText.SetLabelText(keys[0])
        self.labTransaction.SetLabelText(values[0])
        self.labSize.SetLabelText(start + "/" + end)
        
    # Virtual event handlers, override them in your derived class
    def onBtnOpenClicked( self, event ):
       if self.labTransaction.IsShown():
            self.labTransaction.Hide()
            self.btnHide.SetLabel("SHOW")
       else:
            self.labTransaction.Show()
            self.btnHide.SetLabel("HIDE")

    def onBtnSpeakClicked( self, event ):
        engine = pyttsx3.init()
        ##engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Fred')
        engine.setProperty('rate', 130)
        engine.say(self.labText.LabelText)
        engine.runAndWait()

    def onBtnNextClicked( self, event ):
        day = str(self.cbDays.Value)[3:]
        day = int(day) - 1
        value = read.readRandomDict(day)
        
        keys = list(value.keys())
        values = list(value.values())
         
        start = value['start']
        end = value['end']
        
        self.labText.SetLabelText(keys[0])
        self.labTransaction.SetLabelText(values[0])
        self.labSize.SetLabelText(start + "/" + end)


