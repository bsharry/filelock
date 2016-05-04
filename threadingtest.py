import threadinkg
lock=threading.Lock()
class MyThread(threading.Thread):
	def run(self):
		print("this is a test")
if __name__=='__main__':
	for i in range(10):
		Thread=MyThread()
		Thread.run()

