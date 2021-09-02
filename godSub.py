#!/usr/bin/python

#Coded By Zerf003
#sub gather with IP 

import requests 
import os
import sys
import time

API_hacker_target = "https://api.hackertarget.com/hostsearch/?q="

def get_subs(user_input):#Za3ma BackEnd of the script
    url = API_hacker_target + str(user_input)
    req  = requests.get(url, verify=True)
    cont = req.content
    cont = cont.decode('utf-8')
    each_sub_details = cont.split('\n')
    for details in each_sub_details:
        details = details.split(',')
        subdomain = details[0]
        IP = details[1]
        with open('subs.txt', 'a') as save:
            save.write('{} {}'.format(subdomain, IP) + '\n')
        output = ' \033[0;31m(+++) Sub\033[0m {}\033[0m \033[0;31m(+++) IP \033[0m{}'.format(subdomain, IP)
        time.sleep(0.00001)
        print(output)
   
def filter_input_output(userInput):
    def check_www(toMake_simple):# check for 'www' in the URL
        if 'www' in toMake_simple:
            toMake_simple = toMake_simple.split('.')
            urlTarget = toMake_simple[1] + "." + toMake_simple[2]
            get_subs(urlTarget)
        else:
            get_subs(toMake_simple)

    if userInput.startswith('http'):
        simple = userInput.split('//')
        simple = simple[1]
        check_www(simple) 
    else:
       check_www(userInput)

user_input = input('\033[0;31m(+++) Enter Target To Grab Subs: '+ "\033[0m")
filter_input_output(user_input)
print('\033[0;31m(+++) Saved in subs.txt')
