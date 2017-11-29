# coding=utf-8

from PyPDF2 import PdfFileReader, PdfFileWriter
readFile = u'E:/文件/其他/人易系统/人易合同.PDF'
#writeFile = 'write.pdf'
# 获取一个 PdfFileReader 对象
pdfReader = PdfFileReader(open(readFile, 'rb'))
# 获取 PDF 的页数
pageCount = pdfReader.getNumPages()
print pageCount
# 返回一个 PageObject
#page = pdfReader.getPage(i)
# 获取一个 PdfFileWriter 对象
#pdfWriter = PdfFileWriter()
# 将一个 PageObject 加入到 PdfFileWriter 中
#pdfWriter.addPage(page)
# 输出到文件中
#pdfWriter.write(open(writeFile, 'wb'))