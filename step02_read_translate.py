# 单个文件直接运行

from itertools import islice
import translators as ts
import re
# from icecream import ic

# def next_n_lines(file_opened, N):
#     return [x.strip() for x in islice(file_opened, N)]

def read_translate(basename):
    out = ""
    block_size = 4500
    # block_size = 4999
    count = 0


    path = basename + '英.txt'

    with open(path,'r') as f:
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
            print(chunk)
            # output = ts.deepl(chunk, sleep_seconds=5, to_language='zh')
            output = ts.google(chunk, sleep_seconds=5.5, to_language='zh')
            # output = ts.baidu(chunk, professional_field='common')

            output_rep = re.sub("[\{\(\[（].*?[）\)\]\}]", "", output)
        
            print(output_rep)
            out+= output_rep

    # 打开一个文件
    fo = open(basename + '中.txt', "w")
    fo.write( out )



    # with open('/Users/chendeen/Desktop/Your Symphony of Selves Discover and Understand More of Who We Are (James Fadiman) (z-lib.org).txt','r') as f:
    #     ff=f.read()
    #     print(ts.translate_html(ff, translator=ts.google, to_language='en', n_jobs=-1))
if __name__ == '__main__':
    basename = r'/Users/chendeen/Desktop/能量/Automatic Story Generation- A Survey of Approaches'
    read_translate(basename)
