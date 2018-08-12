#-*-coding:utf-8*-

"""
wp_api_fs.py
Wang Xiaoqi
create:2018-08-12
一些文件操作的封装
"""

import os

"""
查找指定目录下的所有扩展名
返回一个dictionary，key是小写的扩展名，值是每个扩展名的文件数目
"""
def get_ext(path_name):
    ret = {};
    files = os.listdir(path_name);
    for f in files:
        absf = os.path.join(path_name, f);
        if (os.path.isdir(absf)):
            sub_ext = get_ext(absf);
            for k in sub_ext.keys():
                if(ret.has_key(k) == False):
                    ret[k] = 0;
                ret[k] += sub_ext[k];
        else:
            ext = os.path.splitext(absf)[1][1:].lower();
            if(ret.has_key(ext) == False):
                ret[ext] = 0;
            ret[ext] = ret[ext] + 1;
    return ret;

"""
查找指定目录下指定扩展名的文件
返回一个set()，元素是查找到的文件绝对路径名
exts:一个list，元素是指定的扩展名，空表示所有
path_name:查找的目录
"""
def find_files(path_name, exts):
    ret = set();
    files = os.listdir(path_name);
    for f in files:
        absf = os.path.join(path_name, f);
        if (os.path.isdir(absf)):
            ret.update(find_files(absf, exts));
        else:
            ext = os.path.splitext(absf)[1][1:].lower();
            if((len(exts) == 0) or (ext in exts)):
                ret.add(absf);
    return ret;
    
    
"""
------------------------------------------------------------------------
main
"""
if __name__ == "__main__":
    ext = get_ext("d:\\");
    print(ext);
    files = find_files("d:\\", ["avi"]);
    print(files);
    for f in files:
        print (f);

                       
