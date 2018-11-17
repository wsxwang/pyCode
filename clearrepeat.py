import os;

if __name__ == "__main__":
    files = os.listdir("./");
    for f in files:
        if(f.endswith('.jpg')==False):
            continue;
        t = f.replace('[1]', '');
        if (os.path.exists(t)):
            os.remove(t);
            print "remove ", t;
        else:
            os.rename(f,t);
            print f, "-->", t;
