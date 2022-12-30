from step01_pdf_to_txt_to_file import pdf_to_txt_to_file
from step02_read_translate import read_translate
import os
dirname = r'/home/c/Desktop/ref'
for filename in os.listdir(dirname):
    if filename.endswith('pdf'):
        print(os.path.join(dirname, filename))
        path = os.path.join(dirname, filename)
        pdf_to_txt_to_file(path[:-4])
        read_translate(path[:-4])

