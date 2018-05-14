from sugar import *
class divider:
	def __init__(self,m,n,k):
		self.m=m
		self.n=n
		self.k=k

	def generate_parts(self):
		self.M=[]
		self.P=[]
		self.min=int(pow(self.m,(1/self.k))+1)
		self.max=round(pow(self.m,(1/(self.k-1)))-0.5)
		print('min',self.min,'max',self.max)
		for i in range(self.n):
				g=self.generateMod(self.min)
				self.M.append(g)
				self.P.append(self.m%g)
		return list(zip(self.P,self.M))#(part, mod)

	def generateMod(self,g):
		if isSimple(g):
			if g in self.M:
				g+=1
			elif g<=self.max:
				return g
		else:
			if g%2==0:
				g+=1
			else:
				g+=2
		return self.generateMod(g)

	def recovery(self,keys):
		X=0
		M=1
		for m in list(map((lambda x:x[1]),keys)):
			M*=m
		for key in keys:#key = (part, mod)
			Mi=M/key[1]
			Mi_=inverse_of(Mi,key[1])
			X+=(key[0]*Mi*Mi_)
		X=X%M
		return  OK(X) if X==self.m else ERR("Восстановить секрет не удалось")


