num=int(input("enter num"))
if num > 0:
    if num % 2 ==0:
        print("positive even number")
    else:
        print("positive odd number")    
elif num < 0:
    if num % 2 ==0:
        print("negative even number")  
    else:
        print("negative odd number")
elif num == 0:
    print("neutral")

    print("====================")

    n=int(input("enter the num"))
    if n==0:
        print("neutral")    
    else:
        print("integer")            
