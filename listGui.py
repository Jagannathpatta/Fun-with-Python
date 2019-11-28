import wx
"""app = wx.App()
frame = wx.Frame(None,-1,'List')
frame.Show()
app.MainLoop()
il = wx.ImageList(16,16)
imgidx1 = il.Add(bmp1)
imgidx2 = il.Add(bmp2)
panel = wx.Panel(frame)
lc = wx.ListCtrl(panel, style=wx.LC_REPORT|wx.LC_SINGLE_SEL)
lc.AssignImageList(il)
lc.InsertColumn(0, 'Column 1')
lc.InsertColumn(1, 'Column 2', wx.LIST_FORMAT_RIGHT)
lc.InsertColumn(2, 'Column 3')
for data in GetDataItems():
    index = lc.InsertStringItem(sys.maxint, data[0], imgidx1)
    lc.SetStringItem(index, 1, data[1])
    lc.SetStringItem(index, 2, data[2])
self.Bind(wx.LIST_ITEM_SELECTED, self.OnSelect, lc)"""



def onButton(event):
    print ("Button pressed.")

app = wx.App()
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,250,350)
panel = wx.Panel(frame, wx.ID_ANY)

bmp = wx.Bitmap("paf.jpg", wx.BITMAP_TYPE_ANY)
button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp,
                          size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
 
button.Bind(wx.EVT_BUTTON, onButton)
button.SetPosition((10,10))

frame.Show()
frame.Centre()
app.MainLoop()
