while True :
    a = input("請問你有沒有開過車(yes/no):")
    if a == "yes" or a == "no":
        break
    else :
        print("輸入yes或是no,白癡")
b = input("請問你是幾歲:")
b = int(b)
if a == "yes":
    if b >= 18:
        print("你合法")
    else:
        print("妳怎麼開過車")
else:
    if b >= 18:
        print("你怎麼不去考駕照")
    else:
        print("小屁孩快滾")


