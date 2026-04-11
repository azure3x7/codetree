S = int(input())
age = int(input())

if age >= 19:
    if S == 1:
        print("WOMAN")
    else:
        print("MAN")
elif age < 19:
    if S == 1:
        print("GIRL")
    else:
        print("BOY")