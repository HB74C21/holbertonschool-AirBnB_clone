#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """A command interpreter class."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        try:
            new_instance = models.classes[class_name]()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        all_objs = models.storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        all_objs = models.storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in all_objs:
            del all_objs[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of instances."""
        if arg and arg not in models.classes:
            print("** class doesn't exist **")
            return
        all_objs = models.storage.all()
        if not arg:
            print([str(obj) for obj in all_objs.values()])
        else:
            print([str(obj) for obj in all_objs.values()
                   if type(obj).__name__ == arg])

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        all_objs = models.storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in all_objs:
            print("** no instance found **")
            return
        setattr(all_objs[key], args[2], args[3].strip('"'))
        all_objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
