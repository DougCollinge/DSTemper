import os
import json

class DSSettings:

    def __init__(self,fpath):
        self.settingsPath = fpath
        if os.path.isfile(fpath) :
            fp = open(self.settingsPath,"r")
            self.settings = json.load(fp)
            fp.close()
        else :
            self.settings = {
                "samplePeriod": 2,
                "loggingEnabled": False,
                "loggingFilePath": None
            }
            self.dump()

    def dump(self):
        fp = open(self.settingsPath,"w")
        if fp != None :
            json.dump(self.settings,fp,indent=4)
            fp.close()

    def set(self,name,value):
        print "set {} to {}:",name,value
        self.settings[name] = value
        self.dump()

    def get(self,name):
        return self.settings[name]

# setz = DSSettings(os.path.expanduser("~/.DSTemper.settings"))
#
# setz.set("peanuts",432)
# print setz.get("peanuts")


