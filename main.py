#remake boleh tapi izin dulu!! 
#t.me/mrd4nd

import subprocess
import os
import time
import socket
import requests
import random
import getpass
import sys
import json
import platform
import colorama
from node_modules.colors.themes import string

#JANGAN DI UBAH DEK! #
#JANGAN DI UBAH DEK! #
author = "dandier"
#JANGAN DI UBAH EEK! #
#JANGAN DI UBAH DEK! #

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 0, 0)
end_color = (0, 0, 255)

class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET
	
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
	0kkkO00KK00kOKXKXK000OxxkxdxxxxxdxOO000O0K0000KK00000
KOOk0OO00KKKKXXKKKOKK0OOkxddxxxdxkOOO0KK0K000KO0K0X00
0000KKkkO0OO0000Ok0K0KXK0xdddxxddxkOO000K0KK00KKKKK0K
OO000OkOOOkxdxdddxOO0KKK0kxxxxdxkkOOOkk000KKXXKKKKK00
0OOkO0X0kkkdodoodolodk0Oxdllcclloooodxk0K0XX0O0OkOO00
0OOOO00kdoxdxdooxxddoxxdollcc::::cccclodkKXXkkxkdxdxx
OkOkOOddxxkO0OdxkdokOkloollcc:::llcccllodk0Okxxddoddd
0kkxkkxxOOkdOOkkkddodollll:;;::;;,,;;;:clooddoooooooo
0kxxkkOOO0koxkOOkkkddlolc::cllc:;;,,,;;;;:cloddodolcc
kOOkkOO00Oxdxxxkkk0O0OxxdodoOxddolcc:::c:::cllloddocc
OOOOkkxOOkkkkkxxdkKK00Ok0KK00kkxdolllllllc::clccclclc
OOOOkdOOOO000000OkOXKO0KXXK0kdloddddododo:cooocccc;l:
X0OOOdoOO0000OOkOkO00K0KXK0Ox:c;cloc,;;ldxkkkxdollc::
KXKOkklO0OxkO000000OkkkxxxxxxoldO0x:;dxlloololccllclc
kxkK0OklkkOkkkk00ddo:'..'''''''':kx,:odcc;:l:;;cl:;;;
kxdxxoOlckxxkxk0xc,....',,,'',,d0d..,';,';:c:;clclol;
0xkxkokddxddkOO:';,,'..',,;l0O00d..oKddc;;;,,clooxdoo
00KKXOdOo:cd00Ox,;:,'''''c00OKKx'l0O0xolc;;:ol:colcll
K000OocO0KXXXXXd:::,''.'xKKKK0KKK0kkO0X00doclcdlclccc
0000kddXXXXXXXXl;;;,''.'KXKK000OkO0OO0KXXXX0Okoc,;dxd
0OkkdxXXXXKXXKXl,,,'''.;KK00OkxdxkkkOOKXKXXXOoollO0kl
KKKKOXXXXXXKXKK:''''''.dK0OOkxdddddkKXXXXKKXXOxkokkOx
X00OKXXXKXXKKK0:''''.'xK0OkxdddddOKXXXXXXXKXKKkkxokxd
0000XXXXXKXKKK0c'''';O00Okxxdl:looollll0XX0KKKOodllod
XKKKXXXXXKKKKKOc'.'lK0Okxxddo:cclcclcd,lXX0KKKXoddlll
K0kXNXXXXXKKKKOl',kK0Okxdol,'',,,,,;:l:cKK00KKK0olcod
0OKXNNXXXXKK00OooKK0Okdoll000OO0KKKKKKXXKkO0KKKKxkkll
0OXXNXXXXKKK0k0KKK0Oxdll:.OKKKKKKKKKXKKKoooooxxxooxdc
0O0KXXKKKXK00KKK0Okdoll;..lKXXKKKKKXXXK0:cloxxdxddxxl
0OOk000OxxOKKK0Okxolll,...:OKXXKKKKXXKX0:cldxkxxxxOOO
000O00kOKKK00Okxdolll'....,k0KXXKKKXXXK0:ldkOxkOOkkkO
K00K0k0K00OOkxddollc......'k0KXXXXXKKXXXoodkkkKKkOOOx
0000O0OOOkkxddoooo:......''d0KKKXXXXXKXXOldxxxOOOkkxO
0K00kkkkxxxddoooo,......'''l0KKKKXXXXXXXXcoxxxkkkkxkk
KO00Oxxxxxddooooo......'''':KKKKKKXXXXXXXclxxxk0OkO0O"""
    author = r"""
		Ddos Panel By  TiGER R@MP@GE
    """
    prints(start_color, end_color, banner)
    prints(end_color, start_color, author)
    print("\n") 
    print(Color.LB+"           ["+Color.LR+"VVIP"+Color.LB+"]"+Color.LC+" dandier"+Color.LR+"       ["+Color.LG+"VIP"+Color.LR+"]"+Color.LC+" flood")
    print("\n") 
    print(Color.LR+"           ["+Color.LG+"VIP"+Color.LR+"]"+Color.LC+" gangbang"+Color.LB+"       ["+Color.LR+"VVIP"+Color.LB+"]"+Color.LC+" socket")
    print("\n")
    
    while True:
        cnc = input(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"root"+Color.LB+"@"+Color.LG+"dandier"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
        if "gangbang" in cnc:
            try:
                gb = os.path.join("node_modules/randomstring", "input.py")
                subprocess.run(['python3', gb])
                sys.exit(0)
            except IndexError:
                print('just input gangbang')
        
        elif "dandier" in cnc:
            try:           
                dandier = os.path.join("node_modules/dashdash/etc", "input.py")
                subprocess.run(['python3', dandier])
                sys.exit(0)
            except IndexError:
                print('just input dandier')
                
        elif "flood" in cnc:
            try:
                flood = os.path.join("node_modules/aws4", "input.py")
                subprocess.run(['python3', flood])
                sys.exit(0)
            except IndexError:
                print('just input flood')
                
        elif "raw" in cnc:
            try:
                raw = os.path.join("node_modules/asn1/lib/ber", "input.py")
                subprocess.run(['python3', raw])
                sys.exit(0)
            except IndexError:
                print('just input raw')
                
        elif "socket" in cnc:
            try:
                socket = os.path.join("node_modules/colors/lib/system", "input.py")
                subprocess.run(['python3', socket])
                sys.exit(0)
            except IndexError:
                print('just input raw')
                                
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Method: [ " + cmmnd + " ] Tidak Di Temukan!")
            except IndexError:
                pass
                
if author == "TiGER R@MP@GE":
    main()
else:
    string.authorsalah()
