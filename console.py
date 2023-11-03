#!/usr/bin/python3
""" module for console """
import cmd
import models
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """ define hbnb command class """

    prompt = "(hbnb) "

    def emptyline(self):
        """ define empty line """
        return False

    def do_EOF(self, line):
        """ EOF exit the program """
        return True

    def do_quit(self, line):
        """ quit the program """
        return True

    def do_create(self, line):
        """ Creates a new instance """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance = getattr(models, class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """ Prints the string representation of an instance """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance_id = args[1]

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, line):
        """ destroy all instances """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance_id = args[1]

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return

        del (all_objects[key])
        models.storage.save()

    def do_all(self, line):
        """  """
        all_objects = models.storage.all()

        if not line:
            for items in all_objects.values():
                print(str(items))
        else:
            args = shlex.split(line)
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
                return
            for items in all_objects.values():
                if class_name == type(items).__name__:
                    print(str(items))

    def do_update(self, line):
        """ Updates an instance """

        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        setattr(all_objects[key], attribute_name, attribute_value)
        all_objects[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
