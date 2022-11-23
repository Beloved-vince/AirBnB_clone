#!/usr/bin/python3
"""Write a program called console.py that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class contains the entry point of the command interpreter"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True
  

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            else:
                key = arg[0] + "." + arg[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            else:
                key = arg[0] + "." + arg[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if not arg:
            for key, value in storage.all().items():
                print(value)
        else:
            arg = arg.split()
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if arg[0] in key:
                        print(value)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            else:
                key = arg[0] + "." + arg[1]
                if key not in storage.all():
                    print("** no instance found **")
                elif len(arg) == 2:
                    print("** attribute name missing **")
                elif len(arg) == 3:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], arg[2], arg[3])
                    storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()