#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage

from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


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

    def do_create(self, args):
        """
        Create a new instance of BaseModel,
        saves it (to the JSON file), and prints the id.
        """
        if len(args) == 0:
            print("** class name  missing **")
            return

        args_list = args.split()
        if args_list[0] not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        new_instance = eval("{}()".format(args_list[0]))
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args_list[0], args_list[1])
        objects = storage.all()
        if obj_key in objects:
            print(objects[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args_list[0], args_list[1])
        objects = storage.all()
        if obj_key in objects:
            del objects[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        args_list = args.split()
        objects = storage.all()

        if not args_list or args_list[0] in self.valid_class_names():
            print([str(obj) for obj in objects.values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args_list[0], args_list[1])
        objects = storage.all()
        if obj_key in objects:
            if len(args_list) < 3:
                print("** attribute name missing **")
            elif len(args_list) < 4:
                print("** value missing **")
            else:
                attr_name = args_list[2]
                attr_value = args_list[3]
                obj = objects[obj_key]
                setattr(obj, attr_name, attr_value)
                obj.save()
        else:
            print("** no instance found **")

    def valid_class_names(self):
        """
        Returns a list of valid class names.
        """
        return ["BaseModel", "User", "City", "Place",
                "State", "Amenity", "Review"]


if __name__ == '__main__':
    HBNBCommand().cmdloop()


# #!/usr/bin/python3
# """Entry point of the command interpreter"""
# import cmd
# from models.base_model import BaseModel
# from models import storage

# from models import storage
# from models.user import User
# from models.city import City
# from models.place import Place
# from models.state import State
# from models.amenity import Amenity
# from models.review import Review

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
