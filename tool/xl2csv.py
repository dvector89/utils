# -*- coding: utf8 
import sys
import xlrd

FLOAT = 2
TEXT = 1

def xl2csv(fin, fout, cols, bookid):
    data = xlrd.open_workbook(fin)
    table = data.sheets()[bookid]
    with open(fout, 'w') as f:
        for i in range(table.nrows):
            temp = ''
            for col in cols:
                if FLOAT == table.cell(i, col).ctype:
                    temp += str(table.cell(i, col).value) + '\t'
                elif TEXT == table.cell(i, col).ctype:
                    temp += table.cell(i, col).value.encode('utf8').replace('\n', '    ').replace('\t', '  ') + '\t'
            f.write(temp.strip()+'\n')
    return

if __name__ == '__main__':
    fin, fout, bookid = sys.argv[1:4] # bookid is sheet num, from 0; cols: 栏目 从1 开始，是序列
    bookid = int(bookid) # begin by 0
    cols = [int(x)-1 for x in sys.argv[4:]]
    xl2csv(fin, fout, cols, bookid)
    
        
