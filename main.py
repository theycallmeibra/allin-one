from strip import *
import pyfiglet
import requests
from bs4 import BeautifulSoup as bs



name = pyfiglet.figlet_format("Theycallmeibra")
print(name)


filename = input('Enter FileName here:')

try:
	ccs = open(filename)
except:
	print('No file named'+filename)
	print(' ')
	print('1 error')
	print(' ')


readcc = ccs.readlines()
print(' ')
print(str(len(readcc)) + ' CCs Found')
print(' ')
print('checking .....')
print(' ')


def check():
	x = 0
	for i in readcc:
		main(i)
		x += 1
	print(' ')
	print(str(x)+' Done, No errors')
	print(' ')
	


check()
ccs.close()