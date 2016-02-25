import os

class DSFileLogger :
    def __init__(self,settings):
        self.settings = settings

        self.file = None
        self.enabled = False
        # self.headerLineWritten = os.path.isfile(fpath)

    def set_headers(self,headers):
        self.headers = headers

    def log(self, datetime, temps) :
        if not self.enabled :
            return

        fpath = headers.get("loggingFileName")
        if fpath == None :
            return

        self.headerLineWritten = os.path.isfile(fpath)
        if self.headerLineWritten :
            self.file = open(self.fpath,"a")
        else :
            self.file = open(self.fpath,"w")
            self.file.write("DateTime")
            # hdr = headers.pop(0)
            # self.file.write(hdr)
            for hdr in self.headers :
                self.file.write(", " + hdr)
            self.file.write("\n")
            self.headerLineWritten = True

        self.file.write(datetime)
        # temp = temps.pop(0)
        # self.file.write(str(temp))
        for temp in temps :
            self.file.write(", " + str(temp))
        self.file.write("\n")
        self.file.close()

    def close(self):
        self.file.close()

    def set_enabled(self,enabled):
        self.enabled = enabled

    def set_fpath(self,fpath):
        self.fpath = fpath