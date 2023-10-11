#!/usr/bin/python3
'''The implementation of the console (CLI) for the AirBnB project'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    '''Command Line Interpreter for the AirBnB project'''

    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel,
            'User': User
            }

    def do_quit(self, str_arg):
        '''This command exits the program, same as `EOF`'''

        return True

    def do_EOF(self, str_arg):
        '''This command exits the program, same as `quit`'''

        return True

    def do_create(self, str_arg):
        '''
        Creates a new instance of a class, saves it (to the JSON file)
        and prints the id.

        Ex: (hbnb) create BaseModel
        '''

        args = str_arg.split()

        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
            return

        cls = self.classes[args[0]]
        obj = cls()
        obj.save()
        print(obj.id)

    def complete_create(self, text, line, begidx, endix):
        '''Provides Tab-completion for create command'''

        return [cls for cls in self.classes if cls.startswith(text)]

    def do_show(self, str_arg):
        '''
        Prints the string representation of an instance
        based on the class name and id

        Ex: (hbnb) show User 1234-1234-1234
        '''

        args = str_arg.split()

        if len(args) < 1:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        elif len(args) < 2:
            print('** instance id missing **')
            return

        cls, inst_id = args[0], args[1]
        inst_key = f'{cls}.{inst_id}'

        for key, obj in storage.all().items():
            if key == inst_key:
                print(obj)
                return
        else:
            print('** no instance found **')

    def complete_show(self, text, line, begidx, endix):
        '''Provides Tab-completion for show command'''

        return [cls for cls in self.classes if cls.startswith(text)]

    def do_destroy(self, str_arg):
        '''
        Deletes an instance based on the class name and id,
        and saves the change into the JSON file

        Ex: (hbnb) destroy BaseModel 1234-1234-1234
        '''

        args = str_arg.split()

        if len(args) < 1:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        elif len(args) < 2:
            print('** instance id missing **')
            return

        cls, inst_id = args[0], args[1]
        inst_key = f'{cls}.{inst_id}'
        objs_dict = storage.all()

        for key, obj in objs_dict.items():
            if key == inst_key:
                del objs_dict[key]
                storage.save()
                return
        else:
            print('** no instance found **')

    def complete_destroy(self, text, line, begidx, endix):
        '''Provides Tab-completion for destroy command'''

        return [cls for cls in self.classes if cls.startswith(text)]

    def emptyline(self):
        pass

    def do_all(self, str_arg):
        """
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """

        args = str_arg.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            objects = []
            for obj in storage.all().values():
                if len(args) != 0 and args[0] == obj.__class__.__name__:
                    objects.append(obj.__str__())
                elif len(args) == 0:
                    objects.append(obj.__str__())
            print(objects)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    if not sys.stdin.isatty():
        print()
