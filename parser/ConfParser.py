import os
import ConfigParser
import types
from types import MethodType

from parser.AbstractParse import AbstractParse

CONFIG_FILE = 'config.cfg'
CONNECTION_SECTION = 'connection'


class ConfParser(AbstractParse):
    def __init__(self, filepath):
        self.__config__ = None
        self.filepath = filepath

        #setattr(self, "get_url", self.__get_conf__)

    def parse(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(os.path.join(self.filepath, CONFIG_FILE)))
        self.__config__ = config
#        self.__bind_attributes()

    def get_url(self):
        return self.__config__.get(CONNECTION_SECTION, "url")


    def __bind_attributes(self):
        attribuites = dict(self.__config__.items(CONNECTION_SECTION))
        for key, val in attribuites.items():
            #setattr(self, "get_" + key, )
            self.__dict__.update({key: val})

    def __get_conf__(self, *args,**kwarg):
        return self.__config__.get(CONNECTION_SECTION, "url")



    # def __getattr__(self, name, **kwargs):
    #
    #
    #     if name[:3] == "get":
    #         attrib_name = name[4:]
    #
    #         print self.__dict__.get(attrib_name)
    #         #return self.__dict__.get(attrib_name)
    #
    #         return self
    #         #return self.__getConf__(attrib_name[:1].lower() + attrib_name[1:])
    #     raise AttributeError("Not found %s attribute" % name)
