#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" JSON for log configuration """

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import codecs
import json
import logging
import logging.config
import sys


def main():
    # each time we need to log something we can create a logger object
    # The operation of creating a logger should be quite cheap.
    # getLogger() without arguments returns the "root" logger.
    logger = logging.getLogger()
    logger.info("This is an INFO message on the root logger.")

    # If we need to separate things, we can always create child loggers:
    child = logging.getLogger().getChild("child")
    child.warning("This is a WARNING message on the child logger.")

    # let's create an error. This will send an email
    child.error("This is an ERROR message.")

    # With this line we can see how the "mypkg" loggers work
    import mypkg




if __name__ == "__main__":
    # create an initial logger. It will only log to console and it will disabled
    # when we read the logging configuration from the config file.
    # This logger can be useful when we need early logging. E.g. we may want to log
    # the location of the JSON file (e.g. if we get it from a CLI argument).
    logging.basicConfig(level="INFO")
    logger = logging.getLogger()
    logger.info("This is the logger configured by `logging.basicConfig()`.")
    logger.info("We will disable this logger when we setup logger using the config file.")
    logger.info("This logger can be useful if we e.g. want to log the path of the config file")
    logger.info("we will be using which we can get e.g. as a command line argument etc.")
    logger.info("")

    # set up proper logging. This one disables the previously configured loggers.
    config_file = "log_config%d.json" % sys.version_info.major
    logger.info("config file: %s", config_file)

    # We use codecs.open because it is equivalent to Python 3 open()
    with codecs.open(config_file, "r", encoding="utf-8") as fd:
        logging.config.dictConfig(json.load(fd))

    logger = logging.getLogger()   # Probably not needed, but we don't lose anything to get it
    logger.info("This is the logger configured by `logging.config.dictConfig()`.")

    main()
