# Kiril Krushkov
# Skilaverkefni 1
# Á ensku.
from random import *

answer = "Access"
while answer == "Access":
    print("Chapter 1 - List")
    print("Chapter 2 - Random")
    print("Chapter 3 - String List")
    print("Chapter 4 - Dice")
    print("Chapter 5 - Subject")
    print("Chapter 6 - Quit")
    pick = int(input("Choose between 1-6:  "))

    # Chapter 1 (List)
    if pick == 1:
        numberslist = []
        numberslist50 = []
        counter = 0
        counter2 = 0
        for x in range(7):
            number = float(input("Enter a number: "))
            numberslist.append(number)

        while counter2 < 7:
            print(str(numberslist[counter2]), end="; ")
            counter2 = counter2 + 1
            fjnumber = len(numberslist)
            medaltal = sum(numberslist) / fjnumber
        print("\nThere are", fjnumber,"numbers")
        print("Highest numbers are: ", max(numberslist))
        print("The smallest numbers are: ", min(numberslist))
        print("The sum of the numbers are: ", sum(numberslist))
        print("The divide numer is: ", round(medaltal, 3))
        for number in numberslist:
            if number <= 50.5:
                numberslist50.append(number)
                counter = counter + 1

        if counter == 1:
            print("The numbers under or equal to 50.5 are: ", numberslist50, "and there are: ", counter, "numbers")
        elif counter == 0:
            print("")
        else:
            print("The numbers under or equal to 50.5 are: ", numberslist50, "and there are: ", counter, "numbers")

    if pick == 2:
        numberslist = []
        counter = 1
        counter2 = 1
        counter3 = 0
        counter4 = 0
        for w in range(70):
            number = randint(0, 500)
            numberslist.append(number)
            print(number, end=" ")
            if counter % 4 == 0:
                print(" ")
            counter = counter + 1
        print(" ")
        print("")
        print(max(numberslist))
        print(min(numberslist))

        numberslist.reverse()
        for x in numberslist:
            print(x, end=" ")
            if counter2 % 6 == 0:
                print(" ")
            counter2 += 1
            if x >= 1 and x <= 250:
                counter3 = counter3 + 1
            if x >= 250 and x <= 500:
                counter4 = counter4 + 1

        print("\nNumbers from 1-250 are:", counter3)
        print("\nNumbers from 250-500 are:", counter4)

    if pick == 3:
        numberslist = []
        numberlist2 = []
        for x in range(5):
            name = input("Put your name: ")
            numberslist.append(name)
            numberlist2.append(name)

        yes = 0
        while yes == 0:
            print("1. Not sorted")
            print("2. Alphabetical order")
            print("3. Reversed alphabetical order")
            print("4. Pick a name")
            print("5. Exit")
            valmynd = int(input("Pick 1-5: "))
            if valmynd == 1:
                print(numberslist)
                print("Not sorted number list")
                print(" ")

            if valmynd == 2:
                numberslist.sort()
                print(numberslist)
                print("List in alphabetical order")
                print(" ")

            if valmynd == 3:
                numberslist.reverse()
                print(numberslist)
                print("List of reverse alphabetical order")
                print(" ")

            if valmynd == 4:
                numbername = int(input("Pick 1-5: "))
                numbername = numbername - 1
                if numbername < 6:
                    print(numberlist2[numbername])
                    print(" ")

            if valmynd == 5:
                break
    if pick == 4:
        numberlist = []
        listt = []
        often = int(input("How many times do you want to throw the dice?: "))
        counter1 = 0
        counter2 = 0
        counter3 = 0
        counter4 = 0
        counter5 = 0
        counter6 = 0
        numberlist.append(counter1)
        numberlist.append(counter2)
        numberlist.append(counter3)
        numberlist.append(counter4)
        numberlist.append(counter5)
        numberlist.append(counter6)

        for x in range(often):
            dice = randint(1, 6)
            listt.append(dice)
            if dice == 1:
                numberlist[0] += 1
            if dice == 2:
                numberlist[1] += 1
            if dice == 3:
                numberlist[2] += 1
            if dice == 4:
                numberlist[3] += 1
            if dice == 5:
                numberlist[4] += 1
            if dice == 6:
                numberlist[5] += 1

        print("The number that came the most times is: ", (numberlist.index(max(numberlist)) + 1), "she came", max(numberlist),
              "times")
        print("")
        mest = 0
        print(numberlist)
        for i in range(6):
            if mest < listt.count(i + 1):
                mest = listt.count(i + 1)
        for e in range(6):
            if mest == listt.count(e + 1):
                print(e + 1, "Came most often,", listt.count(e + 1), "times")
                print("")

        print("Number that came the fewest times", (numberlist.index(min(numberlist)) + 1), "she came", min(numberlist), "times")
        print("")
        least = 0
        print(numberlist)
        for i in range(6):
            if least > listt.count(i + 1):
                least = listt.count(i + 1)
        for e in range(6):
            if least == listt.count(e + 1):
                print(e + 1, "Came the most often,", listt.count(e + 1), "times")
                print("")

    if pick == 5:
        listt = []
        users = int(input("How many are enrolled in FOR1TÖ05BU?: "))
        for x in range(users):
            names = input("What´s the name of contestant?: ")
            listt.append(names)
            listt.reverse()
        for i in listt:
            print(i)

    if pick == 6:
        print("Thank you!")
        import time
        time.sleep(2)
        break