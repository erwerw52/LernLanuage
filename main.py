import wx
import UI

if __name__ == '__main__':
    app = wx.App()
    frm = UI.LernLanuage(None)
    frm.Show()
    app.MainLoop()