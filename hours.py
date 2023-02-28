weeks =int(input("Enter the num: "))
print(type(weeks))

hours = []
for i in range(weeks):
    hours.append(int(input("Weeks: ")))

while True:
    status = input("Status: ")
    if status == "T":
        print(sum(hours))
        break;
    elif status == "A":
        print(sum(hours)/weeks)
        break;
