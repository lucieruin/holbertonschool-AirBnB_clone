#!/usr/bin/python3
""" module for console """
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
