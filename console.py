#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Console for AirBnB clone project"""
    prompt = '(hbnb) '
    

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not line:
            print("** class name missing **")
            return
        if line != "BaseModel":
            print("** class doesn't exist **")
            return
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        if line != "BaseModel":
            print("** class doesn't exist **")
            return
        if not line:
            print("** instance id missing **")
            return
        if line != "BaseModel":
            print("** no instance found **")
            return
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if not line:
            print("** class name missing **")
            return
        if line != "BaseModel":
            print("** class doesn't exist **")
            return
        if not line:
            print("** instance id missing **")
            return
        if line != "BaseModel":
            print("** no instance found **")
            return
    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        if not line:
            print("** class name missing **")
            return
        if line != "BaseModel":
            print("** class doesn't exist **")
            return
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        if not line:
            print("** class name missing **")
            return
        if line != "BaseModel":
            print("** class doesn't exist **")
            return
        if not line:
            print("** instance id missing **")
            return
        if line != "BaseModel":
            print("** no instance found **")
            return
        if not line:
            print("** attribute name missing **")
            return
        if line != "BaseModel":
            print("** value missing **")
            return
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
