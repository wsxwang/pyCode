#-*-coding:utf-8-*-
"""
检测列表中IP地址的链接速率
调用系统的ping命令
"""

import os
import time
import re
import sys

def ping_speed(ip):
    if os.name == "nt":
        cmd = "ping " + ip + " -n 1";
        pattern = "=(?P<speed>\d+)ms";
    else:
        cmd = "ping " + ip + " -c 2";
        pattern = "=(?P<speed>\d+) ms";
    output = os.popen(cmd);
    echoInfo = output.read();
    m = re.search(pattern, echoInfo);
    if m != None:
        return int(m.group("speed"));
    return sys.maxint;
   
if __name__ == "__main__":
    ip_lst = ["172.86.224.36"
              ,"173.247.231.43"
              ,"173.247.233.252"
              ,"107.151.131.204"
              ,"69.28.50.196"
              ,"162.221.4.12"
              ,"184.8.7.141"
              ,"174.139.64.86"
              ,"174.139.45.92"
              ,"173.247.233.170"
              ,"65.255.41.84"
              ,"174.139.94.78"
              ,"174.139.79.222"
              ,"100.43.143.230"
              ,"67.198.226.174"
              ,"174.139.43.45"
              ,"173.247.231.45"
              ];
    ip_speed_lst = [];
    for ip in ip_lst:
        pairs = (ip, ping_speed(ip));
        ip_speed_lst.append(pairs);
        print pairs;

    sortedlst = sorted(ip_speed_lst, key=lambda pairs:pairs[1]);
    print sortedlst;

        
