from random import randint

def MR(n):
    t=2
    
    def get_vars(N):
        S=r=0
        for s in range(128,0,-1):
            if ((n-1)%(2**s)==0):
                k=(n-1)//(2**s)
                if(2**s*k+1==n and k%2==1):
                    S=s
                    r=k
        return S,r
    S=r=0
    SR=get_vars(n)

    if SR:
        S,r=SR[0],SR[1]
    else:
        return(str(n)+"Bad number")

    b=[]
    for i in range(t):
        a=randint(2,n-1)#last not included
        b.append( pow(a,r,n) )
        for j in range(1,S+1):
            b.append( (pow(b[-1],2,n)))
        if  b[-1]!=1:
            return(str(n)+" - составное»")
        elif b[b.index(1)-1]!=n-1:
            return(str(n)+" - составное»")  
        b=[]
    return str(n)+" - простое"
            

    
    
def mr_test(n):
            num=MR(n)
            if  "простое" in num:
                return True
            else:
                return False

