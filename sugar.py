
from millerrabin import mr_test
def eratosthenes(n):
	sieve = list(range(n + 1))
	sieve[1] = 0    
	for i in sieve:
		if i > 1:
			for j in range(i + i, len(sieve), i):
				sieve[j] = 0
	res=[]
	for x in sieve:
		if x:
			res.append(x)
	return res

SIMPLE_EVENS=eratosthenes(1000000)
def isSimple(g):
		#return mr_test(g)
		return True if g in SIMPLE_EVENS else False

def extended_euclidean_algorithm(a, b):
    """
    Возвращает кортеж из трёх элементов (gcd, x, y), такой, что
    a * x + b * y == gcd, где gcd - наибольший
    общий делитель a и b.

    В этой функции реализуется расширенный алгоритм
    Евклида и в худшем случае она выполняется O(log b).
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def exgcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = exgcd(b % a, a)
        return (g, x - (b // a) * y, y)


def inverse_of(a, m):
    g, x, y = exgcd(abs(a), m)
    if g != 1:
        raise Exception('Обратного элемента не существует')
    else:
        if a > 0:
            return x % m
        else:
            return -x % m
    
def OK(value=""):
	return {"status":True,"value":value}

def ERR(value=""):
	return {"status":False,"value":value}