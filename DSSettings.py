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
            self.settings = {}

    def default(self,name,value):
        if not name in self.settings :
            self.set(name,value)

    def dump(self):
        fp = open(self.settingsPath,"w")
        if fp != None :
            json.dump(self.settings,fp,indent=4)
            fp.close()

    def set(self,name,value):
        # print "set {} to {}:",name,value
        self.settings[name] = value
        self.dump()

    def get(self,name):
        if name in self.settings :
            return self.settings[name]
        else :
            return None

# setz = DSSettings(os.path.expanduser("~/.DSTemper.settings"))
#
# setz.set("peanuts",432)
# print setz.get("peanuts")


