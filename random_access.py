#-*-coding:utf-8*-

"""
random_access.py
Wang Xiaoqi
create:2018-08-12
随机访问视频文件
"""

import os
from wp_api_fs import *


video_ext = ["avi", "mkv", "mp4", "mpg", "mov", "rm", "rmvb", "wmv"];


"""
------------------------------------------------------------------------
main
"""
if __name__ == "__main__":
    ret = find_files("d:\\09-bt", video_ext);
    print(ret);
