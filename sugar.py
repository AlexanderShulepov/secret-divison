
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

SIMPLE_EVENS=eratosthenes(20000000)
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


def inverse_of(n, p):
    """
    Возвращает обратную величину
    n по модулю p.

    Эта функция возвращает такое целое число m, при котором
    (n * m) % p == 1.
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Или n равно 0, или p не является простым.
        return False
    else:
        return x % p
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def OK(value=""):
	return {"status":True,"value":value}

def ERR(value=""):
	return {"status":False,"value":value}