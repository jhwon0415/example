import math

'''
a = int(raw_input("a :"))
b = int(raw_input("b :"))
c = int(raw_input("c :"))

k = b*b-4*a*c

if k<0:
    print 'xx'
elif k==0:
    print -b/2
elif k>0:
    print (-b+math.sqrt(math.fabs(b*b-4*a*c)))/2
    print (-b-math.sqrt(math.fabs(b*b-4*a*c)))/2

'''

'''
while True:

    n = int(raw_input("n = "))

    if n == 0:
        break

    i=0
    while i < 9:
        print '%d*%d = %d' %(n, i+1, n*(i+1))
        i = i + 1


'''

'''
s = 'abc'
print s*2

n = int(raw_input("n = "))
print n
i=n
print i
space = ' '
star = "*"
while i!=-1:
    print space*(i) + star*((n-i)*2-1)
    i = i -1

'''

'''
n = int(raw_input("n = "))

for i in range(0,9):
    print '%d*%d = %d' % (n, i + 1, n * (i + 1))
    i = i + 1


print [x**2 for x in [1,2,3]]
print [x**2 for x in [1,2,3] if(x%2) == 0]

l = []
nums = [1,2,3]

for i in nums:
    l.append(i ** 2)

print l
'''
'''
print [k for k in range(0,5) if k%2==1]

t = (1,2,3)

user = {'usr0' : {'name': 'l', 'num' : 456}, 'usr1' : {'name' : 'j', 'num' : 123}}

for key,value in user.iteritems():
    print key, value

## assignemnt

'''

'''
## assignment_1

from random import randint

score = 0

l = (0,1,2)
d = {0:"kawi", 1:"bawi", 2:"bo"}

# 0 kawi 1 bawi 2 bo
while score != 3:
    my = int(raw_input("kawi bawi bo : "))
    yours = randint(0,2)
    if my not in l:
        print "0:kawi 1:bawi 2:bo"
        continue
    result = my - yours

    if (result == 1)or(result == -2):
        score +=1
        print d[my], d[yours], score,"win"
        if(score == 1):
            print "finish"
            break;
    elif result == 0:
        print d[my], d[yours], score, "draw"
    else:
        score -= 1
        print d[my], d[yours],score,"lose"

'''



'''
import math


def quardratic_formula(a,b,c):

    k = b**2-4*a*c

    if k < 0:
        return ()
    elif k == 0:
        return (-b / 2)
    elif k > 0:
        return ((-b + math.sqrt(abs(b **2 - 4 * a * c))) / 2,(-b - math.sqrt(abs(b **2 - 4 * a * c))) / 2)


print quardratic_formula(4,-5,1)

'''

'''
f = lambda  x : x**2
print type(f)

print f(5)

'''

'''
multiply_add = lambda x,y=0,z=0 : (x+y)*z

print multiply_add(1,z=3)

'''
'''
#assignment 2

#mutiply of Matrix : learn 2 dimensional list -> list comprehension

n = int(raw_input("row , col num = "))
l = []
for i in range(0,n):
    l.append(raw_input("row%d : "%(i)).split())

print l
tmp = [j for i in l for j in i]
r=1
for n in tmp:
    r = r * int(n)
print r

'''


#assignment 3

#make Matrix n*n, Matrix add return matrix
n = int(raw_input("row , col num = "))
l1 = []
for i in range(0,n):
    l1.append(raw_input("row%d : "%(i)).split())
print l1

n = int(raw_input("row , col num = "))
l2 = []
for i in range(0, n):
    l2.append(raw_input("row%d : " % (i)).split())

print l2

## use list comprehesion -> make one line

matrix =  [[0 for x in range(n)] for x in range(n)]



