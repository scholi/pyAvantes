import struct
import numpy as np

_Raw8_Fields = [("version","5s"),
    ("numSpectra","B"),
    ("length","I"),
    ("seqNum","B"),
    ("measMode","B",{0:"scope",1:"absorbance",2:"scope corrected for dark",3:"transmission",4:"reflectance",5:"irradiance",6:"relative irradiance",7:"temperature"}),
    ("bitness","B"),
    ("SDmarker","B"),
    ("specID","10s"),
    ("userfriendlyname","64s"),
    ("status","B"),
    ("startPixel","H"),
    ("stopPixel","H"),
    ("IntTime","f"),
    ("integrationdelay","I"),
    ("Avg","I"),
    ("enable","B"),
    ("forgetPercentage","B"),
    ("Boxcar","H"),
    ("smoothmodel","B"),
    ("saturationdetection","B"),
    ("TrigMode","B"),
    ("TrigSource","B"),
    ("TrigSourceType","B"),
    ("strobeCtrl","H"),
    ("laserDelay","I"),
    ("laserWidth","I"),
    ("laserWavelength","f"),
    ("store2ram","H"),
    ("timestamp","I"),
    ("SPCfiledate","4c"),
    ("detectorTemp","f"),
    ("boardTemp","f"),
    ("NTC2volt","f"),
    ("ColorTemp","f"),
    ("CalIntTime","f"),
    ("fitdata","5d"),
    ("comment","130s")
]
class Raw8:
    def __init__(self, filename):
        self.res = {}
        with open(filename,"rb") as f:
            self.res = {}
            for k in _Raw8_Fields:
                s = struct.Struct(k[1])
                dat = s.unpack(f.read(s.size))
                if len(dat)==1:
                    dat = dat[0]
                self.res[k[0]] = dat
            dataLength =  self.res['stopPixel']-self.res['startPixel']+1
            self.dataLenth = dataLength
            self.data = {
                'wl': struct.unpack(f"<{dataLength}f",f.read(4*dataLength)),
                'scope': struct.unpack(f"<{dataLength}f",f.read(4*dataLength)),
                'dark': struct.unpack(f"<{dataLength}f",f.read(4*dataLength)),
                'ref': struct.unpack(f"<{dataLength}f",f.read(4*dataLength))
                }
    
    def getData(self, name):
        return np.array(self.data[name])

    def getScope(self):
        return self.getData("scope")

    def getWavelength(self):
        return self.getData("wl")

    def getDark(self):
        return self.getData("dark")

    def getRef(self):
        return self.getData("ref")