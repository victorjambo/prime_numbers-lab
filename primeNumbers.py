def prime_numbers(arg):
	listPrime = []
	for num in range(1, arg + 1):
		if num > 1:
			for i in range(2,num):
				if (num % i) == 0:
					break
			else:
				listPrime.append(num)
	return list(set(listPrime))
