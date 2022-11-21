<<<<<<< HEAD
#!/usr/bin/python3
=======
<<<<<<< HEAD
>>>>>>> 20e20696e0117667c8f1e0054b01b90882641e05
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
<<<<<<< HEAD
=======
=======
#!/usr/bin/python3
import cmd

class BaseModel(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Help command"""
        pass

    def do_quit(self, line):
        """Quit command"""
        return True

if __name__ == '__main__':
    BaseModel().cmdloop()
>>>>>>> 76bd7d7 (Authors)
>>>>>>> 20e20696e0117667c8f1e0054b01b90882641e05
