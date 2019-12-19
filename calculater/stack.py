l = []
print("1.데이터 추가")
print("2.꺼내기")
print("3.멘위 내용 출력")
while True:
    answer = input()
    if answer == "1":
        inputnum = input()
        l.append(inputnum)
    elif answer == "2":
        poppednum = l.pop(len(l)-1)
        print("꺼내진 데이터:", poppednum)
    elif answer == "3":
        print(l[len(l)-1])
