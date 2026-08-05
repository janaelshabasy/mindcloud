import random
numbers="0123456789"
l_letters="abcdefghijklmnopqrstuvwxyz"
u_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special="!@#$%&*?_"
list=[]
p=int(input("do you want 1: a secure random password , or 2: create your own password? (1/2)"))
i=0
len=0
if p==1:
  while len<8:
        len=int(input("enter password length (min 8): "))
  while True:
    list.clear()
    length=len
    loop=random.randint(1,length-3)
    i=0
    while i<loop:
        list.append(random.choice(numbers))
        i+=1
    length=length-loop
    loop=random.randint(1,length-2)
    i=0
    while i<loop:
        list.append(random.choice(l_letters))
        i+=1
    length=length-loop
    loop=random.randint(1,length-1)
    i=0
    while i<loop:
        list.append(random.choice(u_letters))
        i+=1
    length=length-loop
    loop=random.randint(1,length)
    i=0
    while i<loop:
        list.append(random.choice(special))
        i+=1
    random.shuffle(list)
    print(*list)
    x=input("do you want another password (y/n)? ")
    if x=="n":
        break
if p==2:
 while True:
    i=0
    req=0
    r1,r2,r3,r4=0,0,0,0
    password=input("enter password: ")
    for elements in password:
        for elem in numbers:
            if r1==1:
                break
            elif elem==elements:
                req+=1
                r1=1
                break
        for elem in l_letters:
            if r2==1:
                break
            if elem==elements:
                req+=1
                r2=1
                break
        for elem in u_letters:
            if r3==1:
                break
            if elem==elements:
                req+=1
                r3=1
                break
        for elem in special:
            if r4==1:
                break
            if elem==elements:
                req+=1
                r4=1
                break
    print(req)
    if req==1:
        print("Password Strength: Weak")
    if req==2:
        print("Password Strength: Medium")
    if req==3:
        print("Password Strength: Strong") 
    if req==4:
        print("Password Strength: Very Strong") 
    if req==1 or req==2:
        pas=password
        if r1==0:
            pas= pas + str(random.choice(numbers))
        if r2==0:
            pas= pas + str(random.choice(l_letters))
        if r3==0:
            pas= pas + str(random.choice(u_letters))
        if r4==0:
            pas= pas + str(random.choice(special))
        print("suggested very strong password ",pas)
        x=input("do you want to re enter the password (y/n)? ")
        if x=="n":
            print("password is ",password)
            break
    else:
        break

        
    
