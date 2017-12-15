#coding:utf-8
import win32api
import win32con
win32api.MessageBox(win32con.NULL, 'Python 你好！'.decode('utf-8'), '你好'.decode('utf-8'), win32con.MB_OK)

import win32com
from win32com.client import Dispatch, constants
"""
1. word
   重要概念：
       Application:WORD应用程序
       Document: 一个打开的文档对象
       Paragraph: 段落
       ParagraphFormat: 段落格式
       Section ：代表指定文档、区域或所选文档中的节"""


    w = win32com.client.Dispatch('Word.Application')
    # 或者使用下面的方法，使用启动独立的进程：
    # w = win32com.client.DispatchEx('Word.Application')

    # 后台运行
    w.Visible = 0       # 不显示
    w.DisplayAlerts = 0 # 不警告

    # 打开文件
    doc = w.Documents.Open( FileName = filenamein ) # 打开已有文件
    # doc = w.Documents.Add() # 创建新的文档

    # 插入文字
    myRange = doc.Range(0,0)    # 两个参数分别代表起始点,结束点
    myRange.InsertBefore('Hello from Python!')

    # 使用样式
    wordSel = myRange.Select()
    wordSel.Style = constants.wdStyleHeading1

    # 正文文字替换
    w.Selection.Find.ClearFormatting()
    w.Selection.Find.Replacement.ClearFormatting()
    w.Selection.Find.Execute(OldStr, False, False, False, False, False, True, 1, True, NewStr, 2)

    # 页眉文字替换
    w.ActiveDocument.Sections[0].Headers[0].Range.Find.ClearFormatting()
    w.ActiveDocument.Sections[0].Headers[0].Range.Find.Replacement.ClearFormatting()
    w.ActiveDocument.Sections[0].Headers[0].Range.Find.Execute(OldStr, False, False, False, False, False, True, 1, False, NewStr, 2)

    # 在文档末尾新增一页并添加一个表格
    pre_section = doc.Secitons(0)
    new_seciton = doc.Range(pre_section.Range.End, pre_section.Range.End).Sections.Add()
    new_range = new_seciton.Range
    new_table = new_range.Tables.Add(doc.Range(new_range.End,new_range.End), 5, 5)
        #在文档末尾添加一个5*5的表格

    # 表格操作
    doc.Tables[0].Rows[0].Cells[0].Range.Text ='123123'
    worddoc.Tables[0].Rows.Add() # 增加一行

    # 转换为html
    wc = win32com.client.constants
    w.ActiveDocument.WebOptions.RelyOnCSS = 1
    w.ActiveDocument.WebOptions.OptimizeForBrowser = 1
    w.ActiveDocument.WebOptions.BrowserLevel = 0 # constants.wdBrowserLevelV4
    w.ActiveDocument.WebOptions.OrganizeInFolder = 0
    w.ActiveDocument.WebOptions.UseLongFileNames = 1
    w.ActiveDocument.WebOptions.RelyOnVML = 0
    w.ActiveDocument.WebOptions.AllowPNG = 1
    w.ActiveDocument.SaveAs( FileName = filenameout, FileFormat = wc.wdFormatHTML )

    # 增加10个新页，然后跳转到新页中增加内容
        #(最好将其提取为一个函数)
    section_index = 0
    for i in range(0, 10):
         pre_section = doc.Secitons(section_index)
         new_seciton = doc.Range(pre_section.Range.End,              pre_section.Range.End).Sections.Add()
         new_range = new_seciton.Range

         content_pg = new_range.Paragraphs.Add()
         content_pg.Range.Font.Name,content_pg.Range.Font.Size = 'Times New Roman',24
         caption_pg.Range.ParagraphFormat.Alignment = 0
            # 0,1,2 分别对应左对齐、居中、右对齐
         caption_pg.Range.InsertBefore('Hello,Page ' + str(i+1))

         section_index +=  1

    doc.PrintOut()  # 打印

    # doc.Close()   # 关闭
    w.Documents.Close(wc.wdDoNotSaveChanges)
    w.Quit()

2. excel
    import win32com.client as win32

    # add_a_workbook
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        """
            0代表隐藏对象，但可以通过菜单再显示
            -1代表显示对象
            2代表隐藏对象，但不可以通过菜单显示，只能通过VBA修改为显示状态
        """
        excel.Application.ScreenUpdating = False  # 关闭屏幕更新
        excel.DisplayAlerts = 0 # 不警告

        wb = excel.Workbooks.Add() # 新建工作薄
        # wb = excel.Workbooks.Open('workbook1.xlsx')
            # 打开已存在的工作薄
        wb.SaveAs('add_a_workbook.xlsx') # 新建的用SaveAa(),否则用Save()
        # wb.Close(SaveChanges=0)
        excel.Application.Quit()

    # add_a_worksheet
        sht = wb.Worksheets.Add()
        # wb.Worksheets("Sheet1")  # 已存在
        # wb.Worksheets(1)  # 序号
        sht.Name = 'sheet1'
        sht.Range("A1").Value = 1

    # Range and Offset
        sht.Cells(1,1).Value = 'A1'   # 从1开始

        sht.Cells(1,1).Offset(2,4).Value = "D2"  # ?
            # offset中的参数自身就算一行一列,这是与VBA不同处

        sht.Range("A2").Value = 'A2'
        sht.Range("A3:B4").Value = 'A3:B4'
        sht.Range("A6:B7,A9:B10").Value = "A6:B7,A9:B10"
        sht.Range(sht.Cells(1,1),sht.Cells(3,3)).Value = rglist # 嵌套的列表

    # cell_color and Format
        for i in range (1,21):
            sht.Cells(i,1).Value = i
            sht.Cells(i,1).Interior.ColorIndex = i

        sht.Cells(3,2).Font.Color = -16776961

        sht.Cells(3,2).Font.Bold = True
        sht.Cells(3,2).Font.Name = '宋体'

        sht.Range("A1:A5").HorizontalAlignment = win32.constants.xlRight
            # 返回或设置指定对象的水平对齐方式    靠右
        sht.Rows(1).VerticalAlignment = win32.constants.xlCenter
            # 返回或设置指定对象的垂直对齐方式  居中

        sht.Rows.AutoFit() # 可自动调整工作表中的所有行

        sht.Range("B1:B5").NumberFormat = "$###,##0.00"

    # autoFill
        sht.Range("A1:A2").AutoFill(sht.Range("a1:a10"),win32.constants.xlFillDefault)
            # 将A1:A2自动填充到A1:A10

    # Column/Row Formatting
        sht.Columns(1).ColumnWidth = 1
        sht.Range("B:B").ColumnWidth = 1

        sht.Columns.AutoFit() # 可自动调整工作表中的所有列

        sht.Rows("2:500").Delete

        sht.Rows(12).Value = '' # 整行
        sht.Range('E2').EntireColumn.Address    # $E:$E 整列
        sht.Range('E2').EntireRow.Address       # $2:$2 整行

      # UsedRange
        row = len(sht.UsedRange.Rows)  # 已使用的最大区域的行数
            # sht.UsedRange.Rows.Count # 抛异常 无此属性

        sht.UsedRange.Rows(1).Value[0]
        sht.UsedRange.Rows.Value
        sht.UsedRange.Address
        sht.UsedRange.Cells(1).Address # 绝对地址
        sht.UsedRange.Cells(1).Row     # 已用区域的起始点行号

      # CurrentRegion
        sht.Range('E2').CurrentRegion.Count  # UsedRange中无此属性
            # 区域中所有单元格总数
        sht.Range('E2').CurrentRegion.Rows.Count
            # 区域中行数和

    # Intersect     # (同工作表中的)参数的重叠区域
        excel.Application.Intersect(sht.Range('a2:b3'),sht.Range('b3:c4')).Address
            # $B$3

    # End
        sht.Cells(2,1).End(win32.constants.xlDown).Offset(2,1).Value = ''
        sht.Rows(2).End(win32.constants.xlToRight).Address
            # 函数意义及方向同VBA： xlToLeft/ xlUp / xlToRight/ xlDown

    # Resize # ？
        sht.Range('E2').Resize(2,2).Address  # $F$3
        sht.Range('E2').Offset(2,2).Address  # $F$3
            # Resize并未扩大区域,效果与Offset效果,为何?(在wps中测试)

    # Activate/Select 焦点转移
        sht.Activate
        sht.Select()
        excel.Selection.ColumnWidth = 4
            # 只能是excel !!

    # Names
        wb.Names.Count      # sht.Names.Count 下同
        wb.Names(1).Name
        wb.Names(1).Visible = False     # 隐藏
        sht.Names(1).Name = 'date'      # 重命名

        sht.Range('A2').Name = 'STD'
        print(sht.Range('STD').Value)
        print(sht.Evaluate('STD'))   # 同上一行

        wb.Names.Add(Name="abc",RefersTo="=sheet1!$A$1:$J$1",Visible=False)
            # 创建新的命名
            # RefersTo中不加工作表名时为全局命名(整个工作簿可用),否则为局部命名
        sht.Names.Add("abc","=$A$1:$J$1",True)
            # 创建sht中的局部命名

        print(help(sht.Names.Add)) # 查看Add函数有哪些参数


    # Copying Data from Worksheet to Worksheet

        sht.Range('A2:J10').Formula = "=row()*column()" # 公式

        wb.Worksheets.FillAcrossSheets(wb.Worksheets("Sheet1").Range("A2:J10"))
            # 将sheet1中A2:J10的数据复制到wb中所有工作表的相同位置

            # FillAcrossSheets：将单元格区域复制到集合中所有其他工作表的同一位置
            # 还有一可选参数,指定如何复制区域:
            #   xlFillWithAlldefault/xlFillWithContents/xlFillWithFormats(详VBA)

        sht.Copy(None,sht)  # 参数：Copy(Before,After)
            # 复制工作表
        sht.UsedRange.Rows(1).Copy(sht.Range('F2')
            # 将已用区域的第一行数据复制到从F2开始的单元格区域(自动扩展)

        sht.Range("B2:K2").Value = [i for i in range(1,11)]
            # 同一行赋值

        func = excel.Application.WorksheetFunction.Transpose
            # VBA中的转置函数

        sht.Range("B2:B11").Value = list(zip([i for i in range(1,11)]))
            # 同一列赋值 变为多行一列
        sht.Range("B2:B11").Value = func([i for i in range(1,11)])
            # 同上

        sht.Range('f1:h1').Value = func(sht.Range('b3:b5').Value)
            # 同一行赋值 将列中的值倒置

        sht.Range("B2:E4").Value = sht.Range("B6:E8").Value
            # 多维 对 多维

    # FormatConditions: 条件格式 参见VBA

        sht.Range("B2:K33").Select()
        excel.Selection.FormatConditions.AddColorScale(ColorScaleType = 3)
            # 添加三色度渐变刻度 二色度参数为2

        rng = sht.UsedRange
        CON = win32.constants
        rng.FormatConditions.Add(CON.xlCellValue,CON.xlEqual,'A')  # 值 等于A
            # sht/wb 无FormatConditions属性
        rng.FormatConditions(rng.FormatConditions.Count).Interior.ColorIndex = 3
            # 给前面新建的添加格式 前面新建的在最末
      或：
        fmt = rng.FormatConditions.Add(CON.xlCellValue,CON.xlEqual,'A')
        fmt.Interior.ColorIndex = 3
        fmt.Border  # 抛异常
        excel.Selection.FormatConditions(excel.Selection.FormatConditions.Count).SetFirstPriority()

        [csc1,csc2,csc3] = [excel.Selection.FormatConditions(1).ColorScaleCriteria(n) for n in range(1,4)]
        csc1.Type = win32.constants.xlConditionValueLowestValue
        csc1.FormatColor.Color = 13011546
        csc1.FormatColor.TintAndShade = 0

    # AddComment 添加批注
        sht.Cells(1).AddComment("abc")      # 同一地址不能重复添加
        sht.Cells(1).Comment.Visible = True # 批注显示或隐藏
        sht.Cells(1).Comment.Text('ppp')    # 更改批注内容
        sht.Cells(1).Comment.Delete()       # 删除

    # AutoFilter 自动筛选
        sht.AutoFilterMode = False  # 去掉原来的筛选
        sht.UsedRange.Columns(5).AutoFilter(1,"=C")
            # 参见VBA

    # FileDialog 文件对话框--->返完整路径
        fdag = excel.Application.FileDialog(3)
            # 参数： 3：文件选择 设置后可多选
                     4：文件夹选择
                     1：文件打开
        fdag.AllowMultiselect= True # 多选设置 文件夹时无效
        if fdag.show  == -1:        # 对话框点"确定"时返-1
            print(list(fdag.SelectedItems))  # 选择结果

    # PageSetup 页面设置
        pgs = sht.PageSetup
        pgs.Zoom = 150  # 缩放比例 10--400% 之间
        pgs.PrintArea = sht.UsedRange.Address  # 打印区域
        pgs.Orientation = win32.constants.xlLandscape
            # 横向打印  纵向为：xlPortrait
        sht.PrintPreview(True) # 打印预览

    #------------------------------------------

    from win32com.client import Dispatch
    import win32com.client as win32

    class easyExcel:
        """一个使Excel更易于获取的实用程序。记住
       保存数据是你的问题，正如错误处理一样。
       一次操作在一本工作簿上"""

        def __init__(self, filename=None):
            self.xlApp = win32.Dispatch('Excel.Application')
            if filename:
                self.filename = filename
                self.xlBook = self.xlApp.Workbooks.Open(filename)
            else:
                self.xlBook = self.xlApp.Workbooks.Add()
                self.filename = ''

        def save(self, newfilename=None):
            if newfilename:
                self.filename = newfilename
                self.xlBook.SaveAs(newfilename)
            else:
                self.xlBook.Save()

        def close(self):
            self.xlBook.Close(SaveChanges=0)
            del self.xlApp

        def getCell(self, sheet, row, col): #获取单元格的数据
            sht = self.xlBook.Worksheets(sheet)
            return sht.Cells(row, col).Value

        def setCell(self, sheet, row, col, value): #设置单元格的数据
            sht = self.xlBook.Worksheets(sheet)
            sht.Cells(row, col).Value = value

        def getRange(self, sheet, row1, col1, row2, col2):
            #获得一块区域的数据，返回为一个二维元组
            "return a 2d array (i.e. tuple of tuples)"
            sht = self.xlBook.Worksheets(sheet)
            return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value

        def addPicture(self, sheet, pictureName, Left, Top, Width, Height):  #插入图片
            sht = self.xlBook.Worksheets(sheet)
            sht.Shapes.AddPicture(pictureName, 1, 1, Left, Top, Width, Height)

        def cpSheet(self, before): #复制工作表
            shts = self.xlBook.Worksheets
            shts(1).Copy(None,shts(1))  # Copy(Before,After)

# wps.Application.Quit()
    if __name__ == "__main__":
        PNFILE = r'c:\screenshot.bmp'
        xls = easyExcel(r'D:\test.xls')
        xls.addPicture('Sheet1', PNFILE, 20,20,1000,1000)
        xls.cpSheet('Sheet1')
        xls.save()
        xls.close()

#-----------------------------------
# 例：将工作表转化为JSON

    import _wh_lib as wh
    import json

    wps = win32.gencache.EnsureDispatch('Excel.Application')
    wps.Visible = True

    wb = wps.Workbooks.Open('D:\ABC分析.xls')
    sht = wb.Worksheets(1)
    rows = sht.UsedRange.Rows

    res = list()
    json.encoder.FLOAT_REPR = lambda x:format(x,'.4f')
        # 设置小数位
    with wh.TimeTest():
        #--------------------------
        keys = rows(2).Value[0]  # 列表元素为字典的key
            # rows的参数从1开始
        for i in range(3,len(rows)):
            res.append(OrderedDict(zip(keys,rows(i).Value[0])))

        s = json.dumps(res,indent=4,ensure_ascii=False)
        print(s)
        # -------下面的算法快得多-----
        # vals = sht.UsedRange.Rows.Value  # 一次获取全部值
        # keys = vals[1]  # 列表从0开始计数
        # for row in range(2,len(vals)):
            # res.append(OrderedDict(zip(keys,vals[row])))

        # s = json.dumps(res,indent=4,ensure_ascii=False)
        # print(s)

