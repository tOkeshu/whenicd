#!/usr/bin/env python

from os.path import exists, join, dirname, expanduser
from os import getcwd, system as cmd
import json
from hashlib import sha256

def cdrc(directory):
    return join(directory, ".cdrc")

def cdrc_exists(directory):
    return exists(cdrc(directory))

def get_cdrc_path(path):
    if path == '/':
        return None
    return cdrc(path) if cdrc_exists(path) else get_cdrc_path(dirname(path))


def do_prompt(s, path):
    try:
        ans = raw_input(s)
    except (KeyboardInterrupt, EOFError):
        ans = "N"
    while (ans in ["?","h","help"]) or (ans in ["i","inspect"]):
        if ans in ["?","h","help"]:
            print """y - Do execute this file
n - Do not execute this file (default)
i - Inspect file content
? - This help"""
        elif ans in ["i","inspect"]:
            print "== Content of {} ==".format(path)
            for line in file(path).readlines():
                print "> ", line,
            print "== End of {} ==".format(path)
        try:
            ans = raw_input(s)
        except (KeyboardInterrupt, EOFError):
            ans = "N"
    if ans == "y" or ans == "yes":
        return True
    else:
        return False

def prompt_for_new_file(path):
    if do_prompt("[whenicd] The cdrc file at " + path + " is new. Execute? [y,N,i,?]", path):
            return True
    else: # user hit ^D
        return False

def prompt_for_changed_file(path):
    if do_prompt("[whenicd] The hash for " + path + " has changed! Still execute? [y,N,i,?]", path):
            return True
    else:
        return False


def hash_file(path):
    cdrc = file(path)
    content = cdrc.read()
    return sha256(content).hexdigest()

def execute_cdrc(path, configfile):
    configfile['knownDirs'][path] = hash_file(path)
    json.dump(configfile, file(expanduser("~/.cdrc.cfg"), "w"))
    cmd("bash {}".format(path))

if __name__ == '__main__':
    try:
        configFile = json.load(file(expanduser("~/.cdrc.cfg")))
    except IOError:
        # First start
        configFile = {'knownDirs': {}}
    path = get_cdrc_path(getcwd())
    if path:
        if path in configFile['knownDirs']:
            if hash_file(path) == configFile['knownDirs'][path]:
                execute_cdrc(path, configFile)
            elif prompt_for_changed_file(path):
                execute_cdrc(path, configFile)
        elif prompt_for_new_file(path):
            execute_cdrc(path, configFile)
