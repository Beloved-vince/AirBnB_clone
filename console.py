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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
