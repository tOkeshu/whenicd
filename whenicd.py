#!/usr/bin/env python

from os.path import exists, join, dirname
from os import getcwd, system as cmd
from sys import argv


def cdrc(directory):
    return join(directory, ".cdrc")

def cdrc_exists(directory):
    return exists(cdrc(directory))

def get_cdrc_path(path):
    if path == '/':
        return None
    return cdrc(path) if cdrc_exists(path) else get_cdrc_path(dirname(path))


if __name__ == '__main__':
    path = get_cdrc_path(getcwd())
    if path:
        cmd("bash {}".format(path))

