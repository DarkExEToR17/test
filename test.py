# these are imports it imports external library like colorama or internal like os sys and time
# to install colorama youll need to open a shell and write the following command 
# by the way colorama is used to produce color in a python shell like color commands in cmd
import os 
import colorama
import sys
from colorama import Fore
import time
import random

# this is the command to add color, write Fore. and then add the name of your color, you can find all the color name on colorama page

# this is the menu function 
#it'll make the shell interface using a print and then you can paste any ascii text to make an interface

def menu():
	global onstart
	print(f"""





				 
{Fore.blue}█████╗  █████╗ ██████╗ ██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     
{Fore.blue}██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
{Fore.blue}██║  ██║███████║██████╔╝█████╔╝    ██║   ██║   ██║██║   ██║██║     
{Fore.Red}██║  ██║██╔══██║██╔══██╗██╔═██╗    ██║   ██║   ██║██║   ██║██║     
{Fore.Red}██████╔╝██║  ██║██║  ██║██║  ██╗   ██║   ╚██████╔╝╚██████╔╝███████╗
                 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                  

{Fore.MAGENTA}                                                                                                   
[help]	[shutdown]
 
Disclaimer FOR EDUCTIONAL PURPOSE ONLY
 
[1] Wifi Password Cracker BETA 

{Fore.WHITE}
""")

# this is the command variable, its an input() btw between these () after the input you can writ everything you want im gonna show this to you

	command = input(">")

	
#this is the command pattern 
# i coded the exit command to help you with atleast one command

	if command == "1":
		print("Loading...")
		lower = "abcdefghijklmnopqrstuvwxyz"
		upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		numbers = "1234567890"
		symbols = "@#€!?&$"
		
		string = lower + upper + numbers + symbols
        length = 25
        password = "".join(random.sample(string,length)
        print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
                print("Dont Work:" + password)
         print("Dont Work:" + password)
          print("Dont Work:" + password)
           print("Dont Work:" + password)
        
		
		
		if command == "help":
		print("Hacking Tool")

	if command == "shutdown":
		sys.exit()

def onstart():
    cmd = 'mode 120,28' # this define the size of your shell window
    os.system(cmd) # this will execute the variable associated to the size in the shell
    os.system("cls && title Test - Multitool")# this will clear the commands written and all the prints after the command has executed
    menu() # this add the menu "gui"

onstart()



 
