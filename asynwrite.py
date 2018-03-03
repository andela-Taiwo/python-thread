import threading
import time
from contextlib import contextmanager

class AsyncWrite(threading.Thread):
	
	def __init__(self, output_file, text):
		super().__init__() 
		self.output_file = output_file
		self.text = text

	# @contextmanager
	# def run(self):
	# 	f = open(self.output_file, 'a')
	# 	f.write(self.text + "\n")
	# 	f.close()
	# 	time.sleep(2)
	# 	print("Finisehd writing to a file" + self.output_file)
	
	def __enter__(self):
		self.f = open(self.output_file, 'a')
		self.f.write(self.text + "\n")
		time.sleep(2)
		print("Finisehd writing to a file" + self.output_file)

	def __exit__(self, *args):
		self.f.close()
		
def main():
	message = input("Write a line of a text > ")
	background =  AsyncWrite("output_file.txt", message)
	with background:
		background.start()
	print("This program can continue in the background")
	background.join()
	print("Waited to complete thread")

if __name__ == "__main__":
	main()
		
