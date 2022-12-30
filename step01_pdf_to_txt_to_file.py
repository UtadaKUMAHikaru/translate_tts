# -*- encoding: utf-8 -*-
# 单个文件直接运行

try:
    from urllib.request import urlopen
except:
    from urllib import urlopen

from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import  LAParams

# 读取pdf的函数，返回内容
def readPdf(pdf_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr=rsrcmgr, outfp=retstr, laparams=laparams)

    process_pdf(rsrcmgr=rsrcmgr, device=device, fp=pdf_file)
    device.close()

    content = retstr.getvalue()
    retstr.close()

    return content

def pdf_to_txt_to_file(name):
    url = name + '.pdf'

    pdf_file = open( url,'rb')

    # pdf_file = urlopen(url) # 也可以换成本地pdf文件，用open rb模式打开
    content = readPdf(pdf_file)

    import re
    new_content = re.sub(r'\n',' ', content)

    # print(new_content)
    pdf_file.close()

    fo = open(name+r'英.txt', 'w')
    fo.write(new_content)

if __name__ == '__main__':

    name = r"/Users/chendeen/Desktop/能量/Automatic Story Generation- A Survey of Approaches"
    pdf_to_txt_to_file(name)
