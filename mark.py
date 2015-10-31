#!/usr/bin/env python

import sys, re, random, pickle

tokens={}
digest={}

r=re.compile(r"^..:.. [^\s]*>")

def occur(p,t):
    if p not in tokens:
        tokens[p]={}
    if t not in tokens[p]:
        tokens[p][t]=1
    else:
        tokens[p][t]+=1

numLines = 0
if len(sys.argv)>2:
    if len(sys.argv)>3:
        ml=int(sys.argv[3])
    else:
        ml=1
    for f in open(sys.argv[1],errors='ignore'):
        for l in open(f[:-1],errors='ignore'):
            if r.match(l):
                l = l[l.find(">")+2:].split()
                if len(l) < ml: continue
                numLines += 1
                p=''
                for t in map(str.lower, filter(str.isalpha, l)):
                    occur(p,t)
                    p=t
                occur(p,'')
    print('Processed %d lines' %numLines)
    for p in tokens:
        c=0
        for t in tokens[p]:
            c+=tokens[p][t]
        d=[]
        c=float(c)
        r=0.0
        for t in tokens[p]:
            r+=tokens[p][t]/c
            d+=[(t,r)]
        digest[p]=d
    pickle.dump(digest,open(sys.argv[2],"wb"))
elif len(sys.argv)==2:
    digest=pickle.load(open(sys.argv[1],"rb"))
else:
    print("Usage: %s {digest|filelist digest [minlength]}"%sys.argv[0])
    sys.exit(1)

def bsearch(a, v, lo, hi):
    mid = (lo+hi)//2
    if hi == lo or a[mid][1] == v: return mid
    if hi - lo == 1:
        return lo if a[lo][1] < v else hi
    return bsearch(a, v, lo if v<a[mid][1] else mid+1, mid-1 if v<a[mid][1] else hi)

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

def genToken(prevToken):
    nextTokens = digest[prevToken]
    rand = random.random()
    nt=nbsearch(nextTokens, rand, 0, len(nextTokens))
    return nextTokens[nt][0]

def gen():
    result = ''
    token = ''
    while 1:
        token = genToken(token)
        if '' == token: return result.rstrip()
        result += token+' '

print(gen())
