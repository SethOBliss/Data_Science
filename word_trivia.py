import random
wins=1
for words in range(0,500) :
    print ('choose length of the word \nyou can either choose 5 or 6 or 7 ')
    l=int(input('enter no. of letters \n(5/6/7) \n= '))
    w5=[]
    with open('word5.txt','r') as filehandle:
        for line5 in filehandle:
            wl52=line5[:-1]
            w5.append(wl52)
    w6=[]
    with open('word6.txt','r') as filehandle:
        for line6 in filehandle:
            wl62=line6[:-1]
            w6.append(wl62)
    w7=[]
    with open('word7.txt','r') as filehandle:
        for line7 in filehandle:
            wl72=line7[:-1]
            w7.append(wl72)
    rl=random.randint(0,5757)
    w1=w5[rl]
    r2=random.randint(0,500)
    w=w6[r2]
    w2=w7[r2]
    if l==5 :
        print ('so you chose 5 letter words')
        print ('choose a difficulty hard or easy \nif you choose easy you will get a word with single blank space \n of you chose hard difficulty you will get 2 blank spaces')
        d=str(input('enter difficulty(easy/hard)= '))
        if d=='easy' :
            print ('you chose easy mode ' )
            r=random.randint(0,4)
            print (w1[:r]+'_'+w1[r+1:])
            print ('for givig answer just write you answer in the slit given below\nyou only have three lives this will end')
            for i in range (0,3):
                c=str(input('enter your answer= '))
                if c==w1 :
                    print ('BINGO!')
                    print ('win streak= ',wins)
                    wins+=1
                    break
                elif c=='show answer':
                    print ('haa looser this was easy\nit is',w1)
                    wins=0
                    wins+=1
                    break
                elif i==3 :
                    print('game over')
                    wins=0
                    wins+=1
                else :
                    print ('Nada! \ntry again')
        elif d=='hard' :
            print ('you chose hard mode ')
            r1=random.randint(0,2)
            r2=random.randint(3,4)
            print (w1[:r1]+'_'+w1[r1+1:r2]+'_'+w1[r2+1:])
            print ('for givig answer just write you answer in the slit given below\nyou only have three lives this will end')
            for i in range (0,3):
                c=str(input('enter your answer= '))
                if c==w1 :
                    print ('BINGO!')
                    print ('win streak= ',wins)
                    wins+=1
                elif c=='show answer':
                    print ('haa looser this was easy\nit is',w1)
                    wins=0
                    wins+=1
                    break
                elif i==3 :
                    print('game over')
                    wins=0
                    wins+=1
                else :
                    print ('Nada! \ntry again')
        else :
            print ('choose a valid difficlty')
    elif l==6 :
        print ('so you chose 6 letter words')
        print ('choose a difficulty hard or easy \nif you choose easy you will get a word with single blank space \n of you chose hard difficulty you will get 2 blank spaces')
        d=str(input('enter difficulty(easy/hard)= '))
        if d=='easy' :
            print ('you chose easy mode ')
            r=random.randint(0,4)
            print (w[:r]+'_'+w[r+1:])        
            print ('for givig answer just write you answer in the slit given below\nyou only have three lives')
            for i in range (0,3):
                c=str(input('enter your answer= '))
                if c==w :
                    print ('BINGO!')
                    print ('win streak= ',wins)
                    wins+=1
                    break
                elif c=='show answer':
                    print ('haa looser this was easy\nit is',w)
                    wins=0
                    wins+=1
                    break
                elif i==3 :
                    print('game over')
                    wins=0
                    wins+=1
                else :
                    print ('Nada! \ntry again')
        elif d=='hard' :
            print ('you chose hard mode ')
            r1=random.randint(0,2)
            r2=random.randint(3,5)
            print (w[:r1]+'_'+w[r1+1:r2]+'_'+w[r2+1:]) 
            print ('for givig answer just write you answer in the slit given below\nyou only have three lives this all ends there')
            for i in range (0,3):
                c=str(input('enter your answer= '))
                if c==w :
                    print ('BINGO!')
                    print ('win streak= ',wins)
                    wins+=1
                    break
                elif c=='show answer':
                    print ('haa looser this was easy\nit is',w)
                    wins=0
                    wins+=1
                    break
                elif i==3 :
                    print('game over')
                    wins=0
                    wins+=1
                else :
                    print ('Nada! \ntry again')
        else :
            print ('choose a valid difficlty')
    elif l==7 :
        print ('so you chose 7 letter words')
        print ('choose a difficulty hard or easy \nif you choose easy you will get a word with single blank space \n of you chose hard difficulty you will get 2 blank spaces')
        d=str(input('enter difficulty(easy/hard)= '))
        if d=='easy' :
            print ('you chose easy mode ')
            r=random.randint(0,5)
            print (w2[:r]+'_'+w2[r+1:])      
            print ('for givig answer just write your answer in the slit given below\nyou only have three lives this all will end')
            for i in range (0,3):
                c=str(input('enter your answer= '))
                if c==w2 :
                    print ('BINGO!')
                    print ('win streak= ',wins)
                    wins+=1
                    break
                elif c=='show answer':
                    print ('haa looser this was easy\nit is',w2)
                    wins=0
                    wins+=1
                    break
                elif i==3 :
                    print('game over')
                    wins=0
                    wins+=1
                else :
                    print ('Nada! \ntry again')
        elif d=='hard' :
            print ('you chose hard mode ')
            r1=random.randint(0,2)
            r2=random.randint(3,5)
            print (w2[:r1]+'_'+w2[r1+1:r2]+'_'+w2[r2+1:])   
            print ('for givig answer just write you answer in the slit given below\nyou only have three lives this ends then there')
            for i in range (0,3):
                c=str(input('enter your answer= '))
                if c==w2 :
                    print ('BINGO!')
                    print ('win streak= ',wins)
                    wins+=1
                    break
                elif c=='show answer':
                    print ('haa looser this was easy\nit is',w2)
                    wins=0
                    wins+=1
                    break
                elif i==3 :
                    print('game over')
                    wins=0
                    wins+=1
                else :
                    print ('Nada! \ntry again')
        else :
            print ('choose a valid difficlty')
    else :
        print ('choose a valid no.\ntry again')
        continue
    print ('Do you want to continue ???? \nif yes type y\nif no type n')
    x=str(input('y/n \n'))
    if x=='y':
        continue
    elif x=='n':
        break
    else :
        print ('INVALID ANSWER!!!\nABORTING!!!\nGOING BACK!!!!\nSHUTTING DOWN!!!')
        break