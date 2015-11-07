#!/usr/bin/python -i
import mysql.connector as m, random
x=m.connect(user="mark",password="markpass")
def gen():
    c=x.cursor()
    c.execute("select id from mark.words where word='';")
    r=c.fetchall()
    b=r[0][0]
    t=[b,b,b]
    r=-1
    v=""
    while r!=b:
        r=random.random()
        c.reset()
        c.execute("select id,word from mark.words where id=(select d from mark.trigrams where a=%s and b=%s and c=%s and f>=%s order by f limit 1);",t+[r])
        r,w=c.fetchone()
        v+=w+" "
        t=t[1:]+[r]
    return v.rstrip()

print("gen()")
