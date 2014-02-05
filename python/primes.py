#/usr/bin/env python

import sys

def calcPrimes(n):
	if n==1:
		print [2]
	elif n==2:
		print [2, 3]
	else:
		primes = [2, 3]
		curr = 5
		lp = 2
		while lp<n:
			np = False
			for x in primes:
				if curr%x == 0:
					# not a prime
					np = True
					break
			if not np:
				lp += 1
				primes.append(curr)
			curr += 2
		return primes


def main():
	if len(sys.argv)!=2:
		print 'Only takes 1 argument, the number of primes to calculate'
	n = 0
	try:
		n = int(sys.argv[1])
		print 'your primes are', calcPrimes(n)
	except:
		print 'Non-integer passed, doing benchmark instead'
		import time
		start = time.clock()
		x = calcPrimes(10000)
		print 'this took: ', time.clock()-start
		print 'the last prime was: ' , x[-1]

if __name__ == '__main__':
	main()
