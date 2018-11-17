#-*-coding:utf-8*-

"""
gallery.py
Wangxiaoqi
create:2018-11-27
看网站的图
"""

import os
from PIL import Image
import matplotlib.pyplot as plt
import requests
import urlparse



"""
------------------------------------------------------------------------
different from web site
"""
def NextImg(url):
    urldict = urlparse.urlparse(url);
    pathdict = urldict.path.split('/');
    numstr=url[52:64];
    num=long(numstr);
    num=num+1;
    ret = url.replace(numstr, str(num));
    return ret;
    
def PreImg(url):
    urldict = urlparse.urlparse(url);
    pathdict = urldict.path.split('/');
    numstr=url[52:64];
    num=long(numstr);
    num=num-1;
    ret = url.replace(numstr, str(num));
    return ret;
    
def LocalImg(url):
    path = url.replace("http://p7.urlpic.club/pic1893/upload/image/20181117/", "C:\\Users\\wsxra\\Downloads\\bt\\");
    return path;


"""
------------------------------------------------------------------------
function
"""
def get_onefile(url):
    print 'url=', url;
    path = LocalImg(url);
    if(os.path.exists(path) == True):
        print 'buffered';
    else:
        print "get...";
        response = requests.get(url);
        print(response.status_code);
        if(response.status_code == 200):
            with open(path, "wb") as writer:
                writer.write(response.content);
                print 'done';
    return path;

def show_oneimg(path):
    plt.clf();
    img = Image.open(path);
    plt.imshow(img);
    plt.autoscale(enable=True,axis='both',tight=True);
    plt.draw();

def get_pre():
    global g_curUrl;
    print "pre";
    g_curUrl = PreImg(g_curUrl);
    path = get_onefile(g_curUrl);
    if (path != None):
        show_oneimg(path);

        
def get_next():
    global g_curUrl;
    print "next";
    g_curUrl = NextImg(g_curUrl);
    path = get_onefile(g_curUrl);
    if (path != None):
        show_oneimg(path);

    
"""
------------------------------------------------------------------------
gui event
"""
def on_click(event):
    print event;
    
def on_press(event):
    if event.key == 'left':
        get_pre();
    if event.key == 'right':
        get_next();
    
"""
------------------------------------------------------------------------
main
"""
g_curUrl = None;
if __name__ == "__main__":
    g_curUrl = "http://p7.urlpic.club/pic1893/upload/image/20181117/111700067075.jpg";
    plt.axis('equal');
    plt.box(False);
    plt.connect('button_press_event', on_click);
    plt.connect('key_press_event', on_press);
    plt.show();
     

