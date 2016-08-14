#-*-coding:utf-8-*-
"""
使用正则表达式检测字符串中的IP地址
"""

import os
import time
import re
import sys

pattern="(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])";

"""
判断是否IP地址
"""
def is_ip(inputstr):
    m = re.match(pattern, inputstr);
    return m != None;

def find_ip(inputstr):
    return re.findall(pattern, inputstr);
   
if __name__ == "__main__":
    assert is_ip("1.2.3.4") == True;
    assert is_ip("001.2.3.4") == True;
    assert is_ip("1.2.3.04") == True;
    assert is_ip("123.2.0.4") == True;
    assert is_ip("1.2.3.204") == True;
    assert is_ip("999.2.3.4") == True;
    assert is_ip("9.2.3.") == False;
    assert is_ip("9.2..4") == False;

    assert find_ip("1.2.3.4") == ["1.2.3.4"];
    assert find_ip("1.2.3.4\r2.3.4.5") == ["1.2.3.4","2.3.4.5"];


        
