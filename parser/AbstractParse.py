class AbstractParse(object):
    def parse(self):
        raise ReferenceError("{0} not implement method {1}".format(self.__class__.__name__, "parse"))
