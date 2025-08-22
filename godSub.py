#coded by: Addad Billal


import os 
import sys 
import time 
import requests

#CONST
API = "https://api.hackertarget.com/hostsearch/?q="


def GetSubs(userInput):
    url = API + str(userInput)
    req = requests.get(url, verify=True)
    content = req.content.decode('utf-8')
    if "error invalid host" in content:
        print("Enter Something Correct ex: example.com")
    else:

        subs_details = content.split('\n')
    
        for details in subs_details:
            if details.strip():  # Check if the line is not empty
                subdomain, IP = details.split(',')
                with open('subs.txt', 'a') as save:
                    save.write(f'{subdomain} {IP}\n')
                output = f' \033[0;36m(+++) \033[0;31mSub\033[0m {subdomain}\033[0m \033[0;36m(+++) \033[0;31mIP \033[0m{IP}'
                time.sleep(0.00001)
                print(output)


def main (userInput):
    def check_www(toMake_simple):
        if 'www' in toMake_simple:
            toMake_simple = toMake_simple.split('.')
            urlTarget = toMake_simple[1] + "." + toMake_simple[2]
            GetSubs(urlTarget)
        else:
            GetSubs(toMake_simple)

    if userInput.startswith('http'):
        simple = userInput.split('//')[1]
        check_www(simple) 
    else:
        check_www(userInput)

os.system("clear || cls")
print("\033[0;36mScript: \033[0;31mSubdomain Finder with IP's \033[0m")
test  = input("Enter the URL or domain: ")
main(test)

  