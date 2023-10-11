#!/usr/bin/python3
'''The implementation of the console (CLI) for the AirBnB project'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Command Line Interpreter for the AirBnB project'''

    prompt = '(hbnb) '

    def do_quit(self, args):
        '''This command exits the program, same as `EOF`'''
        
        return True

    def do_EOF(self, args):
        '''This command exits the program, same as `quit`'''
        
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
