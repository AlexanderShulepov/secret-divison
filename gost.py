import random

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

SIMPLE_EVENS=eratosthenes(100000)

def get_seed(t):
	while True:
		random_choice=SIMPLE_EVENS[random.randint(0,len(SIMPLE_EVENS)-1)]
		if not t%random_choice.bit_length():
			return random_choice



def generate_even(q,t=128):
	while True:
		E=random.uniform(0,1)
		N=round( 2**(t-1)/q ) + round( 2**(t-1)*E/q )
		N=N+1 if N&1==1 else N
		res=get_p(N,q,t)
		if res["status"]:
			return res["num"]

		

def get_p(N,q,t,u=0):
	p=(N+u)*q+1
	if p>2**t:	
		return {"status":False,"num":p}
	if pow( 2,(p-1),p )==1%p and pow( 2,N+u,p )!=1%p:
		return {"status":True,"num":p}

	u=u+2
	return get_p(N,q,u)

def generate_fixed_size_prime(t,seed):
	while seed.bit_length()<t:
		seed=generate_even(q=seed,t=seed.bit_length()*2)
	return seed

def gost_generate():
	t=128
	seed=get_seed(t)
	return generate_fixed_size_prime(t,seed)
