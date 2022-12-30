from itertools import islice
import translators as ts

out = ''
block_size = 4999
count = 0

from pdf_to_txt_to_file import readPdf
content = readPdf(r"/Users/chendeen/Desktop/Kostas, Unintentional intentionality AI&Culture.pdf")



with open('/Users/chendeen/Desktop/Your Symphony of Selves Discover and Understand More of Who We Are (James Fadiman) (z-lib.org).txt','r') as f:
    # while i in range(len(islice(f, 10))//10):
    # bytes_count = len(f.read())
    # f.seek(0,0)
    while True:
        chunk = f.read(block_size)
        # 当文件没有更多内容时，read 调用将会返回空字符串 ''
        if not chunk:
            break
        # ff=next_n_lines(f, 10)
        # print(ff)
        # print(len(ff))

        # tmp=''
        # for i in ff:
        #     tmp+=i
        output = ts.google(chunk, sleep_seconds=5, to_language='zh')
        print(output)
        out+= output

# 打开一个文件
fo = open("Your Symphony of Selves Discover and Understand More of Who We Are (James Fadiman) (z-lib.org)中.txt", "w")
fo.write( out )



# with open('/Users/chendeen/Desktop/Your Symphony of Selves Discover and Understand More of Who We Are (James Fadiman) (z-lib.org).txt','r') as f:
#     ff=f.read()
#     print(ts.translate_html(ff, translator=ts.google, to_language='en', n_jobs=-1))
