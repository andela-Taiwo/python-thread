from threading import Thread, Lock
import time

t_lock = Lock()
def timer(name, delay, repeat):
	print("Timer {0}".format(name))
	t_lock.acquire()
	print("This thread " + name + " has access now")
	while repeat > 0 :
		time.sleep(delay)
		print(name + ":" + str(time.ctime()))
		repeat -= 1
	print("Timer " + name + "complted")
	print("This thread " + name + " has released the lock")
	t_lock.release()

def main():
	t1 = Thread(target=timer , args=["Timer1", 1, 5])
	t2 = Thread(target=timer, args=['Timer2', 2, 5])
	t1.start()
	t2.start()

if __name__ == "__main__":
	main()
