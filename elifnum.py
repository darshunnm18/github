n=int(input("enter num:"))
if n > 0 and n % 2 == 0:
    print(f"{n} is positive even num")
elif n > 0 and n % 2 != 0:
    print(f"{n} is positive odd num")
elif  n < 0 and n % 2 == 0:
    print(f"{n} is negative even num")
elif  n < 0 and n % 2 != 0:
    print(f"{n} is negative odd num")
else:
    print(f"{n} is neutral")



