#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""
import cmd
import re
from shlex import split

from models import storage

from models.base_model import BaseModel



def parse(arg):
    """
    Method written to take and parse input before use
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            rtl = [i.strip() for i in lexer]
            rtl.append(brackets.group())
            return rtl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        rtl = [i.strip() for i in lexer]
        rtl.append(curly_braces.group())
        return rtl


class HBNBCommand(cmd.Cmd):
    """HBnB Console.
    See https://docs.python.org/3/library/cmd.html\
        for more details

    Attr:
        custom_prompt (str): command line prompt
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Ignore empty lines + ENTER."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_exit(self, arg):
        """Exit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        # Go to a new line and before exiting
        print("")
        self.do_exit()

    def do_create(self, arg):
        """
        Create instance of class
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name  missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        show <class>  <id>
        Display string representation of the class instance
        """
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """
        destroy <class>  <id>
        delete a class instance of a given id
        """
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """
        usage; all <class> or <class>.all()
        Display all instances of a given class
        """
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(args) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """
        usage: update <class> <id>
        Update a class instance of a given id by adding \
            or updating a given attribute
        """
        args = parse(arg)
        objdict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
            return False
        elif len(args) == 2:
            print("** attribute name missing **")
            return False
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        elif len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                k_in_keys = k in obj.__class__.__dict__.keys()
                type_in = type(obj.__class__.__dict__[k]) in {str, int, float}
                if (k_in_keys and type_in):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()


# #!/usr/bin/python3
# """Entry point of the command interpreter"""
# import cmd
# from models.base_model import BaseModel
# from models import storage


# class HBNBCommand(cmd.Cmd):
#     prompt = "(hbnb) "

#     def do_quit(self, args):
#         """
#         Quit the program
#         """
#         return True

#     def do_EOF(self, args):
#         """
#         Exit on EOF (Ctrl-D)
#         """
#         print()  # Print a newline before exiting
#         return True

#     def emptyline(self):
#         """
#         Do nothing on an empty line
#         """
#         pass

#     def do_create(self, args):
#         """
#         Create a new instance of BaseModel,
#         saves it (to the JSON file), and prints the id.
#         """
#         if len(args) == 0:
#             print("** class name  missing **")
#             return
        
#         args_list = args.split()
#         if args_list[0] not in self.valid_class_names():
#             print("** class doesn't exist **")
#             return
        
#         new_instance = eval("{}()".format(args_list[0]))
#         new_instance.save()
#         print(new_instance.id)

#     def do_show(self, args):
#         """
#         Prints the string representation of an instance
#         based on the class name and id.
#         """
#         if not args:
#             print("** class name missing **")
#             return

#         args_list = args.split()
#         if args_list[0] not in self.valid_class_names():
#             print("** class doesn't exist **")
#             return

#         if len(args_list) < 2:
#             print("** instance id missing **")
#             return

#         obj_key = "{}.{}".format(args_list[0], args_list[1])
#         objects = storage.all()
#         if obj_key in objects:
#             print(objects[obj_key])
#         else:
#             print("** no instance found **")

#     def do_destroy(self, args):
#         """
#         Deletes an instance based on the class name and id
#         (save the change into the JSON file).
#         """
#         if not args:
#             print("** class name missing **")
#             return

#         args_list = args.split()
#         if args_list[0] not in self.valid_class_names():
#             print("** class doesn't exist **")
#             return

#         if len(args_list) < 2:
#             print("** instance id missing **")
#             return

#         obj_key = "{}.{}".format(args_list[0], args_list[1])
#         objects = storage.all()
#         if obj_key in objects:
#             del objects[obj_key]
#             storage.save()
#         else:
#             print("** no instance found **")

#     def do_all(self, args):
#         """
#         Prints all string representation of all
#         instances based or not on the class name.
#         """
#         args_list = args.split()
#         objects = storage.all()

#         if not args_list or args_list[0] in self.valid_class_names():
#             print([str(obj) for obj in objects.values()])
#         else:
#             print("** class doesn't exist **")

#     def do_update(self, args):
#         """
#         Updates an instance based on the class name and id by adding
#         or updating attribute (save the change into the JSON file).
#         """
#         if not args:
#             print("** class name missing **")
#             return

#         args_list = args.split()
#         if args_list[0] not in self.valid_class_names():
#             print("** class doesn't exist **")
#             return

#         if len(args_list) < 2:
#             print("** instance id missing **")
#             return

#         obj_key = "{}.{}".format(args_list[0], args_list[1])
#         objects = storage.all()
#         if obj_key in objects:
#             if len(args_list) < 3:
#                 print("** attribute name missing **")
#             elif len(args_list) < 4:
#                 print("** value missing **")
#             else:
#                 attr_name = args_list[2]
#                 attr_value = args_list[3]
#                 obj = objects[obj_key]
#                 setattr(obj, attr_name, attr_value)
#                 obj.save()
#         else:
#             print("** no instance found **")

#     def valid_class_names(self):
#         """
#         Returns a list of valid class names.
#         """
#         return ["BaseModel"]  # Add other class names here


# if __name__ == '__main__':
#     HBNBCommand().cmdloop()