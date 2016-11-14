import urllib

from parser.AbstractParse import AbstractParse

PLAN_FILE_NAME = "plan.xml"


class PlanParser(AbstractParse):
    def __init__(self, url):
        self.url = url

    def parse(self):
        response = urllib.urlretrieve(self.url, PLAN_FILE_NAME)
        return response
