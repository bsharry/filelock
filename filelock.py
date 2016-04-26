class FileLock(object):
	def __init__(self,file):
		self.file=file
		self.lock=False
	def acquire(self,wait=False):
		if self.lock:
			if whatever:
				while self.lock:
					pass
			else:
				raise FileisLockError("the file is locked")
		self.proxy=proxy(self.file,self)
		self.lock=True
		return self.proxy
	def release(self):
		self.file.flush()
		self.lock=False
		del self.proxy.file
	def close(self):
		self.file.close()
		
class proxy(object):
	def __init__(self,file,filelock):
		self.file=file
		self.filelock=filelock
	def __getattr__(self,attr):
		if not hasattr(self,'file'):
			raise FileHasBeenReleaseError("the file has been release")
		return getattr(self.file,attr)
	def close(self):
		FileLock.release(self.filelock)
		
class FileisLockError(Exception):
	pass

class FileHasBeenReleaseError(Exception):
	pass

