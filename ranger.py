import socket
import sys
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

def scan(site):
                ur = site.rstrip()
                ch= site.split('\n')[0].split('.')
                ip1=ch[0]
                ip2=ch[1]
                ip3=ch[2]
                taz = str(ip1)+'.'+str(ip2)+'.'+str(ip3)+'.'
                i = 0
		while i <= 255:
                        i+=1
			print "IP Range ==>"+str(taz)+str(i)
			open('IP.txt', 'a').write(str(taz)+str(i)+'\n')
nam=raw_input('IP List name :')
with open(nam) as f:
    for site in f:
        scan(site)
