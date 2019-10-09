fhand = open('clown.txt')

counts = {}

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

l = []

for k,v in counts.items():
    l.append((v,k))

l = sorted(l, reverse = True)

for k,v in l:
    print(v,k)

lst=[]
for key, val in counts.items():
    lst.append((val, key))

lst = sorted (lst, reverse= True)

for key, val in lst[:3]:
    print(val, key)
