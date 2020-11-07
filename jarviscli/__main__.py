# -*- coding: utf-8 -*-
import Jarvis
import colorama
import sys
from colorama import Fore

def check_python_version():
    return sys.version_info[0] == 3


def main():
    # enable color on windows
    colorama.init()
    # start Jarvis
    jarvis = Jarvis.Jarvis()
    #jarvis.executor('enable sound')
    #jarvis.executor('gtts') # google collects data (conversations are insecure)
    #command = " ".join(sys.argv[1:]).strip()
    #jarvis.executor(command)
    PROMPT_CHAR = '~>'
    prompt = (
        Fore.RED
        + "{} J.A.R.V.I.S. terminal\n".format(PROMPT_CHAR)
        + Fore.RESET)

    initializer = ["enable sound"]
    #closeargs = ["disable gtts"]
    exit = False

    while jarvis.get_is_running():

        if len(initializer) > 0:
            line = initializer[0]
            print(line)
            initializer.pop(0)
        elif exit == False:
            line = input(prompt)

        #if line == "exit": #do stuff before exiting
        #    exit = True

        #if exit == True:
        #    if len(closeargs) > 0:
        #        line = closeargs[0]
        #        closeargs.pop(0)
        #    else:
        #        line = "exit"

        line = jarvis.precmd(line)
        stop = jarvis.onecmd(line)
        stop = jarvis.postcmd(stop, line)

if __name__ == '__main__':
    if check_python_version():
        main()
    else:
        print("Sorry! Only Python 3 supported.")
