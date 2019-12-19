li = ['1','2','3','1','*','+','+']
number = "0123456789"
calculation = "+-*/"
numli = []
calli = []
yes = 0
stop = 0
num1 = 0
num2 = 0
calculated = 0
for a in range(len(li)):
    for b in range(10):
        if li[a] == number[b]:
            numli.append(li[a])
            yes+=1
    if yes == 0:
        for c in range(4):
            if li[a] == calculation[c]:
                calli.append(li[a])
                stop+=1
    if stop != 0:
        num1 = int(numli.pop(len(numli)-1))
        num2 = int(numli.pop(len(numli)-1))
        cal = calli.pop(len(calli)-1)
        if cal == "+":
            calculated = num1+num2
        if cal == "-":
            calculated = num1-num2
        if cal == "*":
            calculated = num1*num2
        if cal == "/":
            calculated = num1%num2
    yes = 0
    if stop != 0:
        numli.append(calculated)
    stop = 0
print(calculated)