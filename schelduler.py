#!/usr/bin/env python

from parser.ConfParser import ConfParser
import os

import sys

__author__ = "Dawid Bialy"
__copyright__ = "Copyright 2016, WhiteCorp"
__status__ = "Production"

dir_path = os.path.dirname(sys.modules['__main__'].__file__)



if __name__ == "__main__":
    config = ConfParser(dir_path)
    config.parse()
    config.getUrl()

    print "yup"