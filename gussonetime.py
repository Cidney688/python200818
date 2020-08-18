import random
num=random.randint(1,20)
i=0
while i<5:
    ans=int(input("請輸入數字:"))
    if ans ==num:
        print("恭喜答對!你只花了",i,"次")
        break
     
    if ans>num:
        print("答案太大")
    elif ans<num:
        print("answer is bigger")
    else:
        print("you're wrong")
    i=i+1
76