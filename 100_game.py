x=0
while True:
    p1= int(input("player 1 enter number from 1 to 10: "))
    if p1>10 or p1<1:
        print ("error, number out of range!")
        p1= int(input("enter again p1: "))
     
    if x+p1>100:
        print ("erorr, sum should be =100 to win")
        p1=int(input("enter a smaller number p1: "))
        
    x=x+p1
    print("sum= ",x)
    if x==100:
        print ("congrats p1 you won!")
        break

    
    
    p2= int(input("player 2 enter number from 1 to 10: "))
    if p2>10 or p1<1:
        print ("error, number out of range!")
        p2= int(input("enter again p2: "))

     
    if x+p2>100:
        print ("erorr, sum should be =100 to win")
        p2=int(input("enter a smaller number p2: "))
        
    x=x+p2
    print("sum= ",x)
    if x==100:
        print ("congrats p2 you won!")
        break
