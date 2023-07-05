#!/usr/bin/python3
'''module that creates a console for HBNB'''


import cmd
import sys
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
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
        if not arg:
            print("** class name missing **")
            return False
        if arg not in models:
            print("** class doesn't exist **")
            return False
        
        print(list(storage.all().items()))
        
    def do_update(self, arg):
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
        if len(prompt) == 2:
            print("** attribute name missing **")
        if len(prompt) == 3:
            print("** value missing **")

        objs = storage.all()
        class_name = prompt[0]
        instance_id = prompt[1]
        name = prompt[2]
        val = prompt[3]
        key = f"{class_name}.{instance_id}"

        if key in objs:
            instance = objs[key].to_dict()
            print(instance)
            #setattr(instance, name, val)
            #storage.save()
        

if __name__ == '__main__':
    models = ["BaseModel"]
    HBNBCommand().cmdloop()
