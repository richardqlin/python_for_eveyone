han = open('mbox.txt')


for line in han:
    line = line.rstrip()
##    if line =='':
##        print('Skip Blank')
##        continue
    wds = line.split()
    print('Words:', wds)
    # Guadian in a compound statement
   
    if len(wds) <3 or wds[0] != 'From' :
        continue
##        print('Ignore')
##        continue

    print(wds[2])
