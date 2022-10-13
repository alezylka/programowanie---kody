"""
@sources: https://www.geeksforgeeks.org/count-arithmetic-progression-subsequences-array/
"""

#program znajdujacy kolejny wyraz ciagu arytmetycznego
liczba_elementow = [1, 2, 3]
n = len(liczba_elementow)
MAX = 1000001

#okreslenie minimum i maksimum tablicy
minimum = +2147483647
maximum = -2147483648

#okreslenie zakresu warotsci tablicy
for i in range(n):
	minimum = min(minimum, liczba_elementow[i])
	maximum = max(maximum, liczba_elementow[i])
	
podciag = [0 for i in range(n + 1)] 
#zadeklarowanie liczby podciagow w zakresie (n + 1), gdzie podajemy n
szukany = n + 1 #zadeklarowanie szukanego elementu ciagu

#wykonujemy wszystkie operacje odejmowanie koniecne do dotarcia do szukanego elementu ciagu
for r in range((minimum - maximum), (maximum - minimum) + 1):   #
	sum = [0 for i in range(MAX + 1)]
		
	for i in range(n):  #przechodzac przez wszystkie elementy podanej tablicy
	    podciag[i] = 1  #zadeklarowawszy wartosc wejsciowa
        #wykonuje sie operacje dodania kolejnych elementow ciagu wraz z ich roznicami

        if (liczba_elementow[i] - r >= 1 and liczba_elementow[i] - r <= 1000000):
		    podciag[i] += sum[liczba_elementow[i] - r]
            szukany += podciag[i] - 1
		    sum[liczba_elementow[i]] += podciag[i]
        
print('szukany element tego ciagu arytmetycznego jest ronwy ' + str(szukany))


