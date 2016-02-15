import os

class DSFileLogger :
    def __init__(self,fpath,headers):
        self.fpath = fpath
        self.file = None
        if os.path.isfile(fpath) :
            self.file = open(fpath,"w+")
        else :
            self.file = open(fpath,"w")
            hdr = headers.pop(0)
            self.file.write(hdr)
            for hdr in headers :
                self.file.write(", " + hdr)

    def log(self,temps) :
        temp = temps.pop(0)
        self.file.write(str(temp))
        for temp in temps :
            self.file.write(", " + str(temp))

    def close(self):
        self.file.close()
