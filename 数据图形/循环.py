count = 0
for num in range(100,1000):
    if(num % 17 == 0):
        print num,
        count = count +1
print
print "Total number is:",count

import threading
from time import ctime,sleep


urls = ['http://mmjpg.com/mm/{cnt}'.format(cnt=cnt) for cnt in range(1, 953)]
print urls