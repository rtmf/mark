#!/usr/bin/python -i
import sys
import re
import mysql.connector as m, random
x=m.connect(user="mark",password="newpass4mark",database="mark")

sql="""use mark;
drop table if exists 3grams;
drop table if exists 1grams;
drop table if exists 3freq1;
create table 3grams (
`1` int(11) not null,
`2` int(11) not null,
`3` int(11) not null,
`⇒` int(11) not null auto_increment,
KEY `i` (`1`,`2`,`3`),
KEY `o` (`⇒`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
create table 3freq1 (
`⇐` int(11) not null,
`…` int(11) not null,
`#` int(11) not null,
`∑` int(11) not null,
`%` float not null,
KEY `i` (`⇐`),
KEY `o` (`…`,`%`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
create table 1grams (
`←` varchar(255) not null,
`⇒` int(11) not null auto_increment,
unique key `o` (`⇒`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
drop procedure if exists cook;
drop procedure if exists msay;""".replace("\n"," ").split(";")+["""create procedure cook()
begin
	declare `∫` integer default null;
	declare `∑` integer default null;
	declare `#` integer default null;
	declare `⇐` integer default null;
	declare `…` integer default null;
	declare `=` integer default null;
	declare `%` float default null;
	declare `⇒` cursor for select `⇒` from 3grams;
	declare `→` cursor for select `…`,`#` from 3freq1 where `⇐`=`⇐`;
	open `⇒`;
	3loop: loop
		fetch `⇒` into `⇐`;
		select 0 into `∑`;
		select sum(`#`) into `∑` from 3freq1 where `⇐`=`⇐`;
		open `→`;
		1loop: loop
			fetch `→` into `…`,`#`;
			set `∑`=`∑`+`#`;
			set `%`=`∑`/`∫`;
			update 3freq1 set `∑`=`∑`, `%`=`%` where `⇐`=`⇐` and `…`=`…`;
		end loop;
		close `→`;
	end loop;
	close `⇒`;
end""","""create procedure msay()
begin
	declare `0`,`1`,`2`,`3`,`⇒`,`⇐`,`…` INTEGER DEFAULT NULL;
	declare `%` FLOAT DEFAULT NULL;
	declare `¶` VARCHAR(255) DEFAULT "";
	declare `→` VARCHAR(255) DEFAULT "";
	select `⇒` into `0` from `1grams` where `1`="";
	set `1`=`0`;
	set `2`=`0`;
	set `3`=`0`;
	genloop: loop
		select rand() into `%`;
		select `…` into `…` from 3freq1 where `1`=`1` and `2`=`2` and `3`=`3` and `%`>=`%` order by `%` limit 1;
		if `…` = `0` then
			leave genloop;
		end if;
		select `←` into `→` from 1grams where `⇒`=`…`;
		if `3`!=`0` then
			select concat_ws(" ",`¶`,`→`) into `¶`;
		else
			set `¶`=`→`;
		end if;
		set `1`=`2`;
		set `2`=`3`;
		set `3`=`→`;
	end loop;
	select `¶`;
end
"""]

def add(p,t,wrd,tok):
    if t not in wrd:
        wrd+=[t]
    if p not in tok:
        tok[p]={}
    if t not in tok[p]:
        tok[p][t]=1
    else:
        tok[p][t]+=1

def new(files,minlength=1,regex=r"^..:.. [^\s]*>"):
    wrd=[]
    tok={}
    out={}
    r=re.compile(regex)
    c=x.cursor()
    for s in sql:
        c.execute(s)
    numLines=0
    for f in files:
        for l in open(f,errors='ignore'):
            if r.match(l):
                l = l[l.find(">")+2:].split()
                if len(l) < ml: continue
                numLines += 1
                p=('','','')
                for t in map(str.lower, filter(str.isalpha, l)):
                    add(p,t)
                    p=(p[1],p[2],t)
                add(p,'')
    print('Processed %d lines' %numLines)
new(sys.argv[1:])
