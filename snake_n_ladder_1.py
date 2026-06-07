import random
p1=input('enter your name= ')
print ('bonjour ',p1)
print ('computer is ready to beat you')
l=0
n=0
i=1
x=100
no=100
while i==1 :
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    print (p1,'got',d1)
    print ('computer got',d2)
    if d1==6 and d2!=6:
        print (p1,'is unlocked')
        break
    elif d2==6 and d1!=6:
        print ('computer is unlocked')
        i=2
        break
    elif d1==6 and d2==6:
        print ('both unlocked simultaneously')
        i=2
        break
    f=input ('press enter')
if d1==6 and d2!=6 :
    while x==100:
        d3=random.randint(1,6)
        d4=random.randint(1,6)
        print (p1,'got',d3)
        print ('computer got',d4)
        l=l+d3
        print (p1,'is now at',l)
        if l==99:
            print(p1,'was bit by snake\nand is at',63)
            l==63
        elif l==97:
            print(p1,'was bit by snake\nand is at',87)
            l=87
        elif l==8:
            print(p1,'was bit by snake\nand is at',4)
            l=4
        elif l==18:
            print(p1,'was bit by snake\nand is at',7)
            l=7
        elif l==26:
            print(p1,'was bit by snake\nand is at',10)
            l=10
        elif l==35:
            print(p1,'was bit by snake\nand is at',5)
            l=5
        elif l==51:
            print(p1,'was bit by snake\nand is at',6)
            l=6
        elif l==54:
            print(p1,'was bit by snake\nand is at',36)
            l=36
        elif l==56:
            print(p1,'was bit by snake\nand is at',1)
            l=1
        elif l==60:
            print(p1,'was bit by snake\nand is at',23)
            l=23
        elif l==75:
            print(p1,'was bit by snake\nand is at',28)
            l=28
        elif l==83:
            print(p1,'was bit by snake\nand is at',43)
            l=45
        elif l==85:
            print(p1,'was bit by snake\nand is at',59)
            l=59
        elif l==90:
            print(p1,'was bit by snake\nand is at',48)
            l=48
        elif l==92:
            print(p1,'was bit by snake\nand is at',25)
            l=25
        elif l==81:
            l=98
            print(p1,'took a ladder to',l)
        elif l==73:
            l=86
            print(p1,'took a ladder to',l)
        elif l==61:
            l=78
            print(p1,'took a ladder to',l)
        elif l==57:
            l=76
            print(p1,'took a ladder to',l)
        elif l==49:
            l=67
            print(p1,'took a ladder to',l)
        elif l==38:
            l=59
            print(p1,'took a ladder to',l)
        elif l==22:
            l=37
            print(p1,'took a ladder to',l)
        elif l==74:
            l=17
            print(p1,'took a ladder to',l)
        elif l==15:
            l=34
            print(p1,'took a ladder to',l)
        elif l==11:
            l=28
            print(p1,'took a ladder to',l)
        elif l==6:
            l=14
            print(p1,'took a ladder to',l)
        elif l==3:
            l=20
            print(p1,'took a ladder to',l)
        elif l==91:
            l=88
            print(p1,'you took aladder to',l)
        elif d4==6 and l==99:
            print(p1,'was bit by snake\nand is at',63)
            l=63
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==97:
            print(p1,'was bit by snake\nand is at',87)
            l=87
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==8:
            print(p1,'was bit by snake\nand is at',4)
            l=4
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==18:
            print(p1,'was bit by snake\nand is at',7)
            l=7
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==26:
            print(p1,'was bit by snake\nand is at',10)
            l=10
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==35:
            print(p1,'was bit by snake\nand is at',5)
            l=5
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==51:
            print(p1,'was bit by snake\nand is at',6)
            l=6
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==54:
            print(p1,'was bit by snake\nand is at',36)
            l=36
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==56:
            print(p1,'was bit by snake\nand is at',1)
            l=1
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==60:
            print(p1,'was bit by snake\nand is at',23)
            l=23
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==75:
            print(p1,'was bit by snake\nand is at',28)
            l=28
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==83:
            print(p1,'was bit by snake\nand is at',43)
            l=45
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==85:
            print(p1,'was bit by snake\nand is at',59)
            l=59
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==90:
            print(p1,'was bit by snake\nand is at',48)
            l=48
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==92:
            print(p1,'was bit by snake\nand is at',25)
            l=25
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==81:
            l=98
            print ('computer is unlocked')
            print(p1,'took a ladder to',l)
            x=101
        elif d4==6 and l==73:
            l=86
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==61:
            l=78
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==57:
            l=76
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==49:
            l=67
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==38:
            l=59
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==22:
            l=37
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==74:
            l=17
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==15:
            l=34
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==11:
            l=28
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==6:
            l=14
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==3:
            l=20
            print(p1,'took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6 and l==91:
            l=88
            print(p1,'you took aladder to',l)
            print ('computer is unlocked')
            x=101
        elif d4==6:
            print ('computer is unlocked')
            x=101
        elif l>=100 :
            print (p1,'won')
            x=101
        ok=input('press enter')
    else :
        while no==100 :
            d5=random.randint(1,6)
            d6=random.randint(1,6)
            print(p1,'got',d5)
            print('computer got',d6)
            l=l+d5
            n=n+d6
            print (p1,'is at',l)
            print ('computer is at',n)
            if l==99:
                print(p1,'was bit by snake\nand is at',63)
                l=63
            elif l==97:
                print(p1,'was bit by snake\nand is at',87)
                l=87
            elif l==8:
                print(p1,'was bit by snake\nand is at',4)
                l=4
            elif l==18:
                print(p1,'was bit by snake\nand is at',7)
                l=7
            elif l==26:
                print(p1,'was bit by snake\nand is at',10)
                l=10
            elif l==35:
                print(p1,'was bit by snake\nand is at',5)
                l=5
            elif l==51:
                print(p1,'was bit by snake\nand is at',6)
                l=6
            elif l==54:
                print(p1,'was bit by snake\nand is at',36)
                l=36
            elif l==56:
                print(p1,'was bit by snake\nand is at',1)
                l=1
            elif l==60:
                print(p1,'was bit by snake\nand is at',23)
                l=23
            elif l==75:
                print(p1,'was bit by snake\nand is at',28)
                l=28
            elif l==83:
                print(p1,'was bit by snake\nand is at',43)
                l=45
            elif l==85:
                print(p1,'was bit by snake\nand is at',59)
                l=59
            elif l==90:
                print(p1,'was bit by snake\nand is at',48)
                l=48
            elif l==92:
                print(p1,'was bit by snake\nand is at',25)
                l=25
            elif l==81:
                l=98
                print(p1,'took a ladder to',l)
            elif l==73:
                l=86
                print(p1,'took a ladder to',l)
            elif l==61:
                l=78
                print(p1,'took a ladder to',l)
            elif l==57:
                l=76
                print(p1,'took a ladder to',l)
            elif l==49:
                l=67
                print(p1,'took a ladder to',l)
            elif l==38:
                l=59
                print(p1,'took a ladder to',l)
            elif l==22:
                l=37
                print(p1,'took a ladder to',l)
            elif l==74:
                l=17
                print(p1,'took a ladder to',l)
            elif l==15:
                l=34
                print(p1,'took a ladder to',l)
            elif l==11:
                l=28
                print(p1,'took a ladder to',l)
            elif l==6:
                l=14
                print(p1,'took a ladder to',l)
            elif l==3:
                l=20
                print(p1,'took a ladder to',l)
            elif l==91:
                l=88  
                print(p1,'took a ladder to',l)
            elif l==99 and n==99:
                print(p1,'and computer were bit by snake\nand are at',63)
                l=63
                n=63
            elif l==97 and n==97:
                print(p1,'and computer were bit by snake\nand are at',87)
                l=87
                n=87
            elif l==8 and n==8:
                print(p1,'and computer were bit by snake\nand are at',4)
                l=4
                n=4
            elif l==18 and n==18:
                print(p1,'and computer were bit by snake\nand are at',7)
                l=7
                n=7
            elif l==26 and n==26:
                print(p1,'and computer were bit by snake\nand are at',10)
                l=10
                n=10
            elif l==35 and n==35:
                print(p1,'and computer were bit by snake\nand are at',5)
                l=5
                n=5
            elif l==51 and n==51:
                print(p1,'and computer were bit by snake\nand are at',6)
                l=6
                l=n
            elif l==54 and n==54:
                print(p1,'and computer were bit by snake\nand are at',36)
                l=36
                l=n
            elif l==56 and n==56:
                print(p1,'and computer were bit by snake\nand are at',1)
                l=1
                l=n
            elif l==60 and n==60:
                print(p1,'and computer were bit by snake\nand are at',23)
                l=23
                l=n
            elif l==75 and n==75:
                print(p1,'and computer were bit by snake\nand are at',28)
                l=28
                l=n
            elif l==83 and n==83:
                print(p1,'and computer were bit by snake\nand are at',43)
                l=45
                l=n
            elif l==85 and n==85:
                print(p1,'and computer were bit by snake\nand are at',59)
                l=59
                l=n
            elif l==90 and n==90:
                print(p1,'and computer were bit by snake\nand are at',48)
                l=48
                l=n
            elif l==92 and n==92:
                print(p1,'and computer were bit by snake\nand are at',25)
                l=25
                l=n
            elif l==81 and n==81:
                l=98
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==73 and n==73:
                l=86
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==61 and n==61:
                l=78
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==57 and n==57:
                l=76
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==49 and n==49:
                l=67
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==38 and n==38:
                l=59
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==22 and n==22:
                l=37
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==17 and n==17:
                l=74
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==15 and n==15:
                l=34
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==11 and n==11:
                l=28
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==6 and n==6:
                l=14
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==3 and n==3:
                l=20
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==88 and n==88:
                l=91
                print(p1,'and computer took a ladder to',l)
            elif n==99:
                print('computer was bit by snake\nand is at',63)
                n==63
            elif n==97:
                print('computer was bit by snake\nand is at',87)
                n=87
            elif n==8:
                print('computer was bit by snake\nand is at',4)
                n=4
            elif n==18:
                print('computer was bit by snake\nand is at',7)
                n=7
            elif n==26:
                print('computer was bit by snake\nand is at',10)
                n=10
            elif n==35:
                print('computer was bit by snake\nand is at',5)
                n=5
            elif n==51:
                print('computer was bit by snake\nand is at',6)
                n=6
            elif n==54:
                print('computer was bit by snake\nand is at',36)
                n=36
            elif n==56:
                print('computer was bit by snake\nand is at',1)
                n=1
            elif n==60:
                print('computer was bit by snake\nand is at',23)
                n=23
            elif n==75:
                print('computer was bit by snake\nand is at',28)
                n=28
            elif n==83:
                print('computer was bit by snake\nand is at',43)
                n=45
            elif n==85:
                print('computer was bit by snake\nand is at',59)
                n=59
            elif n==90:
                print('computer was bit by snake\nand is at',48)
                n=48
            elif n==92:
                print('computer was bit by snake\nand is at',25)
                n=25
            elif n==81:
                n=98
                print('computer took a ladder to',n)
            elif n==73:
                n=86
                print('computer took a ladder to',n)
            elif n==61:
                n=78
                print('computer took a ladder to',n)
            elif n==57:
                n=76
                print('computer took a ladder to',n)
            elif n==49:
                n=67
                print('computer took a ladder to',n)
            elif n==38:
                n=59
                print('computer took a ladder to',n)
            elif n==22:
                n=37
                print('computer took a ladder to',n)
            elif n==74:
                n=17
                print('computer took a ladder to',n)
            elif n==15:
                n=34
                print('computer took a ladder to',n)
            elif n==11:
                n=28
                print('computer took a ladder to',n)
            elif n==6:
                n=14
                print('computer took a ladder to',n)
            elif n==3:
                n=20
                print('computer took a ladder to',n)
            elif n==91:
                n=88
            elif l>=100 :
                print (p1,'won')
                break
            elif n>=100 :
                print ('computer won as said')
                break
            elif l>=100 and n>=100 :
                if l>n :
                    print (p1,'won')
                    break
                elif n>l :
                    print ('computer won as said')
                    break
            fu=input('press enter')
elif d1!=6 and d2==6:
    while x==100:
        d3=random.randint(1,6)
        d4=random.randint(1,6)
        print (p1,'got',d3)
        print ('computer got',d4)
        n=n+d4
        print ('computer is now at',n)
        if n==99:
            print('computer was bit by snake\nand is at',63)
            n==63
        elif n==97:
            print('computer was bit by snake\nand is at',87)
            n=87
        elif n==8:
            print('computer was bit by snake\nand is at',4)
            n=4
        elif n==18:
            print('computer was bit by snake\nand is at',7)
            n=7
        elif n==26:
            print('computer was bit by snake\nand is at',10)
            n=10
        elif n==35:
            print('computer was bit by snake\nand is at',5)
            n=5
        elif n==51:
            print('computer was bit by snake\nand is at',6)
            n=6
        elif n==54:
            print('computer was bit by snake\nand is at',36)
            n=36
        elif n==56:
            print('computer was bit by snake\nand is at',1)
            n=1
        elif n==60:
            print('computer was bit by snake\nand is at',23)
            n=23
        elif n==75:
            print('computer was bit by snake\nand is at',28)
            n=28
        elif n==83:
            print('computer was bit by snake\nand is at',43)
            n=45
        elif n==85:
            print('computer was bit by snake\nand is at',59)
            n=59
        elif n==90:
            print('computer was bit by snake\nand is at',48)
            n=48
        elif n==92:
            print('computer was bit by snake\nand is at',25)
            n=25
        elif n==81:
            n=98
            print('computer took a ladder to',n)
        elif n==73:
            n=86
            print('computer took a ladder to',n)
        elif n==61:
            n=78
            print('computer took a ladder to',n)
        elif n==57:
            n=76
            print('computer took a ladder to',n)
        elif n==49:
            n=67
            print('computer took a ladder to',n)
        elif n==38:
            n=59
            print('computer took a ladder to',n)
        elif n==22:
            n=37
            print('computer took a ladder to',n)
        elif n==74:
            n=17
            print('computer took a ladder to',n)
        elif n==15:
            n=34
            print('computer took a ladder to',n)
        elif n==11:
            n=28
            print('computer took a ladder to',n)
        elif n==6:
            n=14
            print('computer took a ladder to',n)
        elif n==3:
            n=20
            print('computer took a ladder to',n)
        elif n==88:
            n=91
            print('computer took a ladder to',n)
        elif d3==6 and n==99:
            print('computer was bit by snake\nand is at',63)
            n=63
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==97:
            print('computer was bit by snake\nand is at',87)
            n=87
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==8:
            print('computer was bit by snake\nand is at',4)
            n=4
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==18:
            print('computer was bit by snake\nand is at',7)
            n=7
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==26:
            print('computer was bit by snake\nand is at',10)
            n=10
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==35:
            print('computer was bit by snake\nand is at',5)
            n=5
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==51:
            print('computer was bit by snake\nand is at',6)
            n=6
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==54:
            print('computer was bit by snake\nand is at',36)
            n=36
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==56:
            print('computer was bit by snake\nand is at',1)
            n=1
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==60:
            print('computer was bit by snake\nand is at',23)
            n=23
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==75:
            print('computer was bit by snake\nand is at',28)
            n=28
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==83:
            print('computer was bit by snake\nand is at',43)
            n=45
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==85:
            print('computer was bit by snake\nand is at',59)
            n=59
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==90:
            print('computer was bit by snake\nand is at',48)
            n=48
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==92:
            print('computer was bit by snake\nand is at',25)
            n=25
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==81:
            n=98
            print ('computer is unlocked')
            print('computer took a ladder to',l)
            x=101
        elif d3==6 and n==73:
            n=86
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==61:
            n=78
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==57:
            n=76
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==49:
            n=67
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==38:
            n=59
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==22:
            n=37
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==74:
            n=17
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==15:
            n=34
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==11:
            n=28
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==6:
            n=14
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==3:
            n=20
            print('computer took a ladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6 and n==91:
            n=88
            print('computer you took aladder to',l)
            print ('computer is unlocked')
            x=101
        elif d3==6:
            print (p1,'is unlocked')
            x=101
        elif l>=100 :
            print ('computer won')
            x=101
        lol=input('press enter')
    else :
        while no==100 :
            d5=random.randint(1,6)
            d6=random.randint(1,6)
            print(p1,'got',d5)
            print('computer got',d6)
            l=l+d5
            n=n+d6
            print (p1,'is at',l)
            print ('computer is at',n)
            if l==99:
                print(p1,'was bit by snake\nand is at',63)
                l==63
            elif l==97:
                print(p1,'was bit by snake\nand is at',87)
                l=87
            elif l==8:
                print(p1,'was bit by snake\nand is at',4)
                l=4
            elif l==18:
                print(p1,'was bit by snake\nand is at',7)
                l=7
            elif l==26:
                print(p1,'was bit by snake\nand is at',10)
                l=10
            elif l==35:
                print(p1,'was bit by snake\nand is at',5)
                l=5
            elif l==51:
                print(p1,'was bit by snake\nand is at',6)
                l=6
            elif l==54:
                print(p1,'was bit by snake\nand is at',36)
                l=36
            elif l==56:
                print(p1,'was bit by snake\nand is at',1)
                l=1
            elif l==60:
                print(p1,'was bit by snake\nand is at',23)
                l=23
            elif l==75:
                print(p1,'was bit by snake\nand is at',28)
                l=28
            elif l==83:
                print(p1,'was bit by snake\nand is at',43)
                l=45
            elif l==85:
                print(p1,'was bit by snake\nand is at',59)
                l=59
            elif l==90:
                print(p1,'was bit by snake\nand is at',48)
                l=48
            elif l==92:
                print(p1,'was bit by snake\nand is at',25)
                l=25
            elif l==81:
                l=98
                print(p1,'took a ladder to',l)
            elif l==73:
                l=86
                print(p1,'took a ladder to',l)
            elif l==61:
                l=78
                print(p1,'took a ladder to',l)
            elif l==57:
                l=76
                print(p1,'took a ladder to',l)
            elif l==49:
                l=67
                print(p1,'took a ladder to',l)
            elif l==38:
                l=59
                print(p1,'took a ladder to',l)
            elif l==22:
                l=37
                print(p1,'took a ladder to',l)
            elif l==17:
                l=74
                print(p1,'took a ladder to',l)
            elif l==15:
                l=34
                print(p1,'took a ladder to',l)
            elif l==11:
                l=28
                print(p1,'took a ladder to',l)
            elif l==6:
                l=14
                print(p1,'took a ladder to',l)
            elif l==3:
                l=20
                print(p1,'took a ladder to',l)
            elif l==91:
                l=88
                print(p1,'took a ladder to',l)
            elif l==99 and n==99:
                print(p1,'and computer were bit by snake\nand are at',63)
                l=63
                n=63
            elif l==97 and n==97:
                print(p1,'and computer were bit by snake\nand are at',87)
                l=87
                n=87
            elif l==8 and n==8:
                print(p1,'and computer were bit by snake\nand are at',4)
                l=4
                n=4
            elif l==18 and n==18:
                print(p1,'and computer were bit by snake\nand are at',7)
                l=7
                n=7
            elif l==26 and n==26:
                print(p1,'and computer were bit by snake\nand are at',10)
                l=10
                n=10
            elif l==35 and n==35:
                print(p1,'and computer were bit by snake\nand are at',5)
                l=5
                n=5
            elif l==51 and n==51:
                print(p1,'and computer were bit by snake\nand are at',6)
                l=6
                l=n
            elif l==54 and n==54:
                print(p1,'and computer were bit by snake\nand are at',36)
                l=36
                l=n
            elif l==56 and n==56:
                print(p1,'and computer were bit by snake\nand are at',1)
                l=1
                l=n
            elif l==60 and n==60:
                print(p1,'and computer were bit by snake\nand are at',23)
                l=23
                l=n
            elif l==75 and n==75:
                print(p1,'and computer were bit by snake\nand are at',28)
                l=28
                l=n
            elif l==83 and n==83:
                print(p1,'and computer were bit by snake\nand are at',43)
                l=45
                l=n
            elif l==85 and n==85:
                print(p1,'and computer were bit by snake\nand are at',59)
                l=59
                l=n
            elif l==90 and n==90:
                print(p1,'and computer were bit by snake\nand are at',48)
                l=48
                l=n
            elif l==92 and n==92:
                print(p1,'and computer were bit by snake\nand are at',25)
                l=25
                l=n
            elif l==81 and n==81:
                l=98
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==73 and n==73:
                l=86
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==61 and n==61:
                l=78
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==57 and n==57:
                l=76
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==49 and n==49:
                l=67
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==38 and n==38:
                l=59
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==22 and n==22:
                l=37
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==17 and n==17:
                l=74
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==15 and n==15:
                l=34
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==11 and n==11:
                l=28
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==6 and n==6:
                l=14
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==3 and n==3:
                l=20
                l=n
                print(p1,'and computer took a ladder to',l)
            elif l==88 and n==88:
                l=91
                print(p1,'and computer took a ladder to',l)
            elif n==99:
                print('computer was bit by snake\nand is at',63)
                n==63
            elif n==97:
                print('computer was bit by snake\nand is at',87)
                n=87
            elif n==8:
                print('computer was bit by snake\nand is at',4)
                n=4
            elif n==18:
                print('computer was bit by snake\nand is at',7)
                n=7
            elif n==26:
                print('computer was bit by snake\nand is at',10)
                n=10
            elif n==35:
                print('computer was bit by snake\nand is at',5)
                n=5
            elif n==51:
                print('computer was bit by snake\nand is at',6)
                n=6
            elif n==54:
                print('computer was bit by snake\nand is at',36)
                n=36
            elif n==56:
                print('computer was bit by snake\nand is at',1)
                n=1
            elif n==60:
                print('computer was bit by snake\nand is at',23)
                n=23
            elif n==75:
                print('computer was bit by snake\nand is at',28)
                n=28
            elif n==83:
                print('computer was bit by snake\nand is at',43)
                n=45
            elif n==85:
                print('computer was bit by snake\nand is at',59)
                n=59
            elif n==90:
                print('computer was bit by snake\nand is at',48)
                n=48
            elif n==92:
                print('computer was bit by snake\nand is at',25)
                n=25
            elif n==81:
                n=98
                print('computer took a ladder to',n)
            elif n==73:
                n=86
                print('computer took a ladder to',n)
            elif n==61:
                n=78
                print('computer took a ladder to',n)
            elif n==57:
                n=76
                print('computer took a ladder to',n)
            elif n==49:
                n=67
                print('computer took a ladder to',n)
            elif n==38:
                n=59
                print('computer took a ladder to',n)
            elif n==22:
                n=37
                print('computer took a ladder to',n)
            elif n==17:
                n=74
                print('computer took a ladder to',n)
            elif n==15:
                n=34
                print('computer took a ladder to',n)
            elif n==11:
                n=28
                print('computer took a ladder to',n)
            elif n==6:
                n=14
                print('computer took a ladder to',n)
            elif n==3:
                n=20
                print('computer took a ladder to',n)
            elif n==91:
                n=88
            elif l>=100 :
                print (p1,'won')
                break
            elif n>=100 :
                print ('computer won as said')
                break
            elif l>=100 and n>=100 :
                if l>n :
                    print (p1,'won')
                    break
                elif n>l :
                    print ('computer won as said')
                    break
            lo1=input('press enter') 
elif d1==6 and d2==6 :
    while x==100:
        d3=random.randint(1,6)
        d4=random.randint(1,6)
        print (p1,'got',d3)
        print ('computer got',d4)
        l=l+d3
        n=n+d4
        print(p1,'is at',l)
        print('computer is at',n)
        if l==99:
            print(p1,'was bit by snake\nand is at',63)
            l==63
        elif l==97:
            print(p1,'was bit by snake\nand is at',87)
            l=87
        elif l==8:
            print(p1,'was bit by snake\nand is at',4)
            l=4
        elif l==18:
            print(p1,'was bit by snake\nand is at',7)
            l=7
        elif l==26:
            print(p1,'was bit by snake\nand is at',10)
            l=10
        elif l==35:
            print(p1,'was bit by snake\nand is at',5)
            l=5
        elif l==51:
            print(p1,'was bit by snake\nand is at',6)
            l=6
        elif l==54:
            print(p1,'was bit by snake\nand is at',36)
            l=36
        elif l==56:
            print(p1,'was bit by snake\nand is at',1)
            l=1
        elif l==60:
            print(p1,'was bit by snake\nand is at',23)
            l=23
        elif l==75:
            print(p1,'was bit by snake\nand is at',28)
            l=28
        elif l==83:
            print(p1,'was bit by snake\nand is at',43)
            l=45
        elif l==85:
            print(p1,'was bit by snake\nand is at',59)
            l=59
        elif l==90:
            print(p1,'was bit by snake\nand is at',48)
            l=48
        elif l==92:
            print(p1,'was bit by snake\nand is at',25)
            l=25
        elif l==81:
            l=98
            print(p1,'took a ladder to',l)
        elif l==73:
            l=86
            print(p1,'took a ladder to',l)
        elif l==61:
            l=78
            print(p1,'took a ladder to',l)
        elif l==57:
            l=76
            print(p1,'took a ladder to',l)
        elif l==49:
            l=67
            print(p1,'took a ladder to',l)
        elif l==38:
            l=59
            print(p1,'took a ladder to',l)
        elif l==22:
            l=37
            print(p1,'took a ladder to',l)
        elif l==74:
            l=17
            print(p1,'took a ladder to',l)
        elif l==15:
            l=34
            print(p1,'took a ladder to',l)
        elif l==11:
            l=28
            print(p1,'took a ladder to',l)
        elif l==6:
            l=14
            print(p1,'took a ladder to',l)
        elif l==3:
            l=20
            print(p1,'took a ladder to',l)
        elif l==99 and n==99:
            print(p1,'and computer were bit by snake\nand are at',63)
            l=63
            n=63
        elif l==97 and n==97:
            print(p1,'and computer were bit by snake\nand are at',87)
            l=87
            n=87
        elif l==8 and n==8:
            print(p1,'and computer were bit by snake\nand are at',4)
            l=4
            n=4
        elif l==18 and n==18:
            print(p1,'and computer were bit by snake\nand are at',7)
            l=7
            n=7
        elif l==26 and n==26:
            print(p1,'and computer were bit by snake\nand are at',10)
            l=10
            n=10
        elif l==35 and n==35:
            print(p1,'and computer were bit by snake\nand are at',5)
            l=5
            n=5
        elif l==51 and n==51:
            print(p1,'and computer were bit by snake\nand are at',6)
            l=6
            l=n
        elif l==54 and n==54:
            print(p1,'and computer were bit by snake\nand are at',36)
            l=36
            l=n
        elif l==56 and n==56:
            print(p1,'and computer were bit by snake\nand are at',1)
            l=1
            l=n
        elif l==60 and n==60:
            print(p1,'and computer were bit by snake\nand are at',23)
            l=23
            l=n
        elif l==75 and n==75:
            print(p1,'and computer were bit by snake\nand are at',28)
            l=28
            l=n
        elif l==83 and n==83:
            print(p1,'and computer were bit by snake\nand are at',43)
            l=45
            l=n
        elif l==85 and n==85:
            print(p1,'and computer were bit by snake\nand are at',59)
            l=59
            l=n
        elif l==90 and n==90:
            print(p1,'and computer were bit by snake\nand are at',48)
            l=48
            l=n
        elif l==92 and n==92:
            print(p1,'and computer were bit by snake\nand are at',25)
            l=25
            l=n
        elif l==81 and n==81:
            l=98
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==73 and n==73:
            l=86
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==61 and n==61:
            l=78
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==57 and n==57:
            l=76
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==49 and n==49:
            l=67
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==38 and n==38:
            l=59
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==22 and n==22:
            l=37
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==17 and n==17:
            l=74
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==15 and n==15:
            l=34
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==11 and n==11:
            l=28
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==6 and n==6:
            l=14
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==3 and n==3:
            l=20
            l=n
            print(p1,'and computer took a ladder to',l)
        elif l==88 and n==88:
            l=91
            print(p1,'and computer took a ladder to',l)
        elif l==91:
            l=88      
        elif n==99:
            print('computer was bit by snake\nand is at',63)
            n==63
        elif n==97:
            print('computer was bit by snake\nand is at',87)
            n=87
        elif n==8:
            print('computer was bit by snake\nand is at',4)
            n=4
        elif n==18:
            print('computer was bit by snake\nand is at',7)
            n=7
        elif n==26:
            print('computer was bit by snake\nand is at',10)
            n=10
        elif n==35:
            print('computer was bit by snake\nand is at',5)
            n=5
        elif n==51:
            print('computer was bit by snake\nand is at',6)
            n=6
        elif n==54:
            print('computer was bit by snake\nand is at',36)
            n=36
        elif n==56:
            print('computer was bit by snake\nand is at',1)
            n=1
        elif n==60:
            print('computer was bit by snake\nand is at',23)
            n=23
        elif n==75:
            print('computer was bit by snake\nand is at',28)
            n=28
        elif n==83:
            print('computer was bit by snake\nand is at',43)
            n=45
        elif n==85:
            print('computer was bit by snake\nand is at',59)
            n=59
        elif n==90:
            print('computer was bit by snake\nand is at',48)
            n=48
        elif n==92:
            print('computer was bit by snake\nand is at',25)
            n=25
        elif n==81:
            n=98
            print('computer took a ladder to',n)
        elif n==73:
            n=86
            print('computer took a ladder to',n)
        elif n==61:
            n=78
            print('computer took a ladder to',n)
        elif n==57:
            n=76
            print('computer took a ladder to',n)
        elif n==49:
            n=67
            print('computer took a ladder to',n)
        elif n==38:
            n=59
            print('computer took a ladder to',n)
        elif n==22:
            n=37
            print('computer took a ladder to',n)
        elif n==74:
            n=17
            print('computer took a ladder to',n)
        elif n==15:
            n=34
            print('computer took a ladder to',n)
        elif n==11:
            n=28
            print('computer took a ladder to',n)
        elif n==6:
            n=14
            print('computer took a ladder to',n)
        elif n==3:
            n=20
            print('computer took a ladder to',n)
        elif n==91:
            n=88
        elif l>=100 :
            print (p1,'won')
            break
        elif n>=100 :
            print ('computer won as said')
            break
        elif l>=100 and n>=100 :
            if l>n :
                print (p1,'won')
                break
            elif n>l :
                print ('computer won as said')
        op=input('press enter')
