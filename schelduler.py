#!/usr/bin/env python
__author__ = "Dawid Bialy"
__copyright__ = "Copyright 2016, WhiteCorp"
__status__ = "Development"

import os
import sys

from parser.ConfParser import ConfParser
from parser.HtmlParser import HtmlParser

dir_path = os.path.dirname(sys.modules['__main__'].__file__)

if __name__ == "__main__":
    config = ConfParser(dir_path)
    config.parse()

    print config.get_url()
#    exit(0)

    html = HtmlParser(config.get_url()).parse()
    # plan = PlanParser(config.get_url())

    print "yup"
