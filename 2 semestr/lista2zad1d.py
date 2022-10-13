"""
@sources: https://www.geeksforgeeks.org/count-arithmetic-progression-subsequences-array/
"""

#program znajdujacy kolejny wyraz ciagu arytmetycznego

MAX = 1000001

def elem_ciagu(a, n):

	#okreslenie minimum i maksimum tablicy
	minarr = +2147483647
	maxarr = -2147483648

	#okreslenie zakresu warotsci tablicy
	for i in range(n):
		minarr = min(minarr, a[i])
		maxarr = max(maxarr, a[i])
	

	#zadeklarowanie liczby podciagow w zakresie (n + 1), gdzie podajemy n 
	dp = [0 for i in range(n + 1)]
	

	#zadeklarowanie szukanego elementu ciagu
	szukany = n + 1

	#wykonujemy wszystkie operacje odejmowanie koniecne do dotarcia do szukanego elementu ciagu
	for d in range((minarr - maxarr), (maxarr - minarr) + 1):
		sum = [0 for i in range(MAX + 1)]
		
		#przechodzimy przez wszystkie elementy podanej tablicy
		for i in range(n):
		
			#zadeklarowanie wartosci wejsciowej
			dp[i] = 1

			#operacja dodania kolejnych elementow ciagu wraz z ich roznicami
			if (a[i] - d >= 1 and a[i] - d <= 1000000):
				dp[i] += sum[a[i] - d]

			szukany += dp[i] - 1
			sum[a[i]] += dp[i]  #

	return szukany

# Driver code
liczba_elementow = [1, 2, 3]
n = len(liczba_elementow)

print(elem_ciagu(liczba_elementow, n))

# This code is contributed by Anant Agarwal.
