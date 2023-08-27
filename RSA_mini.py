import math
import time
import random

Start = 100
End = 200
Text = 380

# N = 667
# n = 616
# p = [29, 23]
# e = 17
# d = 237

def make_prime_list(s, e) :
    N = list(range(2, e))

    for i_ in N :
        i = N.index(i_)
        for j in N[i+1:] :
            if j % N[i] == 0 :
                N.remove(j)
    
    while N[0]<s :
        N.pop(0)

    return N

def random_prime() :
    n = make_prime_list(Start, End)
    p = random.sample(n,2)
    return p

def coprime_list(p) :
    N = list(range(2,p+1))
    
    for i in range(2,p+1) :
        gcd = False
        for j in range(2,i+1) :
            if p%j==0 and i%j==0 :
                gcd = True
        if gcd :
            N.remove(i)
    return N

def random_coprime(p_, q_) :
    i_cl = list(set(coprime_list(p_)) & set(coprime_list(q_)))
    cp = random.choice(i_cl)
    return cp

def RSA() :
    p = random_prime()
    N = p[0]*p[1]
    n = (p[0]-1)*(p[1]-1)
    e = random_coprime(p[0]-1, p[1]-1)
    d = find_d(N, e, n)
    
    return[N, e, d]

def find_d(N, e, n) :
    n_ = n
    euclid = list()
    while e > 1 :
        euclid.append([n, e, -1 * math.trunc(n/e), n%e])
        n = euclid[-1][1]
        e = euclid[-1][3]

    euclid = euclid[::-1]
    
    s = 1
    t = 1
    for e in euclid :
        _s = s
        _t = t

        if e is not euclid[0] :
            s = _t
            t = _s + _t * e[2]
        else :
            t = e[2]
    
    if t<0 :
        t = t+n_
    
    return t

def mod_arith(a, n, N) :
    d = list()
    while n > 0 :
        d.append(n % 10)
        n = math.floor(n/10)
    
    n = 1
    for i in d[::-1] :
        n = (pow(n,10) % N) * (pow(a,i) % N) % N
        
    return n

def encryption(Text, e, N) :
    return mod_arith(Text, e, N)

def decryption(X, d, N) :
    return mod_arith(X, d, N)

def test() :
    count = 0
    test = 0
    for i in range(50) :
        rsa = RSA()
        N = rsa[0]
        e = rsa[1]
        d = rsa[2]

        X = encryption(Text, e, N)
        a = decryption(X, d, N)
        isSame = Text == a

        print("Text :", Text, " // a :", a, " // isSame :", isSame)
        test += 1
        if isSame :
            count += 1
    print(count, "/", test)
    pass


t = time.time()

rsa = RSA()
N = rsa[0]
e = rsa[1]
d = rsa[2]
X = encryption(Text, e, N)
a = decryption(X, d, N)
print("Text :", Text)
print("Output :", a)

# test()

print(f"{time.time()-t:.4f} sec")

