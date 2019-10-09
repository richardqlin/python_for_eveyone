fhand = open('mbox.txt')

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue

    words = line.split()
    print(words)
    print(words[2])

    email = words[1]

    pieces = email.split('@')
    print(pieces[1])
