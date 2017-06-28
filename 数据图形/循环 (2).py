import math
for i in range(50, 100 + 1):
    for j in range(2, int(math.sqrt(i))):
        if i % j == 0:
            break
         else:
        print (i)
