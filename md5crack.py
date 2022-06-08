import os
import platform
import hashlib
import time

RED = "\x1B[31m"
BRED = "\x1B[41m"
GREEN = "\x1B[32m"
BGREEN = "\x1B[42m"
DEFAULT = "\x1B[0m"
nc="\033[1;37m"
yellow="\033[1;33m"



def encrypt_md5():
    plaint = input('Masukin yang mau di enkrip: ')
    encryp = hashlib.md5()
    encryp.update(plaint.encode('ascii'))
    print('hash md5: ', encryp.hexdigest())

def decrypt_md5():
    count = 1

    md5 = input('Masukin hash: ')
    file = input('Masukan path wordlist: ')

    try:
        file = open(file, 'r')
    except:
        print('file wordlist tidak di temukan')
        exit()
        
    for pw in file:
        crack = hashlib.md5()
        crack.update(pw.strip().encode('ascii'))
        mulai = time.time()
        print('Coba password %d: %s' % (count, pw.strip()))
        
        count += 1
        
        kelar = time.time()
        t_waktu = kelar - mulai
        
        if md5.strip() == crack.hexdigest():
            print('Password di temukan: ', pw.strip())
            print('Waktu crack; ', t_waktu, 'detik')
            time.sleep(10)
            
            break
        
        else:
            print('Password tidak di temukan')
        
def menu():
    os.system("clear")
    sistem = platform.uname()
    LOGO = f"""
	                {RED}.YYY555PPPPGGGG?
	                .BBB####&&&&&@@?
	                .GBBB:.....P&&@?
	         .~     .GBBG      5@&@?
	        ^BJ     .GBBG      5@&@?
	       ?B#J     .GBBG      5@&@?   {yellow}| {nc}System    : {GREEN}{sistem.system}{RED}
	      !BBBJ     .PGGG      5@&@?   {yellow}| {nc}Node Name : {GREEN}{sistem.node}{RED}
	      !BB#J                5@&@?   {yellow}| {nc}Machine   : {GREEN}{sistem.machine}{RED}
	      !BB#J     {GREEN}HADES{RED}      5@&@?   {yellow}| {nc}Release   : {GREEN}{sistem.release}
	     {nc} !BB#J        ..      5@&@?
	      !BB#J      #&&&.     5@&@?
	      !BB#J      &&@@.     5@@5
	      !BB#J      &&@&.     P&~
	      !BB#J      &&@&.     !.
	      !BBBY.....:&&@&.
	      !BBB###&&&&&@@@.
	      !YYYY555PPPGGGG.{nc}

	   [{RED}+{nc}]{yellow}MD5 Tool {RED}Encrypt {yellow}and {GREEN}Decrypt {nc}[{RED}+{nc}]
	"""
    print(LOGO)
    
    print(' '*10, '-'*32)
    print(' '*22, 'Menu MD5')
    print(' '*10, '-'*32)
    print(' '*13, f'{nc}1) {RED}Encrypt')
    print(' '*13, f'{nc}2) {GREEN}Decrypt')
    
    pil = input('hades> ')
    if pil == "1":
        os.system('clear')
        print(LOGO)
        encrypt_md5()
    elif pil == "2":
        os.system('clear')
        print(LOGO)
        decrypt_md5()
    else:
        print('Masukin pilihan yang benar!!!')
        menu()
menu()