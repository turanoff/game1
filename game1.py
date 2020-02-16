import random
number = random.randint(0, 10)
i=0

print ("попробуй угадать число от 1 до 10")
while i != number:
    i= int(input())
    if i >= 0 and i <= 10:
        if number < i:
            print("твое число больше загаданного")
        if number > i:
            print("твое число меньше загаданного")
    else:
        print ("используй только цифры от 1 до 10")
print ("угадал, поздравляю, возьми с полки пирожок")
