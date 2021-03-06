#!/usr/bin/python

r = '\033[0m'     #reset
bold = '\033[01m'
d = '\033[02m'     #disable
ul = '\033[04m' #underline
reverse = '\033[07m'
st = '\033[09m' #strikethrough
invis = '\033[08m'#invisible
white = '\033[0m'
cwhite = '\33[37m'
black ='\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lgrey = '\033[37m'
grey = '\033[90m'
lred = '\033[91m'
lgreen = '\033[92m'
yellow = '\033[93m'
lblue = '\033[94m'
pink = '\033[95m'
lcyan = '\033[96m'
bgreen = '\33[42m'
blgreen = '\33[102m'
bred = '\33[41m'
blred = '\33[101m'
borange = '\33[43m'
byellow = '\33[33m'
bcyan = '\33[44m'
blcyan = '\33[104m'
br = '\33[108m'
brown = '\33[33m'
bwhite = '\33[107'

re = red
w = white
b = lblue
g = green
y = yellow

import os

def clear():
  i = 0
  while i <= 5:
    os.system("clear")
    i = i + 1

def quit():
  clear()  
  exit()

def logo():
  print(white + "")
  print(red + "███" + white + "█████████████████████████████████" + red + "███")
  print(red + "████" + white + "███████████████████████████████" + red + "████")
  print(red + "███████" + white + "█████████████████████████" + red + "███████")
  print(red + "██████████" + white + "███████████████████" + red + "██████████")
  print(red + "█████████████" + white + "█████████████" + red + "█████████████")
  print(red + "█████" + white + "███" + red + "████████" + white + "███████" + red + "████████" + white + "███" + red + "█████")
  print(red + "█████" + white + "██████" + red + "████████" + white + "█" + red + "████████" + white + "██████" + red + "█████")
  print(red + "█████" + white + "█████████" + red + "██████████(" + white + "█████████" + red + "█████")
  print(red + "█████" + white + "███████████" + red + "*████(" + white + "████████████" + red + "█████")
  print(red + "█████" + white + "█████████████" + red + "███" + white + "█████████████" + red + "█████")
  print(red + "█████" + white + "█████████████████████████████" + red + "█████")
  print(red + "█████" + white + "█████████████████████████████" + red + "█████")
  print(red + "█████" + white + "█████████████████████████████" + red + "█████")
  print(red + "█████" + white + "█████████████████████████████" + red + "█████")
  print(red + "█████" + white + "█████████████████████████████" + red + "█████")
  print(red + "█████" + white + "█████████████████████████████" + red + "█████")
  print(red + "█████" + white + "█████████████████████████████" + red + "█████")

def name():
  print("")
  print(red + """███████████""")
  print(red + "██" + white + "███████" + red + "██" + yellow + "                     ██ ██")
  print(red + "█" + white + "███" + red + "   " + white + "███" + red + "█" + white + """                        ██""")
  print(red + "█" + white + "█  " + red + "      " + red + "█" + yellow + " ██████████ ████████ ██ ██")
  print(red + "█" + white + "██" + red + "  " + white + "██████" + red + "" + white + " ██████████ ███  ███ ██ ██")
  print(red + "█" + white + "███" + red + "   " + white + "███" + red + "█" + yellow + " ██  ██  ██ ███  ███ ██ ██")
  print(red + "██" + white + "███████" + red + "██" + white + " ██  ██  ██ ████████ ██ ██")
  print(red + "███████████" + r + "") 

def chromelogo():
  print(r + "████████████████" + red + "██████████████████" + white + "████████████████")
  print(white + "████████████" + red + "█████████████████████████" + white + "████████████")
  print("█████████" + red + "███████████████████████████████" + white + "█████████")
  print(white + "███████" + red + "████████████████████████████████████" + white + "███████")
  print(r + "█████" + red + "████████████████████████████████████████" + white + "█████")
  print(r + "████" + red + "█████████████████████████████████████████" + white + "████")
  print(w + "███" + re + "████████████████████████████████████████████" + w + "███")
  print(w + "██" + g + "██████" + re + "████████████" + w + "██████████" + y + "██████████████████" + w + "██")
  print(w + "█" + g + "████████" + re + "████████" + w + "███" + b + "██████████" + w + "███" + y + "███████████████" + w + "██")
  print("█" + g + "██████████" + re + "████" + w + "███" + b + "██████████████" + w + "███" + y + "██████████████" + w + "█")
  print(w + "█" + g + "███████████" + re + "██" + w + "███" + b + "████████████████" + w + "███" + y + "█████████████" + w + "█")
  print(g + "█████████████" + re + "█" + w + "██" + b + "██████████████████" + w + "██" + y + "█████████████" + w + "█")
  print(g + "██████████████" + w + "██" + b + "██████████████████" + w + "███" + y + "█████████████" + w)
  print(g + "██████████████" + w + "██" + b + "██████████████████" + w + "██" + y + "█████████████" + w + "█")
  print(w + "█" + g + "██████████████" + w + "██" + b + "████████████████" + w + "███" + y + "█████████████" + w + "█")
  print("█" + g + "███████████████" + w + "██" + b + "██████████████" + w + "███" + y + "██████████████" + w + "█")
  print("█" + g + "████████████████" + w + "███" + b + "██████████" + w + "██" + y + "████████████████" + w + "██")
  print(w + "██" + g + "████████████████" + w + "██████████████" + y + "███████████████" + w + "███")
  print(w + "███" + g + "████████████████████████████" + y + "███████████████" + w + "████")
  print(w + "████" + g + "██████████████████████████" + y + "███████████████" + w + "█████")
  print(w + "█████" + g + "████████████████████████" + y + "███████████████" + w + "██████")
  print("███████" + g + "█████████████████████" + y + "██████████████" + w + "████████")
  print("█████████" + g + "██████████████████" + y + "████████████" + w + "███████████")
  print("████████████" + g + "████████████" + y + "███████████" + w + "██████████████")
  print("█████████████████" + g + "███████" + y + "███████" + w + "███████████████████")

def googlelogo():
  print(re + """
                     ██████████                    
                ██████████████████                
             ███████████████████████              
            ███████████████████████""")               
  print(y + "          ██████" + re + "█████        ████")                 
  print(y + """          ████████                                
         ████████""")                                 
  print(y + "         ███████" + b + "         ████████████████")         
  print(y + "         ███████" + b + "         ████████████████")         
  print(y + "         ███████         " + b + "████████████████")         
  print(y + "         ████████" + b + "        ███████████████")          
  print(y + "          ████████" + b + "              ████████")          
  print(y + "          ██████" + g + "█████" + g + "        ██████" + b + "████")           
  print(g + "            ████████████████████████" + b + "██")            
  print(g + "             ████████████████████████")    
  print(g + "                ██████████████████")     
  print(g + "                    ██████████")

def testchrome():
  print(r + "                " + red + " ████████████████ " + white + "                ")
  print(white + "            " + red + "█████████████████████████" + white + "            ")
  print("         " + red + "██████████████████████████████ " + white + "         ")
  print(white + "       " + red + "████████████████████████████████████" + white + "       ")
  print(r + "     " + red + " ██████████████████████████████████████ " + white + "     ")
  print(r + "    " + red + "██████████████████████████████████████████" + white + "    ") 
  print(w + "   " + re + "████████████████████████████████████████████" + w + "   ")
  print(w + "  " + g + "██████" + re + "████████████" + w + "██████████" + y + "██████████████████" + w + "  ")
  print(w + " " + g + "████████" + re + "████████" + w + "███" + b + "██████████" + w + "███" + y + "███████████████" + w + "  ")
  print(" " + g + "██████████" + re + "████" + w + "███" + b + "██████████████" + w + "███" + y + "██████████████" + w + " ")
  print(w + " " + g + "███████████" + re + "██" + w + "███" + b + "████████████████" + w + "███" + y + "█████████████" + w + " ")
  print(g + "█████████████" + re + "█" + w + "██" + b + "██████████████████" + w + "██" + y + "█████████████" + w + " ")
  print(g + "██████████████" + w + "██" + b + "██████████████████" + w + "███" + y + "█████████████" + w)
  print(g + "██████████████" + w + "██" + b + "██████████████████" + w + "██" + y + "█████████████" + w + " ")
  print(w + " " + g + "██████████████" + w + "██" + b + "████████████████" + w + "███" + y + "█████████████" + w + " ")
  print(" " + g + "███████████████" + w + "██" + b + "██████████████" + w + "███" + y + "██████████████" + w + " ")
  print(" " + g + "████████████████" + w + "███" + b + "██████████" + w + "██" + y + "████████████████" + w + "  ")
  print(w + "  " + g + "█████████████████" + w + "█████████████" + y + "███████████████" + w + "   ")
  print(w + "   " + g + "████████████████████████████" + y + "███████████████" + w + "    ")
  print(w + "    " + g + "██████████████████████████" + y + "███████████████" + w + "    ")
  print(w + "     " + g + " ███████████████████████" + y + "███████████████" + w + "      ")
  print("       " + g + " ████████████████████" + y + "██████████████" + w + "        ")
  print("         " + g + " h████████████████" + y + "████████████" + w + "           ")
  print("            " + g + " ███████████" + y + "███████████" + w + "              ")
  print("                 " + g + " ██████" + y + "███████" + w + "                   ")
