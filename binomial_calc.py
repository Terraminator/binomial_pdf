#the calculator sucks with ranges

def fac(a: int):
    #faculty of a
    if a<0:
        print("fac(a<0)->Value Error")
        exit()
    res=1
    for i in range(1,a+1):
        res=(i*res)
    return(res)

def bin_coeff(n: int, k: int):
    #binomial coeffcient
    return(fac(n)/(fac(n-k)*fac(k)))

def P(X: int, n: int, p: float):
    #binomial propability
    k=X
    return(bin_coeff(n, k)*(p**k)*((1-p)**(n-k)))
    
def make_range(k):
    #interpret k as a range for binomialcdf
    if not "-" in k:
        print("missing - in range for k")
        usage()
        exit()
    k=range(int(k.split("-")[0]), int(k.split("-")[1])+1)
    return(k)
    
def binomialcdf(n: int, p: float, k: int):
    #cumulative propability for range k
    res=0
    for i in k:
        res+=P(int(i), int(n), float(p))
    return(res)
    
def usage():
    print("usage:\nn;p;k=X\nk can be written as a range: f.e. 1-3(=1,2,3)\n")

def main():
    print("calculator for binomialpdf/binomialcdf")
    usage()
    n, p, k=(False, False, False)
    inp = input("Please enter arguments(n,p,k): ")
    if len(inp.split(";")) < 3 and len(inp.replace(";", ",").split(","))<3:
        print("not enough arguments")
        print(usage)
    elif len(inp.split(";"))<3:
        inp=inp.replace("," ";")
    n, p, k=inp.split(";")
        
    if not "=" in k:
        k=make_range(k)
        print(round(binomialcdf(n,p,k), 4))
    else:
        k=k.split("=")[1]
        print("calculating binomialpdf for: \nn={}\np={}\nk={}".format(str(n), str(p), str(k)))
        print(round(P(int(k), int(n), float(p)), 4))
    if input("do you want to plot the binomial distribution? (y/n): ") == "y":
        print("E(X)="+str(round(float(n)*float(p))))
        import matplotlib.pyplot as plt
        fig = plt.figure("binomial distribution")
        ax = fig.add_axes([0,0,1,1])
        Propability=[]
        for i in range(int(n)):
            Propability.append(i)
        k=[]
        for i in range(int(n)):
            k.append(P(int(i), int(n), float(p)))
        ax.bar(Propability, k)
        plt.show()
if __name__=="__main__":
    main()
