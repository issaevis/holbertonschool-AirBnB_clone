#!/usr/bin/python3
'''module that creates a console for HBNB'''


import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    '''Class to create the command line interface of our project.'''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        exit()

    def emptyline(self):
        '''Do nothing when an empty line is entered'''
        pass

    def do_EOF(self, arg):
        """ Keyboard interrupt signal, exit program. """
        self.do_quit("")

    def do_create(self, arg):
        '''creates a new instance of a Class'''
        if not arg:
            print("** class name missing **")
            return False
        if arg not in models:
            print("** class doesn't exist **")
            return False
        instance = BaseModel()
        instance.save()
        print(f"{instance.id}")

    '''Fixed errors, but doublecheck'''
    def do_show(self, arg):
        '''shows all details about one particular instance.'''
        if not arg:
            print("** class name missing **")
            return False
        prompt = arg.split(" ")
        objs = storage.all()

        if prompt[0] not in models:
            print("** class doesn't exist **")
            return False

        if len(prompt) < 2:
            print("** instance id missing **")
            return False

        class_name = prompt[0]
        instance_id = prompt[1]

        key = f"{class_name}.{instance_id}"
        if key in objs:
            instance = objs[key]     
            print(instance)
            return

        print('** no instance found **')

    def do_destroy(self, arg):
        '''Removes instance from memory and JSON file'''
        if not arg:
            print("** class name missing **")
            return False
        prompt = arg.split(" ")
        if prompt[0] not in models:
            print("** class doesn't exist **")
            return False
        if len(prompt) < 2:
            print("** instance id missing **")
            return False
        
        objs = storage.all()
        class_name = prompt[0]
        instance_id = prompt[1]

        key = f"{class_name}.{instance_id}"
        if key in objs:
            objs.pop(key)
            storage.save()
        else:
            print("Key not found")


    def do_all(self, arg):
        '''Prints all instances of a Class'''
        if not arg:
            print("** class name missing **")
            return False
        if arg not in models:
            print("** class doesn't exist **")
            return False
        
        print(list(storage.all().items()))
        
    def do_update(self, arg):
        '''Updates values to said instance'''
        arg = arg.split()
        flag = 0
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in models:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        for key, value in storage.all().items():
            if value.id == (arg[1]):
                flag += 1
        if flag == 0:
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            print("** value missing **")
            return False
        val = arg[3].split('"')
        setattr(value, arg[2], val[1])
        storage.save()

        

if __name__ == '__main__':
    models = ["BaseModel", "User"]
    HBNBCommand().cmdloop()
