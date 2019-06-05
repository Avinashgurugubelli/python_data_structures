'''
This logger is used to print the messages like info, error, warning, success
'''

from colorama import Fore, Back, Style, init as coloramaInit
coloramaInit()

class Logger:
    @staticmethod
    def error(message):
        print(Fore.LIGHTRED_EX, "Error: {} ".format(message))
        print(Style.RESET_ALL)

    @staticmethod
    def info(message):
        print(Fore.LIGHTBLUE_EX, "Info: {} ".format(message))
        print(Style.RESET_ALL)

    @staticmethod
    def success(message):
        print(Fore.LIGHTGREEN_EX, "Success: {} ".format(message))
        print(Style.RESET_ALL)

    @staticmethod
    def warn(message):
        print(Fore.LIGHTYELLOW_EX, "Warning: {} ".format(message))
        print(Style.RESET_ALL)