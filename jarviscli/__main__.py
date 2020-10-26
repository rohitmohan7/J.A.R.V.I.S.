# -*- coding: utf-8 -*-
import Jarvis
import colorama
import sys


def check_python_version():
    return sys.version_info[0] == 3


def main():
    # enable color on windows
    colorama.init()
    # start Jarvis
    jarvis = Jarvis.Jarvis()
    jarvis.executor('enable sound')
    jarvis.executor('gtts') # google collects data (conversations are insecure)
    command = " ".join(sys.argv[1:]).strip()
    jarvis.executor(command)


if __name__ == '__main__':
    if check_python_version():
        main()
    else:
        print("Sorry! Only Python 3 supported.")
