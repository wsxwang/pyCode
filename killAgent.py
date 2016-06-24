import os
import time

# check whether Agent.exe is running,<0--not running, >=0--running
def checkAgent():
    output = os.popen("tasklist /Nh /FI \"IMAGENAME eq Agent*\"");
    echoInfo = output.read();
    ret = echoInfo.find("Agent")
    if ret >= 0:
        print echoInfo;
    return ret

# kill Agent.exe
def killAgent():
    output = os.popen("taskkill /F /IM Agent.exe")
    print output.read()

if __name__ == "__main__":
    while (1):
        if (checkAgent() >= 0):
            killAgent();
            print "sleep for 5 minutes"
            time.sleep(300);
        else:
            print "wait for Agent.exe"
            time.sleep(60)

