# Put a number and get a string of a product of the powers that its result is x.
# Phan tich 1 so thanh tich nhung luy thua
def to_product(x):
    # Check whether x is greater than 0?
    while True:
        try:
            assert x > 0
            break
        except AssertionError: # Catch AssertionError Exception
            print("!!!Your number musts be greater than 0!!!")
            x = int(input("Enter a number: "))

    aList = []
    t = x
    n = 2
    countList = {}
    s = str(x) + " = "

    # Check whether t mod n is zero or not
    while (t != 1):
        if (t % n == 0):
            # print("%d chia het cho %d, \n--> %d : " % (t, n, t), end="")
            t = t / n
            # print("%d = %d" % (n, t))
            aList.append(n)
        else:
            n = n + 1

    # Count times one element appear in list
    # Add them into dictionary
    j = -1
    for i in aList:
        if (j != i):
            j = i
            countList[j] = aList.count(i)

    # update string s
    count = 0
    for k, v in countList.items():
        s = s + str(k) + "^" + str(v)
        if (count < len(countList)-1):
            s = s + " x "
        count = count + 1

    return s

# num = int(input("Enter a number: "))
# to_product(num)
