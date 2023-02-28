password = str(input("Enter the password: "))
flag = 0
SpecialSym =['$', '@', '#', '%','!','(',')']
while True:

    if  not any(char.islower() for char in password):
        flag = -1
        break
    elif not any(char.isupper() for char in password):
        flag = -1
        break
    elif not any(char.isdigit() for char in password):
        flag = -1
        break
    elif not any(char in SpecialSym for char in password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Your password needs at least one uppercase letter, lowercase letter, number and symbol!")
