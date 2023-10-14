#!/usr/bin/python3
'''The implementation of the console (CLI) for the AirBnB project'''
import cmd
import re
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''Command Line Interpreter for the AirBnB project'''

    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Place': Place,
            'Amenity': Amenity,
            'Review': Review
            }

    @staticmethod
    def splitter(str_args):
        '''
        Customized split method to handle double-quoted arguments with spaces

        Ex: update User 3587-2190-7659 "name" "Robert Downey Jr"
        '''

        arguments = re.findall(r'([^\'"\s]+|"[^"]*"|\'[^\']*\')', str_args)

        if len(arguments) > 2:
            if arguments[2][0] == '{' and arguments[-1][-1] == '}':
                arguments[2] = ''.join(arguments[2:])
                del arguments[3:]
                if arguments[1][0] == '"' and arguments[1][-1] == '"':
                    arguments[1] = arguments[1].strip('"')
                elif arguments[1][0] == '\'' and arguments[1][-1] == '\'':
                    arguments[1] = arguments[1].strip('\'')

                return arguments
        if len(arguments) > 3:
            copy_attr = arguments[3]

        # Clean up the  quotes
        for i in range(len(arguments)):
            if arguments[i][0] == '"' and arguments[i][-1] == '"':
                arguments[i] = arguments[i].strip('"')
            elif arguments[i][0] == '\'' and arguments[i][-1] == '\'':
                arguments[i] = arguments[i].strip('\'')

        if len(arguments) > 3:
            arguments[3] = copy_attr

        return arguments

    @staticmethod
    def parse_all(line):
        '''Parse commands such as: <model>.all()'''

        cls = line.split('.')[0]

        return f'all {cls}'

    @staticmethod
    def parse_count(line):
        '''Parse commands such as: <model>.count()'''

        cls = line.split('.')[0]

        return f'count {cls}'

    @staticmethod
    def parse_show_destroy(line):
        '''
        Parse commands like: <model>.show("66-79") or <model>.destroy("68-46")
        '''

        line = line.strip()
        line = line[:-1]
        line = line.replace('.', ' ', 1).replace('(', ' ', 1).replace(',', '')
        splitted = line.split()

        splitted.extend(['', '', ''])
        command, cls, inst_id = splitted[1], splitted[0], splitted[2]

        new_line = f'{command} {cls} {inst_id}'

        return new_line

    @staticmethod
    def parse_update(line):
        """Parse commands like: User.update(1723-5609, "name", "Robert Jr")"""

        update_p = r'^ *(?P<cls>\w+)?.update\('
        update_p += r'(?P<id>[\w\'"][^,]*)?'
        update_p += r'(, *(?P<name>[\w\'"]*[^,]*))?'
        update_p += r'(, *(?P<value>[\w\'"]*[^,]*))?'
        update_p += r'(, *.+)*\) *$'

        match = re.search(update_p, line)

        if match:
            class_name = match.group('cls')
            if not class_name:
                class_name = ''
            _id = match.group('id')
            if not _id:
                _id = ''
            attr_name = match.group('name')
            if not attr_name:
                attr_name = ''
            attr_value = match.group('value')
            if not attr_value:
                attr_value = ''

            new_line = f"update {class_name} {_id} {attr_name} {attr_value}"
            return new_line

    @staticmethod
    def parse_update_2(line):
        """
        Parse commands like:
        (hbnb) User.update("6693-5721", {"first_name":  "John", "age": 89})
        """

        update_p2 = r'^ *(?P<cls>\w+)?.update\('
        update_p2 += r'(?P<id>[\w\'"][^,]*)'
        update_p2 += r'(, *(?P<dict>{.*}))'
        update_p2 += r'(, *.+)*\) *$'

        match = re.search(update_p2, line)

        if match:
            class_name = match.group('cls')
            if not class_name:
                class_name = ''
            _id = match.group('id')
            if not _id:
                _id = ''
            obj_dict = match.group('dict')
            if not obj_dict:
                obj_dict = ''

            new_line = f"update {class_name} {_id} {obj_dict}"
            return new_line

    def precmd(self, line):
        '''Preprocess the command line'''

        if not sys.stdin.isatty():
            print()

        update_p = r'^ *(?P<cls>\w+)?.update\('
        update_p += r'(?P<id>[\w\'"][^,]*)?'
        update_p += r'(, *(?P<name>[\w\'"]*[^,]*))?'
        update_p += r'(, *(?P<value>[\w\'"]*))?'
        update_p += r'(, *.+)*\) *$'

        update_p2 = r'^ *(?P<cls>\w+)?.update\('
        update_p2 += r'(?P<id>[\w\'"][^,]*)'
        update_p2 += r'(, *(?P<dict>{.*}))'
        update_p2 += r'(, *.+)*\) *$'

        cmds_formers = {r'^ *\w*.all\(\) *$': self.parse_all,
                        r'^ *\w*.count\(\) *$': self.parse_count,
                        r'^ *\w*.show\(.*\) *$': self.parse_show_destroy,
                        r'^ *\w*.destroy\(.*\) *$': self.parse_show_destroy,
                        update_p2: self.parse_update_2,
                        update_p: self.parse_update}

        for pattern in cmds_formers:
            if re.search(pattern, line):
                return cmds_formers[pattern](line)
        else:
            return line

    def do_create(self, str_args):
        '''
        Creates a new instance of a class, saves it (to the JSON file)
        and prints the id.

        Ex: (hbnb) create BaseModel
        '''

        args = self.splitter(str_args)

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

    def do_show(self, str_args):
        '''
        Prints the string representation of an instance
        based on the class name and id

        Ex: (hbnb) show User 1234-1234-1234
        '''

        args = self.splitter(str_args)

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

        return [cls + ' ' for cls in self.classes if cls.startswith(text)]

    def do_destroy(self, str_args):
        '''
        Deletes an instance based on the class name and id,
        and saves the change into the JSON file

        Ex: (hbnb) destroy BaseModel 1234-1234-1234
        '''

        args = self.splitter(str_args)

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

        return [cls + ' ' for cls in self.classes if cls.startswith(text)]

    def do_all(self, str_args):
        """
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.

        Ex: (hbnb) all Amenity
        """

        args = self.splitter(str_args)

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

    def complete_all(self, text, line, begidx, endix):
        '''Provides Tab-completion for all command'''

        return [cls for cls in self.classes if cls.startswith(text)]

    def do_update(self, str_args):
        """
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.

        Ex: (hbnb) update User 49faff9a-6318-451f-87b6-9105 first_name "Betty"
        """
        args = self.splitter(str_args)
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        if f"{args[0]}.{args[1]}" not in objects.keys():
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return

            obj = objects[f"{args[0]}.{args[1]}"]
            dict_attrs = eval(args[2])

            for key, val in dict_attrs.items():
                setattr(obj, key, val)

        if len(args) == 4:
            obj = objects[f"{args[0]}.{args[1]}"]

            if args[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = value_type(args[3])
            else:
                obj.__dict__[args[2]] = eval(args[3])

        storage.save()

    def complete_update(self, text, line, begidx, endix):
        '''Provides Tab-completion for update command'''

        return [cls + ' ' for cls in self.classes if cls.startswith(text)]

    def do_count(self, str_args):
        """
        Retrieve the number of instances of a class

        Executed by typing: (hbnb) <class name>.count()
        """
        args = self.splitter(str_args)
        objects_dict = storage.all()
        counting = 0

        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]

        for key, obj in objects_dict.items():
            if cls_name == key.split('.')[0]:
                counting += 1

        print(counting)

    def emptyline(self):
        '''Pass when an empty line is entered'''

        pass

    def do_quit(self, str_args):
        '''This command exits the program, same as `EOF`'''

        return True

    def do_EOF(self, str_args):
        '''This command exits the program, same as `quit`'''

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
