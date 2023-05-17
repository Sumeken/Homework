def main():
    answer= input("What is the time?")
    time = convert(answer)
    if time >=7 and time<=8:
        print("breakfast time")
    if time >=12 and time<=13:
        print("lunch time")
    if time >=18 and time<=19:
        print("dinner time")

def convert(given):
    hours, minutes = given.split(":")
    minutes1=float(minutes)/60
    return float(hours)+minutes1

main()