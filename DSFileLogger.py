import os

class DSFileLogger :
    def __init__(self,fpath,headers):
        self.fpath = fpath
        self.file = None
        self.enabled = False

        if os.path.isfile(fpath) :
            self.file = open(fpath,"w+")
        else :
            self.file = open(fpath,"w")
            hdr = headers.pop(0)
            self.file.write(hdr)
            for hdr in headers :
                self.file.write(", " + hdr)

    def log(self,temps) :
        if not self.enabled :
            return
        temp = temps.pop(0)
        self.file.write(str(temp))
        for temp in temps :
            self.file.write(", " + str(temp))

    def close(self):
        self.file.close()

    def set_enabled(self,enabled):
        self.enabled = enabled

    def set_fpath(self,fpath):
        self.fpath = fpath