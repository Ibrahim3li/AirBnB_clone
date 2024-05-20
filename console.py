#!/user/bin/python3
"""Module for HBNB project console."""
import cmd

class HBNBCommand(cmd.Cmd):
   prompt = "(HBNB)"


   def do_quit(self, arg):
      """exit the console command"""
      return True 
   
   def do_EOF(slef, arg):
      """handle EOF to exit the console command"""
      return True 
   def emptyline(self):
      """do nothing on empty input line"""
      pass
   
   def help_quit(self):
      print("quit comman to exit the console")

   def help_EOF(slef):
      print("exit the program with EOF (Ctrl-D). ")  

if __name__ =='__main__':   
 HBNBCommand().cmdloop()
