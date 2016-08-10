inval = input("Enter a starting number: ")

i = int(inval)

while (i > 1):
    if (i % 2) == 0:
        i = i/2
    else:
        i = (i*3) + 1

    print str(i) + " "
