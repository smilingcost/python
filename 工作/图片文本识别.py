# coding=utf-8

from PIL import Image
import pytesseract
tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'  #文件配置中指定tessdata-dir
img=Image.open(u'C:/Users/Administrator/Desktop/QQ截图20171129155756.jpg')
img.show()
text=pytesseract.image_to_string(img,lang='chi_sim',config=tessdata_dir_config)
f=open('text.txt',"wb")
f.write(text)
f.close()

print text

#tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'