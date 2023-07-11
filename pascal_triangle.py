def pascalTriangleFunction(n):
    # Initials variables
    aList = [0, 1]
    countOne = 1
    index = 0
    stop = 2*n - 1 # A stop point
    # A loop that stop when number of ones
    # in the list greater 2*n-1
    while (countOne <= stop):
        if countOne%2 != 0:
            aList.append(0)
            if countOne == stop:
                break
            
        Sum = aList[index] + aList[index+1]
        if Sum == 1:
            countOne = countOne + 1
        
        aList.append(Sum)
        index = index + 1
    
    return aList

def digitsOfGreatestNum(aList):
    Max = max(aList)
    count = 0
    
    while (Max != 0):
        Max = Max // 10
        count = count + 1
    
    return count

def spaceNum(n):
    s = ""
    
    for i in range(n):
        s = s + " "
    
    return s

def pascalTriangle(n):
    aList = pascalTriangleFunction(n)
    digits = digitsOfGreatestNum(aList)
    countDown = n - 1 #floor n minus 1
    
    for i in range(len(aList)):
        # Don't print 0
        if aList[i] == 0:
            print("\n")
            continue
        
        # Enter new line and print an element
        if aList[i] == 1:
            if aList[i-1] == 0:
                print(spaceNum(digits * countDown) + "%{}d".format(digits) % (1), end=spaceNum(digits))
                countDown = countDown - 1
            else:
                print("%{}d".format(digits) % (1), end=spaceNum(digits))
        else:
            print("%{}d".format(digits) % (aList[i]), end=spaceNum(digits))
            
n = int(input("Enter n: "))
assert n > 0, "Your input number (n) is less than or equal 0."

print("-----< Pascal Triangle >-----")
pascalTriangle(n)
