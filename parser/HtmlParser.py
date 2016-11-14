import urllib2

from parser.AbstractParse import AbstractParse


class HtmlParser(AbstractParse):
    def __init__(self, url):
        self.url = url

    def parse(self):
        print self.__get_content()
#        return self.__get_content()


    def __get_content(self):
        return urllib2.urlopen(self.url).read()

