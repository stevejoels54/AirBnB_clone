#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit the program
        """
        return True

    def do_EOF(self, args):
        """
        Exit on EOF (Ctrl-D)
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing on an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
