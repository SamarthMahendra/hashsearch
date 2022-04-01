import random
import string
import time
d={}
dd=[]
def randomfill():
    for i in range(20000000):
        s=''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 9)))
        h=s[0]
        dd.append(s)
        if h in d:
            d[h].append(s)
        else:
            d[h] = [s]
    return
def cushash(s):
    return s[0]


def search(ss):
    print("Searching using linear search :")
    aa=time.process_time()
    flag = 0
    for i in dd:
        if ss==i:
            flag = 1
            break
    if flag:
        print("Found")
    else:
        print("Not Found")
    zz = time.process_time()
    print("time taken to search :")
    print(zz - aa)




def hashsearch(ss):
    print("Searching using hash search :")
    a=time.process_time()
    h = cushash(ss)
    flag = 0
    for i in d[h]:
        if i == ss:
            flag = 1
            break
    if flag:
        print("Found")
    else:
        print("Not Found")
    z=time.process_time()
    print("time taken to search : ")
    print(z-a)
    return
print("Filling db with lots of words...")
randomfill()
print("Done!")
print("Enter a word into db : ")
s=input()
h=s[0]
dd.append(s)
if h in d:
    d[h].append(s)
else:
    d[h]=[s]
print("Search a word :")
word=input()
hashsearch(word)

search(word)




