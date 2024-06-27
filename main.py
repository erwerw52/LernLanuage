import wx
import UI

if __name__ == '__main__':
    app = wx.App()
    frm = UI.LernEnglish(None)
    frm.Show()
    app.MainLoop()