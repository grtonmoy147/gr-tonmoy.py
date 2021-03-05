#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 B4.py')

from requests.exceptions import ConnectionError
from mechanize import Browser

#### browser ####
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#### exit ####
def exb():
	print (R + 'Exit')
	os.sys.exit()

#### clear ####
def cb():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std ####
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

#### token remove ####
def trb():
    os.system('rm -rf token.txt')

##### LOGO #####
logo='''
\033[1;94m ┈┈┈┈╱▔▔▔▔╲┈┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈┈╱▔▔▔▔╲┈┈┈┈
\033[1;94m ┈┈┈▕▕TM.05▏▏┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈▕▕TM.05▏▏┈┈┈
\033[1;94m ┈┈┈▕▕▂╱╲▂▏▏┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈▕▕▂╱╲▂▏▏┈┈┈
\033[1;94m ┈┈┈┈╲┊┊┊┊╱┈┈┈┈\033[1;94mShabirBaloch.\033[1;91m┈┈┈┈╲┊┊┊┊╱┈┈┈┈
\033[1;96m ┈┈┈┈▕╲▂▂╱▏┈┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈┈▕╲▂▂╱▏┈┈┈┈
\033[1;96m ╱▔▔▔▔┊┊┊┊▔▔▔▔╲☞☞☞☞☞☞\033[1;91m☜☜☜☜☜╱▔▔▔▔┊┊┊┊▔▔▔▔╲
\033[1;96m................\033[1;grtonmoy147\147[1;91m...............
\033[1;96m................\033[1;93m✬🄵🄰🄲🄴🄱🄾🄾🄺✬\033[1;91m..............

\033[1;96m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

\033[1;91m☞ Auther     : gr tonmoy147
\033[1;92m☞ WhatsApp   : 01782660025


\033[1;93m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                '''
back=0
successfull=[]
checkpoint=[]
oks=[]
cps=[]
id=[]

#### login ####
def login():
	cb()
	try:
		tb=open('token.txt', 'r')
		menu() 
	except (KeyError,IOError):
		cb()
		print (logo)
		print (R + '◈━━━━▷' + S + ' Login With ✬🄵🄰🄲🄴🄱🄾🄾🄺✬ ' + R + '◁━━━━◈')
		print
		id=raw_input(S + '[☆] ' + S + 'Email: ' + G +'')
		pwd=getpass.getpass(S + '[♡] ' + R + 'Password : ')
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("token.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print (S + '[☆]' + Y + ' Login successfull 100% ✓')
		    os.system('xdg-open https://www.youtube.com/channel/UCAGKWM8EwDFZ9sP8CdJhGBA')
		    menu()
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print (R + 'Account has a checkpoint !')
		        t()
		        login()
		    else:
		        print (R + 'number/user id/ password is wrong !')
		        trb()
		        t()
		        login()
def menu():
	cb()
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + 'Token Invalid !')
		trb()
		t()
		login()
	try:
		otw=requests.get('https://graph.facebook.com/me?access_token='+tb)
		a=json.loads(otw.text)
	except KeyError:
		print (G + 'Account has a checkpoint !')
		trb()
		t()
		login()
	except requests.exceptions.ConnectionError:
		print (W + 'No internet connection !')
		t()
		exb()
	cb()
	print (logo)
	print (S + '[☆] ' + G + 'ID Name: ' + R + a['name'])
	print (S + '[☆] ' + G + 'User ID: ' + R + a['id'])
	print
	print (S + 50*'-')
	print
	print (S + '[' + P + '☞1' + S + ']' + S + ' Fast Cloning New Update')
	print (S + '[' + P + '☞2' + S + ']' + S + ' Update B4_BALOCH Tool')
	print (S + '[' + P + '☞3' + S + ']' + S + ' B4_BALOCH WhatsApp Group')
	print (S + '[' + Y + '☞4' + S + ']' + G + ' Log Out')
	print (S + '[' + Y + '☞0' + S + ']' + R + ' Exit')
	print
	print (S + 50*'-')
	print
	mb()


def mb():
	bm=raw_input(W + ' ✬🄵🄰🄲🄴🄱🄾🄾🄺✬   ')
	if bm =='':
		print (R + 'Select a valid option !')
		mb()
	elif bm =='1':
		pak()
	elif bm =='2':
	    os.system('rm -rf $HOME/B4_BALOCH')
	    os.system('cd $HOME && git clone https://github.com/shabirbaloch125/Baloch')
	    cb()
	    print (logo)
	    psb('☆10%')
	    psb('☆☆20%')
	    psb('☆☆☆30%')
	    psb('☆☆☆☆40%')
	    psb('☆☆☆☆☆50%')
	    psb('☆☆☆☆☆☆60%')
	    psb('☆☆☆☆☆☆☆70%')
	    psb('☆☆☆☆☆☆☆☆80%')
	    psb('☆☆☆☆☆☆☆☆☆90%')
	    psb('☆☆☆☆☆☆☆☆☆☆100%')
	    psb('Frends login new Account✓')
	    psb('WhatsApp Num  01782660025✓')
	    psb('WellCome To  gr tonmoy147)
	    psb('Congratulations grtonmoy Tool Has Been Updated Successfully')
	    psb('🔓User Name☆ grtonmoy)
	    psb('🔓Password ☆ grtonmoy147)
	    
	    psb('Please Login Again')
	    time.sleep(2)
