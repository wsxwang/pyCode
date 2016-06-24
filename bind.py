#-*-coding:utf-8-*-

import xlrd
import xlwt

def unicodeTupleToStr(u):
    ret = u'';
    for c in u:
        ret = ret + unicode(c) + u',';
    return ret;

def readRows(filename):
    book = xlrd.open_workbook(filename);
    sheet = book.sheets()[0];

    rows = []
    
    for i in range(sheet.nrows):
        rows.append(sheet.row_values(i))

    return rows;

# 比较两个cell，一方包含另一方即返回成功
def cmpCells(c1,c2):
    cmpkey1 = c1;
    cmpkey2 = c2;
    if isinstance(c1, unicode) == False:
        cmpkey1 = unicode(c1);
    if isinstance(c2, unicode) == False:
        cmpkey2 = unicode(c2);
    return cmpkey1==cmpkey2;
    return cmpkey1 in cmpkey2 or cmpkey2 in cmpkey1;

# 根据第三列值合并掌厅、短厅文件
def bind_ztdt():
    rows1 = readRows("zt.xlsx");
    rows2 = readRows("dt.xls");
    rows3 = [];
    
    for r1 in rows1:
        found = False;
        for r2 in rows2:
            if cmpCells(r1[2], r2[2]):
                found = True;
                r1 += r2;
                rows2.remove(r2);
                break;
        if found == False:
            r1 += (-1,  '', '');
        rows3.append(r1);

    book3 = xlwt.Workbook(encoding='utf-8');
    sheet3 = book3.add_sheet("bind_ztdt");
    for i in range(len(rows3)):
        for j in range(6):
            sheet3.write(i, j, rows3[i][j]);
    for i in range(len(rows2)):
        sheet3.write(i+len(rows3), 0, -1);
        sheet3.write(i+len(rows3), 1, '');
        sheet3.write(i+len(rows3), 2, '');
        sheet3.write(i+len(rows3), 3, rows2[i][0]);
        sheet3.write(i+len(rows3), 4, rows2[i][1]);
        sheet3.write(i+len(rows3), 5, rows2[i][2]);
    book3.save("bind_ztdt.xls");

#在指定列从第startRowIndex行开始向上查找不是空的cell，返回一个tuple(index, cell value)
def getUpCell(rows, colIndex, startRowIndex):
    if startRowIndex == 0:
        return (startRowIndex,rows[startRowIndex][colIndex]);
    if rows[startRowIndex][colIndex] != u'':
        return (startRowIndex,rows[startRowIndex][colIndex]);
    return getUpCell(rows, colIndex, startRowIndex-1);


# 根据第二、三列值合并网厅到汇总文件
def bind_wt():
    rows1 = readRows("wt.xlsx");
    rows2 = readRows("hz.xlsx");

    for i in range(len(rows2)):
        if i < 2:
            continue;
        
        cell2 = getUpCell(rows2, 2, i)[1];
        cell3 = getUpCell(rows2, 3, i)[1];

        cell2inwt = getUpCell(rows1, 2, i)[1];
        cell3inwt = getUpCell(rows1, 3, i)[1];
        if cmpCells(cell2, cell2inwt) and cmpCells(cell3, cell3inwt):
            if rows2[i][7] == u'':
                rows2[i][7] = rows1[i][8];
            for c in [10,11,12,13,14]:
                if rows2[i][c] == u'':
                    rows2[i][c] = rows1[i][c+4];

    book3 = xlwt.Workbook(encoding='utf-8');
    sheet3 = book3.add_sheet("bind_wt");
    for i in range(len(rows2)):
        for j in range(len(rows2[i])):
            sheet3.write(i, j, rows2[i][j]);
    book3.save("bind_wt.xls");

#汇总bind_wt.xls和bind_ztdt.xls
def bind():
    rows1 = readRows("bind_ztdt.xls");
    rows2 = readRows("bind_wt.xls");
    rows2.append([u'' for i in range(15)]);
    rows2.append([u'' for i in range(15)]);
    rows2.append([u'' for i in range(15)]);
    rows2.append([u'' for i in range(15)]);

    for r1 in rows1:
        cellzt = r1[2];
        celldt = r1[5];
        found = False;
        for i in range(len(rows2)):
            cellwt = rows2[i][3];
            if r1[0] != -1:
                if cmpCells(cellwt, r1[2]):
                    found = True;
                    if rows2[i][8] == u'':
                        rows2[i][8] = r1[1];
            if r1[3] != -1:
                if cmpCells(cellwt, r1[5]):
                    found = True;
                    if rows2[i][9] == u'':
                        rows2[i][9] = r1[4];
        if found == False:
            newRow = [u'' for i in range(15)];
            if r1[0] != -1:
                newRow[3] = r1[2];
                newRow[8] = r1[1];
            if r1[3] != -1:
                newRow[3] = r1[5];
                newRow[9] = r1[4];
            rows2.append(newRow);
            
    book3 = xlwt.Workbook(encoding='utf-8');
    sheet3 = book3.add_sheet("bind");
    for i in range(len(rows2)):
        for j in range(len(rows2[i])):
            sheet3.write(i, j, rows2[i][j]);
    book3.save("bind.xls");
                    
    
if __name__ == "__main__":
    try:
        #bind_ztdt();
        #bind_wt();
        bind();
    except Exception,e:
        print str(e);
