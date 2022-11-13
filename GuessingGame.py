import random

def menu():
    print("\n\t1.Easy\n\t2.Hard\n\t3.EXIT")

def tbk ():
    nmr = random.randint(1,10)
    bnr = 0
    a =1
    ac = 10
    while a <= 10:
        print("\n<===(",ac,"Chance left)===>")
        gues = int(input("\tInput: "))
        if gues == nmr:
            print("\tCorrect!!")
            break
        elif gues > nmr:
            print("\t  Too high")
            a+=1
            ac-=1
        elif gues < nmr:
            print("\t  Too small")
            a+=1
            ac-=1
        else:
            a+=1
            ac-=1

def tbk2 ():
    nmr = random.randint(1,10)
    bnr = 0
    a =1
    ac = 4
    while a <= 4:
        print("\n<===(",ac,"Chance left)===>")
        gues = int(input("\tInput: "))
        if gues == nmr:
            bnr+=1
            a+=1
            ac-=1
        else:
            a+=1
            ac-=1
    print("\n\tCorrect Answer:",bnr)

menu()
kan = int(input("    Choose: "))
while kan >=1 and kan <=2:
    if kan == 1:
        tbk()
    elif kan == 2:
        tbk2()
    elif kan == 3:
        kan = 6
    menu()
    kan = int(input("    Choose option: "))
print("\t==EXIT==")