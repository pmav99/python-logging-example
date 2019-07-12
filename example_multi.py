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
import logging

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

from ruamel.yaml import YAML

yaml=YAML(typ="safe", pure=True)


def get_yaml_config():
    config_file = "log_config.yml"
    # We use codecs.open because it is equivalent to Python 3 open()
    with codecs.open(config_file, "r", encoding="utf-8") as fd:
        config = yaml.load(fd.read())
    return config


def _multi(ExecutorClass, pool_size, task, task_kwargs):
    with ExecutorClass(pool_size) as executor:
        futures = [executor.submit(task, **kwargs) for kwargs in task_kwargs]
    results = [ft.result() for ft in as_completed(futures)]
    return results


def multithread(no_threads, task, task_kwargs=None):
    results = _multi(ThreadPoolExecutor, no_threads, task, task_kwargs)
    return results


def multiprocess(no_processes, task, task_kwargs=None):
    results = _multi(ProcessPoolExecutor, no_processes, task, task_kwargs)
    return results


def task(a, b, c, d=None):
    logger.info("a: %s", a)
    logger.info("b: %s", b)
    logger.info("c: %s", c)
    logger.info("d: %s", d)


kwargs = [
    dict(a=1, b=2, c=1),
    dict(a=2, b=3, c=3),
    dict(a=4, b=4, c=4),
    dict(a=4, b=4, c=4, d=9),
    dict(a=4, b=4, c=4, d=8),
    dict(a=4, b=4, c=4),
    dict(a=4, b=4, c=4),
    dict(a=4, b=4, c=4),
]


def main():
    logger.info("Starting multithread")
    multithread(4, task, kwargs)
    logger.info("Finished multithread")

    logger.info("Starting multiprocess")
    multiprocess(4, task, kwargs)
    logger.info("Finished multiprocess")


if __name__ == "__main__":
    # get log configuration
    # log_config = get_json_config()
    log_config = get_yaml_config()

    # set up proper logging. This one disables the previously configured loggers.
    logging.config.dictConfig(log_config)

    # create the logger object
    logger = logging.getLogger()

    main()
