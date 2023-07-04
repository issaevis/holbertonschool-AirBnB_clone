#!/usr/bin/python3
'''module that creates a console for HBNB'''


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    '''Class to create the command line interface of our project.'''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        exit()

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        """ Keyboard interrupt signal, exit program. """
        self.do_quit("")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
