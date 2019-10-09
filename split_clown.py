fname = input('Enter File: ')

if len(fname) < 1: fname ='clown.txt'

han = open(fname)

di = dict()


for lin in han:
    lin = lin.strip()
    print(lin)
    wds = lin.split()
    print(wds)
    for w in wds:
        #print('**',w,di.get(w,-99))
        # if the key is not there the count is zero
##        oldcount = di.get(w,0)
##        print(w,'old',oldcount)
##
##        newcount = oldcount + 1
##        di[w] = newcount
        # idiom: retrieve / create/ update counter
        di[w] = di.get(w,0) + 1

        #print(w,'new',newcount)
        
##        if w in di:
##            di[w] = di[w] + 1
##            #print('**Existing**')
##        else:
##            di[w] = 1
##            #print('**NEW**')
##        print(w,di[w])

#print(di)

#now we want to find the most common word

largest = -1
theword = None

for k,v in di.items():
    print (k,v)
    if v > largest:
        largest = v
        theword = k #cature/remember the word that the largest
print(theword, largest)
        
    
tups = di.items()

print(tups)

tmp = []

for k,v in di.items():
    tmp.append((v,k))

tmp = sorted(tmp)

for v, k in tmp:
    print(k,v)





