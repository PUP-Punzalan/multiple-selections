def highToLow(n1, n2, n3, n4):
    highestn = max(n1,n2,n3,n4)

    if n2 > n1:
        lowestn = n1
        secondn = n2
    else:
        lowestn = n2
        secondn = n1
    
    if n3 > secondn:
        thirdn = n3
    else:
        thirdn = secondn
        secondn = lowestn
        lowestn = n3

    # rechecking value by swapping the value
    if lowestn > secondn:
        lowestn = lowestn + secondn
        secondn = lowestn - secondn
        lowestn = lowestn - secondn

    # rechecking value by swapping the value
    if secondn > thirdn:
        secondn = secondn + thirdn
        thirdn = secondn - thirdn
        secondn = secondn - thirdn

    if n4 > thirdn:
        highestn = n4
    else:
        highestn = thirdn
        thirdn = secondn
        secondn = lowestn
        lowestn = n4
    
    # rechecking value by swapping the value
    if lowestn > secondn:
        lowestn = lowestn + secondn
        secondn = lowestn - secondn
        lowestn = lowestn - secondn

    # rechecking value by swapping the value
    if secondn > thirdn:
        secondn = secondn + thirdn
        thirdn = secondn - thirdn
        secondn = secondn - thirdn

    print(f"The arrangement is {highestn:.2f}, {thirdn:.2f}, {secondn:.2f}, {lowestn:.2f}")

# highest > third > second > lowest
number1 = float(input("Insert 1st number: "))
number2 = float(input("Insert 2nd number: "))
number3 = float(input("Insert 3rd number: "))
number4 = float(input("Insert 4th number: "))

highToLow(number1, number2, number3, number4)