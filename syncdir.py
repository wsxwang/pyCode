#-*-coding:utf-8*-

"""
syncdir.py
Wangxiaoqi
create:2016-09-15
同步两个目录所有内容
"""

import Tkinter as tk
import tkMessageBox
import os


class Values:
    c_dir1 = None;
    c_dir2 = None;
    c_ignoredir = None;
    c_ignoreext = None;
    c_syncmethod = None;

    set1 = set();
    set2 = set();

def createWidgets(master):
    r = 0;
    tk.Label(master, text="目录1").grid(row=r, column=0, sticky=tk.W);
    values.c_dir1 = tk.Entry(master, width=100);
    values.c_dir1.grid(row=r, column=1, columnspan=2);

    r = r + 1;
    tk.Label(master, text="目录2").grid(row=r, column=0, sticky=tk.W);
    values.c_dir2 = tk.Entry(master, width=100);
    values.c_dir2.grid(row=r, column=1, columnspan=2);

    r = r + 1;
    tk.Label(master, text="忽略的子目录").grid(row=r, column=0, sticky=tk.W);
    values.c_ignoredir = tk.Entry(master, width=100);
    values.c_ignoredir.insert(0, "以逗号分割");
    values.c_ignoredir.grid(row=r, column=1, columnspan=2);

    r = r + 1;
    tk.Label(master, text="忽略的文件名扩展名").grid(row=r, column=0, sticky=tk.W);
    values.c_ignoreext = tk.Entry(master, width=100);
    values.c_ignoreext.insert(0, "以逗号分割");
    values.c_ignoreext.grid(row=r, column=1, columnspan=2);

    r = r + 1;
    tk.Button(master, text="列举不同",width=10, command=btfunc_list).grid(row=r,column=0);

    r = r + 1;
    tk.Button(master, text="采取操作",width=10, command=btfunc_do).grid(row=r,column=0);
    values.c_syncmethod = tk.Listbox(master, selectmode = tk.SINGLE, width=40, height=6);
    for item in ["仅复制目录1特有文件到目录2", "仅复制目录2特有文件到目录1", "相互复制文件", "仅删除目录1特有文件及目录", "仅删除目录2特有文件及目录", "仅保留两个目录相同的文件及目录"]:
        values.c_syncmethod.insert(tk.END, item);    
    values.c_syncmethod.grid(row=r, column=1, sticky=tk.W);
    values.c_syncmethod.select_set(0, 0);


def btfunc_do():
    print values.c_dir1.get();
    print values.c_dir2.get();
    print values.c_ignoredir.get();
    print values.c_ignoreext.get();
    print values.c_syncmethod.curselection();
    print values.c_syncmethod.get(values.c_syncmethod.curselection());

def btfunc_list():
    listdiff(os.path.realpath(values.c_dir1.get()), os.path.realpath(values.c_dir2.get()));
    
    print "\n\nonly1"
    for i in  values.set1:
        print i
    print "\nonly2"
    for i in values.set2:
        print i

    #... 保存在txt中
    tkMessageBox.showinfo("", "结果保存在diff.txt中");
    
def ignorefile(path1, path2):
    try:
        if ((os.path.isdir(path1) == False) and (os.path.isdir(path2) == False)) == False:
            return False;
        # 两个文件是否相同则忽略
        if (os.path.getsize(path1) == os.path.getsize(path2)):
            return True;
        # 文件扩展名相同则忽略
        sufix = os.path.splitext(path1)[1][1:];
        if values.c_ignoreext.get().find(sufix) > 0:
            return True;
    except Exception as e:
        print '[', path1, '|', path2, ']', e;
    return False;

        
"""
列举两个目录的不同之处
步骤：
扫描dir1和dir2，
    对于不同文件及子目录，记录在日志中    
    对于同名子目录，递归查找
"""
def listdiff(dir1, dir2):
    files1 = os.listdir(dir1);
    files2 = os.listdir(dir2);
    only1 = set(files1).difference(set(files2));
    only2 = set(files2) - (set(files1));
    both = set(files1)&set(files2);
    for item in only1:
        sub1 = os.path.join(dir1, item);
        values.set1 = values.set1.union(set([sub1]));
    for item in only2:
        sub2 = os.path.join(dir2, item);
        values.set2 |= set([sub2]);
    for item in both:
        sub1 = os.path.join(dir1, item);
        sub2 = os.path.join(dir2, item);
        if os.path.isdir(sub1) and os.path.isdir(sub2):
            #检查是否需要忽略该子目录
            listdiff(sub1, sub2);
            continue;
        elif ignorefile(sub1, sub2):
            continue;
        else:
            values.set1 = values.set1.union(set([sub1]));
            values.set2 |= set([sub2]);

    
"""
------------------------------------------------------------------------
main
"""
values = Values();

if __name__ == "__main__":
    root = tk.Tk();

    createWidgets(root);
    
    root.title("同步两个目录的所有内容");
    root.mainloop();
