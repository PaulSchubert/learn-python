
class primeNumCheck:

	def __init__(self, num):
		self.num = num
	
	def isPrime(self):
		if self.num > 1:
			for i in range(2, int(self.num/2)+1):
				if(self.num % i) == 0:
					return False

		elif self.num <= 1:
			return False

		return True


