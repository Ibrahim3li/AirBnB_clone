#!usr/bin/python3
"""module for HBNB commaan interprater"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file_storage = FileStorage()
    file_storage.reload()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.file_storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in HBNBCommand.file_storage.all():
            print(HBNBCommand.file_storage.all()[key])
        else:
            print("** no instance found **")

    # Add other commands (destroy, all, update) here

if __name__ == '__main__':
    HBNBCommand().cmdloop()
