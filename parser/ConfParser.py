import os
import ConfigParser
from types import MethodType

CONFIG_FILE = 'config.cfg'
CONNECTION_SECTION = 'connection'


class ConfParser(object):
    def __init__(self, filepath):
        self.__config__ = None
        self.filepath = filepath

    def parse(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(os.path.join(self.filepath, CONFIG_FILE)))
        self.__config__ = config

    def __getConf__(self):
        print "asd"
        # print "getconf:" + key
        # return self.__config__.get(CONNECTION_SECTION, key)

    def __getattr__(self, name, **kwargs):
        if name[:3] == "get":
            attrib_name = name[3:]
            setattr(self, name, MethodType(self.__getConf__, self, type(self)))

            return self
            #return self.__getConf__(attrib_name[:1].lower() + attrib_name[1:])
        raise AttributeError("Not found %s attribute" % name)
