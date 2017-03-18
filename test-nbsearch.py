import random
def nbsearch(a,v,lo,hi):
    mid = (lo+hi)//2
    if mid<=lo:
        return mid
    elif a[mid][1]>=v and a[mid-1][1]<v:
        return mid
    elif a[mid][1]<v:
        return nbsearch(a,v,mid,hi)
    else:
        return nbsearch(a,v,lo,mid)

def rndtest():
    a = []
    for i in range(100):
        a.append(('foo', random.random()))
    a.sort()
    for i in range(100):
        n = random.randint(1, len(a)-1)
        v = a[n][1] #(a[n][1]+a[n-1][1])/2.0
        n2 = nbsearch(a, v, 0, len(a))
        if n != n2:
            print('failed to find ', v, 'at index', n)
            for i in range(len(a)):
                print(i, a[i])
            raise SystemExit
    print('passed')

for i in range(100):
    rndtest()


